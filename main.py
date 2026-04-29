import requests
import os
import json

API_KEY = os.getenv("MINUTETEMP_API_KEY")
headers = {"X-API-Key": API_KEY}

stations = ["KDFW", "KORD"]

def fetch_station(station):
    url = f"https://api.minutetemp.com/api/v1/stations/{station}/forecast/runs"
    r = requests.get(url, headers=headers)

    print("======")
    print("STATION:", station)
    print("STATUS:", r.status_code)

    data = r.json()

    # SAFETY CHECK (important)
    if "data" not in data or "runs" not in data["data"]:
        print("BAD RESPONSE:", data)
        return None

    return data["data"]["runs"][0]

results = {}

for s in stations:
    results[s] = fetch_station(s)

print("====== FINAL OUTPUT ======")
print(json.dumps(results, indent=2))
