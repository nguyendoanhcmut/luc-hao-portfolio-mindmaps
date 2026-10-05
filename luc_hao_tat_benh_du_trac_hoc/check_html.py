import os

html_path = 'luc_hao_tat_benh_du_trac_hoc_branches.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

print("File size:", len(content), "bytes")
print("katex.min.js in file:", "katex.min.js" in content)
print("markmap-view in file:", "markmap-view" in content)
print("id=\"theme-toggle\" in file:", 'id="theme-toggle"' in content)
