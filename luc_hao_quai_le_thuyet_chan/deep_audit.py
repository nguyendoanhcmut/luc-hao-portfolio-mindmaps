import os
import sys
import json
import re
from collections import Counter

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

print("=================================================================")
print("GATE 2: DEPTH AUDIT")
print("=================================================================")

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

# Bullet statistics
bullets = []
for idx, line in enumerate(lines):
    m = re.match(r'^(\s*)[-*+]\s+(.*)$', line)
    if m:
        indent = len(m.group(1))
        bullets.append({
            'line': idx + 1,
            'indent': indent,
            'depth': indent // 2,
            'text': m.group(2)
        })

print(f"Total lines: {len(lines)}")
print(f"Total headings: {len(headings)}")
print(f"Total bullets: {len(bullets)}")

bullet_depth_dist = Counter(b['depth'] for b in bullets)
print("Bullet depth distribution:")
for d in sorted(bullet_depth_dist.keys()):
    print(f"  Indent depth {d}: {bullet_depth_dist[d]} bullets")

# Check section depth and children
# Every H2 should have content, subsections (or bullets)
h2_indices = [i for i, h in enumerate(headings) if h['level'] == 2]
h2_sections_info = []

for idx, h2_idx in enumerate(h2_indices):
    h = headings[h2_idx]
    start_line = h['line']
    end_line = headings[h2_indices[idx + 1]]['line'] - 1 if idx + 1 < len(h2_indices) else len(lines)
    sec_lines = lines[start_line:end_line]
    sec_text = "\n".join(sec_lines)
    sec_headings = [hd for hd in headings if start_line < hd['line'] <= end_line]
    sec_bullets = [b for b in bullets if start_line < b['line'] <= end_line]
    
    words = len(sec_text.split())
    is_compliant = (len(sec_headings) > 0 or len(sec_bullets) >= 5) and words >= 50
    h2_sections_info.append({
        'title': h['title'],
        'line': start_line,
        'headings_count': len(sec_headings),
        'bullets_count': len(sec_bullets),
        'word_count': words,
        'compliant': is_compliant
    })

shallow_h2 = [s for s in h2_sections_info if not s['compliant']]
print(f"\nH2 sections: {len(h2_sections_info)}")
print(f"Compliant H2 sections: {len(h2_sections_info) - len(shallow_h2)}")
if shallow_h2:
    print("Shallow H2 sections:", shallow_h2)
else:
    print("All H2 sections have extensive depth and subsections/bullets!")

print("=================================================================")
print("GATE 3: GROUNDING & FIGURE INTEGRITY AUDIT")
print("=================================================================")

# 1. Figures audit
# Figures manifest
figs_in_manifest = fig_manifest.get('figures', [])
print(f"Total figures in figures_manifest.json: {len(figs_in_manifest)}")

embedded_figs = []
missing_figs = []

for fig in figs_in_manifest:
    fid = fig['id']
    fn = fig['file_name']
    rel_path = fig.get('rel_path', '')
    caption = fig.get('caption', '')
    
    # check in markdown
    fn_base = os.path.basename(fn)
    found_in_md = (fn in md_content) or (fn_base in md_content) or (rel_path in md_content)
    
    # check disk existence
    abs_path = fig.get('abs_path')
    if not abs_path or not os.path.exists(abs_path):
        # try dir_path/assets/fn_base or dir_path/fn_base
        cand1 = os.path.join(dir_path, 'assets', fn_base)
        cand2 = os.path.join(dir_path, fn)
        if os.path.exists(cand1):
            abs_path = cand1
        elif os.path.exists(cand2):
            abs_path = cand2
    
    disk_exists = os.path.exists(abs_path) if abs_path else False
    
    if found_in_md:
        embedded_figs.append({
            'id': fid,
            'file': fn,
            'disk_exists': disk_exists,
            'caption': caption
        })
    else:
        missing_figs.append({
            'id': fid,
            'file': fn,
            'disk_exists': disk_exists,
            'caption': caption
        })

print(f"Figures embedded in branches.md: {len(embedded_figs)} / {len(figs_in_manifest)}")
if missing_figs:
    print(f"Missing figures ({len(missing_figs)}): {[f['id'] for f in missing_figs]}")
else:
    print("All figures from manifest are embedded in branches.md!")

# Check Markdown figure tags count
md_img_markdown = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', md_content)
md_img_html = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', md_content)
total_embedded_tags = len(md_img_markdown) + len(md_img_html)
print(f"Total markdown image tags: {len(md_img_markdown)}")
print(f"Total HTML img tags: {len(md_img_html)}")
print(f"Total image references in branches.md: {total_embedded_tags}")

# Check anchor claims / evidence blocks around figures
# Check pattern of evidence blocks or analysis under figures
proof_blocks = re.findall(r'\*\*([^*]+(?:chứng minh|nghiệm chứng|phân tích|quái tượng|luận giải)[^*]*)\*\*', md_content, re.IGNORECASE)
print(f"Evidence / proof / analysis bold anchors found: {len(proof_blocks)}")

# Check dialogues, dates, hexagram examples
hex_mentions = re.findall(r'(Thuần Càn|Thuần Khôn|Thủy Lôi Truân|Sơn Thủy Mông|Thủy Thiên Nhu|Thiên Thủy Tụng|Địa Thủy Sư|Thủy Địa Tỷ|Phong Thiên Tiểu Súc|Thiên Trạch Lý|Địa Thiên Thái|Thiên Địa Bĩ|Hỏa Thiên Đại Hữu|Thiên Sơn Độn|Hỏa Lôi Phệ Hạp|Sơn Hỏa Bí|Sơn Địa Bác|Địa Lôi Phục|Thiên Lôi Vô Vọng|Sơn Lôi Di|Trạch Phong Đại Quá|Thuần Khảm|Thuần Ly|Trạch Sơn Hàm|Lôi Phong Hằng|Thiên Sơn Độn|Lôi Thiên Đại Tráng|Hỏa Địa Tấn|Địa Hỏa Minh Di|Phong Hỏa Gia Nhân|Hỏa Trạch Khuê|Thủy Sơn Kiển|Lôi Thủy Giải|Sơn Trạch Tổn|Phong Lôi Ích|Trạch Thiên Quải|Thiên Phong Cấu|Trạch Địa Tụy|Địa Phong Thăng|Trạch Thủy Khốn|Thủy Phong Tỉnh|Trạch Hỏa Cách|Hỏa Phong Đỉnh|Thuần Chấn|Thuần Cấn|Thuần Tốn|Thuần Đoài|Phong Thủy Hoán|Thủy Trạch Tiết|Phong Trạch Trung Phu|Lôi Trạch Quy Muội|Lôi Hỏa Phong|Hỏa Sơn Lữ|Phong Sơn Tiệm|Lôi Địa Dự|Địa Lôi Phục)', md_content)
print(f"Hexagram names mentioned: {len(hex_mentions)}")

# Dates mentions (ngày, tháng, năm can chi)
date_mentions = re.findall(r'(ngày\s+[A-ZÀ-Ỵa-zà-ỹ]+\s+[a-zà-ỹ]+|tháng\s+[A-ZÀ-Ỵa-zà-ỹ]+\s+[a-zà-ỹ]+|năm\s+[A-ZÀ-Ỵa-zà-ỹ]+\s+[a-zà-ỹ]+)', md_content, re.IGNORECASE)
print(f"Date / Can Chi mentions: {len(date_mentions)}")

# Dialogues mentions ("...", ông nói, tôi nói, hỏi:, đáp:)
dialogue_markers = re.findall(r'(người xin đoán hỏi|tôi trả lời|tôi nói|ông ta nói|bà ấy nói|khách hỏi|tôi đoán|đoán rằng|nghiệm chứng:)', md_content, re.IGNORECASE)
print(f"Dialogue / Case markers: {len(dialogue_markers)}")

# Luc Hao domain grounding terms in bullets
luc_hao_terms_regex = re.compile(
    r'(Thế hào|Ứng hào|Dụng thần|Phụ Mẫu|Huynh Đệ|Tử Tôn|Thê Tài|Quan Quỷ|'
    r'Thanh Long|Chu Tước|Câu Trận|Câu Trần|Đằng Xà|Bạch Hổ|Huyền Vũ|'
    r'Tý|Sửu|Dần|Mão|Thìn|Tị|Ngọ|Mùi|Thân|Dậu|Tuất|Hợi|'
    r'Giáp|Ất|Bính|Đinh|Mậu|Kỷ|Canh|Tân|Nhâm|Quý|'
    r'Tuần Không|Không Vong|Nguyệt phá|Nhật xung|hóa thoái|hóa tiến|'
    r'tương xung|tương hợp|tam hợp|tam hình|phục tàng|phi thần|phục thần|'
    r'độc phát|tuyệt|mộ|sinh|khắc|vượng|suy|quái|hào|quẻ|phong thủy|hóa giải)',
    re.IGNORECASE
)
grounded_bullets = sum(1 for b in bullets if luc_hao_terms_regex.search(b['text']))
print(f"Grounded bullets: {grounded_bullets} / {len(bullets)} ({grounded_bullets/len(bullets):.4f})")

print("=================================================================")
print("GATE 4: LEXICON RESOLUTION AUDIT")
print("=================================================================")

key_terms = scout_manifest.get('global_lexicon', {}).get('key_terms', [])
key_entities = scout_manifest.get('global_lexicon', {}).get('key_entities', [])

print(f"Total key terms: {len(key_terms)}")
resolved_terms = []
unresolved_terms = []

for kt in key_terms:
    term_str = kt['term'] if isinstance(kt, dict) else kt
    # Search in markdown
    # Strip parentheses or split alternatives
    variants = [term_str]
    clean_t = re.sub(r'\(.*?\)', '', term_str).strip()
    if clean_t and clean_t != term_str:
        variants.append(clean_t)
    if '/' in term_str:
        variants.extend(term_str.split('/'))
    if ' - ' in term_str:
        variants.extend(term_str.split(' - '))
        
    found_count = 0
    for v in variants:
        v = v.strip()
        if not v:
            continue
        c = len(re.findall(re.escape(v), md_content, re.IGNORECASE))
        found_count += c
        
    if found_count > 0:
        resolved_terms.append((term_str, found_count))
    else:
        unresolved_terms.append(term_str)

print(f"Resolved terms: {len(resolved_terms)} / {len(key_terms)}")
for t, c in resolved_terms:
    print(f"  [FOUND {c:3d}x] {t}")
if unresolved_terms:
    print(f"Unresolved terms: {unresolved_terms}")

print(f"\nTotal key entities: {len(key_entities)}")
resolved_entities = []
unresolved_entities = []

for ke in key_entities:
    clean_e = re.sub(r'\(.*?\)', '', ke).strip()
    variants = [ke, clean_e]
    found_count = 0
    for v in variants:
        v = v.strip()
        if not v:
            continue
        c = len(re.findall(re.escape(v), md_content, re.IGNORECASE))
        found_count += c
        
    if found_count > 0:
        resolved_entities.append((ke, found_count))
    else:
        unresolved_entities.append(ke)

print(f"Resolved entities: {len(resolved_entities)} / {len(key_entities)}")
for e, c in resolved_entities:
    print(f"  [FOUND {c:3d}x] {e}")
if unresolved_entities:
    print(f"Unresolved entities: {unresolved_entities}")

