import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('te_thuyet_luc_hao_du_trac_hoc_branches.md', 'r', encoding='utf-8') as f:
    text = f.read()

print("Matches for Dã Hạc:", len(re.findall(r"Dã Hạc", text, re.IGNORECASE)))
print("Matches for Tăng San:", len(re.findall(r"Tăng San", text, re.IGNORECASE)))
print("Matches for Bốc Phệ:", len(re.findall(r"Bốc Phệ", text, re.IGNORECASE)))
print("Matches for Hỏa Châu Lâm:", len(re.findall(r"Hỏa Châu Lâm", text, re.IGNORECASE)))

# Also check source text or fragments to see where Dã Hạc was in the scout manifest
with open('te_thuyet_luc_hao_du_trac_hoc_scout_manifest.json', 'r', encoding='utf-8') as f:
    manifest_text = f.read()

print("Dã Hạc in manifest:", len(re.findall(r"Dã Hạc", manifest_text, re.IGNORECASE)))
for line in manifest_text.splitlines():
    if "Dã Hạc" in line:
        print("  Manifest line:", line)
