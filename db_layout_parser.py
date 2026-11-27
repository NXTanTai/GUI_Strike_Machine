"""
Đọc file "DB Memory Address" (Excel) và tự nhận diện các vùng INPUT / ACTUAL (output) / ERROR (alarm).

Hỗ trợ cả 2 định dạng:
  - Bản cũ (Default): có khối header (IP, Write Time, Offset..., Size..., Read (ms)),
    nhãn vùng (Bit_Input / Input / Bit_Output / Output) nằm ở cột phụ (cột E) cùng dòng với tag đầu vùng.
  - Bản mới (Update): không có header, nhãn vùng là 1 dòng riêng ở cột Name (Type + Address trống).

Quy tắc nhận diện vùng:
  - Nhãn chứa "alarm"/"error"   -> ERROR
  - Nhãn chứa "output"/"actual" -> ACTUAL
  - Nhãn chứa "input"           -> INPUT
  - Nếu file không có nhãn ERROR: các tag STRING (VD Alarm_Info) được đưa sang vùng ERROR.
  - Tag nằm trước nhãn đầu tiên: xếp theo offset header (nếu có), không thì INPUT.

Offset / size mỗi vùng được tính từ địa chỉ tag thực tế; vùng trước được kéo dài tới
đầu vùng sau để các vùng liền nhau (PLCReadBlock gom được vào 1 request).
"""

from __future__ import annotations

import re
from typing import Any, Optional

import pandas as pd

REGION_INPUT  = "INPUT"
REGION_ACTUAL = "ACTUAL"
REGION_ERROR  = "ERROR"
REGION_ORDER  = (REGION_INPUT, REGION_ACTUAL, REGION_ERROR)

DTYPE_SIZE = {"BOOL": 1, "BYTE": 1, "INT": 2, "WORD": 2, "DINT": 4, "DWORD": 4, "REAL": 4}

DEFAULTS = {
    "ip_plc":      "172.16.100.100",
    "write_time":  100,
    "db_name":     1,
    "data_read":   200,
    "input_read":  500,
    "error_read":  1500,
}

# nhãn header (chuẩn hoá: lower, bỏ khoảng trắng / ":" ) -> key
_HEADER_KEYS = {
    "ip":             "ip_plc",
    "writetime":      "write_time",
    "offsetdata":     "offsets_data",
    "datasize":       "data_size",
    "datareadms":     "data_read",
    "offsetinput":    "offsets_input",
    "inputsize":      "input_size",
    "inputreadms":    "input_read",
    "offseterror":    "offsets_error",
    "errorsize":      "error_size",
    "errorreadms":    "error_read",
}

_REGION_KEYS = {
    REGION_INPUT:  ("offsets_input", "input_size",  "input_read"),
    REGION_ACTUAL: ("offsets_data",  "data_size",   "data_read"),
    REGION_ERROR:  ("offsets_error", "error_size",  "error_read"),
}

_DB_RE = re.compile(r"^DB\s*(\d+)$", re.IGNORECASE)
_PREFIX_RE = re.compile(r"^((?:P\d+|T\d+)_)(.*)$")


def _cell(v) -> str:
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return ""
    s = str(v).strip()
    return "" if s.lower() == "nan" else s


def _norm(s: str) -> str:
    return re.sub(r"[\s_:\-().]", "", s).lower()


def classify_region(label: str) -> Optional[str]:
    """Nhãn vùng -> INPUT / ACTUAL / ERROR (None nếu không phải nhãn vùng)."""
    n = _norm(label)
    if not n:
        return None
    if "alarm" in n or "error" in n:
        return REGION_ERROR
    if "output" in n or "actual" in n:
        return REGION_ACTUAL
    if "input" in n:
        return REGION_INPUT
    return None


def normalize_name(raw: str) -> str:
    name = re.sub(r"[\s\-]+", "_", raw.strip())
    return re.sub(r"_+", "_", name).strip("_")


def parse_address(value) -> tuple[int, int]:
    """'198.1' / 198.1 / 198 -> (byte, bit)."""
    if isinstance(value, float):
        s = repr(value)
    else:
        s = _cell(value)
    if not s:
        raise ValueError("empty address")
    if "." in s:
        b, bit = s.split(".", 1)
        byte_addr, bit_addr = int(b), int(bit.rstrip("0") or "0")
    else:
        byte_addr, bit_addr = int(float(s)), 0
    if not 0 <= bit_addr <= 7:
        raise ValueError(f"bit {bit_addr} out of range")
    return byte_addr, bit_addr


def _tag_size(dtype: str, string_max_chars: int) -> int:
    if dtype == "STRING":
        return 2 + string_max_chars
    return DTYPE_SIZE.get(dtype, 1)


def _int_or_none(v) -> Optional[int]:
    try:
        return int(float(_cell(v)))
    except (TypeError, ValueError):
        return None


def _read_header(df: pd.DataFrame, stop_row: int) -> dict:
    """Đọc khối header kiểu cũ (cặp 'nhãn' -> ô bên phải) nằm trên dòng tiêu đề bảng."""
    header: dict[str, Any] = {}
    for r in range(stop_row):
        row = df.iloc[r]
        for c in range(len(row) - 1):
            key = _HEADER_KEYS.get(_norm(_cell(row.iloc[c])))
            if not key:
                continue
            val = _cell(row.iloc[c + 1])
            if not val:
                continue
            header[key] = val if key == "ip_plc" else _int_or_none(val)
    return header


def _find_db_number(df: pd.DataFrame) -> Optional[int]:
    for r in range(len(df)):
        for v in df.iloc[r]:
            m = _DB_RE.match(_cell(v))
            if m:
                return int(m.group(1))
    return None


def _find_table_header(df: pd.DataFrame) -> tuple[int, int, int, int]:
    """Tìm dòng tiêu đề bảng (Name / Type / Address) -> (row, col_name, col_type, col_addr)."""
    for r in range(len(df)):
        cols = {_norm(_cell(v)): i for i, v in enumerate(df.iloc[r])}
        if "name" in cols and "type" in cols and "address" in cols:
            return r, cols["name"], cols["type"], cols["address"]
    raise ValueError("Không tìm thấy dòng tiêu đề Name / Type / Address")


def _dedupe_name(name: str, region: str, seen: dict[str, str]) -> str:
    """Tên trùng ở vùng ACTUAL -> chèn 'Current_' sau tiền tố (P1_Air_FillingTime -> P1_Current_Air_FillingTime)."""
    if name not in seen:
        return name
    m = _PREFIX_RE.match(name)
    if region == REGION_ACTUAL and m and not m.group(2).startswith("Current"):
        candidate = f"{m.group(1)}Current_{m.group(2)}"
    else:
        candidate = f"{name}_{region}"
    i = 2
    base = candidate
    while candidate in seen:
        candidate = f"{base}_{i}"
        i += 1
    return candidate


def parse_db_layout(df: pd.DataFrame, string_max_chars: int = 50, logger=None) -> dict:
    """
    Trả về dict tương thích với self.db_dict cũ:
      ip_plc, write_time, db_name,
      offsets_input / input_size / input_read,
      offsets_data  / data_size  / data_read,
      offsets_error / error_size / error_read,
      DB_LAYOUT [(name, TYPE, byte, bit)], DB_TOTAL_BYTES
    và thêm: DB_REGIONS {region: [tag names]}, DB_FORMAT ("header" | "auto"), DB_WARNINGS [str]
    """
    warnings: list[str] = []

    def warn(msg: str):
        warnings.append(msg)
        if logger:
            logger.warning("[DB LAYOUT]: %s", msg)

    hdr_row, c_name, c_type, c_addr = _find_table_header(df)
    header = _read_header(df, hdr_row)
    has_header_offsets = all(k in header for k in ("offsets_input", "offsets_data", "offsets_error"))

    tags: list[dict] = []                 # {name, dtype, byte, bit, region, explicit}
    seen: dict[str, str] = {}             # name -> region
    current_region: Optional[str] = None
    has_error_marker = False

    for r in range(hdr_row + 1, len(df)):
        row = df.iloc[r]
        name_raw = _cell(row.iloc[c_name])
        dtype    = _cell(row.iloc[c_type]).upper()
        addr_raw = row.iloc[c_addr]

        # Nhãn vùng ở cột phụ (định dạng cũ, cột E...)
        for c in range(len(row)):
            if c in (c_name, c_type, c_addr) or c < c_name:
                continue
            region = classify_region(_cell(row.iloc[c]))
            if region:
                current_region = region
                has_error_marker |= region == REGION_ERROR
                break

        if not name_raw:
            continue

        # Dòng nhãn vùng (định dạng mới): có Name, không Type / Address
        if not dtype and not _cell(addr_raw):
            region = classify_region(name_raw)
            if region:
                current_region = region
                has_error_marker |= region == REGION_ERROR
            else:
                warn(f"Dòng {r + 1}: '{name_raw}' không có Type/Address và không phải nhãn vùng -> bỏ qua")
            continue

        if dtype not in DTYPE_SIZE and dtype != "STRING":
            warn(f"Dòng {r + 1}: '{name_raw}' kiểu '{dtype}' không hỗ trợ -> bỏ qua")
            continue

        try:
            byte_addr, bit_addr = parse_address(addr_raw)
        except ValueError as e:
            warn(f"Dòng {r + 1}: '{name_raw}' địa chỉ '{_cell(addr_raw)}' lỗi ({e}) -> bỏ qua")
            continue

        tags.append({
            "name_raw": name_raw,
            "dtype":    dtype,
            "byte":     byte_addr,
            "bit":      bit_addr if dtype == "BOOL" else None,
            "region":   current_region,
            "row":      r + 1,
        })

    if not tags:
        raise ValueError("File DB không có tag hợp lệ")

    # ---- Gán vùng cho tag chưa có nhãn ----
    for t in tags:
        if t["region"] is not None:
            continue
        if has_header_offsets:
            starts = sorted((header[_REGION_KEYS[rg][0]], rg) for rg in REGION_ORDER)
            t["region"] = next((rg for off, rg in reversed(starts) if t["byte"] >= off), REGION_INPUT)
        else:
            t["region"] = REGION_INPUT

    # Không có nhãn ERROR -> tag STRING (Alarm_Info, ...) thuộc vùng ERROR
    if not has_error_marker:
        for t in tags:
            if t["dtype"] == "STRING":
                t["region"] = REGION_ERROR

    # ---- Chuẩn hoá tên + xử lý trùng ----
    db_layout: list[tuple[str, str, int, Any]] = []
    regions_tags: dict[str, list[str]] = {rg: [] for rg in REGION_ORDER}
    for t in sorted(tags, key=lambda x: (x["byte"], x["bit"] or 0)):
        name = normalize_name(t["name_raw"])
        new_name = _dedupe_name(name, t["region"], seen)
        if new_name != name:
            warn(f"Dòng {t['row']}: tên '{name}' ({t['region']}, {t['byte']}) trùng với vùng "
                 f"{seen[name]} -> đổi thành '{new_name}'")
        seen[new_name] = t["region"]
        t["name"] = new_name
        db_layout.append((new_name, t["dtype"], t["byte"], t["bit"]))
        regions_tags[t["region"]].append(new_name)

    # ---- Kiểm tra chồng lấn địa chỉ ----
    occupied: dict[tuple[int, Optional[int]], str] = {}
    for t in tags:
        size = _tag_size(t["dtype"], string_max_chars)
        keys = [(t["byte"], t["bit"])] if t["dtype"] == "BOOL" else [(t["byte"] + i, None) for i in range(size)]
        for k in keys:
            clash = occupied.get(k) or (occupied.get((k[0], None)) if k[1] is not None else None)
            if clash:
                warn(f"'{t['name']}' chồng địa chỉ với '{clash}' tại byte {k[0]}")
                break
        for k in keys:
            occupied.setdefault(k, t["name"])

    # ---- Tính offset / size từng vùng ----
    bounds: dict[str, list[int]] = {}
    for t in tags:
        # Tag Spare không được đọc → không dùng để xác định biên vùng
        # (VD Spare1..10 nằm sau Alarm_Info làm vùng ACTUAL "chồng" lên ERROR)
        if t["name"].lower().startswith("spare"):
            continue
        end = t["byte"] + _tag_size(t["dtype"], string_max_chars)
        b = bounds.setdefault(t["region"], [t["byte"], end])
        b[0] = min(b[0], t["byte"])
        b[1] = max(b[1], end)

    ordered = sorted(bounds.items(), key=lambda kv: kv[1][0])
    for (rg, b), (rg_next, b_next) in zip(ordered, ordered[1:]):
        if b[1] > b_next[0]:
            warn(f"Vùng {rg} [{b[0]}..{b[1]}) chồng lên vùng {rg_next} bắt đầu tại {b_next[0]}")
        else:
            b[1] = b_next[0]      # lấp khoảng trống

    for rg in REGION_ORDER:
        if rg not in bounds:
            warn(f"Không tìm thấy vùng {rg}")

    db_total_bytes = max(b[1] for b in bounds.values())

    # Ghép các chuỗi ô lại thành kết quả
    db_name = _find_db_number(df) or DEFAULTS["db_name"]
    result: dict[str, Any] = {
        "ip_plc":     header.get("ip_plc") or DEFAULTS["ip_plc"],
        "write_time": header.get("write_time") or DEFAULTS["write_time"],
        "db_name":    db_name,
    }
    for rg in REGION_ORDER:
        k_off, k_size, k_read = _REGION_KEYS[rg]
        start, end = bounds.get(rg, (0, 0))
        result[k_off]  = start
        result[k_size] = end - start
        result[k_read] = header.get(k_read) or DEFAULTS[k_read]

        if has_header_offsets and rg in bounds:
            h_off, h_size = header.get(k_off), header.get(k_size)
            if h_off != start or (h_size is not None and h_size != end - start):
                warn(f"Vùng {rg}: header ghi offset={h_off} size={h_size}, "
                     f"nhận diện được offset={start} size={end - start} -> dùng giá trị nhận diện")

    result["DB_LAYOUT"]      = db_layout
    result["DB_TOTAL_BYTES"] = db_total_bytes
    result["DB_REGIONS"]     = regions_tags
    result["DB_FORMAT"]      = "header" if header else "auto"
    result["DB_WARNINGS"]    = warnings
    return result