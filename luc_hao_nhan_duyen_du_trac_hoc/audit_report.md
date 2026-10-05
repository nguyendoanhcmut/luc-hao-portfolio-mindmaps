# Tier-2 Quality Audit Report

## Summary
- **Audited Pages**: [7, 50, 100, 140, 175, 218]
- **Pass Threshold**: >= 0.95 compliance
- **Overall Verdict**: PASS

## Audit Results Table
| Page | Chapter | Diacritics (A) | Completeness (B) | Assets (C) | Cleanliness (D) | Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 7 | PHẦN CƠ SỞ - Ch 1 (ch01.md) | PASS | PASS | PASS | PASS | PASS |
| 50 | CHƯƠNG 8 (ch08.md) | PASS | PASS | PASS | PASS | PASS |
| 100 | CHƯƠNG 2 (ch16.md) | PASS | PASS | PASS | PASS | PASS |
| 140 | CHƯƠNG 8 (ch22.md) | PASS | PASS | PASS | PASS | PASS |
| 175 | CHƯƠNG 4 (ch26.md) | PASS | PASS | PASS | PASS | PASS |
| 218 | CHƯƠNG 9 (ch31.md) | PASS | PASS | PASS | PASS | PASS |

## Detailed Excerpt Verification

- **Page 7**:
  - **Source Scan**: `pages/page_0007.png` (Printed book page 4)
  - **Assembled Markdown**: `chapters/ch01.md` (lines 80–110)
  - **Image Text**: "Lục hào dự đoán hôn nhân căn cứ vào nam nữ khác nhau mà Dụng thần cũng khác nhau. Nam dự đoán hôn nhân lấy Thê Tài làm Dụng thần. Nữ dự đoán hôn nhân thì lấy Quan Quỷ làm Dụng thần... Ví dụ 1: Ngày Tân Sửu tháng Tị năm Ất Dậu, dự đoán hôn sự con gái, được quẻ Địa Sơn Khiêm biến Địa Thủy Sư."
  - **Markdown Text**: "Lục hào dự đoán hôn nhân căn cứ vào nam nữ khác nhau mà Dụng thần cũng khác nhau. Nam dự đoán hôn nhân lấy Thê Tài làm Dụng thần. Nữ dự đoán hôn nhân thì lấy Quan Quỷ làm Dụng thần... **Ví dụ 1:** Ngày Tân Sửu tháng Tị năm Ất Dậu, dự đoán hôn sự con gái, được quẻ Địa Sơn Khiêm biến Địa Thủy Sư."
  - **Criterion A (Diacritics)**: PASS. All Vietnamese tonal accents and diacritics (ă, â, đ, ê, ô, ơ, ư) match the source image exactly and conform to Unicode NFC normalization.
  - **Criterion B (Completeness)**: PASS. Complete narrative, hexagram table details (Huynh Đệ, Tử Tôn, Phụ Mẫu, Quan Quỷ, Thê Tài, Đằng Xà, Câu Trần, Chu Tước, Thanh Long, Huyền Vũ, Bạch Hổ, Phục thần), and commentary preserved without truncation or summarization.
  - **Criterion C (Asset Fidelity)**: PASS. Hexagram diagram cleanly cropped as `assets/page_0007_img_01.png` and correctly referenced via `![Quẻ Địa Sơn Khiêm biến Địa Thủy Sư](assets/page_0007_img_01.png)`.
  - **Criterion D (Cleanliness)**: PASS. Printed page number "4" at the bottom is completely removed from Markdown.

- **Page 50**:
  - **Source Scan**: `pages/page_0050.png` (Printed book page 47)
  - **Assembled Markdown**: `chapters/ch08.md` (lines 61–86)
  - **Image Text**: "Ví dụ 3: Ngày Giáp Dần tháng hợi năm Bính Tuất, nữ đoán hôn nhân con trai (sinh 1976), được quẻ Trạch Phong Đại Quá biến Thiên Phong Cấu... Thê Tài làm Dụng thần. Trong quẻ Thê Tài lưỡng hiện, lấy hào phát động Thê Tài Mùi thổ làm Dụng thần."
  - **Markdown Text**: "**Ví dụ 3:** Ngày Giáp Dần tháng hợi năm Bính Tuất, nữ đoán hôn nhân con trai (sinh 1976), được quẻ Trạch Phong Đại Quá biến Thiên Phong Cấu... Thê Tài làm Dụng thần. Trong quẻ Thê Tài lưỡng hiện, lấy hào phát động Thê Tài Mùi thổ làm Dụng thần."
  - **Criterion A (Diacritics)**: PASS. Accurate tonal marks and vowels in standard Unicode NFC.
  - **Criterion B (Completeness)**: PASS. All 5 paragraphs, astrological metadata (MỘC, Không Vong: Tý, Sửu), hexagram structure, and outcome feedback are fully transcribed.
  - **Criterion C (Asset Fidelity)**: PASS. Diagram exists as `assets/page_0050_img_01.png` and is linked via `![Quẻ Trạch Phong Đại Quá biến Thiên Phong Cấu](assets/page_0050_img_01.png)`.
  - **Criterion D (Cleanliness)**: PASS. Book page number "47" is cleanly stripped.

- **Page 100**:
  - **Source Scan**: `pages/page_0100.png` (Printed book page 97)
  - **Assembled Markdown**: `chapters/ch16.md` (lines 182–209)
  - **Image Text**: "Quẻ du hồn, chủ chia ly, lại Quan Quỷ động hóa hồi đầu khắc, bản thân muốn ly hôn với chồng. Quẻ tại cung Khảm, chồng là một người rất nhanh trí... Ví dụ 6: Ngày Nhâm Thân tháng Dần, nữ (57 tuổi) đoán có thể kết hôn với người đàn ông hay không? Được quẻ Thủy Sơn Kiển biến Thủy Hỏa Ký Tế."
  - **Markdown Text**: "Quẻ du hồn, chủ chia ly, lại Quan Quỷ động hóa hồi đầu khắc, bản thân muốn ly hôn với chồng. Quẻ tại cung Khảm, chồng là một người rất nhanh trí... **Ví dụ 6:** Ngày Nhâm Thân tháng Dần, nữ (57 tuổi) đoán có thể kết hôn với người đàn ông hay không? Được quẻ Thủy Sơn Kiển biến Thủy Hỏa Ký Tế."
  - **Criterion A (Diacritics)**: PASS. Exact match of Vietnamese characters in Unicode NFC.
  - **Criterion B (Completeness)**: PASS. Continuity from preceding page preserved, full hexagram table and analysis paragraphs transcribed verbatim.
  - **Criterion C (Asset Fidelity)**: PASS. Diagram exists as `assets/page_0100_img_01.png` and is embedded via `![Quẻ Thủy Sơn Kiển biến Thủy Hỏa Ký Tế](assets/page_0100_img_01.png)`.
  - **Criterion D (Cleanliness)**: PASS. Printed page number "97" is cleanly omitted.

- **Page 140**:
  - **Source Scan**: `pages/page_0140.png` (Printed book page 137)
  - **Assembled Markdown**: `chapters/ch22.md` (lines 1–43)
  - **Image Text**: "CHƯƠNG 8: ỨNG KỲ HÔN NHÂN\n\nThông thường dựa vào Dụng thần để phán đoán ứng kỳ... Ví dụ 1: Ngày Quý Tị tháng Mùi năm Giáp Thân, nam đoán quan hệ với người tình có lâu dài không? Được quẻ Sơn Địa Bác biến Hỏa Địa Tấn... Ví dụ 2: Ngày Giáp Thìn tháng Thân..."
  - **Markdown Text**: "# CHƯƠNG 8: ỨNG KỲ HÔN NHÂN\n\nThông thường dựa vào Dụng thần để phán đoán ứng kỳ... **Ví dụ 1:** Ngày Quý Tị tháng Mùi năm Giáp Thân, nam đoán quan hệ với người tình có lâu dài không? Được quẻ Sơn Địa Bác biến Hỏa Địa Tấn... **Ví dụ 2:** Ngày Giáp Thìn tháng Thân..."
  - **Criterion A (Diacritics)**: PASS. Perfect Vietnamese diacritics and NFC encoding.
  - **Criterion B (Completeness)**: PASS. Heading, introductory rules, both divination examples (Ví dụ 1 & Ví dụ 2) and hexagram tables completely transcribed.
  - **Criterion C (Asset Fidelity)**: PASS. Both diagrams are extracted (`assets/page_0140_img_01.png`, `assets/page_0140_img_02.png`) and correctly referenced in Markdown.
  - **Criterion D (Cleanliness)**: PASS. Book page number "137" cleanly removed.

- **Page 175**:
  - **Source Scan**: `pages/page_0175.png` (Printed book page 172)
  - **Assembled Markdown**: `chapters/ch26.md` (lines 94–123)
  - **Image Text**: "minh bản thân rất yêu chồng từ tận đáy lòng. Dụng thần tại hào 5, hào 5 là tôn vị, chồng rất quan trọng trong lòng cô... Ví dụ 5: Ngày Bính Ngọ tháng Ngọ năm Tân Tị, nữ đoán duyên phận vợ chồng, được quẻ Sơn Phong Cổ biến Thủy Phong Tỉnh."
  - **Markdown Text**: "minh bản thân rất yêu chồng từ tận đáy lòng. Dụng thần tại hào 5, hào 5 là tôn vị, chồng rất quan trọng trong lòng cô... **Ví dụ 5:** Ngày Bính Ngọ tháng Ngọ năm Tân Tị, nữ đoán duyên phận vợ chồng, được quẻ Sơn Phong Cổ biến Thủy Phong Tỉnh."
  - **Criterion A (Diacritics)**: PASS. Diacritics exactly match source image; NFC verified.
  - **Criterion B (Completeness)**: PASS. Verbatim transcription of cross-page split sentence, analytical reasoning, hexagram table, and feedback.
  - **Criterion C (Asset Fidelity)**: PASS. Diagram preserved as `assets/page_0175_img_01.png` and embedded via `![Quẻ Sơn Phong Cổ biến Thủy Phong Tỉnh](assets/page_0175_img_01.png)`.
  - **Criterion D (Cleanliness)**: PASS. Bottom page number "172" omitted.

- **Page 218**:
  - **Source Scan**: `pages/page_0218.png` (Printed book page 215)
  - **Assembled Markdown**: `chapters/ch31.md` (lines 1–28)
  - **Image Text**: "CHƯƠNG 9: LY HÔN\n\nHào Thế vượng tướng được sinh, thuyết minh bản thân mang hy vọng về hôn nhân... Ví dụ 1: Ngày Kỷ Hợi tháng Mão, nữ đoán chồng muốn [tạp/ly] hôn, kết quả ra sao? Được quẻ Sơn Phong Cổ."
  - **Markdown Text**: "# CHƯƠNG 9: LY HÔN\n\nHào Thế vượng tướng được sinh, thuyết minh bản thân mang hy vọng về hôn nhân... **Ví dụ 1:** Ngày Kỷ Hợi tháng Mão, nữ đoán chồng muốn ly hôn, kết quả ra sao? Được quẻ Sơn Phong Cổ."
  - **Criterion A (Diacritics)**: PASS. Vietnamese accents match source text; standard NFC encoding.
  - **Criterion B (Completeness)**: PASS. Chapter title, 4 guideline paragraphs, Ví dụ 1 table, astrological analysis, and feedback verbatim (with typographic correction of typographical slip "tạp hôn" to "ly hôn").
  - **Criterion C (Asset Fidelity)**: PASS. Hexagram diagram extracted as `assets/page_0218_img_01.png` and referenced via `![Quẻ Sơn Phong Cổ](assets/page_0218_img_01.png)`.
  - **Criterion D (Cleanliness)**: PASS. Bottom page number "215" cleanly excluded.
