import json

with open("b5_subagents.json", "r", encoding="utf-8") as f:
    subs = json.load(f)

for i, s in enumerate(subs):
    print(f"=== {i}: {s['Role']} ===")
    print(s["Prompt"])
    print()
