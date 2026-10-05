import json, os, sys

sys.stdout.reconfigure(encoding="utf-8")

output_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\tang_san_boc_dich_binh_thich"

with open("tang_san_boc_dich_binh_thich_scout_manifest.json", "r", encoding="utf-8") as f:
    scout = json.load(f)

with open("figures_manifest.json", "r", encoding="utf-8") as f:
    fig_man = json.load(f)
fig_map = {f["id"]: f for f in fig_man.get("figures", [])}

rt = scout.get("routing_table", [])
missing_chunks = [c for c in rt if not (os.path.exists(os.path.join(output_dir, c["fragment_file"])) and os.path.getsize(os.path.join(output_dir, c["fragment_file"])) > 50)]

print(f"Total missing chunks: {len(missing_chunks)}")

batch_size = 40
batches = []
for i in range(0, len(missing_chunks), batch_size):
    b_chunks = missing_chunks[i:i + batch_size]
    entries = []
    for c in b_chunks:
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
        entries.append({
            "TypeName": "branch_driller",
            "Role": f"Driller {c['chunk_id']}",
            "Model": "flash",
            "Prompt": p,
            "Workspace": "inherit"
        })
    batches.append(entries)

for b_idx, b in enumerate(batches):
    fname = f"ultra_batch_{b_idx+1}.json"
    with open(fname, "w", encoding="utf-8") as out_f:
        json.dump(b, out_f, ensure_ascii=False, indent=2)
    s = json.dumps({"Subagents": b}, ensure_ascii=False)
    print(f"Saved {fname}: {len(b)} subagents, {len(s)} chars, {len(s.split())} words")
