import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("te_thuyet_luc_hao_du_trac_hoc_scout_manifest.json", "r", encoding="utf-8") as f:
    scout_manifest = json.load(f)

with open("te_thuyet_luc_hao_du_trac_hoc_branches.md", "r", encoding="utf-8") as f:
    md_content = f.read()

lines = md_content.splitlines()

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

skeleton_nodes = extract_skeleton_nodes(scout_manifest.get('master_skeleton', []))

matched_sections = []
missing_sections = []

for node in skeleton_nodes:
    s_title = node['title']
    s_norm = norm(s_title)
    
    # Strip roman numerals or leading numbers like "I. ", "1. ", "Chương 1: " for flexible matching
    clean_s = re.sub(r'^[IVXLCDM]+\.\s*', '', s_title, flags=re.I).strip()
    clean_s_norm = norm(clean_s)
    
    matched = None
    # 1. Direct normalized equality or substring in heading titles
    for h in headings:
        h_norm = norm(h['title'])
        if s_norm == h_norm or s_norm in h_norm or h_norm in s_norm:
            matched = h
            break
        if clean_s_norm and (clean_s_norm == h_norm or clean_s_norm in h_norm or h_norm in clean_s_norm):
            matched = h
            break
            
    # 2. Key phrases
    if not matched:
        words = [w for w in re.split(r'[\s:,\-]+', clean_s) if len(w) >= 3]
        if words:
            for h in headings:
                # check if majority or all keywords match
                if all(w.lower() in h['title'].lower() for w in words):
                    matched = h
                    break
        if not matched and words:
            for h in headings:
                if any(w.lower() in h['title'].lower() for w in words if len(w) >= 4):
                    matched = h
                    break

    # 3. Text presence
    in_text = False
    if not matched:
        if clean_s.lower() in md_content.lower() or s_title.lower() in md_content.lower():
            in_text = True

    if matched:
        matched_sections.append({
            'skeleton_title': s_title,
            'level': node['level'],
            'matched_heading': matched['title'],
            'matched_level': matched['level'],
            'line': matched['line'],
            'type': 'heading'
        })
    elif in_text:
        matched_sections.append({
            'skeleton_title': s_title,
            'level': node['level'],
            'matched_heading': 'IN_TEXT',
            'matched_level': None,
            'line': None,
            'type': 'in_text'
        })
    else:
        missing_sections.append(s_title)

print(f"Total skeleton nodes: {len(skeleton_nodes)}")
print(f"Matched sections: {len(matched_sections)}")
print(f"Missing sections: {len(missing_sections)}")
if missing_sections:
    print("Missing:", missing_sections)
for m in matched_sections:
    if m['type'] == 'in_text' or 'Lục Hợp' in m['skeleton_title'] or 'Tam Hợp' in m['skeleton_title'] or 'Hồn' in m['skeleton_title']:
        print(f"  {m['skeleton_title']} -> {m['matched_heading']} ({m['type']})")
