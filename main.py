import requests
import os
import json

API_KEY = os.getenv("MINUTETEMP_API_KEY")

headers = {
    "X-API-Key": API_KEY
}

stations = ["KDFW", "KORD"]

def get_station_data(station):
    url = f"https://api.minutetemp.com/api/v1/stations/{station}/forecast/runs"
    r = requests.get(url, headers=headers)

    print("======")
    print(station)
    print("STATUS:", r.status_code)

    data = r.json()
    return data["data"]["runs"][0]

dfw = get_station_data("KDFW")
ord = get_station_data("KORD")

# --- minimal feature extraction ---
def safe_temp(run):
    # we don't fully trust schema yet → defensive
    return run.get("temperature", 0)

dfw_temp = safe_temp(dfw)
ord_temp = safe_temp(ord)

delta = dfw_temp - ord_temp

# --- simple signal logic (we will upgrade later to full model engine) ---
if delta > 2:
    signal = "LONG DFW"
elif delta < -2:
    signal = "LONG KORD"
else:
    signal = "FLAT"

output = {
    "timestamp": dfw.get("fetched_at"),
    "contract": "DFW vs KORD temp spread",
    "edge": delta,
    "signal": signal,
    "risk": "LOW" if abs(delta) < 3 else "MED"
}

print("====== SIGNAL ======")
print(output)

with open("signals.json", "w") as f:
    json.dump(output, f)
