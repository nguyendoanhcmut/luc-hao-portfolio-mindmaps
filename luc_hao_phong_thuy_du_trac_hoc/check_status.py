import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_phong_thuy_du_trac_hoc"
manifest_path = os.path.join(base_dir, "luc_hao_phong_thuy_du_trac_hoc_scout_manifest.json")

with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

rt = manifest["routing_table"]
done = []
missing = []

for c in rt:
    frag_file = os.path.join(base_dir, c["fragment_file"])
    if os.path.exists(frag_file) and os.path.getsize(frag_file) > 50:
        done.append(c)
    else:
        missing.append(c)

print(f"Total chunks: {len(rt)}")
print(f"Done: {len(done)}")
print(f"Missing: {len(missing)}")
if missing:
    print(f"Next 15 missing chunks:")
    for c in missing[:15]:
        print(f"  - {c['chunk_id']} ({c['title'][:40]}) -> {c['fragment_file']}")
