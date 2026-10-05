import sys
import re
import os
import json

sys.stdout.reconfigure(encoding='utf-8')

dir_path = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_quai_le_thuyet_chan"
fig_manifest_path = os.path.join(dir_path, "figures_manifest.json")
branches_path = os.path.join(dir_path, "luc_hao_quai_le_thuyet_chan_branches.md")

with open(fig_manifest_path, "r", encoding="utf-8") as f:
    fig_data = json.load(f)

with open(branches_path, "r", encoding="utf-8") as f:
    text = f.read()

figs = fig_data["figures"]
print(f"Total figures in manifest: {len(figs)}")

# Check each figure
manifest_files = [f["file_name"] for f in figs]
found_manifest_files = []
missing_manifest_files = []

for fn in manifest_files:
    if fn in text:
        found_manifest_files.append(fn)
    else:
        missing_manifest_files.append(fn)

print(f"Figures found in markdown: {len(found_manifest_files)} / {len(manifest_files)}")
if missing_manifest_files:
    print("Missing files:", missing_manifest_files)

# Check proof and deduction blocks count
proof_blocks = re.findall(r'\*\*Hình này chứng minh điều gì\*\*', text)
deduct_blocks = re.findall(r'\*\*Từ đâu mà thấy được\*\*', text)
hinh_anchors = re.findall(r'-\s+\*\*Hình\s+\d+\b', text)

print(f"Figure anchors found: {len(hinh_anchors)}")
print(f"'Hình này chứng minh điều gì' blocks: {len(proof_blocks)}")
print(f"'Từ đâu mà thấy được' blocks: {len(deduct_blocks)}")

# Check physical file existence in assets/
assets_dir = os.path.join(dir_path, "assets")
existing_assets = set(os.listdir(assets_dir)) if os.path.exists(assets_dir) else set()
missing_assets = [fn for fn in manifest_files if fn not in existing_assets]
print(f"Physical asset files existing: {len(manifest_files) - len(missing_assets)} / {len(manifest_files)}")
if missing_assets:
    print("Missing assets on disk:", missing_assets)
