import json, glob, os, re

# Load manifest routing
mf = json.load(open('tang_san_boc_dich_binh_thich_scout_manifest.json', encoding='utf-8'))
routing = mf['routing_table']

frag_files = [sec['fragment_file'] for sec in routing]

asset_to_frags = {}
img_pat = re.compile(r'assets/([^\s"\'\)]+)')

for ff in frag_files:
    if not os.path.exists(ff): continue
    txt = open(ff, encoding='utf-8').read()
    found_in_ff = set()
    for m in img_pat.finditer(txt):
        asset = 'assets/' + m.group(1)
        asset_to_frags.setdefault(asset, []).append((ff, txt.count(asset)))

dups = {k: v for k, v in asset_to_frags.items() if len(v) > 1 or (len(v) == 1 and v[0][1] > 1)}
print(f'Duplicate assets: {len(dups)}')
for k, v in sorted(dups.items()):
    print(f'  {k}: {v}')

# Now check which sections are assigned the missing figures
fig_mf = json.load(open('figures_manifest.json', encoding='utf-8'))
by_id = {f['id']: f for f in fig_mf.get('figures', [])}

missing_ids = ['fig_07', 'fig_10', 'fig_11', 'fig_32', 'fig_104', 'fig_106', 'fig_108', 'fig_109', 'fig_110', 'fig_112', 'fig_113', 'fig_114']
print('\nMissing figures assignment:')
for sec in routing:
    for fid in missing_ids:
        if fid in sec.get('figure_ids', []):
            fig_info = by_id.get(fid, {})
            print(f"  {fid} ({fig_info.get('file_name')}): assigned to {sec['chunk_id']} -> {sec['fragment_file']}")
