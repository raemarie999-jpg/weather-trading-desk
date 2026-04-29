import requests
import os

API_KEY = os.getenv("MINUTETEMP_API_KEY")

headers = {
    "X-API-Key": API_KEY
}

stations = ["KDFW", "KORD"]

for station in stations:
    url = f"https://api.minutetemp.com/api/v1/stations/{station}/forecast/runs"
    r = requests.get(url, headers=headers)

    print("======")
    print(station)
    print("STATUS:", r.status_code)
    print(r.text[:1000])
r = requests.get(url, headers=headers)

print(r.status_code)
print(r.text[:3000])
