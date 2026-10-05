import json
import os

output_dir = r"C:/Users/Admin/.gemini/antigravity/scratch/luc_hao_portfolio_ocr/luc_hao_nhan_duyen_du_trac_hoc".replace("\\", "/")
skill_dir = r"C:/Users/Admin/.gemini/config/skills/branches".replace("\\", "/")

with open(f"{output_dir}/luc_hao_nhan_duyen_du_trac_hoc_scout_manifest.json", "r", encoding="utf-8") as f:
    sm = json.load(f)

routing_table = sm.get("routing_table", [])

def make_driller_prompt(c):
    cid = c["chunk_id"]
    title = c["title"]
    start_lvl = c["start_heading_level"]
    frag_file = c["fragment_file"]
    sec_txt = c["section_text_file"].replace("\\", "/")
    assigned_fids = c.get("figure_ids", [])
    
    hashes = "#" * start_lvl
    sub_hashes = "#" * min(start_lvl + 1, 5)
    
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
   (Tra cứu file_name, rel_path, figure_number, caption trong figures_manifest.json tương ứng với id).
   LƯU Ý CỰC KỲ QUAN TRỌNG:
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
7. Ghi TOÀN BỘ nội dung fragment ra:
   {output_dir}/{frag_file}
8. Gửi tin nhắn hoàn thành: Driller done. {output_dir}/{frag_file}.
"""
    return {
        "TypeName": "branch_driller",
        "Role": f"Driller {cid}",
        "Prompt": prompt,
        "Model": "flash"
    }

wave1 = [make_driller_prompt(c) for c in routing_table[:15]]
wave2 = [make_driller_prompt(c) for c in routing_table[15:23]]
wave3 = [make_driller_prompt(c) for c in routing_table[23:]]

with open(f"{output_dir}/driller_wave1.json", "w", encoding="utf-8") as f:
    json.dump(wave1, f, ensure_ascii=False, indent=2)

with open(f"{output_dir}/driller_wave2.json", "w", encoding="utf-8") as f:
    json.dump(wave2, f, ensure_ascii=False, indent=2)

with open(f"{output_dir}/driller_wave3.json", "w", encoding="utf-8") as f:
    json.dump(wave3, f, ensure_ascii=False, indent=2)

print("Concise prompt waves generated successfully.")
