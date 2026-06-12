import requests
import time

API_KEY  = "F9E77E256CF43CB0895BE34EA3B0CB85"
TRACKING = "872151172901"

# Bước 1: Xóa tracking cũ (nếu đã đăng ký trước)
requests.post(
    "https://api.17track.net/track/v2.2/deletetrack",
    headers={"17token": API_KEY},
    json=[{"number": TRACKING}]
)

# Bước 2: Đăng ký lại, KHÔNG truyền carrier → tự detect
res = requests.post(
    "https://api.17track.net/track/v2.4/register",
    headers={"17token": API_KEY},
    json=[{"number": TRACKING}]
)
print("Đăng ký:", res.json())

# Bước 3: Chờ
print("Chờ 5s...")
time.sleep(5)

# Bước 4: Lấy kết quả
res = requests.post(
    "https://api.17track.net/track/v2.4/gettrackinfo",
    headers={"17token": API_KEY},
    json=[{"number": TRACKING}]
)
data = res.json()

# In gọn
accepted = data.get("data", {}).get("accepted", [])
if accepted:
    info = accepted[0].get("track_info", {})
    print("Status:", info.get("latest_status"))
    print("Latest event:", info.get("latest_event"))
    events = info.get("tracking", {}).get("providers", [{}])[0].get("events", [])
    print(f"Tổng events: {len(events)}")
    for ev in events[:5]:
        print(" -", ev.get("time_iso"), ev.get("description"))
else:
    print("Rejected:", data.get("data", {}).get("rejected"))