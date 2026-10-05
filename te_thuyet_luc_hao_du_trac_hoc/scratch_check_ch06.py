import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('fragments/ch06_chuong_1_vu_tru_quan_cua_dich_branches.md', 'r', encoding='utf-8') as f:
    ch06 = f.read()

print("Contains fig_01:", "fig_01" in ch06)
print("Contains fig:", "fig" in ch06.lower())
print("Contains [Figure:", "[figure" in ch06.lower())

for line in ch06.splitlines():
    if any(k in line.lower() for k in ['hình', 'figure', 'sơ đồ', 'bát quái', 'thái cực', 'fig']):
        print("Line:", line[:120])
