import json
import os

output_dir = r"C:/Users/Admin/.gemini/antigravity/scratch/luc_hao_portfolio_ocr/luc_hao_tat_benh_du_trac_hoc".replace("\\", "/")
skill_dir = r"C:/Users/Admin/.gemini/config/skills/branches".replace("\\", "/")

with open(f"{output_dir}/luc_hao_tat_benh_du_trac_hoc_scout_manifest.json", "r", encoding="utf-8") as f:
    sm = json.load(f)

with open(f"{output_dir}/figures_manifest.json", "r", encoding="utf-8") as f:
    fm = json.load(f)

f_map = {f["id"]: f for f in fm.get("figures", [])}
routing_table = sm.get("routing_table", [])

def make_driller_prompt(c):
    cid = c["chunk_id"]
    title = c["title"]
    start_lvl = c["start_heading_level"]
    frag_file = c["fragment_file"]
    sec_txt = c["section_text_file"].replace("\\", "/")
    assigned_fids = c.get("figure_ids", [])
    
    # Detail figures for this chunk
    fig_details = []
    for fid in assigned_fids:
        if fid in f_map:
            fig = f_map[fid]
            fig_details.append({
                "id": fid,
                "figure_number": fig.get("figure_number", fid.replace("fig_", "")),
                "file_name": fig.get("file_name"),
                "caption": fig.get("caption", "")
            })
    
    hashes = "#" * start_lvl
    sub_hashes = "#" * min(start_lvl + 1, 5)
    
    fig_spec = ""
    if fig_details:
        fig_spec = "DANH SÁCH HÌNH CẦN NHÚNG TRONG CHUNK NÀY:\n"
        for fd in fig_details:
            fig_spec += f"- {fd['id']}: Hình {fd['figure_number']}. {fd['caption']} (assets/{fd['file_name']})\n"
    else:
        fig_spec = "Chunk này không có hình đồ hình quẻ được gán.\n"

    prompt = f"""Bạn là branch_driller phụ trách chunk {cid}: "{title}".
QUY TẮC PHẠM VI ĐỌC: Đọc file nguồn {sec_txt}, file {output_dir}/figures_manifest.json và prompt này.

THÔNG SỐ:
- section_text_file: {sec_txt}
- section_title: {title}
- start_level: {start_lvl}
- max_heading_level: 5
- figures_manifest: {output_dir}/figures_manifest.json
- assigned_figures: {json.dumps(assigned_fids)}
- output_file: {output_dir}/{frag_file}

{fig_spec}

CHỈ THỊ ĐẶC BIỆT BẮT BUỘC TỪ USER & LINEAGE (VI PHẠM SẼ BỊ FAIL):
1. Dòng đầu tiên của file BẮT BUỘC là:
{hashes} {title}
2. Các tiểu mục lý thuyết bên trong dùng {sub_hashes}. Tuyệt đối không nhảy cấp, không tạo H1.
3. TUYỆT ĐỐI KHÔNG dùng bảng vẽ hào Markdown (| Hào | Thế/Ứng | ...) và KHÔNG dùng tiêu đề ##### để chèn bảng hào!
4. MỌI hình ảnh trong assigned_figures ({len(assigned_fids)} hình) BẮT BUỘC phải chèn đúng cú pháp:
   - **Hình N.** {{Tên quẻ}}
     - <img src="assets/page_XXXX_img_YY.png" alt="Hình N" />
     - **Hình này chứng minh điều gì**
       - ...
     - **Từ đâu mà thấy được**
       - ...
   LƯU Ý CỰC KỲ QUAN TRỌNG VỀ EVIDENCE BLOCK:
   - Khối hình này BẮT BUỘC thụt lề lồng bên dưới bullet của Ví dụ/Quái lệ tương ứng (ví dụ: `- **Ví dụ K:** ...`).
   - Mỗi khối hình (từ `- **Hình N.**` đến dòng con cuối) TỐI ĐA 10 DÒNG!
   - Mỗi hình trong assigned_figures xuất hiện đúng 1 lần duy nhất trong fragment.
5. Bảo toàn luồng đối thoại thực tế giữa tác giả và người coi bói, các bước suy luận chi tiết (Căn cứ - Nhìn vào) và ứng nghiệm thực tế dưới dạng các bullet chi tiết cùng cấp với khối hình bên dưới `- **Ví dụ K:** ...`:
   - **Phán đoán chi tiết:**
     - Căn cứ: ...
     - Nhìn vào: ...
   - **Ứng nghiệm thực tế:**
     - ...
6. Tỷ lệ số dòng của khối hình trên tổng số dòng không vượt quá 50% (cần phân tích sâu sắc các lập luận lý thuyết và giải quẻ từ nguồn).
7. BANNED BUZZWORDS: Tuyệt đối không dùng các từ ngữ rỗng: đột phá, vượt trội, toàn diện, cách mạng, seamless, robust.
8. Ghi TOÀN BỘ nội dung fragment ra:
   {output_dir}/{frag_file}
9. Gửi tin nhắn hoàn thành: Driller done. {output_dir}/{frag_file}.
"""
    return {
        "TypeName": "branch_driller",
        "Role": f"Driller {cid}",
        "Prompt": prompt,
        "Model": "flash"
    }

waves = [
    ("wave1", routing_table[0:15]),
    ("wave2", routing_table[15:29]),
    ("wave3", routing_table[29:43]),
    ("wave4", routing_table[43:57]),
    ("wave5", routing_table[57:71]),
    ("wave6", routing_table[71:86])
]

for wname, chunks in waves:
    wdata = [make_driller_prompt(c) for c in chunks]
    wfile = f"{output_dir}/driller_{wname}.json"
    with open(wfile, "w", encoding="utf-8") as f:
        json.dump(wdata, f, ensure_ascii=False, indent=2)
    print(f"Generated {wfile} with {len(wdata)} drillers.")

print("All waves generated successfully.")
