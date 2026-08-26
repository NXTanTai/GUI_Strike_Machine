import sqlite3, shutil
from pathlib import Path

db_path = Path(r"D:\SM_PRD\DB_address\history.db")

# Luôn backup trước khi đổi schema
shutil.copy(db_path, db_path.with_suffix(".db.bak"))

conn = sqlite3.connect(str(db_path))
cur = conn.cursor()

existing = {row[1] for row in cur.execute("PRAGMA table_info(history)").fetchall()}

# Nếu tồn tại cả 2 cột trùng lặp "Oven SV" và "Oven SV." → gộp dữ liệu vào 1 cột trước
if "Oven SV" in existing and "Oven SV." in existing:
    cur.execute('''
        UPDATE history
        SET "Oven SV." = "Oven SV"
        WHERE ("Oven SV." IS NULL OR "Oven SV." = '')
          AND "Oven SV" IS NOT NULL AND "Oven SV" != ''
    ''')
    cur.execute('ALTER TABLE history DROP COLUMN "Oven SV"')  # SQLite 3.35+ hỗ trợ DROP COLUMN
    conn.commit()
    print("Đã gộp và xóa cột trùng 'Oven SV'")

# Đổi tên cột: Oven -> Furnace
rename_map = {
    "Oven SV.": "Furnace SV.",
    "T-Oven.":  "T-Furnace.",
}
existing = {row[1] for row in cur.execute("PRAGMA table_info(history)").fetchall()}
for old, new in rename_map.items():
    if old in existing and new not in existing:
        cur.execute(f'ALTER TABLE history RENAME COLUMN "{old}" TO "{new}"')
        print(f"Đã đổi '{old}' -> '{new}'")

conn.commit()
conn.close()
print("Xong.")