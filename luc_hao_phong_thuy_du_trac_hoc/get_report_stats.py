import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_phong_thuy_du_trac_hoc"
md_path = os.path.join(base_dir, "luc_hao_phong_thuy_du_trac_hoc_branches.md")
html_path = os.path.join(base_dir, "luc_hao_phong_thuy_du_trac_hoc_branches.html")
report_path = os.path.join(base_dir, "luc_hao_phong_thuy_du_trac_hoc_verification_report.json")
manifest_path = os.path.join(base_dir, "luc_hao_phong_thuy_du_trac_hoc_scout_manifest.json")

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

with open(report_path, "r", encoding="utf-8") as f:
    report = json.load(f)

with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

headings = len(re.findall(r"^#{1,6}\s+", text, re.MULTILINE))
figures = len(re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', text))
exercises = len(manifest.get("exercises", []))

import subprocess
res = subprocess.run(["python", r"C:\Users\Admin\.gemini\config\skills\branches\scripts\verify_lineage.py", base_dir], capture_output=True, text=True, encoding="utf-8")
warnings_count = len([l for l in res.stdout.splitlines() if "[WARN]" in l])

print(f"Headings: {headings}")
print(f"Figures: {figures}")
print(f"Exercises: {exercises}")
print(f"Completeness: {report.get('completeness_score', 1.0)}")
print(f"Lineage: {'PASSED' if 'LINEAGE PASSED' in res.stdout else 'FAILED'}")
print(f"Warnings: {warnings_count}")
print(f"MD size: {os.path.getsize(md_path)} bytes")
print(f"HTML size: {os.path.getsize(html_path)} bytes")
