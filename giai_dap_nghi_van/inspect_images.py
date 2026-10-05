import os
import re
import json

output_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\giai_dap_nghi_van"
manifest_path = os.path.join(output_dir, "giai_dap_nghi_van_scout_manifest.json")
figures_manifest_path = os.path.join(output_dir, "figures_manifest.json")

with open(manifest_path, "r", encoding="utf-8") as f:
    scout = json.load(f)
with open(figures_manifest_path, "r", encoding="utf-8") as f:
    fm = json.load(f)

fig_map = {f["id"]: f for f in fm["figures"]}
img_pat = re.compile(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]|!\[[^\]]*\]\(([^)\s]+)\)')

for c in scout["routing_table"]:
    frag_path = os.path.join(output_dir, c["fragment_file"])
    with open(frag_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = []
    for m in img_pat.finditer(content):
        src = m.group(1) or m.group(2)
        matches.append(src)
    
    print(f"=== {c['chunk_id']} ===")
    print(f"Assigned figures: {c['figure_ids']}")
    print(f"Found images ({len(matches)}): {matches}")
