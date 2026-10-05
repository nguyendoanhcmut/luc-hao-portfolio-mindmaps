import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Fix ch06
ff_ch06 = 'fragments/ch06_chuong_4_hon_thien_giap_ty_branches.md'
content = open(ff_ch06, encoding='utf-8').read()
content = content.replace('assets/page_0030_img_01.png', 'assets/page_0034_img_01.png')
open(ff_ch06, 'w', encoding='utf-8').write(content)
print("Fixed ch06")

# 2. Fix ch07
ff_ch07 = 'fragments/ch07_chuong_5_luc_than_ca_branches.md'
content = open(ff_ch07, encoding='utf-8').read()
content = content.replace('assets/page_0032_img_01.png', 'assets/page_0035_img_01.png')
open(ff_ch07, 'w', encoding='utf-8').write(content)
print("Fixed ch07")

# 3. Fix ch18
ff_ch18 = 'fragments/ch18_chuong_16_tu_thoi_vuong_tuong_branches.md'
content = open(ff_ch18, encoding='utf-8').read()
content = content.replace('assets/page_0066_img_01.png', 'assets/page_0054_img_01.png')
open(ff_ch18, 'w', encoding='utf-8').write(content)
print("Fixed ch18")

# 4. Fix ch13 (indentation)
ff_ch13 = 'fragments/ch13_chuong_11_ngu_hanh_tuong_sinh_branches.md'
lines = open(ff_ch13, encoding='utf-8').readlines()
new_lines = []
for l in lines:
    if l.startswith('- **Hình 21.**') or l.startswith('- **Hình 22.**') or l.startswith('- **Hình 23.**'):
        new_lines.append('  ' + l)
    elif len(new_lines) > 0 and (new_lines[-1].startswith('  - **Hình 2') or new_lines[-1].startswith('    -')):
        # child of figure block that was unindented
        if l.startswith('  - '):
            new_lines.append('  ' + l)
        elif l.startswith('    - '):
            new_lines.append('  ' + l)
        else:
            new_lines.append(l)
    else:
        new_lines.append(l)
open(ff_ch13, 'w', encoding='utf-8').writelines(new_lines)
print("Fixed ch13")

# 5. Fix ch108 (indentation)
ff_ch108 = 'fragments/ch108_chuong_106_benh_tat_branches.md'
lines = open(ff_ch108, encoding='utf-8').readlines()
new_lines = []
for l in lines:
    if l.startswith('- **Hình 499.**') or l.startswith('- **Hình 500.**'):
        new_lines.append('  ' + l)
    elif len(new_lines) > 0 and (new_lines[-1].startswith('  - **Hình 499') or new_lines[-1].startswith('  - **Hình 500') or new_lines[-1].startswith('    -')):
        if l.startswith('  - '):
            new_lines.append('  ' + l)
        elif l.startswith('    - '):
            new_lines.append('  ' + l)
        else:
            new_lines.append(l)
    else:
        new_lines.append(l)
open(ff_ch108, 'w', encoding='utf-8').writelines(new_lines)
print("Fixed ch108")

# 6. Fix ch09
ff_ch09 = 'fragments/ch09_chuong_7_ong_bien_branches.md'
txt_ch09 = open(ff_ch09, encoding='utf-8').read()

# Remove old figure blocks in ch09
old_fig9_block = """- Minh họa sự biến hóa của quẻ khi hào động làm thay đổi cấu trúc quái tượng:
    - **Hình 9.** Quẻ Trạch Thiên Quải biến Càn Vi Thiên
      - <img src="assets/page_0035_img_01.png" alt="Hình 9" />
      - **Hình này chứng minh điều gì**
        - Minh họa quy luật biến đổi thể quẻ khi hào âm cực phát động biến thành dương, đưa quẻ Trạch Thiên Quải chuyển hóa thành quẻ Bát thuần Càn.
      - **Từ đâu mà thấy được**
        - Quẻ Quải có năm hào dương ở dưới và một hào âm ở thượng hào; khi hào thượng âm động (X) biến thành dương (⚊), toàn bộ sáu hào trở thành dương thuần túy, tạo thành quẻ Càn Vi Thiên."""

old_fig10_block = """- **Biến hóa phức hợp ở ngoại quái làm thay đổi bản thể quẻ:**
  - Minh họa sự động biến của các hào ngoại quái:
    - **Hình 10.** Quẻ Sơn Lôi Di biến Phong Lôi Ích
      - <img src="assets/page_0036_img_01.png" alt="Hình 10" />
      - **Hình này chứng minh điều gì**
        - Minh chứng cho nguyên tắc hào động ở ngoại quái làm chuyển đổi quẻ tượng, đưa quẻ Sơn Lôi Di biến thành quẻ Phong Lôi Ích trong khi nội quái giữ nguyên.
      - **Từ đâu mà thấy được**
        - Ngoại quái Cấn (Sơn) có hào động biến đổi thành ngoại quái Tốn (Phong), nội quái Chấn (Lôi) tĩnh bất biến, minh chứng quy luật hào nào động thì hào đó biến, hào tĩnh thì giữ nguyên."""

old_fig11_block = """- **Minh họa sự động biến nội quái và quy tắc an hào biến:**
  - **Hình 11.** Quẻ Sơn Lôi Di biến Sơn Hỏa Bí
    - <img src="assets/page_0037_img_01.png" alt="Hình 11" />
    - **Hình này chứng minh điều gì**
      - Thể hiện sự biến hóa tại nội quái làm quẻ Sơn Lôi Di chuyển thành quẻ Sơn Hỏa Bí, minh chứng cách nạp địa chi cho hào biến và nguyên tắc xác định Lục thân theo bản cung quẻ gốc.
    - **Từ đâu mà thấy được**
      - Ngoại quái Cấn giữ tĩnh nguyên vẹn, nội quái Chấn (Lôi) có hào phát động biến thành Ly (Hỏa); hào động tiếp nhận địa chi của quẻ Ly nhưng danh xưng Lục thân vẫn quy chiếu theo ngũ hành bản cung của quẻ Di."""

# Normalize newlines
txt_ch09 = txt_ch09.replace('\r\n', '\n')
old_fig9_block = old_fig9_block.replace('\r\n', '\n')
old_fig10_block = old_fig10_block.replace('\r\n', '\n')
old_fig11_block = old_fig11_block.replace('\r\n', '\n')

txt_ch09 = txt_ch09.replace(old_fig9_block, '')
txt_ch09 = txt_ch09.replace(old_fig10_block, '')
txt_ch09 = txt_ch09.replace(old_fig11_block, '')

# Now insert fig_09, fig_10, fig_11 at their correct locations
target_can_kham = """  - Kết quả là cả nội quái và ngoại quái của quẻ Càn đều biến thành Khảm, toàn quẻ chuyển hóa thành quẻ Bát thuần Khảm."""
fig9_replacement = """  - Kết quả là cả nội quái và ngoại quái của quẻ Càn đều biến thành Khảm, toàn quẻ chuyển hóa thành quẻ Bát thuần Khảm.
  - **Hình 9.** Sơ đồ quẻ Càn biến quẻ Khảm
    - <img src="assets/page_0036_img_01.png" alt="Hình 9" />
    - **Hình này chứng minh điều gì**
      - Minh họa trường hợp các hào 1, 3, 4, 6 quẻ Càn đồng động biến thành quẻ Khảm.
    - **Từ đâu mà thấy được**
      - Hào 2 và 5 là hào tĩnh giữ nguyên dương, các hào động hóa âm tạo thành Bát thuần Khảm."""

target_khon_kham = """  - Kết quả hào giữa của cả nội quái và ngoại quái đều hóa dương, đưa quẻ Khôn chuyển hóa thành quẻ Bát thuần Khảm."""
fig10_replacement = """  - Kết quả hào giữa của cả nội quái và ngoại quái đều hóa dương, đưa quẻ Khôn chuyển hóa thành quẻ Bát thuần Khảm.
  - **Hình 10.** Sơ đồ quẻ Khôn biến quẻ Khảm
    - <img src="assets/page_0036_img_02.png" alt="Hình 10" />
    - **Hình này chứng minh điều gì**
      - Minh họa quẻ Khôn có hào 2 và hào 5 phát động hóa dương tạo thành quẻ Khảm.
    - **Từ đâu mà thấy được**
      - Hai hào trung chính động biến thành dương, các hào khác tĩnh giữ nguyên âm."""

target_khon_can = """  - Toàn quẻ Khôn chuyển hóa hoàn toàn thành quẻ Bát thuần Càn."""
fig11_replacement = """  - Toàn quẻ Khôn chuyển hóa hoàn toàn thành quẻ Bát thuần Càn.
  - **Hình 11.** Sơ đồ quẻ Khôn biến quẻ Càn
    - <img src="assets/page_0036_img_03.png" alt="Hình 11" />
    - **Hình này chứng minh điều gì**
      - Minh họa cả sáu hào âm của quẻ Khôn đều phát động biến thành quẻ Bát thuần Càn.
    - **Từ đâu mà thấy được**
      - Sáu hào giao X đồng loạt chuyển hóa thành sáu hào dương."""

txt_ch09 = txt_ch09.replace(target_can_kham, fig9_replacement)
txt_ch09 = txt_ch09.replace(target_khon_kham, fig10_replacement)
txt_ch09 = txt_ch09.replace(target_khon_can, fig11_replacement)

open(ff_ch09, 'w', encoding='utf-8').write(txt_ch09)
print("Fixed ch09")
