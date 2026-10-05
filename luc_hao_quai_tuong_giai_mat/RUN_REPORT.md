# RUN REPORT: Lục Hào Quái Tượng Giải Mật

- **Document Title**: Lục Hào Quái Tượng Giải Mật (Vương Hổ Ứng)
- **Document Slug**: `luc_hao_quai_tuong_giai_mat`
- **Output Directory**: `C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_quai_tuong_giai_mat`
- **Output Markdown**: `luc_hao_quai_tuong_giai_mat_branches.md`
- **Output Mindmap HTML**: `luc_hao_quai_tuong_giai_mat_branches.html`

---

## 1. Phase Summary & Statistics

| Giai đoạn | Trạng thái | Thời gian ước tính | Kết quả chính |
| :--- | :---: | :---: | :--- |
| **Phase 1: Extract** | Hoàn thành | Sẵn có | 194 trang OCR, 189 assets hình ảnh, figures manifest |
| **Phase 2: Page Images** | Hoàn thành | Sẵn có | 194 ảnh raster hóa độ phân giải cao tại `pages/` |
| **Phase 3: Scout** | Hoàn thành | ~1.5m | 65 chunks, 73 sections, 185 quái tượng diagrams định tuyến |
| **Phase 4: Drill** | Hoàn thành | ~2.5m | 65 fragments độc lập, 185 hình ảnh nhúng cú pháp chuẩn Markmap |
| **Phase 5: Merge** | Hoàn thành | ~1.0s | Master tree: 74 tiêu đề (1 H1, 9 H2, 64 H3), 3.797 dòng |
| **Phase 6: Audit** | Hoàn thành | ~1.0s | Completeness Score: 1.0 (100%), Lineage: PASSED (0 lỗi) |
| **Phase 7: Render** | Hoàn thành | ~0.8s | 3.659 mindmap nodes, 221 KB HTML tương tác |
| **Phase 8: Report** | Hoàn thành | ~0.2s | Hoàn tất báo cáo tổng hợp |

---

## 2. Chỉ số Chất lượng & Tuân thủ Chỉ thị Đặc biệt

1. **Tuân thủ triệt để cấu trúc đồ hình & hiển thị Markmap**:
   - **Tuyệt đối KHÔNG sử dụng bảng Markdown** (`| Hào | ... |`) và **KHÔNG sử dụng tiêu đề con `#####`**, giúp Markmap trên trình duyệt web giữ nguyên 100% hình ảnh đồ hình không bị nuốt/mất.
   - Toàn bộ 185 hình ảnh quái tượng (`fig_05` đến `fig_189`) được nhúng trực tiếp bằng thẻ `<img src="assets/..." alt="Hình N" />` chuẩn xác.
   - Mỗi khối bằng chứng hình ảnh (Evidence Block) tuân thủ nghiêm ngặt giới hạn $\le 10$ dòng (thực tế 6 dòng), bao gồm:
     - `- **Bảng Quẻ & Quái lệ ...**:` (Anchor Claim)
       - `  - **Hình N.** {Tên quẻ}`
         - `    - <img src="assets/..." alt="Hình N" />`
         - `    - **Hình này chứng minh điều gì**`
           - `{Luận điểm cốt lõi}`
         - `    - **Từ đâu mà thấy được**`
           - `{Căn cứ quái hào, lục thân, nhật nguyệt}`

2. **Bảo toàn 100% chiều sâu học thuật và thực chiến**:
   - Tường thuật trọn vẹn luồng đối thoại thực tế giữa tác giả Vương Hổ Ứng và đương số.
   - Phân tích chi tiết từng bước suy luận: Căn cứ, Nhìn vào, Dụng thần, Thế Ứng, Nhật Nguyệt sinh khắc chế hóa, hào động biến, tiến thoái thần.
   - Ghi nhận đầy đủ diễn biến và ứng nghiệm thực tế trong đời sống.

3. **Kiểm định Cơ học & Ý nghĩa (Verification)**:
   - `verify_lineage.py`: **LINEAGE PASSED** (0 errors).
   - `Section Coverage`: 73/73 (100%).
   - `Depth Score`: 100% (cấu trúc nhánh đào sâu 3-4 cấp).
   - `Grounding Score`: 100% (toàn bộ hào chi, nhật nguyệt, căn cứ định lượng được bảo toàn).
   - `Lexicon Score`: 100% (Quái tượng, Dụng thần, Thế Ứng, Động biến được tích hợp đầy đủ).
   - Cảnh báo: 4 cảnh báo duy nhất là 4 ảnh trang trí bìa sách không chứa thông tin quái tượng (`page_0001_img_01.png`, `page_0002_img_01.png`, `page_0002_img_02.png`, `page_0003_img_01.png`), đã được chủ động loại bỏ trong `skeleton.json`.
