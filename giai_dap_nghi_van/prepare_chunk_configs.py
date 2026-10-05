import json
import os

output_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\giai_dap_nghi_van"
skill_dir = r"C:\Users\Admin\.gemini\config\skills\branches"

manifest_path = os.path.join(output_dir, "giai_dap_nghi_van_scout_manifest.json")
with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

figures_manifest_path = os.path.join(output_dir, "figures_manifest.json")
global_context_pack = manifest.get("global_context_pack", "")
rule_index = manifest.get("rule_index", [])

cfg_dir = os.path.join(output_dir, "fragments")
os.makedirs(cfg_dir, exist_ok=True)

configs = []
for c in manifest["routing_table"]:
    cid = c["chunk_id"]
    cfg_data = {
        "chunk_id": cid,
        "section_title": c["title"],
        "section_text_file": c["section_text_file"],
        "start_level": c["start_heading_level"],
        "max_heading_level": manifest.get("max_heading_level", 5),
        "drill_threshold_words": c.get("drill_threshold_words", 1500),
        "figures_manifest": figures_manifest_path,
        "assigned_figures": c["figure_ids"],
        "exercises": c["exercises"],
        "domain": manifest.get("domain", "luc_hao"),
        "rule_index": rule_index,
        "global_context_pack": global_context_pack,
        "output_file": os.path.join(output_dir, c["fragment_file"]),
        "skill_dir": skill_dir
    }
    cfg_file = os.path.join(cfg_dir, f"cfg_{cid}.json")
    with open(cfg_file, "w", encoding="utf-8") as cf:
        json.dump(cfg_data, cf, indent=2, ensure_ascii=False)
    configs.append(cfg_file)

print(f"Generated {len(configs)} chunk config files in {cfg_dir}")
