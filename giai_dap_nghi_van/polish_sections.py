import os

target_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\giai_dap_nghi_van"
frag_dir = os.path.join(target_dir, "fragments")

# 1. Polish ch03: Merge the figure block under "### Lý luận về 5 loại Nguyên thần" or add claim bullets
ch03_path = os.path.join(frag_dir, "ch03_chuong_10_nghi_van_ve_5_loai_nguyen_than_branches.md")
with open(ch03_path, "r", encoding="utf-8") as f:
    ch03_content = f.read()

# Replace "### Đồ hình minh họa chứng tích quẻ Giải biến Quy Muội" with claim bullets under previous section
old_ch03_part = """### Đồ hình minh họa chứng tích quẻ Giải biến Quy Muội
- **Chứng cứ đồ hình và mối tương quan hào tượng**:
  - **Hình 3.** Sơ đồ quẻ Giải biến Quy Muội"""

new_ch03_part = """- **Minh định quẻ Giải biến Quy Muội về tương tác Huynh Đệ lâm Chu Tước**:
  - Hào sơ Huynh Đệ Dần mộc phát động lâm Chu Tước, gặp Không Vong: Biểu thị khẩu thiệt tranh chấp giữa đường nhưng Không Vong chủ hư kinh (sợ bóng sợ gió), người xem chỉ chứng kiến chứ không trực tiếp vướng vào kiện cáo.
  - Hào Thế Thê Tài Thìn thổ bị Huynh Đệ động khắc: Báo hiệu hao tổn tài vật, đồ dùng mang theo người (thực tế máy tính xách tay bị hỏng giữa đường).
  - Khẩu quyết xuất Không định kỳ khắc Thế: Dù hiện tại Không Vong không thể khắc Thế, nhưng nếu có việc quan trọng cần xuất Không thì vẫn ứng kỳ, song quẻ sự vụ ngắn ngày lấy tượng lúc gieo làm trọng.
  - **Hình 3.** Sơ đồ quẻ Giải biến Quy Muội"""

ch03_content = ch03_content.replace(old_ch03_part, new_ch03_part)
with open(ch03_path, "w", encoding="utf-8") as f:
    f.write(ch03_content)

# 2. Polish ch15: Add claim bullets under "### Bản chất hào hóa Nhật Nguyệt"
ch15_path = os.path.join(frag_dir, "ch15_chuyen_luan_ly_thuyet_phan_inh_ly_tuong_branches.md")
with open(ch15_path, "r", encoding="utf-8") as f:
    ch15_content = f.read()

old_ch15_part = """  - **Trường hợp Hóa Hồi Đầu Khắc (Đại hung)**: Nếu hào động là Tị hỏa mà biến ra Tý thủy, mặc dù Tý thủy chính là Nhật thần hoặc Nguyệt kiến, thì bản chất ngũ hành Thủy vẫn khắc Hỏa; đây dứt khoát là Hóa Hồi Đầu Khắc mang tính chất hung hiểm triệt để, không thể coi là hóa cát."""

new_ch15_part = """  - **Trường hợp Hóa Hồi Đầu Khắc (Đại hung)**: Nếu hào động là Tị hỏa mà biến ra Tý thủy, mặc dù Tý thủy chính là Nhật thần hoặc Nguyệt kiến, thì bản chất ngũ hành Thủy vẫn khắc Hỏa; đây dứt khoát là Hóa Hồi Đầu Khắc mang tính chất hung hiểm triệt để, không thể coi là hóa cát.
- **Nguyên lý tương tác hai chiều giữa Nhật Nguyệt và Hào biến**:
  - Nhật Nguyệt là cán cân điều tiết toàn quẻ, nhưng khi hào động biến ra chi trùng với Nhật Nguyệt thì chi đó đóng vai trò là Hào biến trực tiếp tác động lên hào gốc.
  - Nếu hào biến quay lại khắc hào động (hồi đầu khắc), sức tàn phá càng tăng gấp bội do hào biến thừa hưởng vượng khí tối cao từ Nhật Nguyệt.
  - Việc nhận định "hóa Nhật Nguyệt là hóa cát" mà bỏ qua tương khắc ngũ hành là ngụy biện kinh viện làm sai lệch kết quả dự đoán.
  - Trong thực chiến: Hào Tử Tôn là cội nguồn của tài lộc, khi Tử Tôn động hóa Phụ Mẫu hồi đầu khắc trùng Nhật Nguyệt thì nguồn sinh tài hoàn toàn bị triệt hạ."""

ch15_content = ch15_content.replace(old_ch15_part, new_ch15_part)
with open(ch15_path, "w", encoding="utf-8") as f:
    f.write(ch15_content)

print("Polished ch03 and ch15 successfully.")
