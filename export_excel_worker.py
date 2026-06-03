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
    MAX_ROWS   = 999_999

    HEADERS = ["No.", "Name.", "Group.", "Pressure.", "T-Oven.",
               "Front.", "Middle.", "End.", "Date."]

    # No. | Name. | Group. | Pressure. | T-Oven. | Front. | Middle. | End. | Date.
    COL_WIDTHS = [8, 15, 15, 12, 12, 12, 12, 12, 20]

    # ── Query ────────────────────────────────────────────────────────────────
    conn   = sqlite3.connect(db_path)
    cursor = conn.cursor()

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

    # ── Tạo workbook ─────────────────────────────────────────────────────────
    base_path = Path(file_path)
    stem      = base_path.stem
    suffix    = base_path.suffix or ".xlsx"
    parent    = base_path.parent

    created_files: list[str] = []

    def make_workbook(part_num: int):
        part_path = parent / f"{stem}_part{part_num}{suffix}"
        wb = xlsxwriter.Workbook(str(part_path), {"constant_memory": True})
        ws = wb.add_worksheet("Sheet1")

        hdr_fmt = wb.add_format({
            "bold":         True,
            "font_size":    13,
            "font_color":   "#1E40AF",
            "bottom":       2,
            "border_color": "#3B82F6",
        })
        data_fmt = wb.add_format({
            "font_size": 12,
            "valign":    "vcenter",
        })

        for col_idx, width in enumerate(COL_WIDTHS):
            ws.set_column(col_idx, col_idx, width)

        for col_idx, col_name in enumerate(HEADERS):
            ws.write(0, col_idx, col_name, hdr_fmt)

        created_files.append(str(part_path))
        return wb, ws, data_fmt

    # ── Ghi data theo chunk ──────────────────────────────────────────────────
    part_num     = 1
    row_in_sheet = 1
    wb, ws, data_fmt = make_workbook(part_num)

    while True:
        rows = cursor.fetchmany(CHUNK_SIZE)
        if not rows:
            break

        for row in rows:
            if row_in_sheet > MAX_ROWS:
                wb.close()
                part_num        += 1
                row_in_sheet     = 1
                wb, ws, data_fmt = make_workbook(part_num)

            for col_idx, value in enumerate(row):
                ws.write(row_in_sheet, col_idx, value, data_fmt)

            row_in_sheet += 1

    wb.close()
    conn.close()

    return created_files