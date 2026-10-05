import json

with open("batch_prompts.json", "r", encoding="utf-8") as f:
    batches = json.load(f)

for b_idx, b in enumerate(batches):
    subagents = []
    for item in b:
        subagents.append({
            "TypeName": "branch_driller",
            "Role": f"Driller {item['chunk_id']}",
            "Model": "flash",
            "Prompt": item["prompt"],
            "Workspace": "inherit"
        })
    with open(f"b{b_idx+1}_subagents.json", "w", encoding="utf-8") as out_f:
        json.dump(subagents, out_f, ensure_ascii=False, indent=2)

print(f"Generated b1 to b{len(batches)} subagents JSON files.")
