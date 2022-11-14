import io
import json
from pathlib import Path
import time

now = int(time.time())

dddd = Path(".")
for filename in dddd.glob("**/*.json"):
    with io.open(filename, "r+", newline='\n') as f:
        orig = f.read()
        j = json.loads(orig)
        if filename.parent == "z": # tier / mapinfo dir
            j = sorted(j, key=lambda x: (x["track"], x["type"], x.get("data", "0"), x.get("form", "box"), x.get("target", "")))
            #for z in j: z["id"] = now
        pretty = json.dumps(j, sort_keys=True, indent='\t', separators=(',', ': '))
        if orig != pretty:
            f.seek(0)
            f.truncate()
            f.write(pretty)
