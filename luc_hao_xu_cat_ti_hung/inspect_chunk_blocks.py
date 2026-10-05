import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
from parse_utils import clean_lines

manifest = json.load(open('luc_hao_xu_cat_ti_hung_scout_manifest.json', encoding='utf-8'))

for c in manifest['routing_table']:
    cid = c['chunk_id']
    raw = open(c['section_text_file'], encoding='utf-8').read()
    cleaned = clean_lines(raw)
    paragraphs = [p.strip() for p in cleaned.split('\n\n') if p.strip()]
    
    # Check paragraphs that start with Ví dụ, Quẻ, or image
    ex_count = 0
    img_count = 0
    for p in paragraphs:
        if re.match(r'^\*{0,2}(?:Ví dụ|VÍ DỤ|Quẻ|Một ví dụ khác)\b', p, re.IGNORECASE):
            ex_count += 1
        if '![' in p:
            img_count += 1
    print(f"[{cid}] '{c['title'][:30]}' total_paras={len(paragraphs)}, ex_markers={ex_count}, imgs={img_count}, assigned_figs={len(c['figure_ids'])}")
