import json

with open("b2_subagents.json", "r", encoding="utf-8") as f:
    subs = json.load(f)

for i, s in enumerate(subs):
    print(f"=== SUBAGENT {i}: {s['Role']} ===")
    print(s["Prompt"])
    print()
