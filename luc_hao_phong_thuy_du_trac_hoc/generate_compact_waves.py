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
remaining_chunks = rt[2:]  # 207 chunks

# Group into 7 waves of ~30 chunks
batch_size = 30
waves = []

for i in range(0, len(remaining_chunks), batch_size):
    batch = remaining_chunks[i:i + batch_size]
    entries = []
    for c in batch:
        cid = c["chunk_id"]
        c_figs = [fig_map[fid] for fid in c.get("figure_ids", []) if fid in fig_map]
        fig_items = [f"{f['id']}:{f['rel_path']}:{f.get('caption', '')}" for f in c_figs]
        fig_str = "; ".join(fig_items) if fig_items else "None"
        frag_out = os.path.join(base_dir, c["fragment_file"])
        
        prompt = (
            f"chunk_id: {cid}\n"
            f"section_text_file: {c['section_text_file']}\n"
            f"section_title: {c['title']}\n"
            f"start_level: {c['start_heading_level']}\n"
            f"output_file: {frag_out}\n"
            f"assigned_figures: {fig_str}\n"
            f"Transform section_text_file into Markdown fragment at output_file following your system instructions. Then send message: Driller done."
        )
        entries.append({
            "TypeName": "branch_driller",
            "Role": f"Driller {cid}",
            "Prompt": prompt,
            "Model": "flash"
        })
    waves.append(entries)

for idx, w in enumerate(waves):
    fname = os.path.join(base_dir, f"compact_wave_{idx + 1}.json")
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(w, f, ensure_ascii=False, indent=2)
    print(f"Wave {idx + 1}: {len(w)} drillers -> {fname} (size {os.path.getsize(fname)} bytes)")
