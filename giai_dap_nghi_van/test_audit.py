import os
import re
import glob
import json

target_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\giai_dap_nghi_van"
figures_path = os.path.join(target_dir, "figures_manifest.json")
manifest_path = os.path.join(target_dir, "giai_dap_nghi_van_scout_manifest.json")

with open(figures_path, "r", encoding="utf-8") as f:
    figures_manifest = json.load(f)
figures_by_id = {f["id"]: f for f in figures_manifest.get("figures", [])}
figures_by_rel = {f["rel_path"]: f for f in figures_manifest.get("figures", [])}

with open(manifest_path, "r", encoding="utf-8") as f:
    scout_manifest = json.load(f)

IMG_PAT = re.compile(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]|!\[[^\]]*\]\(([^)\s]+)\)')
FIG_TITLE = re.compile(r'^\s*-\s+\*\*(?:Hình|Figure|Ảnh)\s+.*')

print("Loaded manifests successfully.")
