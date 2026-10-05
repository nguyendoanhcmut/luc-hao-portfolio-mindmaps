import json, os, re, glob
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, r'C:\Users\Admin\.gemini\config\skills\branches\scripts')
import verify_lineage

passed, errors, warnings = verify_lineage.audit('.')
print(f'Total errors: {len(errors)}')

mf = json.load(open('tang_san_boc_dich_binh_thich_scout_manifest.json', encoding='utf-8'))
routing = mf['routing_table']
sec_by_cid = {s['chunk_id']: s for s in routing}

fig_mf = json.load(open('figures_manifest.json', encoding='utf-8'))
by_id = {f['id']: f for f in fig_mf.get('figures', [])}
by_file = {'assets/' + f.get('file_name', ''): f for f in fig_mf.get('figures', [])}

# Figure assignments in manifest
fig_owner = {}
for sec in routing:
    for fid in sec.get('figure_ids', []):
        fig_owner[fid] = sec['chunk_id']

# 1. Missing figures (not embedded)
missing_errs = [e for e in errors if 'is not embedded' in e]
print(f'\n--- MISSING FIGURES ({len(missing_errs)}) ---')
for e in missing_errs:
    m = re.search(r'figure (fig_\d+)', e)
    if m:
        fid = m.group(1)
        finfo = by_id.get(fid, {})
        owner = fig_owner.get(fid, 'UNKNOWN')
        frag = sec_by_cid.get(owner, {}).get('fragment_file', '')
        print(f"  {fid} ({finfo.get('file_name')}, {finfo.get('caption', '')[:30]}): OWNER={owner} -> {frag}")

# 2. Duplicate embeds
dup_errs = [e for e in errors if 'Duplicate embed' in e]
print(f'\n--- DUPLICATE EMBEDS ({len(dup_errs)}) ---')
for e in dup_errs:
    m = re.search(r"Duplicate embed of '([^']+)'", e)
    if m:
        asset = m.group(1)
        fid = by_file.get(asset, {}).get('id', 'UNKNOWN')
        owner = fig_owner.get(fid, 'UNKNOWN')
        # find where it is embedded
        where = []
        for sec in routing:
            fpath = sec['fragment_file']
            if os.path.exists(fpath):
                cnt = open(fpath, encoding='utf-8').read().count(asset)
                if cnt > 0:
                    where.append((sec['chunk_id'], fpath, cnt))
        print(f"  {asset} ({fid}): TRUE_OWNER={owner} | FOUND_IN={where}")

# 3. No anchor claim / outside figure block
anchor_errs = [e for e in errors if 'no anchor claim' in e]
print(f'\n--- NO ANCHOR / OUTSIDE BLOCK ({len(anchor_errs)}) ---')
for e in anchor_errs:
    print(f"  {e}")
