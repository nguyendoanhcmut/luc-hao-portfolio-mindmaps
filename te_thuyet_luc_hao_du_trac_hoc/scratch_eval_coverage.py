import os
import sys
import json
import re
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

manifest_path = "te_thuyet_luc_hao_du_trac_hoc_scout_manifest.json"
fig_manifest_path = "figures_manifest.json"
branches_path = "te_thuyet_luc_hao_du_trac_hoc_branches.md"

with open(manifest_path, "r", encoding="utf-8") as f:
    scout_manifest = json.load(f)

with open(fig_manifest_path, "r", encoding="utf-8") as f:
    fig_manifest = json.load(f)

with open(branches_path, "r", encoding="utf-8") as f:
    md_content = f.read()

lines = md_content.splitlines()

# 1. Section Coverage
headings = []
for idx, line in enumerate(lines):
    m = re.match(r'^(#{1,6})\s+(.*)$', line)
    if m:
        headings.append({
            'level': len(m.group(1)),
            'title': m.group(2).strip(),
            'line': idx + 1
        })

print(f"Total headings in branches.md: {len(headings)}")

def norm(text):
    return re.sub(r'[\s\-_–—:：,()（）!！?？\.\$\\\{\}]+', '', text.lower())

def extract_skeleton_nodes(items, parent=None):
    res = []
    for item in items:
        node = {'title': item['title'], 'level': item.get('level', 2), 'parent': parent, 'item': item}
        res.append(node)
        if 'children' in item and item['children']:
            res.extend(extract_skeleton_nodes(item['children'], item['title']))
    return res

skeleton_nodes = extract_skeleton_nodes(scout_manifest.get('master_skeleton', []))
print(f"Total skeleton nodes in master_skeleton: {len(skeleton_nodes)}")

matched_sections = []
missing_sections = []

for node in skeleton_nodes:
    s_title = node['title']
    s_norm = norm(s_title)
    matched = None
    
    # 1. Direct normalized equality or substring in heading titles
    for h in headings:
        h_norm = norm(h['title'])
        if s_norm == h_norm or s_norm in h_norm or h_norm in s_norm:
            matched = h
            break
            
    # 2. Key phrases
    if not matched:
        words = [w for w in re.split(r'[\s:,\-]+', s_title) if len(w) > 3]
        for h in headings:
            if any(w.lower() in h['title'].lower() for w in words):
                matched = h
                break

    if matched:
        matched_sections.append({
            'skeleton_title': s_title,
            'level': node['level'],
            'matched_heading': matched['title'],
            'matched_level': matched['level'],
            'line': matched['line']
        })
    else:
        missing_sections.append(s_title)

coverage_score = len(matched_sections) / len(skeleton_nodes) if skeleton_nodes else 1.0
print(f"\n--- Gate 1: Coverage ---")
print(f"Matched: {len(matched_sections)} / {len(skeleton_nodes)} (Score: {coverage_score:.4f})")
if missing_sections:
    print(f"Missing sections: {missing_sections}")

# Also check routing table titles
rt_titles = [rt['title'] for rt in scout_manifest.get('routing_table', [])]
print(f"Total routing_table entries: {len(rt_titles)}")
rt_matched = 0
rt_missing = []
for t in rt_titles:
    t_norm = norm(t)
    matched = False
    for h in headings:
        h_norm = norm(h['title'])
        if t_norm == h_norm or t_norm in h_norm or h_norm in t_norm:
            matched = True
            break
    if not matched:
        words = [w for w in re.split(r'[\s:,\-]+', t) if len(w) > 3]
        for h in headings:
            if any(w.lower() in h['title'].lower() for w in words):
                matched = True
                break
    if matched:
        rt_matched += 1
    else:
        rt_missing.append(t)
print(f"Routing table matched: {rt_matched} / {len(rt_titles)}")
if rt_missing:
    print(f"Routing table missing: {rt_missing}")
