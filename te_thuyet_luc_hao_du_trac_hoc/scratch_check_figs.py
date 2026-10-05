import sys
import os
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

manifest_path = 'te_thuyet_luc_hao_du_trac_hoc_scout_manifest.json'
with open(manifest_path, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

chunks_with_figs = [rt for rt in manifest.get('routing_table', []) if rt.get('figure_ids')]
print(f'Total chunks with figures: {len(chunks_with_figs)}')
for c in chunks_with_figs[:5]:
    print(c['chunk_id'], c['title'], c['figure_ids'], c['fragment_file'])

# Let's inspect the fragment file for ch06
ch06_file = chunks_with_figs[0]['fragment_file']
print(f"\n--- Checking {ch06_file} ---")
if os.path.exists(ch06_file):
    with open(ch06_file, 'r', encoding='utf-8') as f:
        content = f.read()
    print("Length:", len(content))
    print("Content preview:")
    print(content[:1500])
else:
    print("File does not exist!")
