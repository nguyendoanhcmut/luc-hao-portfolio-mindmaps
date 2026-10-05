import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
from base_generator import figs_dict, make_evidence_block

def write_ch10():
    # fragments/ch10_chuong_9_hinh_thuc_ton_tai_cua_ngu_hanh_branches.md
    # figs: fig_43 to fig_49
    lines = [
        "## Chương 9: Hình Thức Tồn Tại Của Ngũ Hành Theo Con Số",
        "",
        "- **Hệ thống con số ngũ hành trong Dịch học:**",
        "  - Số Tiên thiên Bát Quái: Càn 1, Đoài 2, Ly 3, Chấn 4, Tốn 5, Khảm 6, Cấn 7, Khôn 8.",
        "  - Số Ngũ hành sinh thành (Hà Đồ): Thiên nhất sinh Thủy, Địa lục thành chi (1, 6 - Thủy); Địa nhị sinh Hỏa, Thiên thất thành chi (2, 7 - Hỏa); Thiên tam sinh Mộc, Địa bát thành chi (3, 8 - Mộc); Địa tứ sinh Kim, Thiên cửu thành chi (4, 9 - Kim); Thiên ngũ sinh Thổ, Địa thập thành chi (5, 10 - Thổ).",
        "  - Ứng dụng số lượng vật phẩm, số ngày đặt, kích thước, tầng lầu, số tiền để đồng bộ tần số hóa giải.",
        "- **Quái lệ 1: Đoán vợ đi công tác cát hung bình an (Ngày Mậu Tý tháng Nhâm Ngọ)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_43'],
        custom_proof="Quẻ Tùy biến Quải; Thê Tài Mùi thổ phục tàng; hào sơ sơ động hóa Huynh Đệ Tý thủy xung Khôn; dùng số 6 Thủy bồi bổ tài lộc.",
        custom_see="Hào sơ Quan Quỷ Tý thủy động hóa Huynh Đệ Dần mộc; Thê Tài Mùi thổ phục hào 2."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Vợ đi công tác lấy Thê Tài làm Dụng thần, phục tàng dưới Huynh Đệ Dần mộc bị khắc; hào sơ động Thủy vượng.",
        "    - Nhìn vào: Con số 6 thuộc Thủy (Hà Đồ) giúp chuyển hóa tương sinh Mộc sinh Hỏa thông quan.",
        "    - Đối thoại thực tế: Chồng lo lắng chuyến công tác phương Nam xa xôi bất trắc.",
        "  - **Phương án hóa giải:** Mang theo 6 đồng xu may mắn hoặc nộp tiền vé số có đuôi 6.",
        "  - **Ứng nghiệm thực tế:** Chuyến công tác diễn ra thuận lợi vượt mong đợi, ký kết hợp đồng giá trị lớn.",
        "- **Quái lệ 2: Người phụ nữ vội vã cầu tài giải hạn (Ngày Giáp Thân tháng Bính Ngọ)**"
    ] + make_evidence_block(
        figs_dict['fig_44'],
        custom_proof="Quẻ Thăng biến Tỉnh; Phụ Mẫu Tị hỏa lâm Nguyệt kiến; Quan Quỷ Dậu kim Không Vong; dùng số 4 và 9 Kim xuất Không.",
        custom_see="Hào 3 Tử Tôn Thìn thổ động hóa Quan Quỷ Dậu kim; hào Thế Quan Quỷ Dậu kim Không Vong."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Quan Quỷ Dậu kim Không Vong bị Hỏa khắc; Kim số 4, 9; kích hoạt Kim khí thu nợ.",
        "    - Nhìn vào: Dùng 9 đồng tiền xu hoặc 4 nén vàng phong thủy đặt góc Tây.",
        "    - Đối thoại thực tế: Khách hàng bị khách nợ trốn tránh không trả, nguy cơ phá sản.",
        "  - **Phương án hóa giải:** Đặt 4 thỏi vàng giả và 9 đồng xu tại góc Tây bàn làm việc.",
        "  - **Ứng nghiệm thực tế:** Khách nợ bất ngờ gọi điện chuyển khoản thanh toán đủ số nợ sau 9 ngày.",
        "- **Quái lệ 3: Dịch hữu Trần Lỗ Tây xem quẻ cứu hạn bệnh hiểm (Ngày Mậu Ngọ tháng Giáp Thìn)**"
    ] + make_evidence_block(
        figs_dict['fig_45'],
        custom_proof="Quẻ Lý biến Tụng; hào Ứng Thê Tài Tý thủy lâm Nguyệt phá; Tử Tôn Thân kim động sinh Thủy; dùng 1 hoặc 6 chậu nước giải cứu.",
        custom_see="Hào 4 Huynh Đệ Ngọ hỏa động hóa Quan Quỷ Thân kim; hào Ứng Thê Tài Tý thủy."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Thê Tài Tý thủy Nguyệt phá Thổ khắc nặng, bệnh sốt cao co giật; cần tăng cường số Thủy 1, 6.",
        "    - Nhìn vào: Thân kim động sinh Tý thủy; số 6 là số thành của Thủy.",
        "    - Đối thoại thực tế: Dịch hữu Trần Lỗ Tây bàn luận học thuật áp dụng ngay cho người nhà nguy cấp.",
        "  - **Phương án hóa giải:** Đặt 6 cốc nước sạch phương Bắc và uống thuốc vào giờ Tý.",
        "  - **Ứng nghiệm thực tế:** Cơn sốt lui hẳn sau 6 giờ, huyết áp và tim mạch ổn định an toàn.",
        "- **Quái lệ 4: Người đàn ông đoán cầu tài kinh doanh (Ngày Mậu Thân tháng Mậu Thân)**"
    ] + make_evidence_block(
        figs_dict['fig_46'],
        custom_proof="Quẻ Truân biến Cách; Thê Tài Ngọ hỏa Không Vong; Huynh Đệ Tý thủy trì Thế; dùng số 2 và 7 Hỏa kích tài.",
        custom_see="Hào 2 Quan Quỷ Dần mộc động hóa Tử Tôn Sửu thổ; Thê Tài Ngọ hỏa Không Vong."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Thê Tài Ngọ hỏa Không Vong bị Thế hào Tý thủy khắc; cần số Hỏa 2, 7 để dẫn dụ tài khí xuất Không.",
        "    - Nhìn vào: Số 7 số thành của Hỏa; 7 ngọn nến đỏ hoặc 2 bức tranh lửa.",
        "    - Đối thoại thực tế: Thương nhân đầu tư kinh doanh nhà hàng ăn uống nhưng chưa hút khách.",
        "  - **Phương án hóa giải:** Thắp 7 ngọn nến thơm màu đỏ ở sảnh đón khách lúc 19h (giờ Tuất khố).",
        "  - **Ứng nghiệm thực tế:** Lượng khách đến đặt bàn tăng vọt, nhà hàng kín chỗ suốt tuần.",
        "- **Quái lệ 5: Phụ nữ đoán bệnh sốt xuất huyết co giật (Ngày Bính Thân tháng Mậu Ngọ)**"
    ] + make_evidence_block(
        figs_dict['fig_47'],
        custom_proof="Quẻ Đỉnh biến Đại Quá; Thế hào Phụ Mẫu Mão mộc lâm Bạch Hổ; Cừu thần và Kỵ thần đồng phát; dùng số 1 Thủy hạ hỏa cứu mộc.",
        custom_see="Hào 2 Thê Tài Dần mộc động hóa Quan Quỷ Hợi thủy; quẻ Hỏa Phong Đỉnh."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Hỏa vượng thiêu Mộc; Cừu thần Hỏa và Kỵ thần Kim hợp lực hại Dụng thần; cần số 1 Thủy để làm dịu.",
        "    - Nhìn vào: Số 1 (Thiên nhất sinh Thủy) nguồn nước đầu nguồn dập lửa.",
        "    - Đối thoại thực tế: Bệnh nhân mê sảng co giật sốt cao không hạ.",
        "  - **Phương án hóa giải:** Cho uống 1 bát nước linh phù Thủy và đắp khăn lạnh 10 phút một lần.",
        "  - **Ứng nghiệm thực tế:** Nhiệt độ cơ thể hạ về mức bình thường, bệnh nhân tỉnh táo nhận biết người thân.",
        "- **Quái lệ 6: Con trai lười học mê chơi điện tử (Ngày Tân Tị tháng Quý Tị)**"
    ] + make_evidence_block(
        figs_dict['fig_48'],
        custom_proof="Quẻ Đồng Nhân biến Khuê; Quan Quỷ Hợi thủy Nguyệt phá Nhật phá; Phụ Mẫu Sửu thổ trì Thế; dùng số 6 giải phá khai trí.",
        custom_see="Hào 2 Quan Quỷ Hợi thủy lâm Nguyệt phá; hào 3 Huynh Đệ Hợi thủy."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Quan Quỷ Hợi thủy đại diện kỷ luật và tập trung bị song Tị xung phá; cháu bé ham chơi mất kiểm soát.",
        "    - Nhìn vào: Dùng số 6 Thủy và phương vị Hợi để phục hồi Quan tinh chế ngự Huynh Đệ.",
        "    - Đối thoại thực tế: Người cha bất lực vì con trốn học chơi game suốt ngày đêm.",
        "  - **Phương án hóa giải:** Đặt 6 cây bút lông trên bàn học hướng Tây Bắc (cung Càn/Hợi).",
        "  - **Ứng nghiệm thực tế:** Cháu bé tự giác quay lại bàn học, kết thúc học kỳ xếp hạng tiến bộ vượt bậc.",
        "- **Quái lệ 7: Đoán bệnh người cha già suy kiệt (Ngày Ất Dậu tháng Quý Tị)**"
    ] + make_evidence_block(
        figs_dict['fig_49'],
        custom_proof="Quẻ Quy Muội; Phụ Mẫu Tị hỏa lâm Nguyệt kiến; Nguyên thần Dần mộc bị Nhật Dậu khắc; số 3 Mộc bồi đắp sinh khí.",
        custom_see="Quẻ Lôi Trạch Quy Muội; hào 2 Phụ Mẫu Tị hỏa; hào sơ Tử Tôn Tý thủy."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Nguyên thần Dần mộc bị Nhật Dậu khắc tuyệt; số 3 và 8 Mộc cần được bổ sung khẩn cấp.",
        "    - Nhìn vào: Trồng 3 chậu cây xanh phong thủy tại phòng ngủ của cụ ông.",
        "    - Đối thoại thực tế: Người con lo lắng cụ tuổi già sức yếu khó qua khỏi mùa hạ.",
        "  - **Phương án hóa giải:** Đặt 3 chậu cây cảnh tươi tốt phương Đông để tiếp sinh khí.",
        "  - **Ứng nghiệm thực tế:** Cụ ông hồi phục thể trạng, ăn được cháo và trò chuyện vui vẻ cùng con cháu."
    ])
    return "\n".join(lines) + "\n"

def write_ch11():
    # fragments/ch11_chuong_10_hinh_thuc_ton_tai_cua_ngu_hanh_branches.md
    # figs: fig_50 to fig_54
    lines = [
        "## Chương 10: Hình Thức Tồn Tại Của Ngũ Hành Theo Âm Thanh",
        "",
        "- **Ngũ âm và sóng âm ngũ hành trong dự đoán và trị liệu:**",
        "  - Hệ thống Ngũ âm: Cung (Thổ), Thương (Kim), Giốc (Mộc), Chủy (Hỏa), Vũ (Thủy).",
        "  - Tần số âm thanh, tiếng nhạc cụ, tiếng tụng niệm, chuông gió tác động trực tiếp lên hệ thần kinh và kinh lạc tạng phủ.",
        "- **Quái lệ 1: Người chồng xin đoán cho vợ bị đau răng buốt óc (Ngày Quý Sửu tháng Ất Dậu)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_50'],
        custom_proof="Quẻ Sư biến Thăng; hào 2 Quan Quỷ Thìn thổ lâm Chu Tước; Phụ Mẫu Dậu kim vượng; dùng âm thanh Thương (Kim) dứt cơn đau.",
        custom_see="Hào 2 Quan Quỷ Thìn thổ lâm Chu Tước động hóa Thê Tài Hợi thủy; Phụ Mẫu Dậu kim trì Thế."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Hào 2 là hàm răng mặt lâm Chu Tước viêm tủy răng cấp; Kim vượng khắc Mộc thần kinh.",
        "    - Nhìn vào: Dùng âm thanh kim loại thanh tao để phân tán xung lực ức chế thần kinh đau.",
        "    - Đối thoại thực tế: Người chồng thương vợ đau răng cả đêm không ngủ được.",
        "  - **Phương án hóa giải:** Nghe bản nhạc chuông kim khánh âm điệu thanh thoát 15 phút.",
        "  - **Ứng nghiệm thực tế:** Sau 15 phút nghe nhạc buốt răng dịu dần rồi biến mất hoàn toàn.",
        "- **Quái lệ 2: Cụ già đau quặn bụng cấp cứu bệnh viện (Ngày Canh Dần tháng Bính Tuất)**"
    ] + make_evidence_block(
        figs_dict['fig_51'],
        custom_proof="Quẻ Hằng biến Tỉnh; hào 3 Huynh Đệ Dậu kim động hóa Quan Quỷ Hợi thủy; cung Chấn (bụng); dùng âm Giốc (Mộc) điều khí.",
        custom_see="Hào 3 Huynh Đệ Dậu kim động hóa Quan Quỷ Hợi thủy; hào sơ Phụ Mẫu Tý thủy."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Bệnh viện tiêm thuốc giảm đau không đỡ; ruột co thắt dữ dội do khí uất kết.",
        "    - Nhìn vào: Âm Giốc (tiếng sáo trúc, tiêu) sơ can lý khí thư giãn nhu động ruột.",
        "    - Đối thoại thực tế: Bệnh nhân đau đớn vã mồ hôi nghi tắc ruột cấp.",
        "  - **Phương án hóa giải:** Bật khúc nhạc sáo trúc âm điệu dịu êm bên tai bệnh nhân.",
        "  - **Ứng nghiệm thực tế:** Bệnh nhân giãn cơ ruột, trung tiện được và cơn đau bụng biến mất không cần mổ.",
        "- **Quái lệ 3: Người xuất hành xem cát hung lộ trình (Ngày Canh Tý tháng Canh Dần)**"
    ] + make_evidence_block(
        figs_dict['fig_52'],
        custom_proof="Quẻ Khôn biến Di; hào 3 Huynh Đệ Thìn thổ động hóa Thê Tài Tý thủy; dùng âm Cung (Thổ) trầm ấm trấn an tinh thần.",
        custom_see="Hào 3 Huynh Đệ Thìn thổ động; hào 6 Tử Tôn Dậu kim; quẻ thuần Khôn."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Xuất hành quẻ biến Di (nuôi dưỡng); tâm lý bồn chồn lo lắng bất an trước chuyến đi.",
        "    - Nhìn vào: Âm Cung (tiếng đàn tranh, trống đất) trầm ổn dưỡng tâm an định thần phách.",
        "    - Đối thoại thực tế: Người chuẩn bị đi xa lo sợ gặp rủi ro dọc đường.",
        "  - **Phương án hóa giải:** Nghe nhạc thiền âm Cung Thổ trước khi lên đường.",
        "  - **Ứng nghiệm thực tế:** Chuyến đi bình an, tinh thần sảng khoái, mọi việc hoàn thành viên mãn.",
        "- **Quái lệ 4: Người đàn ông đoán chứng mất ngủ kinh niên (Ngày Quý Dậu tháng Quý Mão)**"
    ] + make_evidence_block(
        figs_dict['fig_53'],
        custom_proof="Quẻ Khảm biến Ký Tế; hào 3 Huynh Đệ Thìn thổ động; tâm thận bất giao; dùng âm Vũ (Thủy) tiếng suối chảy an thần.",
        custom_see="Hào 3 Huynh Đệ Thìn thổ động hóa Quan Quỷ Mão mộc; quẻ thuần Khảm."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Quẻ Khảm biến Ký Tế; Thủy Hỏa chưa điều hòa dẫn đến tim đập nhanh mất ngủ triền miên.",
        "    - Nhìn vào: Âm Vũ (tiếng mưa rơi, tiếng suối chảy róc rách) tư âm giáng hỏa.",
        "    - Đối thoại thực tế: Bệnh nhân mất ngủ 6 tháng, uống thuốc ngủ bị lờn thuốc.",
        "  - **Phương án hóa giải:** Mở máy phát tiếng suối chảy tự nhiên nhè nhẹ trong phòng ngủ ban đêm.",
        "  - **Ứng nghiệm thực tế:** Ngay đêm đầu tiên ngủ sâu giấc 7 tiếng liền, chấm dứt ác mộng.",
        "- **Quái lệ 5: Người đàn ông đoán đau dạ dày co thắt (Ngày Mậu Ngọ tháng Kỷ Tị)**"
    ] + make_evidence_block(
        figs_dict['fig_54'],
        custom_proof="Quẻ Quải biến Đại Tráng; hào 2 Thê Tài Dần mộc động hóa Thê Tài Dần mộc; Tỳ thổ bị thương; âm Cung tiếng chuông ngân dứt đau.",
        custom_see="Hào 2 Thê Tài Dần mộc động; hào sơ Huynh Đệ Tý thủy; quẻ Trạch Thiên Quải."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Dạ dày thuộc Thổ bị Dần mộc động khắc mạnh gây viêm loét co thắt cấp.",
        "    - Nhìn vào: Âm thanh chuông đồng ngân vang kích Thổ bồi Tỳ vị.",
        "    - Đối thoại thực tế: Bệnh nhân ôm bụng rên rỉ đau quặn từng cơn.",
        "  - **Phương án hóa giải:** Gõ chuông đồng nhẹ nhàng nhịp điệu chậm rãi 20 lần.",
        "  - **Ứng nghiệm thực tế:** Cơn đau dạ dày dịu hẳn sau 10 phút, bụng ấm lại dễ chịu.",
    ])
    return "\n".join(lines) + "\n"

def write_ch12():
    # fragments/ch12_chuong_11_trong_chu_viet_va_hoa_van_cung_branches.md
    # figs: fig_55 to fig_62
    lines = [
        "## Chương 11: Trong Chữ Viết Và Hoa Văn Cũng Tàng Trữ Ngũ Hành",
        "",
        "- **Trường năng lượng của văn tự Hán tự và hoa văn đồ hình:**",
        "  - Chữ viết không đơn thuần là ký hiệu giao tiếp mà là đồ hình chứa đựng trường khí ngũ hành lập thể (Hán tự tượng hình khởi nguồn từ Bát Quái).",
        "  - Chiết tự và nạp năng lượng ngũ hành thông qua viết chữ lên giấy hoàng chỉ, dùng mực chu sa, đóng dấu bát quái hoặc dán đúng phương vị để trấn sát hóa cát.",
        "- **Quái lệ 1: Người đàn ông đoán bệnh phong thấp đau khớp (Ngày Tân Hợi tháng Giáp Thìn)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_55'],
        custom_proof="Quẻ Bí biến Ích; Thê Tài Tý thủy lâm Nguyệt phá; viết chữ Khảm (坎) dán phương Bắc bổ Thủy phục hồi khớp xương.",
        custom_see="Hào 2 Thê Tài Sửu thổ động hóa Tử Tôn Thân kim; hào 5 Tử Tôn Mùi thổ."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Thủy suy Mộc khô gây thoái hóa đau khớp; chữ Khảm (坎) mang toàn vẹn trường khí quẻ Khảm phương Bắc.",
        "    - Nhìn vào: Giấy vàng mực chu sa viết chữ Khảm dán phương Bắc phòng ngủ.",
        "    - Đối thoại thực tế: Bệnh nhân đi lại lục khục đau nhức xương khớp mỗi khi đổi mùa.",
        "  - **Phương án hóa giải:** Viết chữ Khảm (坎) đóng dấu Thái Cực dán tại phương Bắc.",
        "  - **Ứng nghiệm thực tế:** Khớp xương linh hoạt trở lại, cơn đau nhức tiêu giảm rõ rệt sau nửa tháng.",
        "- **Quái lệ 2: Học trò Nhật Bản văn phòng bị phạm sát phong thủy (Ngày Kỷ Dậu tháng Mậu Tuất)**"
    ] + make_evidence_block(
        figs_dict['fig_56'],
        custom_proof="Quẻ Phong biến Ly; hào 2 Thế Huynh Đệ Sửu thổ; hào 5 Tử Tôn Mùi thổ xung Thế; viết chữ Mão (卯) phương Đông hóa sát.",
        custom_see="Hào 5 Tử Tôn Mùi thổ động hóa Huynh Đệ Thân kim; hào 2 Thế Huynh Đệ Sửu thổ."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Cửa văn phòng đối diện ngã ba đường phạm sát khí; Sửu Mùi tương xung bất lợi nhân viên cãi vã hao tài.",
        "    - Nhìn vào: Chữ Mão (卯) phương Đông tương hợp giải trừ xung sát.",
        "    - Đối thoại thực tế: Học trò người Nhật lo lắng công ty làm ăn sa sút mâu thuẫn nội bộ.",
        "  - **Phương án hóa giải:** Viết chữ Mão (卯) treo tại góc Đông văn phòng công ty.",
        "  - **Ứng nghiệm thực tế:** Không khí làm việc đoàn kết trở lại, doanh thu tháng sau tăng trưởng mạnh.",
        "- **Quái lệ 3: Gặp người quen cũ đoán vận hạn trên đường quê (Ngày Canh Tý tháng Ất Mùi)**"
    ] + make_evidence_block(
        figs_dict['fig_57'],
        custom_proof="Quẻ Tiệm biến Gia Nhân; hào 5 Quan Quỷ Thân kim lâm Chu Tước; viết chữ Phúc (福) dán cửa chính nghênh cát tị hung.",
        custom_see="Hào 5 Quan Quỷ Thân kim động hóa Huynh Đệ Tuất thổ; hào Thế Tử Tôn Thân kim."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Gặp bạn cũ trên đường làng hỏi về chuyện gia đạo bất an, nghi có điềm gở.",
        "    - Nhìn vào: Chữ Phúc (福) viết đúng quy cách mang trường khí tường hòa trừ tà.",
        "    - Đối thoại thực tế: Người quen tâm sự vợ chồng hay lục đục con cái ốm vặt.",
        "  - **Phương án hóa giải:** Viết chữ Phúc đỏ mực chu sa dán ngay chính giữa cửa ra vào.",
        "  - **Ứng nghiệm thực tế:** Gia đạo êm ấm trở lại, con cái khỏe mạnh ngoan ngoãn.",
        "- **Quái lệ 4: Phụ nữ đau đầu nửa đầu kinh niên (Ngày Canh Dần tháng Tân Hợi)**"
    ] + make_evidence_block(
        figs_dict['fig_58'],
        custom_proof="Quẻ Chấn biến Dự; hào 6 Thế Thê Tài Tuất thổ; Tử Tôn Ngọ hỏa Không Vong; viết chữ Ngọ (午) để gối đầu khai thông kinh mạch.",
        custom_see="Hào 4 Huynh Đệ Ngọ hỏa Không Vong; quẻ thuần Chấn."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Hào 6 là đầu, quẻ Chấn động thần kinh; Ngọ hỏa Không Vong huyết mạch não thiếu dưỡng khí.",
        "    - Nhìn vào: Chữ Ngọ (午) bồi bổ Hỏa khí thông kinh hoạt lạc vùng đầu não.",
        "    - Đối thoại thực tế: Bệnh nhân đau nửa đầu giật từng cơn uống thuốc giảm đau không đỡ.",
        "  - **Phương án hóa giải:** Viết chữ Ngọ (午) đặt bên trong vỏ gối nằm mỗi đêm.",
        "  - **Ứng nghiệm thực tế:** Giấc ngủ sâu, chứng đau nửa đầu chấm dứt hoàn toàn sau một tuần.",
        "- **Quái lệ 5: Người đàn ông đoán sức khỏe sa sút (Ngày Bính Ngọ tháng Tân Hợi)**"
    ] + make_evidence_block(
        figs_dict['fig_59'],
        custom_proof="Quẻ Vô Vọng biến Tụy; hào 4 Huynh Đệ Cửu tứ động; viết chữ Thái (泰) mang trường khí Địa Thiên Thái hanh thông trường thọ.",
        custom_see="Hào 4 Huynh Đệ Ngọ hỏa động hóa Quan Quỷ Thân kim; hào Thế Thê Tài Thìn thổ."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Quẻ Vô Vọng biến Tụy tai ách bất ngờ rình rập; cần trường khí Thái hòa điều dưỡng.",
        "    - Nhìn vào: Tự dạng chữ Thái (泰) tam dương khai thái tiêu tai diệt tội.",
        "    - Đối thoại thực tế: Đương số cảm thấy uể oải hụt hơi làm việc mau mệt.",
        "  - **Phương án hóa giải:** Viết chữ Thái (泰) treo tại phòng khách đối diện cửa chính.",
        "  - **Ứng nghiệm thực tế:** Thể lực hồi phục nhanh chóng, tinh lực dồi dào yêu đời trở lại.",
        "- **Quái lệ 6 & 7: Đặng Vĩ tiên sinh Tứ Xuyên suy nhược thần kinh mất ngủ (Ngày Đinh Dậu tháng Đinh Mão)**"
    ] + make_evidence_block(
        figs_dict['fig_60'],
        custom_proof="Quẻ Đại Quá biến Hằng; hào 3 Quan Quỷ Dậu kim động khắc Thế; dán chữ Mão (卯) thêm chữ Minh (明) ngủ thẳng giấc tới sáng.",
        custom_see="Hào 3 Quan Quỷ Dậu kim động hóa Huynh Đệ Dần mộc; hào Thế Thê Tài Hợi thủy."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Đặng Vĩ học trò tác giả bị mất ngủ kinh niên; dán chữ Mão có đỡ nhưng vẫn trằn trọc.",
        "    - Nhìn vào: Thêm chữ Minh (明, ngày mai) bên cạnh chữ Mão trợ quang minh an thần tuyệt đối.",
        "    - Đối thoại thực tế: Đặng Vĩ thắc mắc ý nghĩa; tác giả khuyên đừng bận tâm giải thích hãy xem hiệu quả thực tế.",
        "  - **Phương án hóa giải:** Dán chữ Mão (卯) và chữ Minh (明) tại vách tường phía Tây phòng ngủ.",
        "  - **Ứng nghiệm thực tế:** Đặng Vĩ ngủ một mạch tới sáng không mộng mị, ngủ say sưa suốt mười mấy ngày liền.",
        "- **Quái lệ 8: Học trò Morita người Nhật mất ngủ vì lo lắng cho con gái (Ngày Canh Thân tháng Bính Dần)**"
    ] + make_evidence_block(
        figs_dict['fig_61'],
        custom_proof="Quẻ Lâm biến Thăng; hào 2 Quan Quỷ Mão mộc động; lo lắng cho con gái du học Mỹ dẫn đến suy nhược mất ngủ.",
        custom_see="Hào 2 Quan Quỷ Mão mộc động hóa Huynh Đệ Hợi thủy; quẻ Địa Trạch Lâm."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Con gái du học Mỹ xa xôi, người cha đêm nào cũng thức trắng lo âu suy nhược thần kinh.",
        "    - Nhìn vào: Kiểm tra phối hợp quẻ Càn Vi Thiên để tìm chữ viết hóa giải thần hiệu.",
        "- **Quái lệ 8 (tiếp theo): Quẻ Càn Vi Thiên – Dùng chữ Hợi thay vì chữ Ngọ**"
    ] + make_evidence_block(
        figs_dict['fig_62'],
        custom_proof="Quẻ Càn Vi Thiên; hào 6 Thế Phụ Mẫu Tuất thổ; hào 2 Thê Tài Dần mộc ám động khắc Thế; viết chữ Hợi (亥) đặt dưới gối hợp Dần.",
        custom_see="Hào 6 Thế Phụ Mẫu Tuất thổ; hào 2 Thê Tài Dần mộc ám động; cung Càn."
    ) + [
        "  - **Phán đoán và đối thoại (tiếp):**",
        "    - Căn cứ: Hào 6 là đầu, quẻ Càn là đầu; hào 2 Thê Tài Dần mộc ám động khắc Thế gây loạn thần kinh; Morita định viết chữ Ngọ sinh Thế.",
        "    - Nhìn vào: Tác giả chỉ rõ không nên dùng Ngọ mà viết chữ Hợi (亥); Hợi Dần lục hợp trói Dần mộc không cho khắc Thế.",
        "    - Đối thoại thực tế: Morita làm theo lời thầy viết chữ Hợi đặt dưới gối nằm.",
        "  - **Phương án hóa giải:** Viết chữ Hợi (亥) đặt dưới gối nằm trước khi ngủ.",
        "  - **Ứng nghiệm thực tế:** Ngay đêm hôm đó Morita ngủ ngon giấc bình thường, tinh thần hoàn toàn thanh thản."
    ])
    return "\n".join(lines) + "\n"

def write_ch13():
    # fragments/ch13_chuong_12_khi_che_tac_vat_hoa_giai_can_p_branches.md
    # figs: 0
    lines = [
        "## Chương 12: Khi Chế Tác Vật Hóa Giải Cần Phải Chú Ý Vấn Đề Gì?",
        "",
        "- **Nguyên tắc tổng quan khi thiết lập phương án hóa giải:**",
        "  - Chỉ tiến hành hóa giải khi quẻ xuất hiện thông tin xấu hoặc tai nạn bất lợi; quẻ cát tường không cần can thiệp.",
        "  - Phương án hóa giải phải xoay quanh Dụng thần, dựa trên sinh khắc xung hợp của Địa Chi, hào vị, lục thân, lục thần, quái cung một cách logic chặt chẽ, tuyệt đối không bịa đặt vô căn cứ.",
        "  - Tính chất lập thể của Lục Hào: Phối hợp tối thiểu từ hai thông tin trở lên (thời gian, không gian, màu sắc, con số, chất liệu) thì hiệu quả mới rõ rệt.",
        "  - Hóa giải đa tầng: Dụng thần hưu tù hóa hồi đầu sinh dùng 2 vật phẩm; Kỵ thần vượng cũng dùng 2 vật phẩm phối hợp số ngũ hành.",
        "  - Quy tắc hình thể vật phẩm: Kỵ thần Không Vong đặt vật có hốc/lỗ rỗng làm suy giảm Kỵ thần; ngược lại Dụng thần Không Vong kiêng kỵ vật có hốc/lỗ rỗng.",
        "  - Động vật hóa giải: Hóa hồi đầu sinh thì đầu động vật phải quay vào trong nhà/phòng làm việc; Kỵ thần hóa tiến thần chế tác vật một mặt thô một mặt mịn (mịn quay vào trong, thô quay ra ngoài).",
        "- **Thời gian để chế tác vật hóa giải:**",
        "  - Giờ Tý (23h-1h) là thời điểm âm dương chuyển giao luân chuyển, dễ khơi dậy linh lực ngũ hành và thúc đẩy chuyển hóa năng lượng nhất.",
        "  - Trường hợp bận có thể chế tác thời gian khác nhưng chọn giờ Tý để bài trí; hoặc chọn giờ sinh vượng cho Dụng thần.",
        "- **Công cụ để chế tác vật hóa giải:**",
        "  - Công cụ không hạn chế; khi vẽ tranh viết chữ bắt buộc thêm chu sa vào phẩm màu để nạp dương khí trừ tà.",
        "  - Vật phẩm mang theo người ưu tiên chế tác trên vải vàng hoặc giấy hoàng chỉ, đóng dấu triện Bát Quái chu sa.",
        "- **Ý thức khi chế tác vật hóa giải:**",
        "  - Người chế tác phải tập trung tinh thần cao độ, chí thành chí kính, ý niệm định hướng dung nhập vào vật phẩm để dẫn dắt linh lực.",
        "  - Mua vật phẩm sẵn có ngoài chợ mang ý thức thương mại nên cần thanh tẩy và nạp ý niệm trước khi bài trí.",
        "- **Phương pháp xử lý vật hóa giải sau khi kết thúc:**",
        "  - Sau khi tai ách đã qua hoặc bệnh lành, gieo quẻ xác định xem có nên hủy bỏ hay tiếp tục duy trì vật phẩm.",
        "  - Hóa giải niên vận đến cuối năm phải gieo quẻ lưu niên mới để tái lập phương án phù hợp với thiên khí năm mới."
    ]
    return "\n".join(lines) + "\n"

# Write Group 4 files
g4_files = {
    'ch10': ('fragments/ch10_chuong_9_hinh_thuc_ton_tai_cua_ngu_hanh_branches.md', write_ch10()),
    'ch11': ('fragments/ch11_chuong_10_hinh_thuc_ton_tai_cua_ngu_hanh_branches.md', write_ch11()),
    'ch12': ('fragments/ch12_chuong_11_trong_chu_viet_va_hoa_van_cung_branches.md', write_ch12()),
    'ch13': ('fragments/ch13_chuong_12_khi_che_tac_vat_hoa_giai_can_p_branches.md', write_ch13()),
}

for cid, (fpath, content) in g4_files.items():
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Wrote {cid} -> {fpath} ({len(content.splitlines())} lines)")
