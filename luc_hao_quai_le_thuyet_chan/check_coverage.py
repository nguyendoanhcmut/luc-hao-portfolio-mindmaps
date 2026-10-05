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

lines = md_content.splitlines()

# Extract headings
headings = []
for idx, line in enumerate(lines):
    m = re.match(r'^(#{1,6})\s+(.*)$', line)
    if m:
        headings.append({
            'level': len(m.group(1)),
            'title': m.group(2).strip(),
            'line': idx + 1
        })

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

skeleton_nodes = extract_skeleton_nodes(scout_manifest['master_skeleton'])

print("=== CHECKING SECTION COVERAGE ===")
matched_nodes = []
unmatched_nodes = []

for idx, node in enumerate(skeleton_nodes):
    s_title = node['title']
    s_lvl = node['level']
    s_norm = norm(s_title)
    
    matched = None
    for h in headings:
        h_norm = norm(h['title'])
        if s_norm == h_norm or s_norm in h_norm or h_norm in s_norm:
            matched = h
            break
            
    if not matched:
        # Check sub-phrases
        words = [w for w in re.split(r'[\s:,\-]+', s_title) if len(w) > 3]
        for h in headings:
            if any(w.lower() in h['title'].lower() for w in words):
                matched = h
                break
                
    if not matched:
        # Check in text
        if s_norm in norm(md_content):
            matched = {'level': 'text', 'title': 'Found in text body', 'line': 0}
            
    if matched:
        matched_nodes.append((node, matched))
        print(f"[MATCH] Skel: '{s_title}' (lvl {s_lvl}) -> Found H{matched['level'] if isinstance(matched, dict) and 'level' in matched else '?'}: '{matched.get('title') if isinstance(matched, dict) else matched}' (line {matched.get('line') if isinstance(matched, dict) else '?'})")
    else:
        unmatched_nodes.append(node)
        print(f"[MISSING] Skel: '{s_title}' (lvl {s_lvl})")

print(f"\nCoverage: {len(matched_nodes)} / {len(skeleton_nodes)} ({len(matched_nodes)/len(skeleton_nodes):.4f})")
if unmatched_nodes:
    print("Unmatched:", [n['title'] for n in unmatched_nodes])

