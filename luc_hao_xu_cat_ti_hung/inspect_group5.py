import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
from parse_utils import clean_lines

m = json.load(open('luc_hao_xu_cat_ti_hung_scout_manifest.json', encoding='utf-8'))
figs_dict = {f['id']: f for f in json.load(open('figures_manifest.json', encoding='utf-8'))['figures']}

for c in m['routing_table']:
    cid = c['chunk_id']
    if cid in ['ch14_1', 'ch14_2', 'ch14_3', 'ch14_4', 'ch14_5', 'ch14_6', 'ch14_7', 'ch14_8']:
        print(f"\n=================== [{cid}] {c['title']} ===================")
        text = open(c['section_text_file'], encoding='utf-8').read()
        cleaned = clean_lines(text)
        paras = [p.strip() for p in cleaned.split('\n\n') if p.strip()]
        for i, p in enumerate(paras):
            if re.match(r'^\*{0,2}(?:Ví dụ|Quẻ|Một ví dụ khác|##)\b', p, re.IGNORECASE) or '![' in p:
                print(f"P{i}: {p[:110]}...")
