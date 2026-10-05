import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open("tang_san_boc_dich_binh_thich_scout_manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

rt = manifest.get("routing_table", [])
print(f"Total chunks: {len(rt)}")
print(f"Master skeleton sections: {len(manifest.get('master_skeleton', []))}")
for i, c in enumerate(rt[:30]):
    print(f"[{i:03d}] id={c.get('chunk_id')} | lvl={c.get('start_heading_level')} | figs={len(c.get('figure_ids', []))} | ex={len(c.get('exercises', []))} | title={c.get('title')[:40]}")
