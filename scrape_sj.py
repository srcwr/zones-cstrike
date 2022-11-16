from pathlib import Path
import time
import requests

api_key = ""

dddd = Path("z")
for filename in dddd.glob("*.json"):
    mapname = filename.stem
    resp = requests.get(f"https://sourcejump.net/api/records/{mapname}?key={api_key}")
    if resp.status_code == 200 and resp.content != b'[]':
        with open(f"sj/{mapname}.json", "ab") as f:
            f.write(resp.content)
            print(f"wrote to {mapname}.json")
    time.sleep(0.3)
