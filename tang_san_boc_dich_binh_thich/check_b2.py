import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open("b2_subagents.json", "r", encoding="utf-8") as f:
    subs = json.load(f)

for s in subs:
    print(s["Role"], "| Prompt chars:", len(s["Prompt"]))
