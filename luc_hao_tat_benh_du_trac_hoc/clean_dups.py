import os
import re

bad_frags = [
    'fragments/ch03_1_1_dung_than_bi_thuong_lay_dung_than_lam_branches.md',
    'fragments/ch03_5_5_dung_than_khong_ma_khong_uoc_nguyen_th_branches.md',
    'fragments/ch03_8_8_dung_than_nguyet_pha_lay_dung_than_lam_branches.md',
    'fragments/ch03_10_10_dung_than_gap_benh_ia_hoac_lay_dung_t_branches.md',
    'fragments/ch03_12_12_co_hao_ong_hoa_ra_quan_quy_hoac_lay_h_branches.md',
    'fragments/ch03_16_16_dung_than_nhap_mo_lay_hao_mo_kho_o_la_branches.md',
    'fragments/ch03_18_18_mo_kho_cua_ky_than_la_benh_branches.md',
    'fragments/ch03_20_20_nguyen_than_hoa_khong_hoa_pha_hoa_tho_branches.md',
    'fragments/ch03_22_22_quan_quy_khong_hien_tren_que_phi_than_branches.md'
]

for bf in bad_frags:
    with open(bf, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to remove the block:
    #   - **Hình N.** ...
    #     - <img src="assets/..." alt="..." />
    #     - **Hình này chứng minh điều gì**
    #       - ...
    #     - **Từ đâu mà thấy được**
    #       - ...
    
    lines = content.splitlines(keepends=True)
    new_lines = []
    skip = False
    indent = 0
    
    for line in lines:
        if re.search(r'^\s*-\s+\*\*Hình \d+\.\*\*', line):
            skip = True
            indent = len(line) - len(line.lstrip())
            continue
        if skip:
            cur_indent = len(line) - len(line.lstrip())
            if line.strip() == '' or cur_indent > indent:
                continue
            else:
                skip = False
        new_lines.append(line)
        
    with open(bf, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Cleaned {bf}: {len(lines)} lines -> {len(new_lines)} lines")
