import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
m = json.load(open('luc_hao_du_trac_ngo_trung_ngo_scout_manifest.json', encoding='utf-8'))
fm = json.load(open('figures_manifest.json', encoding='utf-8'))
fdict = {f['id']: f for f in fm['figures']}

for c in m['routing_table']:
    figs = c['figure_ids']
    print(f"=== {c['chunk_id']} ({len(figs)} figs): {c['title']} ===")
    for fid in figs:
        f = fdict[fid]
        print(f"   {fid}: #{f.get('figure_number')} | {f['file_name']} | {f.get('caption', '')[:40]}")
