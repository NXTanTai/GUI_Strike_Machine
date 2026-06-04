from PySide6.QtCore import QObject, Signal
import concurrent.futures

class ExportWorker(QObject):
    finished = Signal(str, str)

    def __init__(
        self,
        db_path: str,
        file_path: str,
        name: str = "",
        group: str = "",
        start_date: str = "",
        end_date: str = "",
    ):
        super().__init__()
        self.db_path    = db_path
        self.file_path  = file_path
        self.name       = name.strip()
        self.group      = group.strip()
        self.start_date = start_date.strip()
        self.end_date   = end_date.strip()

    def run(self):
        with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
            future = executor.submit(
                _export_process,
                str(self.db_path),
                self.file_path,
                self.name,
                self.group,
                self.start_date,
                self.end_date,
            )
            try:
                result_paths = future.result()
                self.finished.emit("|".join(result_paths), "")
            except Exception as e:
                self.finished.emit("", str(e))


def _export_process(
    db_path: str,
    file_path: str,
    name: str = "",
    group: str = "",
    start_date: str = "",
    end_date: str = "",
) -> list[str]:
    import sqlite3
    import xlsxwriter
    from pathlib import Path

    CHUNK_SIZE = 10_000
    MAX_ROWS   = 999_997

    HEADERS    = ["No.", "Name.", "Group.", "Pressure.", "T-Oven.",
                  "Front.", "Middle.", "End.", "Date."]
    COL_WIDTHS = [9.1, 11.4, 18.6, 19.0, 21.4, 11.0, 19.5, 19.9, 24.1]
    LAST_COL   = len(HEADERS) - 1
    MERGE_COLS = {0, 1, 8}  # No., Name., Date.

    conn   = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT MAX(id) FROM history")
    max_id    = cursor.fetchone()[0] or 0
    use_parts = max_id > MAX_ROWS

    query = '''
        SELECT "No.", "Name.", "Group.", "Pressure.", "T-Oven.",
               "Front.", "Middle.", "End.", "Date."
        FROM history
    '''
    where_clauses: list[str] = []
    params: list[str] = []

    if name:
        where_clauses.append('"Name." LIKE ?')
        params.append(f"%{name}%")
    if group and group != "All":
        where_clauses.append('"Group." LIKE ?')
        params.append(f"%{group}%")
    if start_date and end_date and start_date != end_date:
        where_clauses.append("""
            (
                SUBSTR("Date.", 15, 4) || '/' ||
                SUBSTR("Date.", 12, 2) || '/' ||
                SUBSTR("Date.", 9, 2) || ' ' ||
                SUBSTR("Date.", 1, 5)
            )
            BETWEEN ? AND ?
        """)
        params.extend([start_date, end_date])

    if where_clauses:
        query += " WHERE " + " AND ".join(where_clauses)
    query += " ORDER BY id ASC"
    cursor.execute(query, params)

    base_path     = Path(file_path)
    stem          = base_path.stem
    suffix        = base_path.suffix or ".xlsx"
    parent        = base_path.parent
    created_files: list[str] = []

    def make_workbook(part_num: int):
        part_path = parent / (
            f"{stem}_part{part_num}{suffix}" if use_parts else f"{stem}{suffix}"
        )
        wb = xlsxwriter.Workbook(str(part_path))
        ws = wb.add_worksheet("Report")

        title_fmt = wb.add_format({
            "font_name": "Times New Roman", "font_size": 20, "bold": True,
            "font_color": "#FFFFFF", "bg_color": "#4472C4",
            "align": "center", "valign": "vcenter",
        })

        def hdr(left, right, bottom=1):
            return wb.add_format({
                "font_name": "Times New Roman", "font_size": 13, "bold": True,
                "font_color": "#FFFFFF", "bg_color": "#4472C4",
                "align": "center", "valign": "vcenter",
                "top": 2, "bottom": bottom, "left": left, "right": right,
            })

        def dat(bg, left, right):
            f = {
                "font_name": "Times New Roman", "font_size": 12,
                "align": "center", "valign": "vcenter",
                "top": 1, "bottom": 1, "left": left, "right": right,
            }
            if bg:
                f["bg_color"] = "#F0F8FF"
            return wb.add_format(f)

        fmts = {
            "hdr":  [hdr(2, 1), hdr(1, 1), hdr(1, 2, bottom=2)],  # first, mid, last
            "even": [dat(True,  2, 1), dat(True,  1, 1), dat(True,  1, 2)],
            "odd":  [dat(False, 2, 1), dat(False, 1, 1), dat(False, 1, 2)],
        }

        for i, w in enumerate(COL_WIDTHS):
            ws.set_column(i, i, w)

        ws.merge_range(0, 0, 1, LAST_COL, "DỮ LIỆU BÁO CÁO", title_fmt)
        ws.set_row(0, 30)
        ws.set_row(1, 10)

        ws.set_row(2, 30)
        for col_idx, col_name in enumerate(HEADERS):
            slot = 0 if col_idx == 0 else (2 if col_idx == LAST_COL else 1)
            ws.write(2, col_idx, col_name, fmts["hdr"][slot])

        created_files.append(str(part_path))
        return wb, ws, fmts

    def get_fmt(fmts, group_num: int, col_idx: int):
        key  = "even" if group_num % 2 == 0 else "odd"
        slot = 0 if col_idx == 0 else (2 if col_idx == LAST_COL else 1)
        return fmts[key][slot]
    
    def flush_group(ws, fmts, pending, row_data, row_group):
        """Flush toàn bộ pending cùng lúc — đảm bảo No./Name./Date. dùng chung màu."""
        if not pending:
            return

        min_start = min(v[0] for v in pending.values())
        g         = row_group.get(min_start, 0)

        all_rows: set[int] = set()
        for start_row, end_row, _ in pending.values():
            all_rows.update(range(start_row, end_row + 1))

        for r in sorted(all_rows):
            g2    = row_group.get(r, g)
            saved = row_data.get(r, [])
            for c, val in enumerate(saved):
                if c not in MERGE_COLS:
                    ws.write(r, c, val, get_fmt(fmts, g2, c))

        for col_idx, (start_row, end_row, value) in pending.items():
            fmt = get_fmt(fmts, g, col_idx)
            if start_row == end_row:
                ws.write(start_row, col_idx, value, fmt)
            else:
                ws.merge_range(start_row, col_idx, end_row, col_idx, value, fmt)

    part_num     = 1
    row_in_sheet = 3
    group_num    = -1           
    prev_no      = object()

    pending:   dict[int, tuple[int, int, object]] = {}
    row_group: dict[int, int]                     = {}
    row_data:  dict[int, list]                    = {}

    wb, ws, fmts = make_workbook(part_num)

    while True:
        rows = cursor.fetchmany(CHUNK_SIZE)
        if not rows:
            break

        for row in rows:
            if row_in_sheet > MAX_ROWS:
                flush_group(ws, fmts, pending, row_data, row_group)
                pending.clear()
                row_group.clear()
                row_data.clear()
                wb.close()
                part_num     += 1
                row_in_sheet  = 3
                group_num     = -1
                prev_no       = object()
                wb, ws, fmts  = make_workbook(part_num)

            current_no = row[0]

            if current_no != prev_no:
                flush_group(ws, fmts, pending, row_data, row_group)
                pending.clear()
                group_num += 1
                prev_no    = current_no

            row_group[row_in_sheet] = group_num
            row_data[row_in_sheet]  = list(row)
            ws.set_row(row_in_sheet, 22)

            for col_idx, value in enumerate(row):
                if col_idx in MERGE_COLS:
                    if col_idx in pending:
                        start_row, end_row, prev_value = pending[col_idx]
                        group_size = end_row - start_row + 1
                        if value == prev_value and group_size < 3:
                            # Mở rộng nhóm
                            pending[col_idx] = (start_row, row_in_sheet, prev_value)
                        else:
                            pending[col_idx] = (row_in_sheet, row_in_sheet, value)
                    else:
                        pending[col_idx] = (row_in_sheet, row_in_sheet, value)
                else:
                    ws.write(row_in_sheet, col_idx, value,
                            get_fmt(fmts, group_num, col_idx))

            row_in_sheet += 1

    # ── Flush cuối ───────────────────────────────────────────────────────────
    flush_group(ws, fmts, pending, row_data, row_group)

    wb.close()
    conn.close()
    return created_files