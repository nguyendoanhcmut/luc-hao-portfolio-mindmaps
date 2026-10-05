import os

html_path = 'luc_hao_du_trac_ngo_trung_ngo_branches.html'
assert os.path.exists(html_path), 'HTML file does not exist'
size = os.path.getsize(html_path)
assert size > 1024, f'HTML too small: {size}'
content = open(html_path, encoding='utf-8').read()
assert 'katex.min.js' in content, 'Missing katex.min.js'
assert 'markmap-view' in content, 'Missing markmap-view'
assert 'id="theme-toggle"' in content, 'Missing id="theme-toggle"'
print(f'HTML VERIFIED: size={size} bytes, katex=OK, markmap=OK, theme-toggle=OK')
