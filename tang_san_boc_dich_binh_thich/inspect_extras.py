import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

mf = json.load(open('tang_san_boc_dich_binh_thich_scout_manifest.json', encoding='utf-8'))
routing = {c['chunk_id']: c for c in mf['routing_table']}
targets = ['ch22_0', 'ch22_1', 'ch22_3', 'ch23', 'ch30', 'ch31', 'ch34', 'ch35_0', 'ch37', 'ch38', 'ch40', 'ch41_1', 'ch41_3']

for cid in targets:
    c = routing[cid]
    ff = c['fragment_file']
    lines = open(ff, encoding='utf-8').readlines()
    print(f'=== {cid}: {ff} ===')
    for i, line in enumerate(lines):
        if 'img' in line or 'assets/' in line:
            start = max(0, i-4)
            end = min(len(lines), i+6)
            print(f'Around line {i+1}:')
            for j in range(start, end):
                print(f'{j+1}: {lines[j]}', end='')
            print('---')
