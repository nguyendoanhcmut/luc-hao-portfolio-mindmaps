import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

branches_path = 'te_thuyet_luc_hao_du_trac_hoc_branches.md'
with open(branches_path, 'r', encoding='utf-8') as f:
    text = f.read()

img_tags = re.findall(r'<img[^>]+>', text)
print(f"Total <img ...> tags in branches.md: {len(img_tags)}")
if img_tags:
    print("First 5 img tags:", img_tags[:5])

hinh_blocks = re.findall(r'\*\*Hình\s+\d+.*?\*\*', text)
print(f"Total **Hình X...** blocks in branches.md: {len(hinh_blocks)}")
if hinh_blocks:
    print("First 5 Hình blocks:", hinh_blocks[:5])

# Let's check how many assets are cited
assets = re.findall(r'src=["\']([^"\']+)["\']', text)
print(f"Total src= citations: {len(assets)}")
print(f"Unique src= citations: {len(set(assets))}")
