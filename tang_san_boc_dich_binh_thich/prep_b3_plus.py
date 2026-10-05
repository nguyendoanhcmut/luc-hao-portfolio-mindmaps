import json, os, sys

sys.stdout.reconfigure(encoding="utf-8")

with open("batch_prompts.json", "r", encoding="utf-8") as f:
    batches = json.load(f)

# Find ch09 in batches[1]
ch09_item = next(item for item in batches[1] if item["chunk_id"] == "ch09")

# Read batch 3
b3 = batches[2]

subagents = [{
    "TypeName": "branch_driller",
    "Role": f"Driller {ch09_item['chunk_id']}",
    "Model": "flash",
    "Prompt": ch09_item["prompt"],
    "Workspace": "inherit"
}]

for item in b3:
    subagents.append({
        "TypeName": "branch_driller",
        "Role": f"Driller {item['chunk_id']}",
        "Model": "flash",
        "Prompt": item["prompt"],
        "Workspace": "inherit"
    })

with open("b3_plus_ch09_subagents.json", "w", encoding="utf-8") as f:
    json.dump(subagents, f, ensure_ascii=False, indent=2)

print(f"Prepared {len(subagents)} subagents for Batch 3 (including ch09).")
