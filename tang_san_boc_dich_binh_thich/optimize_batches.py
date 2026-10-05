import json, os, sys

sys.stdout.reconfigure(encoding="utf-8")

output_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\tang_san_boc_dich_binh_thich"

with open("tang_san_boc_dich_binh_thich_scout_manifest.json", "r", encoding="utf-8") as f:
    scout = json.load(f)

with open("figures_manifest.json", "r", encoding="utf-8") as f:
    fig_man = json.load(f)
fig_map = {f["id"]: f for f in fig_man.get("figures", [])}

rt = scout.get("routing_table", [])

missing_chunks = []
for c in rt:
    frag_rel = c["fragment_file"]
    frag_abs = os.path.join(output_dir, frag_rel)
    if not (os.path.exists(frag_abs) and os.path.getsize(frag_abs) > 50):
        missing_chunks.append(c)

print(f"Total remaining missing chunks: {len(missing_chunks)}")

batch_size = 40
batches = []
for i in range(0, len(missing_chunks), batch_size):
    b_chunks = missing_chunks[i:i + batch_size]
    batch_entries = []
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

        frag_rel = c["fragment_file"]
        frag_abs = os.path.join(output_dir, frag_rel)

        p = f"""You are branch_driller for chunk '{c['chunk_id']}' of 'Tăng San Bốc Dịch Bình Thích'.
READ-SCOPE RULE: Read ONLY your assigned section_text_file:
{c['section_text_file']}

Parameters:
- section_title: {c['title']}
- start_level: {c['start_heading_level']}
- max_heading_level: 5
- output_file: {frag_abs}
- assigned_figures: {json.dumps(assigned_figs, ensure_ascii=False)}

CRITICAL DRILLER RULES:
1. Viết tiêu đề '{c['title']}' ở cấp {'#' * c['start_heading_level']}. Các mục con sâu hơn 1 cấp (tối đa cấp 5 #####).
2. Dưới mỗi heading là các claim bullet (- ...).
3. BỎ 100% bảng chữ vẽ hào dạng bảng Markdown (| Hào | Thế/Ứng | ...) và KHÔNG dùng tiêu đề con ##### để chèn bảng hào.
4. BẮT BUỘC nhúng ảnh từ assets/ chèn trực tiếp dưới claim bullet hỗ trợ bằng cú pháp:
   - {{Anchor claim bullet}}
     - **Hình N.** {{Tên quẻ hoặc Caption}}
       - <img src="assets/..." alt="Hình N" />
       - **Hình này chứng minh điều gì**
         - ...
       - **Từ đâu mà thấy được**
         - ...
   Thẻ <img ... /> đóng chuẩn xác, khối hình <= 10 dòng, thụt lề dưới anchor claim.
5. Bảo toàn trọn vẹn luồng đối thoại thực tế giữa Dã Hạc/Vương Hổ Ứng và đương sự, quy trình suy luận (Căn cứ - Nhìn vào), lời bình Tăng san / Tân bình thích và kết quả ứng nghiệm thực tế.
6. Ghi kết quả vào output_file bằng write_to_file (Overwrite=true). Báo cáo hoàn tất bằng send_message.
"""
        batch_entries.append({
            "TypeName": "branch_driller",
            "Role": f"Driller {c['chunk_id']}",
            "Model": "flash",
            "Prompt": p,
            "Workspace": "inherit"
        })
    batches.append(batch_entries)

for b_idx, b in enumerate(batches):
    fname = f"opt_batch_40_{b_idx+1}.json"
    with open(fname, "w", encoding="utf-8") as out_f:
        json.dump(b, out_f, ensure_ascii=False, indent=2)
    tot_chars = sum(len(x["Prompt"]) for x in b)
    print(f"Saved {fname}: {len(b)} subagents, total chars: {tot_chars}")
