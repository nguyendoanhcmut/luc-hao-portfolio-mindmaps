import os
import sys
import json
import re
from collections import Counter
from datetime import datetime, timezone

sys.stdout.reconfigure(encoding='utf-8')

doc_slug = "te_thuyet_luc_hao_du_trac_hoc"
output_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\te_thuyet_luc_hao_du_trac_hoc"
manifest_path = os.path.join(output_dir, f"{doc_slug}_scout_manifest.json")
fig_manifest_path = os.path.join(output_dir, "figures_manifest.json")
branches_path = os.path.join(output_dir, f"{doc_slug}_branches.md")
report_path = os.path.join(output_dir, f"{doc_slug}_verification_report.json")

with open(manifest_path, "r", encoding="utf-8") as f:
    scout_manifest = json.load(f)

with open(fig_manifest_path, "r", encoding="utf-8") as f:
    fig_manifest = json.load(f)

with open(branches_path, "r", encoding="utf-8") as f:
    md_content = f.read()

lines = md_content.splitlines()

# -------------------------------------------------------------
# 1. Section Coverage Audit (Weight: 0.40)
# -------------------------------------------------------------
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

# We separate TOC headings from body headings (TOC is under ## Mục lục up to ## Lời Tựa)
muc_luc_line = None
loi_tua_line = None
for h in headings:
    if norm(h['title']) == 'mụclục':
        muc_luc_line = h['line']
    elif norm(h['title']) == 'lờitựa' and h['level'] == 2:
        loi_tua_line = h['line']

def is_toc_heading(h):
    if muc_luc_line and loi_tua_line:
        return muc_luc_line <= h['line'] < loi_tua_line
    return False

body_headings = [h for h in headings if not is_toc_heading(h)]

matched_sections = []
missing_sections = []

for node in skeleton_nodes:
    s_title = node['title']
    s_norm = norm(s_title)
    clean_s = re.sub(r'^[IVXLCDM]+\.\s*', '', s_title, flags=re.I).strip()
    clean_s_norm = norm(clean_s)
    
    matched = None
    
    # 1. Check body headings first for exact or substring normalized match
    for h in body_headings:
        h_norm = norm(h['title'])
        if s_norm == h_norm or s_norm in h_norm or h_norm in s_norm:
            matched = h
            break
        if clean_s_norm and (clean_s_norm == h_norm or clean_s_norm in h_norm or h_norm in clean_s_norm):
            matched = h
            break
            
    # 2. Key phrases in body headings
    if not matched:
        words = [w for w in re.split(r'[\s:,\-]+', clean_s) if len(w) >= 3]
        if words:
            for h in body_headings:
                if all(w.lower() in h['title'].lower() for w in words):
                    matched = h
                    break
        if not matched and words:
            for h in body_headings:
                if any(w.lower() in h['title'].lower() for w in words if len(w) >= 4):
                    matched = h
                    break

    # 3. If not in body headings, check all headings (including TOC)
    if not matched:
        for h in headings:
            h_norm = norm(h['title'])
            if s_norm == h_norm or s_norm in h_norm or h_norm in s_norm or (clean_s_norm and (clean_s_norm in h_norm or h_norm in clean_s_norm)):
                matched = h
                break

    # 4. In text presence
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
            'match_type': 'heading'
        })
    elif in_text:
        matched_sections.append({
            'skeleton_title': s_title,
            'level': node['level'],
            'matched_heading': 'IN_TEXT',
            'matched_level': None,
            'line': None,
            'match_type': 'in_text'
        })
    else:
        missing_sections.append(s_title)

coverage_score = len(matched_sections) / len(skeleton_nodes) if skeleton_nodes else 1.0

# -------------------------------------------------------------
# 2. Depth Audit (Weight: 0.30)
# -------------------------------------------------------------
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

bullet_depth_dist = Counter(b['depth'] for b in bullets)

h2_indices = [i for i, h in enumerate(headings) if h['level'] == 2]
shallow_sections = []
compliant_sections_count = 0

for idx, h2_idx in enumerate(h2_indices):
    h = headings[h2_idx]
    start_line = h['line']
    end_line = headings[h2_indices[idx + 1]]['line'] - 1 if idx + 1 < len(h2_indices) else len(lines)
    sec_lines = lines[start_line:end_line]
    sec_text = "\n".join(sec_lines)
    sec_headings = [hd for hd in headings if start_line < hd['line'] <= end_line]
    sec_bullets = [b for b in bullets if start_line < b['line'] <= end_line]
    words = len(sec_text.split())
    
    # Condition: sections > 1500 words must have children or nested claim bullets at least 2 levels deep
    has_subheadings = len(sec_headings) > 0
    has_nested_bullets = any(b['depth'] >= 2 for b in sec_bullets)
    
    is_compliant = True
    if words > 1500:
        if not (has_subheadings or has_nested_bullets):
            is_compliant = False
            shallow_sections.append(h['title'])
    else:
        # even for smaller sections, verify non-empty content
        if words < 30 and len(sec_bullets) == 0:
            is_compliant = False
            shallow_sections.append(h['title'])

    if is_compliant:
        compliant_sections_count += 1

depth_score = compliant_sections_count / len(h2_indices) if h2_indices else 1.0

# -------------------------------------------------------------
# 3. Grounding & Figures Audit (Weight: 0.20)
# -------------------------------------------------------------
figs_in_manifest = fig_manifest.get('figures', [])
total_manifest_figs = len(figs_in_manifest)

embedded_figs = []
missing_figs = []
misplaced_figs = []

for fig in figs_in_manifest:
    fid = fig['id']
    fn = fig['file_name']
    rel_path = fig.get('rel_path', f"assets/{fn}")
    caption = fig.get('caption', '')
    
    tag_matches = re.findall(rf'<img[^>]+src=["\']assets/{re.escape(fn)}["\']', md_content)
    if not tag_matches:
        tag_matches = re.findall(rf'<img[^>]+src=["\'][^"\']*{re.escape(os.path.basename(fn))}["\']', md_content)
        
    if tag_matches:
        embedded_figs.append(fid)
    else:
        missing_figs.append(fid)

proof_blocks = re.findall(r'\*\*Hình này chứng minh điều gì\*\*', md_content)
deduct_blocks = re.findall(r'\*\*Từ đâu mà thấy được\*\*', md_content)
hinh_anchors = re.findall(r'-\s+\*\*Hình\s+\d+\b', md_content)

fig_ratio = len(embedded_figs) / total_manifest_figs if total_manifest_figs else 1.0
proof_ratio = len(proof_blocks) / total_manifest_figs if total_manifest_figs else 1.0
grounding_score = min(1.0, 0.5 * fig_ratio + 0.5 * proof_ratio)

vague_cases = []
if len(proof_blocks) < total_manifest_figs:
    vague_cases.append(f"Missing proof blocks: {total_manifest_figs - len(proof_blocks)}")

# -------------------------------------------------------------
# 4. Lexicon Resolution Audit (Weight: 0.10)
# -------------------------------------------------------------
key_terms = scout_manifest.get('global_lexicon', {}).get('key_terms', [])
key_entities = scout_manifest.get('global_lexicon', {}).get('key_entities', [])

declared_lexicon = []
for kt in key_terms:
    term_str = kt['term'] if isinstance(kt, dict) else kt
    declared_lexicon.append({'type': 'term', 'name': term_str})

for ke in key_entities:
    entity_str = ke['entity'] if isinstance(ke, dict) else ke
    declared_lexicon.append({'type': 'entity', 'name': entity_str})

resolved_lexicon = []
unresolved_lexicon = []

for item in declared_lexicon:
    name = item['name']
    clean_name = re.sub(r'\(.*?\)', '', name).strip()
    
    patterns = [name, clean_name]
    if ' & ' in name:
        patterns.extend(name.split(' & '))
    if ' - ' in name:
        patterns.extend(name.split(' - '))
    if '/' in name:
        patterns.extend(name.split('/'))
        
    found_count = 0
    matched_patterns = []
    for pat in patterns:
        pat = pat.strip()
        if not pat:
            continue
        c = len(re.findall(re.escape(pat), md_content, re.IGNORECASE))
        if c > 0:
            found_count += c
            matched_patterns.append(pat)
            
    if found_count > 0:
        resolved_lexicon.append({'name': name, 'count': found_count, 'matched_patterns': matched_patterns})
    else:
        unresolved_lexicon.append(name)

lexicon_score = len(resolved_lexicon) / len(declared_lexicon) if declared_lexicon else 1.0

# -------------------------------------------------------------
# 5. Completeness Score Computation
# -------------------------------------------------------------
# C = 0.40 * coverage + 0.30 * depth + 0.20 * grounding + 0.10 * lexicon
completeness_score = round(
    0.40 * coverage_score + 
    0.30 * depth_score + 
    0.20 * grounding_score + 
    0.10 * lexicon_score, 
    4
)

is_pass = (completeness_score >= 0.95) and (len(missing_sections) == 0) and (len(missing_figs) == 0)

# Build standard report structure matching portfolio conventions
report_data = {
    "completeness_score": completeness_score,
    "pass": is_pass,
    "gate_scores": {
        "section_coverage": {
            "score": round(coverage_score, 4),
            "observed": len(matched_sections),
            "expected": len(skeleton_nodes),
            "missing": missing_sections
        },
        "depth": {
            "score": round(depth_score, 4),
            "compliant": compliant_sections_count,
            "total": len(h2_indices),
            "shallow": shallow_sections
        },
        "grounding": {
            "score": round(grounding_score, 4),
            "grounded": len(proof_blocks),
            "total": total_manifest_figs,
            "vague": vague_cases,
            "misplaced_figures": misplaced_figs
        },
        "lexicon": {
            "score": round(lexicon_score, 4),
            "resolved": len(resolved_lexicon),
            "declared": len(declared_lexicon),
            "unresolved": unresolved_lexicon
        }
    },
    "audit_metadata": {
        "doc_slug": doc_slug,
        "doc_title": scout_manifest.get("doc_title", "Tế Thuyết Lục Hào Dự Trắc Học"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_headings": len(headings),
        "heading_distribution": {
            f"H{lvl}": sum(1 for h in headings if h['level'] == lvl)
            for lvl in range(1, 7)
        },
        "total_lines": len(lines),
        "total_bullets": len(bullets),
        "bullet_depth_distribution": {f"depth_{k}": v for k, v in sorted(bullet_depth_dist.items())},
        "figures_audit": {
            "total_figures_manifest": total_manifest_figs,
            "embedded_figures": len(embedded_figs),
            "anchor_claims": len(hinh_anchors),
            "proof_blocks": len(proof_blocks),
            "deduction_blocks": len(deduct_blocks),
            "missing_figures": missing_figs
        },
        "lexicon_audit": {
            "key_terms_count": len(key_terms),
            "key_entities_count": len(key_entities),
            "resolved_terms_count": len([r for r in resolved_lexicon if any((kt['term'] if isinstance(kt, dict) else kt) == r['name'] for kt in key_terms)]),
            "resolved_entities_count": len([r for r in resolved_lexicon if any((ke['entity'] if isinstance(ke, dict) else ke) == r['name'] for ke in key_entities)])
        }
    },
    "remediation_directives": []
}

with open(report_path, "w", encoding="utf-8") as f:
    json.dump(report_data, f, indent=2, ensure_ascii=False)

print(f"Successfully generated verification report: {report_path}")
print(f"Completeness Score (C): {completeness_score}")
print(f"Pass Status: {is_pass}")
print("Gate Breakdown:")
print(f"  - Section Coverage (40%): {coverage_score:.4f} ({len(matched_sections)}/{len(skeleton_nodes)})")
print(f"  - Depth (30%): {depth_score:.4f} ({compliant_sections_count}/{len(h2_indices)})")
print(f"  - Grounding (20%): {grounding_score:.4f} ({len(proof_blocks)}/{total_manifest_figs} proof blocks, {len(embedded_figs)}/{total_manifest_figs} figures)")
print(f"  - Lexicon (10%): {lexicon_score:.4f} ({len(resolved_lexicon)}/{len(declared_lexicon)})")
