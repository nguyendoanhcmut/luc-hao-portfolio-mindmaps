import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
from parse_utils import clean_lines

def analyze_chunk(cid, fpath):
    text = open(fpath, encoding='utf-8').read()
    cleaned = clean_lines(text)
    paras = [p.strip() for p in cleaned.split('\n\n') if p.strip()]
    print(f"\n=================== {cid} ===================")
    for i, p in enumerate(paras):
        if re.match(r'^\*{0,2}(?:Ví dụ|Quẻ|Một ví dụ khác)\b', p, re.IGNORECASE) or '![' in p:
            print(f"P{i}: {p[:100]}...")

for cid in ['ch05', 'ch06', 'ch07', 'ch08', 'ch09']:
    analyze_chunk(cid, f"fragments/src/{cid}.txt")
