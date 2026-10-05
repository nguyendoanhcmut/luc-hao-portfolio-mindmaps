import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open("tang_san_boc_dich_binh_thich_scout_manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

rt = manifest.get("routing_table", [])
for c in rt:
    with open(c["section_text_file"], "r", encoding="utf-8") as sf:
        w = len(sf.read().split())
    if w > 3000:
        print(f"{c['chunk_id']}: {c['title']} ({w} words)")
