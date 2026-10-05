import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

dir_path = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_quai_le_thuyet_chan"
manifest_path = os.path.join(dir_path, "luc_hao_quai_le_thuyet_chan_scout_manifest.json")
fig_manifest_path = os.path.join(dir_path, "figures_manifest.json")
branches_path = os.path.join(dir_path, "luc_hao_quai_le_thuyet_chan_branches.md")

with open(manifest_path, "r", encoding="utf-8") as f:
    scout_manifest = json.load(f)

with open(fig_manifest_path, "r", encoding="utf-8") as f:
    fig_manifest = json.load(f)

with open(branches_path, "r", encoding="utf-8") as f:
    md_content = f.read()

print("=== SKELETON ANALYSIS ===")
def extract_nodes(items, parent=None):
    res = []
    for item in items:
        node = {'title': item['title'], 'level': item.get('level', 2), 'parent': parent, 'item': item}
        res.append(node)
        if 'children' in item and item['children']:
            res.extend(extract_nodes(item['children'], item['title']))
    return res

all_nodes = extract_nodes(scout_manifest['master_skeleton'])
print(f"Total skeleton nodes: {len(all_nodes)}")
for i, n in enumerate(all_nodes):
    print(f"  {i}: lvl {n['level']}, parent: {n['parent'][:20] if n['parent'] else 'None'} -> {n['title']}")

print("\n=== HEADINGS IN BRANCHES MD ===")
headings = []
lines = md_content.splitlines()
for idx, line in enumerate(lines):
    m = re.match(r'^(#{1,6})\s+(.*)$', line)
    if m:
        headings.append({
            'level': len(m.group(1)),
            'title': m.group(2).strip(),
            'line': idx + 1
        })
print(f"Total headings in branches.md: {len(headings)}")
for h in headings[:25]:
    print(f"  Line {h['line']}: H{h['level']} {h['title']}")

print("\n=== HEADING LEVEL DISTRIBUTION ===")
from collections import Counter
counts = Counter(h['level'] for h in headings)
for lvl in sorted(counts.keys()):
    print(f"  H{lvl}: {counts[lvl]}")

