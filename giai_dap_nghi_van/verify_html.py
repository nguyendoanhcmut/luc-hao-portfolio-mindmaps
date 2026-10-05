import os

html_path = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\giai_dap_nghi_van\giai_dap_nghi_van_branches.html"
assert os.path.exists(html_path), "File does not exist"
size = os.path.getsize(html_path)
assert size > 1024, f"File size {size} is <= 1KB"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

has_katex = "katex.min.js" in content
has_markmap = "markmap-view" in content
has_toggle = 'id="theme-toggle"' in content

print(f"File size: {size / 1024:.2f} KB")
print(f"katex.min.js present: {has_katex}")
print(f"markmap-view present: {has_markmap}")
print(f'id="theme-toggle" present: {has_toggle}')

assert has_katex and has_markmap and has_toggle, "HTML verification checks failed"
print("HTML verification PASSED completely!")
