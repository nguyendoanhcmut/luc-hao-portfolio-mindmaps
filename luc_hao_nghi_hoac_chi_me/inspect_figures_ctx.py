import json
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

m = json.load(open('luc_hao_nghi_hoac_chi_me_scout_manifest.json', encoding='utf-8'))
fm = json.load(open('figures_manifest.json', encoding='utf-8'))

fig_by_id = {f['id']: f for f in fm['figures']}
fig_num = 1
for chunk in m['routing_table']:
    for fid in chunk['figure_ids']:
        fig_by_id[fid]['global_num'] = fig_num
        fig_num += 1

chunk = m['routing_table'][1] # ch02_1
txt = open(chunk['section_text_file'], encoding='utf-8').read()

for fid in chunk['figure_ids']:
    f = fig_by_id[fid]
    fn = f['file_name']
    pos = txt.find(fn)
    before = txt[max(0, pos-300):pos]
    after = txt[pos+len(fn):min(len(txt), pos+500)]
    print('----------------------------------------')
    print(f"{f['id']} (Hình {f['global_num']}. {f['caption']}):")
    print('BEFORE:', before.replace('\n', ' ')[-150:])
    print('AFTER:', after.replace('\n', ' ')[:200])
