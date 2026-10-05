import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_phong_thuy_du_trac_hoc"
manifest_path = os.path.join(base_dir, "luc_hao_phong_thuy_du_trac_hoc_scout_manifest.json")
figures_manifest_path = os.path.join(base_dir, "figures_manifest.json")

with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

with open(figures_manifest_path, "r", encoding="utf-8") as f:
    figures_manifest = json.load(f)

fig_map = {f["id"]: f for f in figures_manifest.get("figures", [])}
fig_by_rel = {f["rel_path"]: f for f in figures_manifest.get("figures", [])}

TABLE_ROW_PAT = re.compile(r"^\s*\|.*\|\s*$")
IMG_PAT = re.compile(r"!\[(.*?)\]\((assets/[^\)]+)\)")


def extract_figure_proof(phan_doan_text, caption):
    """Generate concise 'Hình này chứng minh điều gì' and 'Từ đâu mà thấy được' from reasoning text."""
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", phan_doan_text) if s.strip()]
    proof = f"Quẻ chứng minh tình trạng phong thủy và ảnh hưởng cát hung tương ứng với quái tượng {caption}."
    basis = "Căn cứ vào hào vị, lục thân, can chi sinh khắc, tuần không và hào động biến trong quẻ."
    
    if sentences:
        first_claims = []
        for s in sentences[:4]:
            if any(k in s.lower() for k in ["hào", "chủ", "tượng", "bất lợi", "tốt", "chứng tỏ", "ảnh hưởng", "phong thủy"]):
                first_claims.append(s)
        if first_claims:
            proof = " ".join(first_claims[:2])
            if len(proof) > 200:
                proof = proof[:197] + "..."
                
        basis_parts = []
        for s in sentences:
            if any(k in s for k in ["Dụng thần", "Thế", "Ứng", "lâm", "động", "hóa", "khắc", "sinh", "Mộ", "Không Vong", "Huyền Vũ", "Bạch Hổ", "Thanh Long", "Chu Tước", "Đằng Xà", "Câu Trận"]):
                basis_parts.append(s)
                if len(basis_parts) >= 2:
                    break
        if basis_parts:
            basis = " ".join(basis_parts)
            if len(basis) > 200:
                basis = basis[:197] + "..."
                
    return proof, basis


def process_case_study(chunk, raw_text):
    title = chunk["title"]
    start_lvl = chunk["start_heading_level"]
    c_figs = [fig_map[fid] for fid in chunk.get("figure_ids", []) if fid in fig_map]
    
    non_table_lines = []
    in_table = False
    for line in raw_text.splitlines():
        l_str = line.strip()
        if not l_str:
            continue
        if l_str.startswith("<!--") and "Page" in l_str:
            continue
        if TABLE_ROW_PAT.match(l_str):
            in_table = True
            continue
        if in_table and ("Không Vong" in l_str or any(l_str.startswith(w) for w in ["THỔ", "THỦY", "HỎA", "KIM", "MỘC"])):
            in_table = False
            non_table_lines.append(l_str)
            continue
        in_table = False
        non_table_lines.append(l_str)
        
    full_text_clean = "\n".join(non_table_lines)
    text_no_img = IMG_PAT.sub("", full_text_clean)
    
    vd_match = re.search(r"(\*\*Ví dụ.*?\*\*:?.*?)(?=(\*\*Phán đoán|\*\*Phản hồi|$))", text_no_img, re.DOTALL)
    pd_match = re.search(r"\*\*Phán đoán.*?\*\*:?(.*?)(?=(\*\*Phản hồi|$))", text_no_img, re.DOTALL)
    ph_match = re.search(r"\*\*Phản hồi.*?\*\*:?(.*)$", text_no_img, re.DOTALL)
    
    context_text = vd_match.group(1).strip() if vd_match else ""
    pd_text = pd_match.group(1).strip() if pd_match else ""
    ph_text = ph_match.group(1).strip() if ph_match else ""
    
    if not pd_text and not ph_text:
        pd_text = text_no_img
        
    md_lines = [f"{'#' * start_lvl} {title}", ""]
    
    if context_text:
        md_lines.append("- **Bối cảnh và thông tin quẻ:**")
        c_sents = [s.strip() for s in re.split(r"(?<=[.;!?])\s+|\n+", context_text) if s.strip()]
        for s in c_sents:
            s_clean = re.sub(r"^\*\*Ví dụ\s*\d*\s*:\*\*\s*", "", s).strip()
            if s_clean:
                md_lines.append(f"  - {s_clean}")
                
    if c_figs:
        md_lines.append("- **Luận giải quái tượng phong thủy:**")
        for fig in c_figs:
            f_num = fig.get("figure_number", "")
            f_label = f"Hình {f_num}." if f_num else "Hình minh họa."
            cap = fig.get("caption", title)
            proof, basis = extract_figure_proof(pd_text, cap)
            
            md_lines.append(f"  - **{f_label}** {cap}")
            md_lines.append(f"    - <img src=\"{fig['rel_path']}\" alt=\"{f_label.rstrip('.')}\" />")
            md_lines.append(f"    - **Hình này chứng minh điều gì**")
            md_lines.append(f"      - {proof}")
            md_lines.append(f"    - **Từ đâu mà thấy được**")
            md_lines.append(f"      - {basis}")
        
    if pd_text:
        md_lines.append("- **Diễn tiến phân tích và suy luận chi tiết:**")
        pd_sents = [s.strip() for s in re.split(r"(?<=[.;!?])\s+|\n+", pd_text) if s.strip()]
        for s in pd_sents:
            s_clean = s.strip()
            if s_clean and not s_clean.startswith("**Phán đoán"):
                md_lines.append(f"  - {s_clean}")
                
    if ph_text:
        md_lines.append("- **Kết quả ứng nghiệm thực tế:**")
        ph_sents = [s.strip() for s in re.split(r"(?<=[.;!?])\s+|\n+", ph_text) if s.strip()]
        for s in ph_sents:
            s_clean = s.strip()
            if s_clean:
                md_lines.append(f"  - {s_clean}")
                
    return "\n".join(md_lines).strip() + "\n"


def process_theory_chunk(chunk, raw_text):
    title = chunk["title"]
    start_lvl = chunk["start_heading_level"]
    c_figs = [fig_map[fid] for fid in chunk.get("figure_ids", []) if fid in fig_map]
    
    clean_lines = []
    in_table = False
    for line in raw_text.splitlines():
        l_str = line.strip()
        if not l_str or (l_str.startswith("<!--") and "Page" in l_str):
            continue
        if TABLE_ROW_PAT.match(l_str):
            in_table = True
            continue
        in_table = False
        # Remove markdown image syntax from theory lines
        l_clean = IMG_PAT.sub("", l_str).strip()
        if l_clean:
            clean_lines.append(l_clean)
            
    md_lines = [f"{'#' * start_lvl} {title}", ""]
    figs_to_embed = list(c_figs)
    
    # Process lines
    for line in clean_lines:
        if line.startswith("#"):
            sub_title = re.sub(r"^#+\s*", "", line).strip()
            # If line is identical or near match to chunk title, skip
            if sub_title.lower() == title.lower() or sub_title.lower() in title.lower() or title.lower() in sub_title.lower():
                continue
            sub_lvl = min(start_lvl + 1, 5)
            md_lines.append(f"{'#' * sub_lvl} {sub_title}")
            md_lines.append("")
            continue
            
        if line == "***" or line == "---":
            continue
            
        # Format regular line as a claim bullet
        if line.startswith("- "):
            md_lines.append(line)
        elif line.startswith("* "):
            md_lines.append(f"- {line[2:].strip()}")
        else:
            md_lines.append(f"- {line}")
            
        # Embed figure if available
        if figs_to_embed:
            fig = figs_to_embed.pop(0)
            f_num = fig.get("figure_number", "")
            f_label = f"Hình {f_num}." if f_num else "Hình minh họa."
            cap = fig.get("caption", title)
            proof, basis = extract_figure_proof(line, cap)
            
            md_lines.append(f"  - **{f_label}** {cap}")
            md_lines.append(f"    - <img src=\"{fig['rel_path']}\" alt=\"{f_label.rstrip('.')}\" />")
            md_lines.append(f"    - **Hình này chứng minh điều gì**")
            md_lines.append(f"      - {proof}")
            md_lines.append(f"    - **Từ đâu mà thấy được**")
            md_lines.append(f"      - {basis}")
            
    while figs_to_embed:
        fig = figs_to_embed.pop(0)
        f_num = fig.get("figure_number", "")
        f_label = f"Hình {f_num}." if f_num else "Hình minh họa."
        cap = fig.get("caption", title)
        proof, basis = extract_figure_proof("\n".join(clean_lines), cap)
        
        md_lines.append("- **Minh họa quái tượng phong thủy:**")
        md_lines.append(f"  - **{f_label}** {cap}")
        md_lines.append(f"    - <img src=\"{fig['rel_path']}\" alt=\"{f_label.rstrip('.')}\" />")
        md_lines.append(f"    - **Hình này chứng minh điều gì**")
        md_lines.append(f"      - {proof}")
        md_lines.append(f"    - **Từ đâu mà thấy được**")
        md_lines.append(f"      - {basis}")
        
    return "\n".join(md_lines).strip() + "\n"


def run():
    rt = manifest["routing_table"]
    reprocessed = 0
    kept = 0
    
    for c in rt:
        frag_path = os.path.join(base_dir, c["fragment_file"])
        # Check if fragment exists and has all assigned figures
        c_figs = [fig_map[fid] for fid in c.get("figure_ids", []) if fid in fig_map]
        needs_regen = False
        if not os.path.exists(frag_path) or os.path.getsize(frag_path) < 200:
            needs_regen = True
        else:
            with open(frag_path, "r", encoding="utf-8") as f:
                f_txt = f.read()
            for fig in c_figs:
                if fig["rel_path"] not in f_txt:
                    needs_regen = True
                    break
                    
        if not needs_regen:
            kept += 1
            continue
            
        src_path = c["section_text_file"]
        if not os.path.exists(src_path):
            continue
            
        with open(src_path, "r", encoding="utf-8") as f:
            raw = f.read()
            
        is_case = ("Ví dụ" in c["title"] or "ví dụ" in c["title"] or 
                   "ch06_13_" in c["chunk_id"] or "ch07_12_" in c["chunk_id"] or "ch08_5_" in c["chunk_id"])
        
        if is_case:
            content = process_case_study(c, raw)
        else:
            content = process_theory_chunk(c, raw)
            
        os.makedirs(os.path.dirname(os.path.abspath(frag_path)), exist_ok=True)
        with open(frag_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        reprocessed += 1
        
    print(f"Reprocessed: {reprocessed}, Kept: {kept}, Total: {len(rt)}")


if __name__ == "__main__":
    run()
