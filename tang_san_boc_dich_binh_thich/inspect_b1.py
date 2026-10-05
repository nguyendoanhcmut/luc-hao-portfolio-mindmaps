import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open("tang_san_boc_dich_binh_thich_scout_manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

with open("figures_manifest.json", "r", encoding="utf-8") as f:
    fig_manifest = json.load(f)

fig_map = {f["id"]: f for f in fig_manifest.get("figures", [])}

rt = manifest.get("routing_table", [])
for i in range(15):
    c = rt[i]
    f_ids = c.get("figure_ids", [])
    fig_details = [f"{fid}: {fig_map[fid]['rel_path']} ({fig_map[fid]['figure_number']} - {fig_map[fid]['caption']})" for fid in f_ids if fid in fig_map]
    print(f"[{i:02d}] {c['chunk_id']} | lvl={c['start_heading_level']} | title={c['title']} | file={c['fragment_file']}")
    if fig_details:
        print("     Figs:", fig_details)
