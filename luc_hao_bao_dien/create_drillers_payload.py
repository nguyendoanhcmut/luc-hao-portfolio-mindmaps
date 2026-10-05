import json
import os
import sys

manifest_path = r'C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_bao_dien\luc_hao_bao_dien_scout_manifest.json'
with open(manifest_path, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

chunks = manifest['routing_table']
output_dir = r'C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_bao_dien'
skill_dir = r'C:\Users\Admin\.gemini\config\skills\branches'

payloads = []
for c in chunks:
    frag_file = os.path.join(output_dir, c['fragment_file']) if not os.path.isabs(c['fragment_file']) else c['fragment_file']
    prompt = (
        f"You are branch_driller for chunk '{c['chunk_id']}': '{c['title']}'.\n"
        f"Parameters:\n"
        f"- section_text_file: {c['section_text_file']}\n"
        f"- section_title: {c['title']}\n"
        f"- start_level: {c['start_heading_level']}\n"
        f"- max_heading_level: {manifest.get('max_heading_level', 5)}\n"
        f"- drill_threshold_words: {c.get('drill_threshold_words', 1500)}\n"
        f"- figures_manifest: {os.path.join(output_dir, 'figures_manifest.json')}\n"
        f"- assigned_figures: {json.dumps(c.get('figure_ids', []))}\n"
        f"- exercises: {json.dumps(c.get('exercises', []), ensure_ascii=False)}\n"
        f"- domain: luc_hao\n"
        f"- output_file: {frag_file}\n"
        f"- skill_dir: {skill_dir}\n\n"
        f"INSTRUCTIONS & RULES:\n"
        f"1. Read only section_text_file and parameter files.\n"
        f"2. Write the fragment starting with heading level {c['start_heading_level']}: '{'#' * c['start_heading_level']} {c['title']}'.\n"
        f"3. Under headings, write claim bullets (- ...). Nest supporting details under each claim.\n"
        f"4. BỎ 100% BẢNG CHỮ VẼ HÀO dạng Markdown (| Hào | Thế/Ứng | ...) và TUYỆT ĐỐI KHÔNG dùng tiêu đề con ##### để chèn bảng hào.\n"
        f"5. Với các quẻ có ảnh trong assets/ (xem figures_manifest hoặc assigned_figures hoặc trong text), BẮT BUỘC chèn evidence block chuẩn:\n"
        f"   - {{Claim bullet: luận điểm, bối cảnh đoán quẻ hoặc kết luận quẻ bói}}\n"
        f"     - **Hình N.** {{Tên quẻ hoặc chú thích ngắn gọn}}\n"
        f"       - <img src=\"assets/page_XXXX_img_YY.png\" alt=\"Hình N\" />\n"
        f"       - **Hình này chứng minh điều gì**\n"
        f"         - ...\n"
        f"       - **Từ đâu mà thấy được**\n"
        f"         - ...\n"
        f"   (Lưu ý: N là số thứ tự hình, ví dụ Hình 1, Hình 2...; evidence block phải thụt lề dưới claim bullet cha; tối đa 10 dòng; ảnh chỉ nhúng duy nhất 1 lần).\n"
        f"6. Bảo toàn luồng đối thoại thực tế giữa tác giả và người coi bói, các bước suy luận chi tiết (Căn cứ - Nhìn vào) và ứng nghiệm thực tế.\n"
        f"7. Ghi fragment vào output_file UTF-8. Báo cáo khi xong: Driller done. {frag_file}."
    )
    payloads.append({
        'TypeName': 'branch_driller',
        'Role': f"Driller {c['chunk_id']}",
        'Model': 'flash',
        'Prompt': prompt
    })

print(f'Generated {len(payloads)} payloads.')
out_path = os.path.join(output_dir, 'drillers_payload.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(payloads, f, indent=2, ensure_ascii=False)
print(f'Saved to {out_path}')
