import json, sys
sys.stdout.reconfigure(encoding='utf-8')

m = json.load(open('luc_hao_xu_cat_ti_hung_scout_manifest.json', encoding='utf-8'))
figs_dict = {f['id']: f for f in json.load(open('figures_manifest.json', encoding='utf-8'))['figures']}
for c in m['routing_table']:
    if c['chunk_id'] in ['ch05', 'ch06', 'ch07', 'ch08', 'ch09']:
        print(f"[{c['chunk_id']}] {c['title']}")
        for fid in c['figure_ids']:
            f = figs_dict[fid]
            print(f"   {fid} (Hình {f['figure_number']}): {f['caption']}")
