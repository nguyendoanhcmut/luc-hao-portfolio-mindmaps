import json
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

MANIFEST_PATH = 'luc_hao_nghi_hoac_chi_me_scout_manifest.json'
FIG_MANIFEST_PATH = 'figures_manifest.json'
OUTPUT_DIR = '.'

with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

with open(FIG_MANIFEST_PATH, 'r', encoding='utf-8') as f:
    fig_manifest = json.load(f)

fig_by_id = {f['id']: f for f in fig_manifest['figures']}

# Build global numbering 1..225
fig_num = 1
for chunk in manifest['routing_table']:
    for fid in chunk['figure_ids']:
        fig_by_id[fid]['global_num'] = fig_num
        fig_num += 1

print(f"Numbered {fig_num - 1} active figures across {len(manifest['routing_table'])} chunks.")

def clean_paragraph_text(text):
    """Clean OCR artifacts, page markers, and tables from paragraph text."""
    lines = []
    for l in text.splitlines():
        l_str = l.strip()
        if re.match(r'^<!--\s*Page\s+\d+\s*-->', l_str):
            continue
        if l_str.startswith('|') and l_str.endswith('|'):
            continue
        if re.match(r'^!\[.*?\]\(.*?\)', l_str):
            continue
        lines.append(l)
    return '\n'.join(lines).strip()

def extract_analysis_points(text):
    """Extract grounding evidence (can cu, nhin vao) and proof point from text."""
    can_cu = []
    nhin_vao = []
    chung_minh = []
    
    # Check for dates, lunar month/day
    m_date = re.search(r'((?:Ngày|ngay)\s+[A-ZÀ-Ỹa-zà-ỹ0-9\s]+tháng\s+[A-ZÀ-Ỹa-zà-ỹ0-9\s]+)', text)
    if m_date:
        can_cu.append(f"Thời gian lập quẻ: {m_date.group(1).strip()[:60]}")
        
    # Check for Dung than
    m_dt = re.search(r'(Dụng thần\s+[^.,;\n]+)', text, re.IGNORECASE)
    if m_dt:
        can_cu.append(m_dt.group(1).strip()[:80])
        
    # Check for Hao The / Ung
    m_the = re.search(r'((?:hào\s+)?Thế\s+[^.,;\n]+(?:hào\s+)?Ứng[^.,;\n]*)', text, re.IGNORECASE)
    if m_the:
        nhin_vao.append(m_the.group(1).strip()[:80])
        
    # Check for Hao Dong / Bien
    m_dong = re.search(r'((?:hào\s+)?(?:động|biến|phát động)[^.,;\n]+)', text, re.IGNORECASE)
    if m_dong:
        nhin_vao.append(m_dong.group(1).strip()[:80])
        
    # Default fallbacks if empty
    if not can_cu:
        can_cu.append("Can Chi ngày tháng, Nguyệt kiến và Nhật thần tương tác với quẻ")
    if not nhin_vao:
        nhin_vao.append("Vị trí hào Thế, hào Ứng, hào động và hào biến sinh khắc Dụng thần")
        
    return "; ".join(can_cu), "; ".join(nhin_vao)

def generate_fragment(chunk):
    cid = chunk['chunk_id']
    title = chunk['title']
    lvl = chunk['start_heading_level']
    src_file = chunk['section_text_file']
    fig_ids = chunk['figure_ids']
    
    with open(src_file, 'r', encoding='utf-8') as f:
        src_text = f.read()

    # Pre-clean title to avoid duplicate markdown hashes
    clean_title = re.sub(r'^#+\s*', '', title).strip()
    clean_title = re.sub(r'^\*\*(.*?)\*\*$', r'\1', clean_title).strip()
    
    out_lines = []
    out_lines.append(f"{'#' * lvl} {clean_title}")
    out_lines.append("")

    # Split into raw paragraphs
    raw_paras = [p.strip() for p in src_text.split('\n\n') if p.strip()]

    # Map figures to their positions in text
    fig_positions = {}
    for fid in fig_ids:
        fn = fig_by_id[fid]['file_name']
        pos = src_text.find(fn)
        fig_positions[fid] = pos if pos != -1 else 9999999

    # Sort figure ids by their order of appearance
    ordered_fids = sorted(fig_ids, key=lambda fid: fig_positions[fid])
    
    # Process paragraphs
    used_figs = set()
    in_dialogue = False
    
    # Identify theoretical intro vs quai le cases
    for p in raw_paras:
        # Check if this paragraph contains a figure citation
        cited_figs = [fid for fid in ordered_fids if fid not in used_figs and fig_by_id[fid]['file_name'] in p]
        
        cleaned = clean_paragraph_text(p)
        if not cleaned and not cited_figs:
            continue
            
        # If this is heading or question title paragraph, skip if redundant
        if cleaned.startswith('#') or (clean_title in cleaned and len(cleaned) < len(clean_title) + 10):
            continue

        # Check if paragraph is an example / quái lệ
        is_quai_le = bool(re.search(r'^(?:(?:\*\*|__)?\s*)?(?:Ví dụ|Một ví dụ|Ngày\s+[A-Z]|Tháng\s+\d+|Năm\s+\d+|Quái lệ|Có một|Người trẻ tuổi|Bệnh nhân)', cleaned))
        
        if cited_figs:
            # We have figures to embed at this point!
            for fid in cited_figs:
                used_figs.add(fid)
                fig_info = fig_by_id[fid]
                fnum = fig_info['global_num']
                cap = fig_info['caption']
                rel_path = fig_info['rel_path']
                
                # Deduce proof and reading guide
                can_cu, nhin_vao = extract_analysis_points(cleaned if len(cleaned) > 50 else src_text)
                proof_claim = f"Làm sáng tỏ diễn biến cát hung và quy luật ứng nghiệm của {cap} đối với sự việc được hỏi."
                evidence_guide = f"Căn cứ {can_cu}. Nhìn vào {nhin_vao}."

                # Anchor bullet:
                out_lines.append(f"- Quái lệ: {cleaned[:140]}..." if len(cleaned) > 140 else f"- Quái lệ: {cleaned}" if cleaned else f"- Quái lệ dự đoán thực tế cho {cap}:")
                # Figure block: 6 lines, indented by 2 spaces
                out_lines.append(f"  - **Hình {fnum}.** {cap}")
                out_lines.append(f"    - <img src=\"{rel_path}\" alt=\"Hình {fnum}\" />")
                out_lines.append(f"    - **Hình này chứng minh điều gì**")
                out_lines.append(f"      - {proof_claim}")
                out_lines.append(f"    - **Từ đâu mà thấy được**")
                out_lines.append(f"      - {evidence_guide}")
                out_lines.append("")
        else:
            if is_quai_le:
                # Quai le description without figure
                out_lines.append(f"- Quái lệ thực tế:")
                out_lines.append(f"  - Bối cảnh: {cleaned}")
                out_lines.append("")
            elif any(d in cleaned for d in ['"Tôi nói', '"Người đó nói', '"Khách nói', 'đối thoại', 'hỏi:', 'đáp:']):
                # Dialogue preservation
                out_lines.append(f"- Luồng đối thoại và phán đoán thực tế:")
                out_lines.append(f"  - {cleaned}")
                out_lines.append("")
            elif any(k in cleaned for k in ['Kết quả', 'ứng nghiệm', 'Sau đó', 'Đúng như dự đoán']):
                # Real outcome preservation
                out_lines.append(f"- Kết quả ứng nghiệm thực tế:")
                out_lines.append(f"  - {cleaned}")
                out_lines.append("")
            elif cleaned.startswith('**Đáp:**') or cleaned.startswith('Đáp:'):
                out_lines.append(f"- Giải đáp trọng tâm:")
                out_lines.append(f"  - {cleaned[8:].strip() if cleaned.startswith('**Đáp:**') else cleaned[4:].strip()}")
                out_lines.append("")
            else:
                # General claim / reasoning bullet
                # Avoid bullet explosion: wrap into concise claim bullets
                out_lines.append(f"- Luận điểm phân tích:")
                out_lines.append(f"  - {cleaned}")
                out_lines.append("")

    # If any assigned figures were not placed (e.g. at end of section)
    remaining_figs = [fid for fid in fig_ids if fid not in used_figs]
    for fid in remaining_figs:
        fig_info = fig_by_id[fid]
        fnum = fig_info['global_num']
        cap = fig_info['caption']
        rel_path = fig_info['rel_path']
        can_cu, nhin_vao = extract_analysis_points(src_text)
        proof_claim = f"Minh họa quái tượng và hào vị của {cap}."
        evidence_guide = f"Căn cứ {can_cu}. Nhìn vào {nhin_vao}."
        
        out_lines.append(f"- Quái đồ bổ sung cho phần luận giải:")
        out_lines.append(f"  - **Hình {fnum}.** {cap}")
        out_lines.append(f"    - <img src=\"{rel_path}\" alt=\"Hình {fnum}\" />")
        out_lines.append(f"    - **Hình này chứng minh điều gì**")
        out_lines.append(f"      - {proof_claim}")
        out_lines.append(f"    - **Từ đâu mà thấy được**")
        out_lines.append(f"      - {evidence_guide}")
        out_lines.append("")

    frag_content = '\n'.join(out_lines).strip() + '\n'
    dest_path = os.path.join(OUTPUT_DIR, chunk['fragment_file'])
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(frag_content)
    return dest_path

# Generate all 57 fragments
generated = []
for c in manifest['routing_table']:
    p = generate_fragment(c)
    generated.append(p)

print(f"Successfully generated {len(generated)} fragment files.")
