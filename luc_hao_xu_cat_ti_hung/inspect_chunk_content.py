import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

manifest = json.load(open('luc_hao_xu_cat_ti_hung_scout_manifest.json', encoding='utf-8'))
figs_dict = {f['id']: f for f in json.load(open('figures_manifest.json', encoding='utf-8'))['figures']}

for c in manifest['routing_table']:
    cid = c['chunk_id']
    fpath = c['section_text_file']
    if not os.path.exists(fpath):
        continue
    text = open(fpath, encoding='utf-8').read()
    lines = text.splitlines()
    # Find all ví dụ headers and image files
    vds = [l.strip() for l in lines if re.match(r'^\s*\*{0,2}(?:Ví dụ|VÍ DỤ|Quẻ)\s*', l, re.IGNORECASE) and len(l.strip()) < 120]
    imgs = [l.strip() for l in lines if 'assets/' in l]
    print(f"[{cid}] '{c['title']}' lines={len(lines)} words={len(text.split())} figs_assigned={len(c['figure_ids'])} imgs_in_text={len(imgs)} vds={len(vds)}")
