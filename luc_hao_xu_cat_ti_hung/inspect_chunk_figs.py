import json, sys
sys.stdout.reconfigure(encoding='utf-8')

manifest = json.load(open('luc_hao_xu_cat_ti_hung_scout_manifest.json', encoding='utf-8'))
figs_dict = {f['id']: f for f in json.load(open('figures_manifest.json', encoding='utf-8'))['figures']}

for c in manifest['routing_table']:
    cid = c['chunk_id']
    fids = c['figure_ids']
    fig_info = [f"{fid} (Hình {figs_dict[fid].get('figure_number')}: {figs_dict[fid].get('file_name')})" for fid in fids if fid in figs_dict]
    print(f"[{cid}] lvl={c['start_heading_level']} | title: {c['title']} | figs={len(fids)}")
    if fig_info:
        for fi in fig_info:
            print(f"   -> {fi}")
