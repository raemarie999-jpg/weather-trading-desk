import requests
import os

API_KEY = os.getenv("MINUTETEMP_API_KEY")

headers = {
    "X-API-Key": API_KEY
}

run_id = "019ddb23-e09f-722e-8094-0983a865ee6f"

url = f"https://api.minutetemp.com/api/v1/forecast/runs/{run_id}"

r = requests.get(url, headers=headers)

print(r.status_code)
print(r.text[:3000])
