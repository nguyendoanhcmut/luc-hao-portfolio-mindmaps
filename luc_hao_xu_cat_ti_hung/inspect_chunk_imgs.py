import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

manifest = json.load(open('luc_hao_xu_cat_ti_hung_scout_manifest.json', encoding='utf-8'))
figs_dict = {f['id']: f for f in json.load(open('figures_manifest.json', encoding='utf-8'))['figures']}

for c in manifest['routing_table']:
    cid = c['chunk_id']
    fpath = c['section_text_file']
    text = open(fpath, encoding='utf-8').read()
    
    # find images and captions
    img_matches = list(re.finditer(r'!\[([^\]]*)\]\((assets/[^)]+)\)', text))
    if img_matches:
        print(f"\n=== [{cid}] {c['title']} (figs={len(img_matches)}) ===")
        for m in img_matches:
            cap = m.group(1)
            src = m.group(2)
            fname = os.path.basename(src)
            # find corresponding figure
            fid = None
            for f in c['figure_ids']:
                if figs_dict[f]['file_name'] == fname:
                    fid = f
                    break
            print(f"  * {fname} -> {fid} (cap: {cap[:40]})")
