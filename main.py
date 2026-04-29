import json
import random
from datetime import datetime

def generate_signal():

    edge = round(random.uniform(-0.18, 0.18), 3)

    if edge > 0.08:
        signal = "STRONG LONG"
    elif edge > 0.03:
        signal = "LONG"
    elif edge < -0.08:
        signal = "STRONG SHORT"
    elif edge < -0.03:
        signal = "SHORT"
    else:
        signal = "NO TRADE"

    return {
        "timestamp": str(datetime.now()),
        "contract": "DFW Above 90",
        "edge": edge,
        "signal": signal,
        "risk": "MODERATE"
    }

data = generate_signal()

with open("signals.json", "w") as f:
    json.dump(data, f, indent=2)

print("signals updated")
