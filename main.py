import requests
import os
import json

API_KEY = os.getenv("MINUTETEMP_API_KEY")

headers = {
    "X-API-Key": API_KEY
}

stations = ["KDFW", "KORD"]


# -----------------------------
# 1. GET LATEST RUN ID
# -----------------------------
def get_latest_run_id(station):
    url = f"https://api.minutetemp.com/api/v1/stations/{station}/forecast/runs"
    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        print("ERROR fetching runs:", station, r.status_code, r.text[:200])
        return None

    data = r.json()

    return data["data"]["runs"][0]["id"]


# -----------------------------
# 2. GET FULL FORECAST DETAIL
# -----------------------------
def get_run_detail(run_id):
    url = f"https://api.minutetemp.com/api/v1/forecast/runs/{run_id}"
    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        print("ERROR fetching run detail:", run_id, r.status_code, r.text[:200])
        return None

    return r.json()


# -----------------------------
# 3. FETCH STATION FULL DATA
# -----------------------------
def fetch_station(station):
    run_id = get_latest_run_id(station)

    if not run_id:
        return None

    print("======")
    print("STATION:", station)
    print("RUN ID:", run_id)

    detail = get_run_detail(run_id)

    return detail


# -----------------------------
# 4. MAIN EXECUTION
# -----------------------------
results = {}

for station in stations:
    results[station] = fetch_station(station)

print("====== FINAL OUTPUT ======")
print(json.dumps(results, indent=2))


# -----------------------------
# 5. OPTIONAL: SAVE FOR DASHBOARD
# -----------------------------
with open("signals.json", "w") as f:
    json.dump(results, f)
