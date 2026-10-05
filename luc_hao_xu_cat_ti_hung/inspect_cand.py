import json

d = json.load(open('candidates.json', encoding='utf-8'))
with open('cand_list.txt', 'w', encoding='utf-8') as f:
    for i, c in enumerate(d.get('candidates', [])):
        f.write(f"{i:2d}: line {c['line']}, page {c.get('page')}, lvl {c.get('level')}: {c['text']}\n")
print(f"Wrote {len(d['candidates'])} candidates.")
