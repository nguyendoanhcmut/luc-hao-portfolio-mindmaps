import json
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

with open("te_thuyet_luc_hao_du_trac_hoc_branches.md", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()

# Extract all headings
headings = []
for idx, line in enumerate(lines):
    m = re.match(r'^(#{1,6})\s+(.*)$', line)
    if m:
        headings.append({
            'level': len(m.group(1)),
            'title': m.group(2).strip(),
            'line': idx + 1
        })

print(f"Total headings: {len(headings)}")
for lvl in range(1, 7):
    c = sum(1 for h in headings if h['level'] == lvl)
    print(f"  H{lvl}: {c}")

# Check bullets and indentations
bullets = []
for idx, line in enumerate(lines):
    m = re.match(r'^(\s*)[-*+]\s+(.*)$', line)
    if m:
        indent = len(m.group(1))
        # Usually 2 spaces per indent level
        bullets.append({
            'line': idx + 1,
            'indent': indent,
            'depth': indent // 2,
            'text': m.group(2)
        })

print(f"Total bullets: {len(bullets)}")
bullet_depth_dist = Counter(b['depth'] for b in bullets)
print("Bullet depth distribution:")
for d, count in sorted(bullet_depth_dist.items()):
    print(f"  Depth {d} (indent {d*2} spaces): {count}")

# Check sections by H2
h2_indices = [i for i, h in enumerate(headings) if h['level'] == 2]
print(f"\nTotal H2 sections: {len(h2_indices)}")

shallow_sections = []
compliant_h2 = 0

for i, h2_idx in enumerate(h2_indices):
    h = headings[h2_idx]
    start_line = h['line']
    end_line = headings[h2_indices[i + 1]]['line'] - 1 if i + 1 < len(h2_indices) else len(lines)
    
    sec_lines = lines[start_line:end_line]
    sec_text = "\n".join(sec_lines)
    words = len(sec_text.split())
    
    # Children headings
    child_hdgs = [hd for hd in headings if start_line < hd['line'] <= end_line]
    
    # Nested bullets in this section
    sec_bullets = [b for b in bullets if start_line < b['line'] <= end_line]
    max_bullet_depth = max([b['depth'] for b in sec_bullets]) if sec_bullets else 0
    has_nested_bullets = any(b['depth'] >= 2 for b in sec_bullets)
    has_subheadings = len(child_hdgs) > 0
    
    is_compliant = True
    if words > 1500:
        # Prompt: "Sections > 1500 words must have children or nested claim bullets at least 2 levels deep."
        if not (has_subheadings or has_nested_bullets):
            is_compliant = False
            shallow_sections.append({
                'title': h['title'],
                'words': words,
                'child_hdgs': len(child_hdgs),
                'max_bullet_depth': max_bullet_depth
            })
    
    if is_compliant:
        compliant_h2 += 1

print(f"H2 compliance: {compliant_h2} / {len(h2_indices)}")
if shallow_sections:
    print("Shallow sections:", shallow_sections)

# Also check by chunks / routing_table if relevant
