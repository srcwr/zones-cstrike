import json
import os

if not os.path.isdir("new"):
    os.makedirs("new")
with open('_.json') as f:
    asdf = json.load(f)

"""
{
	"id": 1,
	"map": "bhop_eazy_v2",
	"type": 0,
	"corner1_x": -64,
	"corner1_y": -192,
	"corner1_z": 49.031,
	"corner2_x": 256,
	"corner2_y": 192,
	"corner2_z": 176.031,
	"destination_x": 0,
	"destination_y": 0,
	"destination_z": 0,
	"track": 0,
	"flags": 0,
	"data": 0,
	"prebuilt": null,
	"form": null,
	"target": null
},
"""

def FillBoxMinMax(a, b):
    for i in range(3):
        y,u = a[i],b[i]
        a[i] = float(min(y,u))
        b[i] = float(max(y,u))

typesss = [
	"start",
	"end",
	"respawn",
	"stop",
	"slay",
	"freestyle",
	"customspeedlimit",
	"teleport",
	"customspawn",
	"easybhop",
	"slide",
	"airaccel",
	"stage",
	"notimergravity",
	"gravity",
	"speedmod"
]

d = {}
for row in asdf["rows"]:
    mapname = row["map"].lower()
    if not mapname in d:
        d[mapname] = []
    del row["map"]
    if "prebuilt" in row: del row["prebuilt"]
    if "form" in row: del row["form"]
    if "target" in row: del row["target"]
    
    ## what a mess.... lmao
    
    row["point_a"] = []
    row["point_a"].append(row["corner1_x"] or 0.0)
    row["point_a"].append(row["corner1_y"] or 0.0)
    row["point_a"].append(row["corner1_z"] or 0.0)
    del row["corner1_x"]
    del row["corner1_y"]
    del row["corner1_z"]
    row["point_b"] = []
    row["point_b"].append(row["corner2_x"] or 0.0)
    row["point_b"].append(row["corner2_y"] or 0.0)
    row["point_b"].append(row["corner2_z"] or 0.0)
    del row["corner2_x"]
    del row["corner2_y"]
    del row["corner2_z"]
    row["dest"] = []
    row["dest"].append(float(row["destination_x"]))
    row["dest"].append(float(row["destination_y"]))
    row["dest"].append(float(row["destination_z"]))
    del row["destination_x"]
    del row["destination_y"]
    del row["destination_z"]
    row["type"] = typesss[row["type"]]
    
    if row["dest"][0] == 0 and row["dest"][1] == 0 and row["dest"][2] == 0:
        del row["dest"]
    if row["flags"] == 0:
        del row["flags"]
    if row["data"] == 0:
        del row["data"]
    
    FillBoxMinMax(row["point_a"], row["point_b"])
    d[mapname].append(row)

for map in d:
    with open("new/" + map + ".json", "w") as f:
        json.dump(d[map], f, sort_keys=True, indent='\t', separators=(',', ': '))

