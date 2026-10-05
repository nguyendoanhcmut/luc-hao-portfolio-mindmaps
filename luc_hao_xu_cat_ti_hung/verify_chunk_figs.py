import json, re

manifest = json.load(open('luc_hao_xu_cat_ti_hung_scout_manifest.json', encoding='utf-8'))
figs_manifest = json.load(open('figures_manifest.json', encoding='utf-8'))
figs_dict = {f['id']: f for f in figs_manifest['figures']}

for c in manifest['routing_table']:
    cid = c['chunk_id']
    if not c['figure_ids']:
        continue
    txt = open(c['section_text_file'], encoding='utf-8').read()
    # find all image tags
    imgs = re.findall(r'!\[([^\]]*)\]\((assets/[^)]+)\)', txt)
    print(f"[{cid}] assigned={len(c['figure_ids'])}, found_in_txt={len(imgs)}")
    for fid in c['figure_ids']:
        fn = figs_dict[fid]['file_name']
        found = fn in txt
        if not found:
            print(f"  MISSING {fid} ({fn}) in {cid}")
