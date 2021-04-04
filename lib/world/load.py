import os
import json
world_dir = [os.path.join("./lib/world", o) for o in os.listdir("./lib/world") if os.path.isdir(os.path.join("./lib/world",o))]

worlds = [];

for dir in world_dir:
  if("__pycache__" in dir): continue;
  print(dir);
  files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
  worlds.append([]);
  for file in files:
    stream = open(file, "r");
    worlds[-1].append(json.loads(stream.read()));

print(worlds);
    