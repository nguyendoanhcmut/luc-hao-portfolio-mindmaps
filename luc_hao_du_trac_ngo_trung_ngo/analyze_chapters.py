import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')
m = json.load(open('luc_hao_du_trac_ngo_trung_ngo_scout_manifest.json', encoding='utf-8'))
fm = json.load(open('figures_manifest.json', encoding='utf-8'))
fdict = {f['id']: f for f in fm['figures']}

for c in m['routing_table']:
    cid = c['chunk_id']
    title = c['title']
    fig_ids = c['figure_ids']
    raw = open(c['section_text_file'], encoding='utf-8').read()
    
    # Check paragraphs
    paragraphs = [p.strip() for p in raw.split('\n\n') if p.strip()]
    non_table_p = [p for p in paragraphs if not p.startswith('|')]
    
    # Check dialogues
    dialogues = [p for p in non_table_p if '"' in p or '“' in p or '”' in p]
    
    # Check outcomes
    outcomes = [p for p in non_table_p if any(w in p.lower() for w in ['thực tế', 'ứng nghiệm', 'kết quả', 'sau đó', 'về sau', 'sau này'])]
    
    print(f"{cid:5s}: {title[:30]:30s} | {len(fig_ids):2d} figs | {len(non_table_p):2d} paras | {len(dialogues):2d} dial | {len(outcomes):2d} out")
