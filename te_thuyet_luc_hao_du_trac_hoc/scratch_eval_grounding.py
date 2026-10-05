import json
import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

with open("figures_manifest.json", "r", encoding="utf-8") as f:
    fig_manifest = json.load(f)

with open("te_thuyet_luc_hao_du_trac_hoc_branches.md", "r", encoding="utf-8") as f:
    text = f.read()

figs = fig_manifest.get('figures', [])
print(f"Total figures in figures_manifest.json: {len(figs)}")

# Check embedding of each figure
missing_figs = []
found_figs = []

for fig in figs:
    fid = fig['id']
    fn = fig['file_name']
    rel_path = fig.get('rel_path', f"assets/{fn}")
    fnum = fig.get('figure_number')
    
    # Check if img tag is present with src=rel_path or fn
    # Pattern: <img src="assets/page_XXXX_img_YY.png"
    if fn in text or rel_path in text:
        found_figs.append(fig)
    else:
        missing_figs.append(fig)

print(f"Found figures by filename: {len(found_figs)} / {len(figs)}")
if missing_figs:
    print("Missing figures:", [f['id'] for f in missing_figs])

# Check Hình anchors
# e.g., - **Hình 1.**
hinh_anchors = re.findall(r'-\s+\*\*Hình\s+(\d+)\.', text)
print(f"Total - **Hình X.** anchors: {len(hinh_anchors)}")
print(f"Unique Hình numbers found: {len(set(hinh_anchors))}")

# Check proof blocks
proof_blocks = re.findall(r'\*\*Hình này chứng minh điều gì\*\*', text)
deduct_blocks = re.findall(r'\*\*Từ đâu mà thấy được\*\*', text)
print(f"Total '**Hình này chứng minh điều gì**': {len(proof_blocks)}")
print(f"Total '**Từ đâu mà thấy được**': {len(deduct_blocks)}")

# Check leaf grounding (specific concepts / terms)
# Check bullets that are leaves (indented bullets with content)
lines = text.splitlines()
leaf_bullets = []
for i in range(len(lines)):
    line = lines[i]
    m = re.match(r'^(\s*)[-*+]\s+(.*)$', line)
    if m:
        indent = len(m.group(1))
        content = m.group(2).strip()
        # check if next line is not more indented
        is_leaf = True
        if i + 1 < len(lines):
            next_m = re.match(r'^(\s*)[-*+]\s+(.*)$', lines[i+1])
            if next_m and len(next_m.group(1)) > indent:
                is_leaf = False
        if is_leaf:
            leaf_bullets.append(content)

print(f"Total leaf bullets: {len(leaf_bullets)}")

# Check if leaves name specific concepts/terms (non-trivial length, specific domain terms)
domain_terms = [
    "quẻ", "hào", "quái", "chi", "can", "ngũ hành", "thế", "ứng", "dụng", "nguyên thần",
    "kỵ thần", "cừu thần", "nhật", "nguyệt", "không vong", "tuần không", "phục thần",
    "phi thần", "động", "biến", "tiến", "thoái", "hợp", "xung", "hình", "tam hợp",
    "phản ngâm", "phục ngâm", "du hồn", "quy hồn", "thần", "tử tôn", "huynh đệ",
    "thê tài", "quan quỷ", "phụ mẫu", "thanh long", "chu tước", "câu trần", "đằng xà",
    "bạch hổ", "huyền vũ", "thổ", "kim", "thủy", "hỏa", "mộc", "tý", "sửu", "dần",
    "mão", "thìn", "tị", "ngọ", "mùi", "thân", "dậu", "tuất", "hợi"
]

grounded_leaves = 0
vague_leaves = []
for leaf in leaf_bullets:
    # ignore pure image tag or anchor lines
    if leaf.startswith('<img') or leaf.startswith('**Hình') or leaf.startswith('**Từ đâu') or leaf.startswith('**Hình này'):
        grounded_leaves += 1
        continue
    # check length and specific terms
    has_term = any(t in leaf.lower() for t in domain_terms)
    if has_term and len(leaf) > 10:
        grounded_leaves += 1
    else:
        # short or vague bullet
        if len(leaf) < 15:
            vague_leaves.append(leaf)
        else:
            grounded_leaves += 1

print(f"Grounded leaf bullets: {grounded_leaves} / {len(leaf_bullets)}")
print(f"Vague leaf bullets count: {len(vague_leaves)}")
if vague_leaves:
    print("Sample vague leaves:", vague_leaves[:5])
