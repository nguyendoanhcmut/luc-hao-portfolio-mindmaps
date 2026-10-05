import json, os, sys

sys.stdout.reconfigure(encoding="utf-8")

output_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\tang_san_boc_dich_binh_thich"

with open("tang_san_boc_dich_binh_thich_scout_manifest.json", "r", encoding="utf-8") as f:
    scout = json.load(f)

with open("figures_manifest.json", "r", encoding="utf-8") as f:
    fig_man = json.load(f)
fig_map = {f["id"]: f for f in fig_man.get("figures", [])}

rt = scout.get("routing_table", [])
c_map = {c["chunk_id"]: c for c in rt}

missing = [c for c in rt if not (os.path.exists(os.path.join(output_dir, c["fragment_file"])) and os.path.getsize(os.path.join(output_dir, c["fragment_file"])) > 50)]

missing_no_42 = [c for c in missing if c["chunk_id"] != "ch42"]
print(f"Missing (excluding ch42): {len(missing_no_42)}")

# Part 1 and Part 2 of ch42
ch42_entry = c_map["ch42"]
part1_figs = []
part2_figs = []
for fid in ch42_entry["figure_ids"]:
    fg = fig_map[fid]
    fnum = fg["figure_number"]
    info = {
        "num": fnum,
        "cap": fg.get("caption", ""),
        "src": fg.get("rel_path", f"assets/{fg.get('file_name','')}")
    }
    if int(fnum) <= 280:
        part1_figs.append(info)
    else:
        part2_figs.append(info)

p_ch42_1 = f"""READ-SCOPE RULE: Read ONLY your assigned section_text_file:
C:\\Users\\Admin\\.gemini\\antigravity\\scratch\\luc_hao_portfolio_ocr\\tang_san_boc_dich_binh_thich\\fragments\\src\\ch42_part1.txt

Parameters:
- chunk_id: ch42_part1
- section_title: Chương 40: THIÊN THỜI (Phần 1)
- start_level: 2
- max_heading_level: 5
- output_file: C:\\Users\\Admin\\.gemini\\antigravity\\scratch\\luc_hao_portfolio_ocr\\tang_san_boc_dich_binh_thich\\fragments/ch42_part1_branches.md
- assigned_figures: {json.dumps(part1_figs, ensure_ascii=False)}

Tuân thủ triệt để system prompt branch_driller:
- Tiêu đề 'Chương 40: THIÊN THỜI' ở cấp ##, các mục con sâu hơn (max cấp 5 #####), claim bullets (- ...) dưới headings.
- BỎ 100% bảng vẽ hào markdown.
- Nhúng ảnh assets/ dưới anchor bullet: **Hình N.** {{Tên/Caption}}, <img src="assets/..." alt="Hình N" />, 2 câu hỏi (chứng minh gì, từ đâu thấy), block <= 10 dòng.
- Bảo toàn trọn vẹn luồng đối thoại thực tế Dã Hạc/Vương Hổ Ứng, lập luận Căn cứ - Nhìn vào, lời bình và ứng nghiệm thực tế.
- Ghi output_file (Overwrite=true), send_message báo hoàn thành."""

p_ch42_2 = f"""READ-SCOPE RULE: Read ONLY your assigned section_text_file:
C:\\Users\\Admin\\.gemini\\antigravity\\scratch\\luc_hao_portfolio_ocr\\tang_san_boc_dich_binh_thich\\fragments\\src\\ch42_part2.txt

Parameters:
- chunk_id: ch42_part2
- section_title: Chương 40: THIÊN THỜI (Phần 2)
- start_level: 0
- max_heading_level: 5
- output_file: C:\\Users\\Admin\\.gemini\\antigravity\\scratch\\luc_hao_portfolio_ocr\\tang_san_boc_dich_binh_thich\\fragments/ch42_part2_branches.md
- assigned_figures: {json.dumps(part2_figs, ensure_ascii=False)}

Tuân thủ triệt để system prompt branch_driller:
- Viết tiếp các mục con dưới dạng heading cấp ### hoặc claim bullets (- ...) dưới headings, max cấp 5 ##### (start_level=0: không viết lại H2).
- BỎ 100% bảng vẽ hào markdown.
- Nhúng ảnh assets/ dưới anchor bullet: **Hình N.** {{Tên/Caption}}, <img src="assets/..." alt="Hình N" />, 2 câu hỏi (chứng minh gì, từ đâu thấy), block <= 10 dòng.
- Bảo toàn trọn vẹn luồng đối thoại thực tế Dã Hạc/Vương Hổ Ứng, lập luận Căn cứ - Nhìn vào, lời bình và ứng nghiệm thực tế.
- Ghi output_file (Overwrite=true), send_message báo hoàn thành."""

driller_ch42_1 = {
    "TypeName": "branch_driller",
    "Role": "Driller ch42_part1",
    "Model": "flash",
    "Prompt": p_ch42_1,
    "Workspace": "inherit"
}
driller_ch42_2 = {
    "TypeName": "branch_driller",
    "Role": "Driller ch42_part2",
    "Model": "flash",
    "Prompt": p_ch42_2,
    "Workspace": "inherit"
}

def make_entry(c):
    f_ids = c.get("figure_ids", [])
    assigned_figs = []
    for fid in f_ids:
        if fid in fig_map:
            fg = fig_map[fid]
            assigned_figs.append({
                "num": fg.get("figure_number", ""),
                "cap": fg.get("caption", ""),
                "src": fg.get("rel_path", f"assets/{fg.get('file_name','')}")
            })
    frag_abs = os.path.join(output_dir, c["fragment_file"])
    p = f"""READ-SCOPE RULE: Read ONLY your assigned section_text_file:
{c['section_text_file']}

Parameters:
- chunk_id: {c['chunk_id']}
- section_title: {c['title']}
- start_level: {c['start_heading_level']}
- max_heading_level: 5
- output_file: {frag_abs}
- assigned_figures: {json.dumps(assigned_figs, ensure_ascii=False)}

Tuân thủ triệt để system prompt branch_driller:
- Tiêu đề '{c['title']}' ở cấp {'#' * c['start_heading_level']}, các mục con sâu hơn (max cấp 5 #####), claim bullets (- ...) dưới headings.
- BỎ 100% bảng vẽ hào markdown.
- Nhúng ảnh assets/ dưới anchor bullet: **Hình N.** {{Tên/Caption}}, <img src="assets/..." alt="Hình N" />, 2 câu hỏi (chứng minh gì, từ đâu thấy), block <= 10 dòng.
- Bảo toàn trọn vẹn luồng đối thoại thực tế Dã Hạc/Vương Hổ Ứng, lập luận Căn cứ - Nhìn vào, lời bình và ứng nghiệm thực tế.
- Ghi output_file (Overwrite=true), send_message báo hoàn thành."""
    return {
        "TypeName": "branch_driller",
        "Role": f"Driller {c['chunk_id']}",
        "Model": "flash",
        "Prompt": p,
        "Workspace": "inherit"
    }

# Batch 3: 38 chunks (ch72 to ch109) + 2 ch42 parts = exactly 40 subagents!
batch_3_chunks = missing_no_42[:38]
batch_4_chunks = missing_no_42[38:]

b3_subagents = [driller_ch42_1, driller_ch42_2] + [make_entry(c) for c in batch_3_chunks]
b4_subagents = [make_entry(c) for c in batch_4_chunks]

with open("batch_3_40.json", "w", encoding="utf-8") as f:
    json.dump(b3_subagents, f, ensure_ascii=False, indent=2)

with open("batch_4_30.json", "w", encoding="utf-8") as f:
    json.dump(b4_subagents, f, ensure_ascii=False, indent=2)

s3 = json.dumps({"Subagents": b3_subagents}, ensure_ascii=False)
s4 = json.dumps({"Subagents": b4_subagents}, ensure_ascii=False)

print(f"Batch 3: {len(b3_subagents)} subagents, {len(s3)} chars, {len(s3.split())} words")
print(f"Batch 4: {len(b4_subagents)} subagents, {len(s4)} chars, {len(s4.split())} words")
