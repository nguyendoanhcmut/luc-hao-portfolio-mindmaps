import sys
import json
import os

output_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\the_gioi_nhan_qua"
manifest_path = os.path.join(output_dir, "the_gioi_nhan_qua_scout_manifest.json")
fig_path = os.path.join(output_dir, "figures_manifest.json")

with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

with open(fig_path, "r", encoding="utf-8") as f:
    fig_data = json.load(f)
figures = {f["id"]: f for f in fig_data.get("figures", [])}

rt = manifest.get("routing_table", [])

from collections import defaultdict
prefix_groups = defaultdict(list)
for c in rt:
    pref = c["chunk_id"].split("_")[0]
    prefix_groups[pref].append(c)

worker_definitions = [
    ("worker_01", prefix_groups["ch01"] + prefix_groups["ch02"]),
    ("worker_02", prefix_groups["ch03"] + prefix_groups["ch04"] + prefix_groups["ch05"] + prefix_groups["ch06"] + prefix_groups["ch07"] + prefix_groups["ch08"]),
    ("worker_03", prefix_groups["ch09"]),
    ("worker_04", prefix_groups["ch10"][:13]),
    ("worker_05", prefix_groups["ch10"][13:]),
    ("worker_06", prefix_groups["ch11"] + prefix_groups["ch12"] + prefix_groups["ch13"]),
    ("worker_07", prefix_groups["ch14"]),
    ("worker_08", prefix_groups["ch15"][:15]),
    ("worker_09", prefix_groups["ch15"][15:30]),
    ("worker_10", prefix_groups["ch15"][30:]),
    ("worker_11", prefix_groups["ch16"]),
    ("worker_12", prefix_groups["ch17"]),
    ("worker_13", prefix_groups["ch18"]),
]

tasks_dir = os.path.join(output_dir, "_driller_tasks")
os.makedirs(tasks_dir, exist_ok=True)

total_chunks_assigned = 0
for w_id, w_chunks in worker_definitions:
    total_chunks_assigned += len(w_chunks)
    worker_task = {
        "worker_id": w_id,
        "total_chunks": len(w_chunks),
        "chunks": []
    }
    for c in w_chunks:
        c_figs = []
        for fid in c.get("figure_ids", []):
            if fid in figures:
                f_obj = figures[fid]
                fn = f_obj.get("file_name", fid)
                c_figs.append({
                    "id": fid,
                    "figure_number": str(f_obj.get("figure_number", "")),
                    "caption": f_obj.get("caption", ""),
                    "rel_path": f_obj.get("rel_path", f"assets/{fn}"),
                })
        worker_task["chunks"].append({
            "chunk_id": c["chunk_id"],
            "title": c["title"],
            "start_heading_level": c["start_heading_level"],
            "src_file": os.path.abspath(c["section_text_file"]),
            "out_file": os.path.abspath(os.path.join(output_dir, c["fragment_file"])),
            "figures": c_figs
        })
    with open(os.path.join(tasks_dir, f"{w_id}.json"), "w", encoding="utf-8") as f:
        json.dump(worker_task, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {len(worker_definitions)} worker task files. Total chunks assigned: {total_chunks_assigned}/179")
