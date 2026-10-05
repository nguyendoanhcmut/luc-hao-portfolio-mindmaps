import json
import os
import sys

out_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\te_thuyet_luc_hao_du_trac_hoc"
manifest_path = os.path.join(out_dir, "te_thuyet_luc_hao_du_trac_hoc_scout_manifest.json")
figures_path = os.path.join(out_dir, "figures_manifest.json")

with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

with open(figures_path, "r", encoding="utf-8") as f:
    fig_data = json.load(f)
    figures_map = {fig["id"]: fig for fig in fig_data.get("figures", [])}

rt = manifest.get("routing_table", [])
print(f"Total chunks: {len(rt)}")

chunks_data = []
for idx, chunk in enumerate(rt):
    c_id = chunk["chunk_id"]
    title = chunk["title"]
    level = chunk["start_heading_level"]
    src_file = chunk["section_text_file"]
    frag_file = os.path.join(out_dir, chunk["fragment_file"])
    fig_ids = chunk.get("figure_ids", [])
    fig_details = []
    for fid in fig_ids:
        if fid in figures_map:
            fig = figures_map[fid]
            fig_details.append({
                "id": fid,
                "num": fig.get("figure_number"),
                "file": fig.get("file_name"),
                "caption": fig.get("caption", ""),
                "rel_path": f"assets/{fig.get('file_name')}"
            })
    
    chunks_data.append({
        "index": idx,
        "chunk_id": c_id,
        "title": title,
        "start_level": level,
        "src_file": src_file,
        "output_file": frag_file,
        "figures": fig_details,
        "parent_titles": chunk.get("parent_titles", [])
    })

with open(os.path.join(out_dir, "chunks_prepared.json"), "w", encoding="utf-8") as f:
    json.dump(chunks_data, f, ensure_ascii=False, indent=2)

print("Saved chunks_prepared.json successfully.")
