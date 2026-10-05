import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open("batch_prompts.json", "r", encoding="utf-8") as f:
    batches = json.load(f)

b2 = batches[1]
subagents = []
for item in b2:
    subagents.append({
        "TypeName": "branch_driller",
        "Role": f"Driller {item['chunk_id']}",
        "Model": "flash",
        "Prompt": item["prompt"],
        "Workspace": "inherit"
    })

with open("b2_subagents.json", "w", encoding="utf-8") as f:
    json.dump(subagents, f, ensure_ascii=False, indent=2)

print(f"Prepared {len(subagents)} subagents for Batch 2.")
for item in b2:
    print(f"- {item['chunk_id']}: {item['title']}")
