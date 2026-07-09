import time
import snap7
from snap7.util import get_bool, get_int, get_dint, get_real, get_string

client = snap7.client.Client()
client.connect('172.16.100.100', 0, 1)

if client.get_connected():
    print("Connected")

DB_NUMBER = 1
START = 198
SIZE = 138
LAYOUT = [
    ("Bit_Alarm",                    "BOOL", 198, 0),

    ("T0_Current Temp",              "REAL", 200, 0),

    ("P1_Current Temp1",             "REAL", 204, 0),
    ("P1_Current Temp2",             "REAL", 208, 0),
    ("P1_Current Temp3",             "REAL", 212, 0),
    ("P1_Current PressureHose",      "REAL", 216, 0),
    ("P1_Current PressureITV",       "REAL", 220, 0),
    ("P1_Current Air FillingTime",   "DINT", 224, 0),
    ("P1_Current Air HoldingTime",   "DINT", 228, 0),
    ("P1_Current Air ReleaseTime",   "DINT", 232, 0),
    ("P1_Current Oil Start Time",    "DINT", 236, 0),
    ("P1_Current Oil End Time",      "DINT", 240, 0),
    ("P1_Number Test Times",         "DINT", 244, 0),

    ("P2_Current Temp1",             "REAL", 248, 0),
    ("P2_Current Temp2",             "REAL", 252, 0),
    ("P2_Current Temp3",             "REAL", 256, 0),
    ("P2_Current PressureHose",      "REAL", 260, 0),
    ("P2_Current PressureITV",       "REAL", 264, 0),
    ("P2_Current Air FillingTime",   "DINT", 268, 0),
    ("P2_Current Air HoldingTime",   "DINT", 272, 0),
    ("P2_Current Air ReleaseTime",   "DINT", 276, 0),
    ("P2_Current Oil Start Time",    "DINT", 280, 0),
    ("P2_Current Oil End Time",      "DINT", 284, 0),
    ("P2_Number Test Times",         "DINT", 288, 0),

    ("P3_Current Temp1",             "REAL", 292, 0),
    ("P3_Current Temp2",             "REAL", 296, 0),
    ("P3_Current Temp3",             "REAL", 300, 0),
    ("P3_Current PressureHose",      "REAL", 304, 0),
    ("P3_Current PressureITV",       "REAL", 308, 0),
    ("P3_Current Air FillingTime",   "DINT", 312, 0),
    ("P3_Current Air HoldingTime",   "DINT", 316, 0),
    ("P3_Current Air ReleaseTime",   "DINT", 320, 0),
    ("P3_Current Oil Start Time",    "DINT", 324, 0),
    ("P3_Current Oil End Time",      "DINT", 328, 0),
    ("P3_Number Test Times",         "DINT", 332, 0),
]

def read_db(plc, db_number, start, size):
    t0 = time.perf_counter()
    data = plc.db_read(db_number, start, size)
    elapsed_ms = (time.perf_counter() - t0) * 1000
    print(f"Take {elapsed_ms:.1f}ms (size={size})")
    return data

def parse(raw: bytearray, base_offset: int) -> dict:
    result = {}
    for name, dtype, offset, bit in LAYOUT:
        rel = offset - base_offset
        if rel < 0 or rel >= len(raw):
            continue
        try:
            if dtype == "BOOL":
                value = get_bool(raw, rel, bit)
            elif dtype == "INT":
                value = get_int(raw, rel)
            elif dtype == "DINT":
                value = get_dint(raw, rel)
            elif dtype == "REAL":
                value = get_real(raw, rel)
            elif dtype == "STRING":
                value = get_string(raw, rel)
            else:
                value = None
            result[name] = value
        except Exception as e:
            result[name] = f"parse error: {e}"
    return result

while True:
    try:
        raw = read_db(plc=client, db_number=DB_NUMBER, start=START, size=SIZE)
        values = parse(raw, base_offset=START)

        print("-" * 30)
        for k, v in values.items():
            print(f"  {k:10s} = {v}")

    except Exception as exc:
        print(f"Read error: {exc}")

    time.sleep(0.5)