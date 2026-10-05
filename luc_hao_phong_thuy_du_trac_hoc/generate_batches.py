import json
import os

base_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_phong_thuy_du_trac_hoc"
manifest_path = os.path.join(base_dir, "luc_hao_phong_thuy_du_trac_hoc_scout_manifest.json")
figures_manifest_path = os.path.join(base_dir, "figures_manifest.json")

with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

with open(figures_manifest_path, "r", encoding="utf-8") as f:
    figures_manifest = json.load(f)

fig_map = {f["id"]: f for f in figures_manifest.get("figures", [])}

rt = manifest["routing_table"]
remaining_chunks = rt[2:]  # index 2 to 208 (207 chunks)

batch_size = 35
batches = []

for i in range(0, len(remaining_chunks), batch_size):
    batch = remaining_chunks[i:i + batch_size]
    entries = []
    for c in batch:
        cid = c["chunk_id"]
        c_figs = [fig_map[fid] for fid in c.get("figure_ids", []) if fid in fig_map]
        fig_lines = []
        for f in c_figs:
            fig_lines.append(f"  * {f['id']}: file='{f['rel_path']}', caption='{f.get('caption', '')}', fignum='{f.get('figure_number', '')}'")
        fig_str = "\n".join(fig_lines) if fig_lines else "None"
        frag_out = os.path.join(base_dir, c["fragment_file"])
        
        prompt = f"""chunk_id: {cid}
section_text_file: {c['section_text_file']}
section_title: {c['title']}
start_level: {c['start_heading_level']}
max_heading_level: 5
output_file: {frag_out}
assigned_figures:
{fig_str}

READ-SCOPE: Read ONLY your section_text_file.
Follow branch_driller system prompt strictly:
1. Heading: {'#' * c['start_heading_level']} {c['title']}. Never write H1.
2. Under headings, write detailed nested claim bullets in Vietnamese.
3. Remove 100% markdown hexagram tables (| Hào | ... |). No ##### headings for hexagrams.
4. For assigned_figures, embed inside anchor claim bullet:
   - {{Anchor claim bullet}}
     - **Hình N.** {{Tên quẻ/chủ đề}}
       - <img src=\"{c_figs[0]['rel_path'] if c_figs else 'assets/...'}\" alt=\"Hình N\" />
       - **Hình này chứng minh điều gì**
         - {{Nội dung chứng minh}}
       - **Từ đâu mà thấy được**
         - {{Căn cứ hào vị, lục thân, can chi, động biến}}
5. Preserve real-world dialogues, step-by-step reasoning (Căn cứ - Nhìn vào), and verified outcomes (Phản hồi).
6. Write fragment directly to output_file.
7. Send: Driller done. {frag_out}.
"""
        entries.append({
            "TypeName": "branch_driller",
            "Role": f"Driller {cid}",
            "Prompt": prompt,
            "Model": "flash"
        })
    batches.append(entries)

for idx, b in enumerate(batches):
    fname = os.path.join(base_dir, f"batch_{idx + 1}.json")
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(b, f, ensure_ascii=False, indent=2)
    print(f"Batch {idx + 1}: {len(b)} drillers -> {fname} (size {os.path.getsize(fname)} bytes)")
