import os, sys
sys.stdout.reconfigure(encoding='utf-8')

html_path = 'tang_san_boc_dich_binh_thich_branches.html'
size = os.path.getsize(html_path)
content = open(html_path, encoding='utf-8').read()

print(f'Size: {size} bytes ({size/1024:.2f} KB)')
print('katex.min.js:', 'katex.min.js' in content)
print('markmap-view:', 'markmap-view' in content)
print('id="theme-toggle":', 'id="theme-toggle"' in content)
