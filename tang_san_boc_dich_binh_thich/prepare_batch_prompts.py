import json, os, sys

sys.stdout.reconfigure(encoding="utf-8")

with open("tang_san_boc_dich_binh_thich_scout_manifest.json", "r", encoding="utf-8") as f:
    scout = json.load(f)

with open("figures_manifest.json", "r", encoding="utf-8") as f:
    fig_man = json.load(f)

fig_map = {f["id"]: f for f in fig_man.get("figures", [])}

rt = scout.get("routing_table", [])
output_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\tang_san_boc_dich_binh_thich"

batches = []
batch_size = 15
for b_i in range(0, len(rt), batch_size):
    batch_chunks = rt[b_i:b_i + batch_size]
    batch_entries = []
    for c in batch_chunks:
        f_ids = c.get("figure_ids", [])
        assigned_figs_info = []
        for fid in f_ids:
            if fid in fig_map:
                fg = fig_map[fid]
                assigned_figs_info.append({
                    "id": fid,
                    "figure_number": fg.get("figure_number", ""),
                    "caption": fg.get("caption", ""),
                    "rel_path": fg.get("rel_path", f"assets/{fg.get('file_name','')}")
                })

        frag_rel = c["fragment_file"]
        frag_abs = os.path.join(output_dir, frag_rel) if not os.path.isabs(frag_rel) else frag_rel

        # Build prompt
        p = f"""You are branch_driller for chunk '{c['chunk_id']}' of 'Tăng San Bốc Dịch Bình Thích'.
Follow branch_driller_prompt.md strictly.

READ-SCOPE RULE: Read ONLY your assigned section_text_file:
{c['section_text_file']}

Parameters:
- section_title: {c['title']}
- start_level: {c['start_heading_level']}
- max_heading_level: 5
- output_file: {frag_abs}
- assigned_figures: {json.dumps(assigned_figs_info, ensure_ascii=False)}

YÊU CẦU CỐT LÕI BẮT BUỘC:
1. Viết tiêu đề '{c['title']}' ở cấp {'#' * c['start_heading_level']}. Các mục con sâu hơn 1 cấp (tối đa cấp 5 #####).
2. Dưới mỗi heading là các claim bullet (- ...).
3. BỎ 100% bảng chữ vẽ hào dạng bảng Markdown (| Hào | Thế/Ứng | ...) và KHÔNG dùng tiêu đề con ##### để chèn bảng hào.
4. BẮT BUỘC PHẢI lấy ảnh từ assets/ chèn trực tiếp vào file dưới claim bullet hỗ trợ bằng cú pháp:
   - {{Anchor claim bullet mô tả luận điểm của hình/quẻ}}
     - **Hình N.** {{Tên quẻ hoặc Caption}}
       - <img src="assets/..." alt="Hình N" />
       - **Hình này chứng minh điều gì**
         - ...
       - **Từ đâu mà thấy được**
         - ...
   Lưu ý: Figure block (**Hình N.**) tối đa 10 dòng và BẮT BUỘC phải thụt lề dưới 1 anchor claim bullet.
5. Bảo toàn luồng đối thoại thực tế giữa tác giả và người coi bói, các bước suy luận (Căn cứ - Nhìn vào) và ứng nghiệm thực tế.
6. Ghi kết quả hoàn chỉnh vào output_file: {frag_abs}
7. Báo cáo hoàn tất bằng send_message về cho orchestrator.
"""
        batch_entries.append({
            "chunk_id": c["chunk_id"],
            "title": c["title"],
            "output_file": frag_abs,
            "prompt": p
        })
    batches.append(batch_entries)

with open("batch_prompts.json", "w", encoding="utf-8") as f:
    json.dump(batches, f, ensure_ascii=False, indent=2)

print(f"Generated batch_prompts.json with {len(batches)} batches.")
