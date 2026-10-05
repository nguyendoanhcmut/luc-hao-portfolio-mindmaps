import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_phong_thuy_du_trac_hoc"
manifest_path = os.path.join(base_dir, "luc_hao_phong_thuy_du_trac_hoc_scout_manifest.json")
figures_manifest_path = os.path.join(base_dir, "figures_manifest.json")

with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

with open(figures_manifest_path, "r", encoding="utf-8") as f:
    figures_manifest = json.load(f)

fig_map = {f["id"]: f for f in figures_manifest.get("figures", [])}
fig_by_rel = {f["rel_path"]: f for f in figures_manifest.get("figures", [])}

IMG_PAT = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']|!\[[^\]]*\]\(([^)\s]+)\)')

seen = {}
duplicates = []

for p in sorted(glob.glob(os.path.join(base_dir, "fragments", "*_branches.md"))):
    fname = os.path.basename(p)
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()
    imgs = [m[0] or m[1] for m in IMG_PAT.findall(text)]
    for src in imgs:
        if src in seen:
            duplicates.append((src, fname, seen[src]))
        else:
            seen[src] = fname

print(f"Total unique images embedded: {len(seen)}")
print(f"Duplicates: {len(duplicates)}")
if duplicates:
    for d in duplicates[:5]:
        print(f"  DUPLICATE: {d}")

expected_ids = set()
def walk(nodes):
    for node in nodes or []:
        if "figure_ids" in node:
            expected_ids.update(node["figure_ids"])
        walk(node.get("children"))
walk(manifest.get("master_skeleton"))

expected_rel = set(fig_map[fid]["rel_path"] for fid in expected_ids if fid in fig_map)
missing = expected_rel - set(seen.keys())
print(f"Expected in master skeleton: {len(expected_rel)}")
print(f"Missing from tree: {len(missing)}")
if missing:
    for m in sorted(list(missing))[:10]:
        print(f"  MISSING: {m}")
