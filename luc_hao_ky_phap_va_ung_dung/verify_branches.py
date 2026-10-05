import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

manifest_file = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_ky_phap_va_ung_dung\luc_hao_ky_phap_va_ung_dung_scout_manifest.json"
branches_file = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_ky_phap_va_ung_dung\luc_hao_ky_phap_va_ung_dung_branches.md"
base_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_ky_phap_va_ung_dung"

with open(manifest_file, "r", encoding="utf-8") as f:
    manifest = json.load(f)

with open(branches_file, "r", encoding="utf-8") as f:
    md_content = f.read()

lines = md_content.splitlines()

# Extract headings
headings = []
for idx, line in enumerate(lines):
    m = re.match(r'^(#{1,6})\s+(.*)$', line)
    if m:
        level = len(m.group(1))
        title = m.group(2).strip()
        headings.append((level, title, idx + 1))

def norm(text):
    return re.sub(r'[\s\-_–—:：,()（）!！?？\.\$\\\{\}]+', '', text.lower())

skeleton = manifest["master_skeleton"]

print("=================================================================")
print("GATE 1: SECTION COVERAGE AUDIT")
print("=================================================================")

gate1_results = []
all_skeleton_nodes = []

for s_idx, sec in enumerate(skeleton):
    s_title = sec["title"]
    s_lvl = sec["level"]
    s_norm = norm(s_title)
    
    # Match top-level section
    s_matched_hdg = None
    for h_lvl, h_title, lno in headings:
        if h_lvl == s_lvl and (s_norm == norm(h_title) or s_norm in norm(h_title) or norm(h_title) in s_norm):
            s_matched_hdg = (h_lvl, h_title, lno)
            break
            
    all_skeleton_nodes.append({
        "type": "parent",
        "title": s_title,
        "level": s_lvl,
        "matched": s_matched_hdg is not None,
        "match": s_matched_hdg
    })
    
    # Children matching
    for ch in sec.get("children", []):
        ch_title = ch["title"]
        ch_lvl = ch["level"]
        ch_norm = norm(ch_title)
        
        ch_matched_hdg = None
        # Check direct or semantic containment in headings
        for h_lvl, h_title, lno in headings:
            h_norm = norm(h_title)
            if ch_norm == h_norm or ch_norm in h_norm or h_norm in ch_norm:
                ch_matched_hdg = (h_lvl, h_title, lno)
                break
        
        # If not direct match, check significant keywords
        if not ch_matched_hdg:
            # Extract key phrases from title
            # e.g., "Ví dụ: Thai sản (Thiên Trạch Lý - Thiên Thủy Tụng)"
            # tokens: ["thai sản", "thiên trạch lý", "thiên thủy tụng"]
            sub_phrases = re.findall(r'[\w\s]{4,}', ch_title)
            sub_phrases = [p.strip().lower() for p in sub_phrases if len(p.strip()) > 3 and not p.strip().lower().startswith("ví dụ")]
            for h_lvl, h_title, lno in headings:
                matches_count = sum(1 for p in sub_phrases if p in h_title.lower())
                if matches_count >= 1:
                    ch_matched_hdg = (h_lvl, h_title, lno)
                    break
        
        # Check text presence if heading still not found
        in_text = ch_title.lower() in md_content.lower()
        
        all_skeleton_nodes.append({
            "type": "child",
            "parent": s_title,
            "title": ch_title,
            "level": ch_lvl,
            "matched": ch_matched_hdg is not None or in_text,
            "match": ch_matched_hdg,
            "in_text": in_text
        })

total_sections = len(all_skeleton_nodes)
covered_sections = sum(1 for n in all_skeleton_nodes if n["matched"])
s_ratio = covered_sections / total_sections

print(f"Total skeleton nodes: {total_sections}")
print(f"Covered nodes: {covered_sections}")
print(f"Gate 1 Score (S): {s_ratio:.4f}")
for n in all_skeleton_nodes:
    status = "PASS" if n["matched"] else "FAIL"
    detail = n["match"] if n["match"] else ("IN_TEXT" if n.get("in_text") else "MISSING")
    print(f"[{status}] L{n['level']} {n['title']} -> {detail}")

print("\n=================================================================")
print("GATE 2: DEPTH COMPLIANCE AUDIT")
print("=================================================================")

# Depth hierarchy check:
# 1. Single H1 root
# 2. Level 2 chapters match skeleton level 2 count
# 3. Maximum depth and appropriate hierarchy transitions (no level skipping like H1 -> H3)
h1_count = sum(1 for h in headings if h[0] == 1)
h2_count = sum(1 for h in headings if h[0] == 2)
h3_count = sum(1 for h in headings if h[0] == 3)
h4_count = sum(1 for h in headings if h[0] == 4)
h5_count = sum(1 for h in headings if h[0] == 5)

hierarchy_valid = True
invalid_transitions = []
for i in range(len(headings) - 1):
    curr_lvl = headings[i][0]
    next_lvl = headings[i+1][0]
    if next_lvl > curr_lvl + 1:
        hierarchy_valid = False
        invalid_transitions.append((headings[i], headings[i+1]))

print(f"H1 count: {h1_count} (expected 1)")
print(f"H2 count: {h2_count} (expected 14)")
print(f"H3 count: {h3_count}")
print(f"H4 count: {h4_count}")
print(f"H5 count: {h5_count}")
print(f"Hierarchy transitions valid: {hierarchy_valid}")
if invalid_transitions:
    print(f"Invalid transitions found: {len(invalid_transitions)}")
    for t1, t2 in invalid_transitions[:5]:
        print(f"  Line {t1[2]} H{t1[0]} '{t1[1]}' -> Line {t2[2]} H{t2[0]} '{t2[1]}'")

# Example coverage check:
# Check every example case in the scout manifest
example_cases = []
for sec in skeleton:
    for ch in sec.get("children", []):
        if "ví dụ" in ch["title"].lower() or "nghiên cứu thực nghiệm" in ch["title"].lower():
            example_cases.append(ch)

print(f"\nTotal example cases in skeleton: {len(example_cases)}")
covered_examples = 0
for ex in example_cases:
    # check hexagram names or subject in text
    ex_title = ex["title"]
    # Extract hexagram pairs if present
    hex_match = re.search(r'\((.*?)\)', ex_title)
    found = False
    if hex_match:
        hex_names = [h.strip() for h in re.split(r'[-–—]', hex_match.group(1))]
        if all(h.lower() in md_content.lower() for h in hex_names):
            found = True
    else:
        # Check title words
        words = [w for w in re.split(r'[\s:,\-]+', ex_title) if len(w) > 3 and w.lower() != "ví dụ"]
        if all(w.lower() in md_content.lower() for w in words):
            found = True
    if found:
        covered_examples += 1
    print(f"  [{'PASS' if found else 'FAIL'}] {ex_title}")

example_ratio = covered_examples / len(example_cases) if example_cases else 1.0
print(f"Example coverage ratio: {covered_examples}/{len(example_cases)} ({example_ratio:.4f})")

# Heading depth compliance component:
# Score components: single root H1 (0.2), 14 H2 chapters (0.3), no skipped levels (0.2), example coverage (0.3)
depth_structural_score = 0.0
if h1_count == 1:
    depth_structural_score += 0.2
if h2_count == 14:
    depth_structural_score += 0.3
if len(invalid_transitions) == 0:
    depth_structural_score += 0.2
else:
    depth_structural_score += max(0.0, 0.2 - 0.05 * len(invalid_transitions))
depth_structural_score += 0.3 * example_ratio

d_ratio = depth_structural_score
print(f"Gate 2 Score (D): {d_ratio:.4f}")

print("\n=================================================================")
print("GATE 3: CONTENT GROUNDING AUDIT")
print("=================================================================")

# 1. Figure / Asset integrity
all_manifest_figures = []
for sec in skeleton:
    for f in sec.get("figures", []):
        all_manifest_figures.append(f)
    for ch in sec.get("children", []):
        for f in ch.get("figures", []):
            all_manifest_figures.append(f)

verified_assets = 0
for fig in all_manifest_figures:
    fid = fig["id"]
    fn = fig["file_name"]
    full_path = os.path.join(base_dir, fn)
    exists = os.path.exists(full_path)
    in_md = (fid in md_content) or (fn in md_content) or (os.path.basename(fn) in md_content)
    has_caption = fig.get("caption", "") in md_content if fig.get("caption") else True
    
    status = exists and in_md
    if status:
        verified_assets += 1
    print(f"  [{'PASS' if status else 'FAIL'}] {fid}: file={fn} (exists={exists}, in_md={in_md})")

asset_ratio = verified_assets / len(all_manifest_figures) if all_manifest_figures else 1.0
print(f"Asset verification: {verified_assets}/{len(all_manifest_figures)} ({asset_ratio:.4f})")

# 2. Leaf node substantive content check
leaf_headings_info = []
for i in range(len(headings)):
    lvl, title, start_line = headings[i]
    end_line = headings[i+1][2] - 1 if i + 1 < len(headings) else len(lines)
    is_leaf = (i == len(headings) - 1) or (headings[i+1][0] <= lvl)
    if is_leaf:
        section_lines = lines[start_line:end_line]
        body = "\n".join(section_lines)
        word_count = len(body.split())
        has_table = "|" in body
        has_latex = "$" in body
        leaf_headings_info.append({
            "title": title,
            "level": lvl,
            "line": start_line,
            "word_count": word_count,
            "has_table": has_table,
            "has_latex": has_latex
        })

print(f"Total leaf sections: {len(leaf_headings_info)}")
substantive_leaves = sum(1 for l in leaf_headings_info if l["word_count"] >= 20)
print(f"Substantive leaf sections (>=20 words): {substantive_leaves}/{len(leaf_headings_info)}")
leaf_ratio = substantive_leaves / len(leaf_headings_info)

# 3. Grounding checks: tables and math formulas presence
tables_count = sum(1 for l in leaf_headings_info if l["has_table"])
latex_count = sum(1 for l in leaf_headings_info if l["has_latex"])
print(f"Leaf nodes with markdown tables: {tables_count}")
print(f"Leaf nodes with LaTeX math: {latex_count}")

# Gate 3 score: Asset grounding (0.5) + Leaf node specificity (0.5)
e_ratio = 0.5 * asset_ratio + 0.5 * leaf_ratio
print(f"Gate 3 Score (E): {e_ratio:.4f}")

print("\n=================================================================")
print("GATE 4: LEXICON RESOLUTION AUDIT")
print("=================================================================")

key_terms = manifest.get("global_lexicon", {}).get("key_terms", [])
key_entities = manifest.get("global_lexicon", {}).get("key_entities", [])

# Term resolution checking
resolved_terms = 0
for t in key_terms:
    term_name = t["term"]
    definition = t["definition"]
    
    # Check term presence or its natural linguistic variants
    search_patterns = [term_name]
    if " - " in term_name:
        parts = term_name.split(" - ")
        search_patterns.append(" và ".join(parts))
        search_patterns.append(" – ".join(parts))
        search_patterns.extend(parts)
    if "12 cung" in term_name:
        search_patterns.extend(["12 cung", "mười hai cung", "thập nhị cung"])
    if "Bạch Hổ chủ đạo lộ" in term_name:
        search_patterns.extend(["bạch hổ", "đạo lộ", "con đường"])
    if "Chẩn bệnh bất duy Quan quỷ" in term_name:
        search_patterns.extend(["quan quỷ là bệnh", "quan quỷ vi bệnh", "dĩ quan quỷ vi bệnh"])
    
    found_matches = []
    for pat in search_patterns:
        cnt = len(re.findall(re.escape(pat), md_content, re.IGNORECASE))
        if cnt > 0:
            found_matches.append((pat, cnt))
            
    if found_matches:
        resolved_terms += 1
        print(f"  [PASS] '{term_name}' -> matches: {found_matches[:2]}")
    else:
        print(f"  [FAIL] '{term_name}' -> NOT FOUND")

term_ratio = resolved_terms / len(key_terms) if key_terms else 1.0
print(f"Terms resolved: {resolved_terms}/{len(key_terms)} ({term_ratio:.4f})")

resolved_entities = 0
for ent in key_entities:
    name = ent.split("(")[0].strip()
    patterns = [name]
    if "Obuchi Keizo" in name:
        patterns.extend(["Obuchi", "Keizo", "Thủ tướng Nhật", "Thủ tướng Nhật Bản", "Tiểu Uyên Huệ Tam"])
        
    found_matches = []
    for pat in patterns:
        cnt = len(re.findall(re.escape(pat), md_content, re.IGNORECASE))
        if cnt > 0:
            found_matches.append((pat, cnt))
            
    if found_matches:
        resolved_entities += 1
        print(f"  [PASS] '{ent}' -> matches: {found_matches[:2]}")
    else:
        print(f"  [FAIL] '{ent}' -> NOT FOUND")

entity_ratio = resolved_entities / len(key_entities) if key_entities else 1.0
print(f"Entities resolved: {resolved_entities}/{len(key_entities)} ({entity_ratio:.4f})")

l_ratio = 0.5 * term_ratio + 0.5 * entity_ratio
print(f"Gate 4 Score (L): {l_ratio:.4f}")

print("\n=================================================================")
print("TOTAL AUDIT SCORE COMPUTATION")
print("=================================================================")
completeness_score = (0.40 * s_ratio) + (0.30 * d_ratio) + (0.20 * e_ratio) + (0.10 * l_ratio)
is_pass = completeness_score >= 0.95

print(f"S (Section Coverage, 0.40): {s_ratio:.4f}")
print(f"D (Depth Compliance, 0.30): {d_ratio:.4f}")
print(f"E (Content Grounding, 0.20): {e_ratio:.4f}")
print(f"L (Lexicon Resolution, 0.10): {l_ratio:.4f}")
print(f"Weighted Score C: {completeness_score:.4f}")
print(f"Verification Result Pass: {is_pass}")
print("=================================================================")
