import json

with open("b4_subagents.json", "r", encoding="utf-8") as f:
    subs = json.load(f)

for i, s in enumerate(subs):
    print(f"=== {i}: {s['Role']} ===")
    print(s["Prompt"])
    print()
