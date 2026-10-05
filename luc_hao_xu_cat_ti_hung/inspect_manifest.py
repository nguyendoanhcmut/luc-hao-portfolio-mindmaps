import json, sys
sys.stdout.reconfigure(encoding='utf-8')

m = json.load(open('luc_hao_xu_cat_ti_hung_scout_manifest.json', encoding='utf-8'))
rt = m.get('routing_table', [])
print(f"Total chunks: {len(rt)}")
for c in rt:
    print(f"{c['chunk_id']:6s} lvl={c['start_heading_level']} figs={len(c.get('figure_ids', [])):2d} file={c['fragment_file']} title='{c['title']}'")
