import json
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

def run_audit():
    manifest_p = r'the_gioi_nhan_qua_scout_manifest.json'
    branches_p = r'the_gioi_nhan_qua_branches.md'

    with open(manifest_p, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    with open(branches_p, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # 1. Section coverage
    def get_skeleton_items(items):
        res = []
        for item in items:
            res.append(item)
            if 'children' in item and item['children']:
                res.extend(get_skeleton_items(item['children']))
        return res

    all_skel = get_skeleton_items(manifest['master_skeleton'])
    headings = re.findall(r'^(#{1,6})\s+(.+)$', md_content, flags=re.MULTILINE)
    md_heading_texts = [h[1].strip() for h in headings]
    md_heading_map = {h[1].strip().lower(): h[0] for h in headings}

    matched_skeleton = []
    unmatched_skeleton = []
    for s in all_skel:
        stitle = s['title'].strip()
        # check exact or case-insensitive or substring
        found = False
        matched_h = None
        for h in md_heading_texts:
            if stitle.lower() == h.lower() or stitle.lower() in h.lower() or h.lower() in stitle.lower():
                found = True
                matched_h = h
                break
        if found:
            matched_skeleton.append({'skeleton_title': stitle, 'heading_found': matched_h})
        else:
            unmatched_skeleton.append(stitle)

    coverage_score = len(matched_skeleton) / len(all_skel) if all_skel else 1.0

    # 2. Depth check
    # Check tree structure, heading depths, claim hierarchies, bullet indentations
    # Let's inspect max heading level, distribution of headings, bullet nesting
    heading_levels = [len(h[0]) for h in headings]
    max_h_level = max(heading_levels) if heading_levels else 0
    min_h_level = min(heading_levels) if heading_levels else 0
    h_level_dist = {i: heading_levels.count(i) for i in range(1, 7)}

    # Bullet depth distribution
    bullet_lines = re.findall(r'^(\s*)[-*+]\s+(.*)$', md_content, flags=re.MULTILINE)
    bullet_depths = [len(b[0]) // 2 for b in bullet_lines]
    bullet_depth_dist = {}
    for d in bullet_depths:
        bullet_depth_dist[d] = bullet_depth_dist.get(d, 0) + 1

    # Check that subsections have claims and sub-bullets
    # Proper depth means: chapters -> subheadings / cases -> claims -> evidence / details
    # Let's check average bullet depth, presence of multi-level hierarchies across sections
    has_deep_hierarchy = (max_h_level >= 3) and (max(bullet_depths) >= 2) and (len(bullet_lines) > 500)

    # Depth score assessment
    # Does every major section have at least subsections/bullets?
    depth_score = 1.0 if has_deep_hierarchy and min(h_level_dist.get(1, 0), h_level_dist.get(2, 0)) >= 1 else 0.85

    # 3. Grounding check
    # Leaf bullets name specific Lục Hào concepts, formulas, outcomes, terms. Figure blocks supported.
    # Check figure blocks:
    # Look for figure mentions or blocks like [fig_...] or Figure / Quẻ / etc.
    all_manifest_figs = []
    for s in all_skel:
        if 'figure_ids' in s:
            all_manifest_figs.extend(s['figure_ids'])

    figure_references = re.findall(r'(fig_\d+|hình \d+|quẻ|hào|hào quẻ)', md_content, flags=re.IGNORECASE)
    # Check explicit figure block mentions
    fig_blocks = re.findall(r'fig_\d+', md_content, flags=re.IGNORECASE)
    unique_manifest_figs = set(all_manifest_figs)
    unique_found_figs = set(f.lower() for f in fig_blocks)

    # Leaf bullets naming specific concepts, formulas, outcomes, terms
    # Look for Luc Hao terminology in bullets
    luc_hao_terms_regex = re.compile(
        r'(Thế hào|Ứng hào|Dụng thần|Phụ Mẫu|Huynh Đệ|Tử Tôn|Thê Tài|Quan Quỷ|'
        r'Thanh Long|Chu Tước|Câu Trận|Đằng Xà|Bạch Hổ|Huyền Vũ|'
        r'Tý|Sửu|Dần|Mão|Thìn|Tị|Ngọ|Mùi|Thân|Dậu|Tuất|Hợi|'
        r'Giáp|Ất|Bính|Đinh|Mậu|Kỷ|Canh|Tân|Nhâm|Quý|'
        r'Tuần Không|Không Vong|Nguyệt phá|Nhật xung|hóa thoái|hóa tiến|'
        r'tương xung|tương hợp|tam hợp|tam hình|phục tàng|phi thần|phục thần|'
        r'độc phát|tuyệt|mộ|sinh|khắc|vượng|suy)',
        re.IGNORECASE
    )

    grounded_bullets = 0
    leaf_bullets = 0
    for indent, text in bullet_lines:
        leaf_bullets += 1
        if luc_hao_terms_regex.search(text):
            grounded_bullets += 1

    grounding_ratio = grounded_bullets / leaf_bullets if leaf_bullets else 0
    # Figure coverage
    fig_coverage = len(unique_found_figs.intersection(set(f.lower() for f in unique_manifest_figs))) / len(unique_manifest_figs) if unique_manifest_figs else 1.0

    # Grounding score: bullet domain grounding + figure support
    grounding_score = min(1.0, 0.7 * (grounding_ratio / 0.5 if grounding_ratio < 0.5 else 1.0) + 0.3 * fig_coverage)

    # 4. Lexicon check
    # Key terms in global_lexicon found in tree
    lexicon = manifest.get('global_lexicon', {})
    key_terms = []
    if isinstance(lexicon, dict):
        if 'key_terms' in lexicon:
            for item in lexicon['key_terms']:
                if isinstance(item, dict) and 'term' in item:
                    key_terms.append(item['term'])
                elif isinstance(item, str):
                    key_terms.append(item)
        if 'key_entities' in lexicon:
            key_terms.extend(lexicon['key_entities'])
    elif isinstance(lexicon, list):
        key_terms.extend(lexicon)

    lexicon_matches = {}
    for term in key_terms:
        # Search for term in markdown
        count = len(re.findall(re.escape(term), md_content, flags=re.IGNORECASE))
        lexicon_matches[term] = count

    matched_lex = [t for t, c in lexicon_matches.items() if c > 0]
    lexicon_score = len(matched_lex) / len(key_terms) if key_terms else 1.0

    # Completeness Score:
    # C = 0.40 * coverage + 0.30 * depth + 0.20 * grounding + 0.10 * lexicon
    C = 0.40 * coverage_score + 0.30 * depth_score + 0.20 * grounding_score + 0.10 * lexicon_score

    res = {
        'coverage': {
            'total_skeleton': len(all_skel),
            'matched': len(matched_skeleton),
            'unmatched': unmatched_skeleton,
            'score': round(coverage_score, 4)
        },
        'depth': {
            'heading_levels': h_level_dist,
            'bullet_depth_dist': bullet_depth_dist,
            'total_bullets': len(bullet_lines),
            'score': round(depth_score, 4)
        },
        'grounding': {
            'total_bullets': leaf_bullets,
            'grounded_bullets': grounded_bullets,
            'grounding_ratio': round(grounding_ratio, 4),
            'manifest_figs_count': len(unique_manifest_figs),
            'found_figs_count': len(unique_found_figs),
            'fig_coverage': round(fig_coverage, 4),
            'score': round(grounding_score, 4)
        },
        'lexicon': {
            'total_terms': len(key_terms),
            'matched_terms': len(matched_lex),
            'terms_detail': lexicon_matches,
            'score': round(lexicon_score, 4)
        },
        'overall_score': round(C, 4),
        'passed': C >= 0.95
    }

    # Check figures_manifest.json
    import os
    figures_manifest = {}
    if os.path.exists('figures_manifest.json'):
        with open('figures_manifest.json', 'r', encoding='utf-8') as f:
            figures_manifest = json.load(f)
    print(f"figures_manifest loaded, type: {type(figures_manifest)}, count: {len(figures_manifest)}")

    # Let's inspect manifest figure_ids
    print(f"Total manifest figure_ids across skeleton: {len(all_manifest_figs)}")
    print(f"Sample manifest figure_ids: {all_manifest_figs[:10]}")

    # In markdown, let's look for figure blocks
    # E.g. **Hình X.** or img src or figure blocks
    hinh_matches = re.findall(r'\*\*Hình\s+(\d+)\b', md_content, re.IGNORECASE)
    print(f"Found **Hình X** matches: {len(hinh_matches)}")
    print(f"Sample Hình matches: {hinh_matches[:10]}")

    # Check mapping between fig_id and Hình X
    # In scout manifest, figure_ids are like 'fig_001', 'fig_1', etc.? Let's check format
    # In manifest: fig_168, etc. Notice that fig_1 -> Hình 1, fig_168 -> Hình 168!
    manifest_fig_nums = set()
    for fid in all_manifest_figs:
        m = re.search(r'\d+', fid)
        if m:
            manifest_fig_nums.add(int(m.group(0)))

    found_fig_nums = set(int(x) for x in hinh_matches)
    print(f"Unique manifest figure numbers: {len(manifest_fig_nums)}")
    print(f"Unique found figure numbers in md: {len(found_fig_nums)}")
    matched_figs = manifest_fig_nums.intersection(found_fig_nums)
    print(f"Matched figures: {len(matched_figs)} / {len(manifest_fig_nums)}")
    missing_figs = sorted(list(manifest_fig_nums - found_fig_nums))
    print(f"Missing figures (first 10): {missing_figs[:10]}")

    # Also check img tags
    img_matches = re.findall(r'<img[^>]+>', md_content, re.IGNORECASE)
    print(f"Total <img> tags in branches.md: {len(img_matches)}")

if __name__ == '__main__':
    run_audit()
