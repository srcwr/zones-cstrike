import json
from pathlib import Path

dddd = Path("sj")
for filename in dddd.glob("*.json"):
    with open(filename, "r", encoding="utf-8") as f:
        sj = json.load(f)
    tier = sj[0]["tier"]
    if tier == 0:
        continue
    aaaa = Path(f"i/{filename.stem}.json")
    aaaa.touch(exist_ok=True)
    with open(aaaa, "r+") as f:
        content = f.read()
        if content == "":
            f.write('[{"tier":' + str(tier) + '}]')
        else:
            info = json.loads(content)
            info[0]["tier"] = tier
            f.seek(0)
            f.truncate()
            json.dump(info, f)
