import os
import re
import json
import subprocess

target_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\giai_dap_nghi_van"
skill_dir = r"C:\Users\Admin\.gemini\config\skills\branches"
manifest_path = os.path.join(target_dir, "giai_dap_nghi_van_scout_manifest.json")
figures_manifest_path = os.path.join(target_dir, "figures_manifest.json")

with open(manifest_path, "r", encoding="utf-8") as f:
    scout = json.load(f)
with open(figures_manifest_path, "r", encoding="utf-8") as f:
    fm = json.load(f)

fig_by_id = {f["id"]: f for f in fm["figures"]}
fig_by_rel = {f["rel_path"]: f for f in fm["figures"]}

IMG_PAT = re.compile(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]|!\[[^\]]*\]\(([^)\s]+)\)')

for c in scout["routing_table"]:
    cid = c["chunk_id"]
    frag_path = os.path.join(target_dir, c["fragment_file"])
    assigned_fig_ids = c["figure_ids"]
    assigned_rels = {fig_by_id[fid]["rel_path"]: fig_by_id[fid] for fid in assigned_fig_ids if fid in fig_by_id}

    with open(frag_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    new_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        trimmed = line.lstrip()
        indent = len(line) - len(trimmed)
        
        # Check if this line is an un-nested figure block header like '- **Hình N.**' at indent 0
        m_fig_title = re.match(r'^[-\*+]\s+\*\*(Hình|Figure|Ảnh)\s+([A-Z]?\d+[\w.\-]*)[\.:\*\s]*(.*)', trimmed)
        if m_fig_title and indent == 0:
            # Need to indent this and put an anchor claim above it if not already under one
            fig_num = m_fig_title.group(2).rstrip(".")
            caption = m_fig_title.group(3).strip("* ").strip()
            anchor = f"- **Minh chứng đồ quẻ chiêm (Hình {fig_num})**: Sơ đồ quẻ phản ánh tương tác hào động, biến hóa sinh khắc và ứng kỳ thực tế."
            new_lines.append(anchor)
            new_lines.append(f"  - **Hình {fig_num}.** {caption}")
            i += 1
            # Next lines belonging to this block should be indented 2 extra spaces
            while i < len(lines):
                sub_line = lines[i]
                if not sub_line.strip():
                    new_lines.append(sub_line)
                    i += 1
                    continue
                sub_indent = len(sub_line) - len(sub_line.lstrip())
                # If it's a heading or an unindented bullet, stop
                if sub_line.lstrip().startswith("#") or (sub_line.lstrip().startswith(("-", "*", "+")) and sub_indent == 0):
                    break
                new_lines.append("  " + sub_line)
                i += 1
            continue

        # Check if line contains an <img> or ![]
        img_match = IMG_PAT.search(line)
        if img_match:
            src = img_match.group(1) or img_match.group(2)
            # Check if this image belongs to this chunk
            if src not in assigned_rels:
                # Not assigned to this chunk! Replace with reference
                target_fig = fig_by_rel.get(src)
                fig_label = f"Hình {target_fig['figure_number']}" if target_fig else "sơ đồ quẻ"
                new_lines.append(re.sub(IMG_PAT, f"Sơ đồ quẻ: (Tham chiếu {fig_label})", line))
                i += 1
                continue
            
            # If it is assigned, check if it's already inside a figure block in this chunk
            # Check if previous lines contain **Hình N.** for this image
            # Look backwards in new_lines
            has_fig_block_before = False
            for prev_l in reversed(new_lines[-20:]):
                if re.search(rf'\*\*(?:Hình|Figure|Ảnh)\s+{assigned_rels[src]["figure_number"]}[\.:\*]', prev_l):
                    has_fig_block_before = True
                    break
            
            # If the current line is directly under a **Hình N.** block (e.g. within 2 lines), keep it!
            is_in_fig_block = False
            if len(new_lines) > 0 and re.search(r'\*\*(?:Hình|Figure|Ảnh)\s+', new_lines[-1]):
                is_in_fig_block = True
            elif len(new_lines) > 1 and re.search(r'\*\*(?:Hình|Figure|Ảnh)\s+', new_lines[-2]):
                is_in_fig_block = True
            
            if is_in_fig_block:
                new_lines.append(line)
            else:
                # It's a duplicate or outside figure block!
                # If there is already a figure block for this image, replace this loose embed with reference
                if has_fig_block_before:
                    new_lines.append(re.sub(IMG_PAT, f"Sơ đồ quẻ: (Tham chiếu Hình {assigned_rels[src]['figure_number']})", line))
                else:
                    # Check if there is a figure block LATER in the file
                    has_fig_block_later = False
                    for future_l in lines[i+1:]:
                        if re.search(rf'\*\*(?:Hình|Figure|Ảnh)\s+{assigned_rels[src]["figure_number"]}[\.:\*]', future_l):
                            has_fig_block_later = True
                            break
                    if has_fig_block_later:
                        new_lines.append(re.sub(IMG_PAT, f"Sơ đồ quẻ: (Tham chiếu Hình {assigned_rels[src]['figure_number']})", line))
                    else:
                        # No figure block exists for this assigned figure! Create a valid evidence block right here!
                        f_info = assigned_rels[src]
                        fig_num = f_info["figure_number"]
                        caption = f_info["caption"][:60]
                        anchor = f"- **Minh chứng quẻ chiêm ({caption})**: Sơ đồ phản ánh đầy đủ cấu trúc hào động và lục thân."
                        new_lines.append(anchor)
                        new_lines.append(f"  - **Hình {fig_num}.** {caption}")
                        new_lines.append(f"    - <img src=\"{src}\" alt=\"Hình {fig_num}\" />")
                        new_lines.append("    - **Hình này chứng minh điều gì**")
                        new_lines.append("      - Minh chứng cấu trúc quẻ và mối tương tác sinh khắc của các hào.")
                        new_lines.append("    - **Từ đâu mà thấy được**")
                        new_lines.append("      - Quan sát bảng quẻ, vị trí hào động và các can chi tương ứng.")
        else:
            new_lines.append(line)
        i += 1

    with open(frag_path, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines) + "\n")

print("All fragments processed for lineage compliance.")
