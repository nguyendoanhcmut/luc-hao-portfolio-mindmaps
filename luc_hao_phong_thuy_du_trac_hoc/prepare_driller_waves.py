import json
import os
import sys

base_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_phong_thuy_du_trac_hoc"
manifest_path = os.path.join(base_dir, "luc_hao_phong_thuy_du_trac_hoc_scout_manifest.json")
figures_manifest_path = os.path.join(base_dir, "figures_manifest.json")

with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

with open(figures_manifest_path, "r", encoding="utf-8") as f:
    figures_manifest = json.load(f)

fig_map = {f["id"]: f for f in figures_manifest.get("figures", [])}

rt = manifest["routing_table"]
chunk_size = 40
waves = []

for i in range(0, len(rt), chunk_size):
    batch = rt[i:i + chunk_size]
    wave_entries = []
    for c in batch:
        cid = c["chunk_id"]
        c_figs = [fig_map[fid] for fid in c.get("figure_ids", []) if fid in fig_map]
        fig_lines = []
        for f in c_figs:
            fig_lines.append(f"- ID: {f['id']}, File: {f['rel_path']}, Caption: {f.get('caption', '')}, FigNum: {f.get('figure_number', '')}")
        fig_info = "\n".join(fig_lines) if fig_lines else "None"
        
        frag_out = os.path.join(base_dir, c["fragment_file"])
        
        prompt = f"""You are branch_driller for chunk '{cid}' ({c['title']}).

Parameters:
- section_text_file: {c['section_text_file']}
- section_title: {c['title']}
- start_level: {c['start_heading_level']}
- max_heading_level: 5
- output_file: {frag_out}
- assigned_figures:
{fig_info}

READ-SCOPE RULE: Read ONLY your section_text_file: {c['section_text_file']}. Do NOT read other outside files.

Requirements:
1. Write the section title at heading level {c['start_heading_level']} (using {'#' * c['start_heading_level']} {c['title']}). Never write an H1.
2. Under headings, write detailed claim bullets in Vietnamese explaining concepts, rules, methods, cases.
3. BỎ 100% bảng chữ vẽ hào dạng bảng Markdown (| Hào | Thế/Ứng | ...) và KHÔNG dùng tiêu đề con ##### để chèn bảng hào.
4. BẮT BUỘC PHẢI lấy ảnh từ assets/ (cho các assigned_figures) chèn trực tiếp dưới bullet phân tích tương ứng theo đúng cú pháp (tối đa 10 dòng cho mỗi block hình):
   - {{Anchor bullet mô tả quẻ/luận đoán}}
     - **Hình N.** {{Tên quẻ/chủ đề}}
       - <img src="{c_figs[0]['rel_path'] if c_figs else 'assets/...'}" alt="Hình N" />
       - **Hình này chứng minh điều gì**
         - {{Nội dung chứng minh}}
       - **Từ đâu mà thấy được**
         - {{Căn cứ hào vị, lục thân, can chi, hào động biến}}
5. Bảo toàn luồng đối thoại thực tế giữa tác giả và người coi bói, các bước suy luận (Căn cứ - Nhìn vào) và ứng nghiệm thực tế (phản hồi).
6. Viết kết quả trực tiếp vào file: {frag_out}.
7. Báo cáo hoàn tất: Driller done. {frag_out}.
"""
        wave_entries.append({
            "TypeName": "branch_driller",
            "Role": f"Driller {cid}",
            "Prompt": prompt,
            "Model": "flash"
        })
    waves.append(wave_entries)

print(f"Total waves: {len(waves)}")
for idx, w in enumerate(waves):
    fname = os.path.join(base_dir, f"driller_wave_{idx + 1}.json")
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(w, f, ensure_ascii=False, indent=2)
    print(f"Wave {idx + 1}: {len(w)} drillers written to {fname}")
