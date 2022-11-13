import io
import json
from pathlib import Path

dddd = Path(".")
for filename in dddd.glob("**/*.json"):
    with io.open(filename, "r+", newline='\n') as f:
        j = json.load(f)
        f.seek(0)
        f.truncate()
        json.dump(j, f, sort_keys=True, indent='\t', separators=(',', ': '))
