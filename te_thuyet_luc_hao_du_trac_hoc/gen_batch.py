import json
import os
import sys

out_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\te_thuyet_luc_hao_du_trac_hoc"
chunks_path = os.path.join(out_dir, "chunks_prepared.json")

with open(chunks_path, "r", encoding="utf-8") as f:
    chunks = json.load(f)

def get_subagents_for_range(start_idx, end_idx):
    selected = chunks[start_idx:end_idx]
    subagents = []
    for c in selected:
        lvl = c["start_level"]
        heading_prefix = "#" * lvl
        figs = c["figures"]
        fig_desc_list = []
        for f in figs:
            fig_desc_list.append(f"- ID: {f['id']}, Hình {f['num']}: {f['caption']} -> <img src=\"{f['rel_path']}\" alt=\"Hình {f['num']}\" />")
        figs_text = "\n".join(fig_desc_list) if fig_desc_list else "Không có hình trong chunk này."

        prompt = f"""You are branch_driller for chunk {c['chunk_id']}: '{c['title']}'.
Read-scope rule: Read ONLY your assigned section_text_file: {c['src_file']}. Do NOT read the full book file.

Parameters:
- section_text_file: {c['src_file']}
- section_title: {c['title']}
- start_level: {lvl}
- max_heading_level: 5
- output_file: {c['output_file']}

ASSIGNED FIGURES:
{figs_text}

CRITICAL RULES FOR LỤC HÀO DỰ TRẮC HỌC:
1. Spine: Start with heading level {lvl}: `{heading_prefix} {c['title']}`. Child headings deeper (up to level 5, never skip levels). Claim bullets under headings.
2. BỎ 100% BẢNG CHỮ VẼ HÀO: KHÔNG dùng bảng Markdown (| Hào | ...) và KHÔNG dùng tiêu đề con (###, ####, #####) để đặt tên quẻ hay chèn bảng vẽ hào.
3. NHÚNG MỌI HÌNH TRONG ASSIGNED FIGURES bằng evidence block lồng dưới claim bullet:
   * Anchor claim bullet nêu nhận định / bối cảnh dự đoán
     - **Hình N.** {c.get('caption', 'Quẻ')}
       - <img src="assets/..." alt="Hình N" />
       - **Hình này chứng minh điều gì**
         - Kết luận dự đoán
       - **Từ đâu mà thấy được**
         - Căn cứ hào vị, lục thân, nhật nguyệt, động biến, ứng kỳ
   - Khối evidence block (từ `**Hình N.**` đến dòng cuối) <= 10 dòng.
   - Nhãn bắt buộc là `**Hình N.**` (ví dụ `**Hình 1.**`, đúng số N trong assigned figures).
4. Chi tiết thực chứng: Bảo toàn đối thoại thực tế giữa tác giả và người coi bói, các bước suy luận cụ thể và ứng nghiệm thực tế.
5. Không dùng buzzwords ("đột phá", "vượt trội", "toàn diện", "cách mạng"). Không tạo dump section. Tỷ lệ dòng figure block < 50% non-heading lines.
6. Write directly to {c['output_file']}. Then report: "Driller done: {c['chunk_id']}."
"""
        subagents.append({
            "TypeName": "branch_driller",
            "Role": f"Driller {c['chunk_id']}",
            "Prompt": prompt,
            "Model": "flash"
        })
    return subagents

if __name__ == "__main__":
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    out_file = sys.argv[3]
    subs = get_subagents_for_range(start, end)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(subs, f, ensure_ascii=False, indent=2)
    print(f"Generated {len(subs)} subagent specs to {out_file}")
