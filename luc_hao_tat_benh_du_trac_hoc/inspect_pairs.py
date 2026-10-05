import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
m = json.load(open('luc_hao_tat_benh_du_trac_hoc_scout_manifest.json', encoding='utf-8'))
rt = {r['chunk_id']: r for r in m['routing_table']}
pairs = [
    ('ch03_1', 'ch03_2'),
    ('ch03_5', 'ch03_6'),
    ('ch03_8', 'ch03_9'),
    ('ch03_10', 'ch03_11'),
    ('ch03_12', 'ch03_14'),
    ('ch03_16', 'ch03_17'),
    ('ch03_18', 'ch03_19'),
    ('ch03_20', 'ch03_21'),
    ('ch03_22', 'ch03_23')
]

for a, b in pairs:
    ra = rt[a]
    rb = rt[b]
    print(f'{a}: title="{ra["title"]}", fids={ra["figure_ids"]}')
    print(f'{b}: title="{rb["title"]}", fids={rb["figure_ids"]}')
