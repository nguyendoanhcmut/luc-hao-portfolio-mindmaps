import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open("batch_prompts.json", "r", encoding="utf-8") as f:
    batches = json.load(f)

b1 = batches[0]
subagents = []
for item in b1:
    subagents.append({
        "TypeName": "branch_driller",
        "Role": f"Driller {item['chunk_id']}",
        "Model": "flash",
        "Prompt": item["prompt"],
        "Workspace": "inherit"
    })

with open("b1_subagents.json", "w", encoding="utf-8") as f:
    json.dump(subagents, f, ensure_ascii=False, indent=2)

print(f"Prepared {len(subagents)} subagents for Batch 1.")
