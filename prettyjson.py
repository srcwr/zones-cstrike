import json
from pathlib import Path
import time
import os.path

"""
for map in fapzormaps.splitlines():
    with open("i/" + map.strip() + ".json", "w+", newline='\n') as f:
        f.write('[{"possible_on_scroll": 1,"possible_on_stamina": 1}]')
"""

now = int(time.time())

dddd = Path(".")
for filename in dddd.glob("**/*.json"):
    with open(filename, "r+", newline='\n') as f:
        orig = f.read()
        if orig == "":
            continue
        j = json.loads(orig)
        if str(filename.parent) == "z": # tier / mapinfo dir
            #for z in j: z["id"] = now
            j = sorted(j, key=lambda x: (str(x["track"]), x["type"], x.get("data", 0), str(x.get("form", 2)), x.get("target", "")))
        pretty = json.dumps(j, sort_keys=True, indent='\t', separators=(',', ': '))
        if orig != pretty:
            f.seek(0)
            f.truncate()
            f.write(pretty)


for filename in dddd.glob("i/*.json"):
    x = "z/" + filename.stem + ".json"
    if not os.path.isfile(x):
        open(x, 'a').close()
        #with open(x, 'a') as f:
        #    f.write("[]")

