# zones-cstrike
work-in-progress standardized zones for bhoptimer (for Counter-Strike: Source)

Pull-requests are welcome.

[home page](https://github.com/srcwr/zones-cstrike)

[github pages page](https://srcwr.github.io/zones-cstrike/)

## To use
in `cfg/sourcemod/plugin.shavit-zones.cfg`
```
shavit_zones_usesql "0"
```
in `cfg/sourcemod/plugin.shavit-zones-json.cfg`
```
shavit_zones_json_url "http://zones-{engine}.srcwr.com/z/{map}.json"

// Or you could use the github pages direct url
shavit_zones_json_url "https://srcwr.github.io/zones-{engine}/z/{map}.json"
```

## other stuff
currently the cutehops zone dump with the sourcejump zone dump merged on top.
- cutehops zone dump, courtesy of may/lilac ([Github](https://github.com/lilac1337) / [Steam](https://steamcommunity.com/profiles/76561198955846348))
- sourcejump dump, courtesy of Eric ([Github]( https://github.com/ecsr) / [Steam](https://steamcommunity.com/id/-eric))
