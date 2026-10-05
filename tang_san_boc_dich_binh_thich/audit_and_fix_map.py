import json, os, re

mf = json.load(open('tang_san_boc_dich_binh_thich_scout_manifest.json', encoding='utf-8'))
routing = mf['routing_table']

fig_mf = json.load(open('figures_manifest.json', encoding='utf-8'))
by_id = {f['id']: f for f in fig_mf.get('figures', [])}
by_file = {'assets/' + f.get('file_name', ''): f for f in fig_mf.get('figures', [])}

img_pat = re.compile(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]|!\[[^\]]*\]\(([^)\s]+)\)')

report = []
for sec in routing:
    cid = sec['chunk_id']
    ff = sec['fragment_file']
    assigned_ids = sec.get('figure_ids', [])
    assigned_assets = ['assets/' + by_id[i]['file_name'] for i in assigned_ids if i in by_id]
    
    if not os.path.exists(ff):
        report.append(f"{cid} ({ff}): FILE NOT FOUND")
        continue
    
    txt = open(ff, encoding='utf-8').read()
    embedded_assets = []
    for m in img_pat.finditer(txt):
        src = m.group(1) or m.group(2)
        embedded_assets.append(src)
    
    # check differences
    missing = [a for a in assigned_assets if a not in embedded_assets]
    extra = [a for a in embedded_assets if a not in assigned_assets]
    dups = [a for a in set(embedded_assets) if embedded_assets.count(a) > 1]
    
    if missing or extra or dups:
        report.append({
            'chunk_id': cid,
            'file': ff,
            'assigned': assigned_assets,
            'embedded': embedded_assets,
            'missing': missing,
            'extra': extra,
            'internal_dups': dups
        })

print(f"Total chunks with figure discrepancies: {len(report)}")
for r in report:
    print(f"\nChunk: {r['chunk_id']} ({r['file']})")
    if r['missing']: print(f"  Missing: {r['missing']}")
    if r['extra']:   print(f"  Extra:   {r['extra']}")
    if r['internal_dups']: print(f"  Internal Dups: {r['internal_dups']}")
