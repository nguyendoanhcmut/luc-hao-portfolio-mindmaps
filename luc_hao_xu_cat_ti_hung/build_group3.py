import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
from base_generator import figs_dict, make_evidence_block

def write_ch05():
    # fragments/ch05_chuong_4_nap_am_cua_can_chi_va_pham_vi_s_branches.md
    # figs: fig_15, fig_16, fig_17, fig_18, fig_19
    lines = [
        "## Chương 4: Nạp Âm Của Can Chi Và Phạm Vi Sử Dụng",
        "",
        "- **Bản chất và quy luật của Nạp Âm 60 Giáp Tý:**",
        "  - Nạp âm Can Chi kết hợp Thiên Can (trời) và Địa Chi (đất) tạo ra trường năng lượng Ngũ hành vi tế, thể hiện tính chất sâu kín của sự vật mà chính ngũ hành can chi chưa bộc lộ hết.",
        "  - 30 cặp nạp âm phân bố tuần hoàn: Hải Trung Kim, Lư Trung Hỏa, Đại Lâm Mộc, Lộ Bàng Thổ, Kiếm Phong Kim, Sơn Đầu Hỏa, Giản Hạ Thủy, Thành Đầu Thổ, Bạch Lạp Kim, Dương Liễu Mộc, Tuyền Trung Thủy, Ốc Thượng Thổ, Tích Lịch Hỏa, Tùng Bách Mộc, Trường Lưu Thủy, Sa Trung Kim, Sơn Hạ Hỏa, Bình Địa Mộc, Bích Thượng Thổ, Kim Bạc Kim, Phúc Đăng Hỏa, Thiên Hà Thủy, Đại Dịch Thổ, Thoa Xuyến Kim, Tang Đố Mộc, Đại Khê Thủy, Sa Trung Thổ, Thiên Thượng Hỏa, Thạch Lựu Mộc, Đại Hải Thủy.",
        "  - Ứng dụng trong hóa giải: Nạp âm dùng để định lượng chất liệu, màu sắc và tính chất vật phẩm hóa giải khi chính ngũ hành của hào chưa đủ độ tinh tế.",
        "- **Quái lệ 1: Người đàn ông xem quẻ lưu niên vận hạn (Ngày Giáp Tuất tháng Giáp Dần năm Quý Mùi)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_15'],
        custom_proof="Hào Thế Phụ Mẫu Mùi thổ nạp âm Sa Trung Kim hưu tù; Tử Tôn Ngọ hỏa vượng động; Quan Quỷ an tĩnh; dùng nạp âm Kim giải trừ tai ách.",
        custom_see="Hào Thế Phụ Mẫu Mùi thổ; hào 4 Quan Quỷ Ngọ hỏa động hóa Tử Tôn Ngọ hỏa; hào sơ Thê Tài Mão mộc."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Tử Tôn Ngọ hỏa vượng tướng phát động khắc chế Quan Quỷ, Quan Quỷ an tĩnh nên năm nay không có họa quan trường lao lý.",
        "    - Nhìn vào: Hào Thế Mùi thổ nạp âm Sa Trung Kim, Kim suy nhược cần thổ sinh kim trợ thân; dự đoán sức khỏe và tài vận cần bồi bổ trường khí nạp âm.",
        "    - Đối thoại thực tế: Khách hàng lo lắng năm tuổi gặp hung; tác giả giải thích rõ nạp âm Sa Trung Kim cần vàng bạc kim loại trợ mệnh.",
        "  - **Phương án hóa giải:** Đeo trang sức bằng vàng hoặc vật phẩm kim loại tròn bên người để tăng cường nạp âm Kim.",
        "  - **Ứng nghiệm thực tế:** Cả năm bình an vô sự, công việc kinh doanh khởi sắc và tránh được nhiều sự cố hao tài.",
        "- **Quái lệ 2: Dự đoán và hóa giải sản phụ khó sinh tại trường Trung y (Ngày Quý Sửu tháng Mậu Thìn)**"
    ] + make_evidence_block(
        figs_dict['fig_16'],
        custom_proof="Quẻ Giải biến Lâm; Tử Tôn Thìn thổ nạp âm Đại Lâm Mộc phục tàng; Thai hào lâm thủy khố cần nạp âm Mộc sơ thông khai khiếu.",
        custom_see="Hào 2 Quan Quỷ Thìn thổ phục Tử Tôn Dần mộc; hào 4 Thê Tài Ngọ hỏa động; quẻ cung Chấn."
    ) + [
        "  - **Phán đoán và đối thoại (phần 1 - quẻ Giải biến Lâm):**",
        "    - Căn cứ: Khi giảng bài tại trường Trung y, một học viên xin đoán cho chị dâu chuyển dạ 2 ngày chưa sinh được; quẻ Giải hào Thai hào Thìn thổ nhập Mộ.",
        "    - Nhìn vào: Tử Tôn phục tàng dưới Quan Quỷ; cần phá Mộ trợ Thai xuất thế.",
        "    - Đối thoại thực tế: Gia đình sản phụ hốt hoảng tính mổ cấp cứu; tác giả bấm quẻ tiếp tục kiểm tra quẻ Tiểu Súc biến Ích.",
        "- **Quái lệ 2 (tiếp theo): Quẻ Tiểu Súc biến Ích xác định phương vị lâm bồn**"
    ] + make_evidence_block(
        figs_dict['fig_17'],
        custom_proof="Quẻ Tiểu Súc biến Ích; cung Tốn (Đông Nam) là rừng cây; Nguyên thần Dần Mão mộc vượng; dùng cành liễu phương Đông Nam khai sinh.",
        custom_see="Hào 5 Huynh Đệ Thân kim động hóa Quan Quỷ Tị hỏa; cung Tốn mộc."
    ) + [
        "  - **Phán đoán và đối thoại (phần 2 - quẻ Tiểu Súc):**",
        "    - Căn cứ: Quẻ thuộc cung Tốn (Đông Nam, mộc), Nguyên thần là Mão mộc và Dần mộc; mộc chủ sinh sôi, khai hoa nở nhụy.",
        "    - Nhìn vào: Nạp âm Dương Liễu Mộc có tính chất nhu thuận, dẫn dắt thai nhi thuận đường sinh nở.",
        "    - Đối thoại thực tế: Tác giả chỉ dẫn bẻ cành dương liễu phương Đông Nam mang vào phòng sinh.",
        "  - **Phương án hóa giải:** Cho người ra hướng Đông Nam bẻ một cành liễu tươi cắm vào bình nước đặt tại đầu giường sản phụ.",
        "  - **Ứng nghiệm thực tế:** Sau khi cắm cành liễu khoảng nửa giờ, sản phụ thuận lợi sinh hạ một bé trai mẹ tròn con vuông mà không cần phẫu thuật.",
        "- **Quái lệ 3: Bà cụ 86 tuổi xem lưu niên thọ mệnh (Ngày Quý Tị tháng Bính Thìn)**"
    ] + make_evidence_block(
        figs_dict['fig_18'],
        custom_proof="Hào Thế Tử Tôn Tý thủy lâm Bạch Hổ động hóa Dần mộc tiết khí; nạp âm Giản Hạ Thủy suy kiệt nhập Mộ ở Thìn thổ.",
        custom_see="Hào sơ Thế Tử Tôn Tý thủy lâm Bạch Hổ động hóa Dần mộc; Nguyệt kiến Thìn thổ là Thủy khố Mộ địa."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Hào Thế Tý thủy lâm Bạch Hổ chủ bệnh tật nguy hiểm, Tý thủy là nước tiểu hệ bài tiết nhập Mộ ở Nguyệt Thìn thổ (bế tắc đường tiểu); nạp âm Giản Hạ Thủy sắp cạn.",
        "    - Nhìn vào: Tháng Thìn Mộ khố mở miệng ngậm Thế; năm Mậu Dần Thổ khắc Thủy nặng nề.",
        "    - Đối thoại thực tế: Con cháu giấu bệnh tình của cụ; tác giả chỉ rõ cụ đang bị bí tiểu ngộ độc niệu nguy kịch tính mạng vào tháng Thìn, Tị.",
        "  - **Phương án hóa giải:** Dùng nước giếng tinh khiết phương Bắc kết hợp linh phù kim Thủy trợ mệnh thông quan.",
        "  - **Ứng nghiệm thực tế:** Quả nhiên cụ bà phát bệnh bí tiểu cấp tính phải nhập viện đặt ống thông, nhờ chuẩn bị trước nên qua khỏi cơn nguy kịch.",
        "- **Quái lệ 4: Nữ thủ kho thuốc đoán tai nạn hao tài (Ngày Bính Thìn tháng Kỷ Mùi)**"
    ] + make_evidence_block(
        figs_dict['fig_19'],
        custom_proof="Thế hào Phụ Mẫu Tý thủy nạp âm Giản Hạ Thủy hưu tù bị Nhật Nguyệt Thổ khắc thương; Huynh Đệ Sửu thổ động đoạt tài.",
        custom_see="Hào 3 Huynh Đệ Sửu thổ động hóa Thê Tài Ngọ hỏa; hào Thế Phụ Mẫu Tý thủy lâm Chu Tước."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Thủ kho thuốc lấy Phụ Mẫu làm Dụng thần bảo quản kho, Thê Tài làm tài sản; Huynh Đệ Sửu thổ động khắc Thế đoạt Tài báo hiệu kho thuốc bị thất thoát hoặc đền bù lớn.",
        "    - Nhìn vào: Canh Chi nạp âm của Sửu thổ là Bích Thượng Thổ khắc hại Tý thủy; cần dùng Kim thông quan Thổ sinh Thủy.",
        "    - Đối thoại thực tế: Chị thủ kho than thở kho thuốc gần đây kiểm kê thiếu hụt nghiêm trọng nguy cơ bị đền tiền và kỷ luật.",
        "  - **Phương án hóa giải:** Đặt vật phẩm kim loại màu trắng (chuông gió đồng) tại cửa kho thuốc để hóa giải sát khí của Huynh Đệ.",
        "  - **Ứng nghiệm thực tế:** Tìm ra nguyên nhân do nhầm lẫn sổ sách và chuột bọ cắn phá, tránh được khoản bồi thường hàng chục triệu đồng."
    ])
    return "\n".join(lines) + "\n"

def write_ch06():
    # fragments/ch06_chuong_5_trich_xuat_thong_tin_ngu_hanh_branches.md
    # figs: fig_20, fig_21, fig_22, fig_23
    lines = [
        "## Chương 5: Trích Xuất Thông Tin Ngũ Hành",
        "",
        "- **Nguyên lý trích xuất Ngũ hành từ vật thể tự nhiên:**",
        "  - Ngũ hành Thủy, Hỏa, Kim, Mộc, Thổ phân bố khắp vạn vật; việc ứng dụng chính xác vật phẩm tương ứng giúp kích hoạt hoặc ức chế trường khí theo ý muốn.",
        "  - Vật phẩm ngũ hành thông dụng: Thủy (nước, mưa, vải đen, cá); Hỏa (nến, lửa, vải đỏ, bếp lò); Mộc (cây cỏ, gỗ, tre trúc, vải bông); Kim (kim loại, chuông đồng, dao kéo, vải trắng); Thổ (đất sét, gốm sứ, vải vàng, tổ yến).",
        "  - Ngũ hành trong trái cây trị bệnh: Táo (ngọt - Thổ); Mận (chua - Mộc); Hạt dẻ (mặn - Thủy); Hạnh đào (đắng - Hỏa); Đào (cay - Kim).",
        "- **Quái lệ 1: Người phụ nữ đoán bệnh viêm sưng tràn dịch đầu gối (Ngày Đinh Dậu tháng Tân Sửu)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_20'],
        custom_proof="Hào sơ Thế Mùi thổ bị Nguyệt phá Nhật xung; hào 2 Tử Tôn Tị hỏa lâm Câu Trần sưng khớp gối; hào 5 Thân kim viêm phổi.",
        custom_see="Hào sơ Thê Tài Mùi thổ lâm Chu Tước; hào 2 Tử Tôn Tị hỏa Không Vong; hào 5 Quan Quỷ Thân kim phát động."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Hào sơ là bàn chân lâm Chu Tước (chứng viêm), hào 2 là đầu gối lâm Câu Trần (sưng trướng tích dịch do Thìn thổ thủy khố); hào 5 Thân kim lâm kim phổi hô hấp kém.",
        "    - Nhìn vào: Tử Tôn lâm Ứng hóa Quan Quỷ biểu thị đang uống thuốc Tây y nhưng thuốc gây tác dụng phụ nặng nề.",
        "    - Đối thoại thực tế: Bệnh nhân xác nhận đầu gối sưng phù đau nhức tràn dịch không đi lại được, khí quản ho hen uống thuốc bị phản ứng phụ mệt mỏi.",
        "  - **Phương án hóa giải:** Dùng ớt đỏ (Tị hỏa nhọn đỏ lâm Câu Trần ruộng đất), rễ cà tím (Mùi thổ hào sơ lâm Chu Tước) và tro giấy viết chữ Xà (蛇) nấu nước sôi ngâm rửa chân gối.",
        "  - **Ứng nghiệm thực tế:** Sau 4 tháng ngâm rửa liên tục, dịch khớp gối tan biến hoàn toàn, chân đi lại bình thường và dứt cơn ho hen.",
        "- **Quái lệ 2: Người phụ nữ xem bệnh cho cha già (Ngày Nhâm Thân tháng Kỷ Mùi)**"
    ] + make_evidence_block(
        figs_dict['fig_21'],
        custom_proof="Phụ Mẫu Thân kim được Nguyệt sinh Nhật phù; Kỵ thần Thê Tài Tị hỏa phục tàng nhập Mộ; trích xuất Thủy Mộc điều dưỡng.",
        custom_see="Hào 4 Phụ Mẫu Thân kim lâm Câu Trần; hào 5 Quan Quỷ Tuất thổ động hóa Huynh Đệ Tý thủy."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Phụ Mẫu Thân kim vượng tướng chứng tỏ bệnh cụ ông không nguy hiểm tính mạng nhưng khí huyết lưu thông kém.",
        "    - Nhìn vào: Hào 5 Quan Quỷ Tuất thổ động hóa Huynh Đệ Tý thủy; cần dùng Thủy làm thông quan điều hòa tạng phủ.",
        "    - Đối thoại thực tế: Người con gái lo lắng cha già suy kiệt ăn ngủ kém.",
        "  - **Phương án hóa giải:** Uống nước sắc từ thảo mộc dưỡng phế sinh tân, đặt bể cảnh nhỏ phương Bắc phòng ngủ cụ.",
        "  - **Ứng nghiệm thực tế:** Cụ ông ăn ngủ ngon miệng, tinh thần minh mẫn khỏe mạnh trở lại.",
        "- **Quái lệ 3: Người phụ nữ xem bệnh cha u bướu (Ngày Đinh Sửu tháng Kỷ Mùi)**"
    ] + make_evidence_block(
        figs_dict['fig_22'],
        custom_proof="Quẻ Cấn biến Cổ; hào 2 Quan Quỷ Dần mộc động hóa Tị hỏa; Phụ Mẫu Ngọ hỏa vượng; dùng Kim khắc Mộc tán u.",
        custom_see="Hào 2 Quan Quỷ Dần mộc động hóa Tử Tôn Tị hỏa; cung Cấn thuộc Thổ."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Cung Cấn chủ u bướu ngưng trệ, Quan Quỷ Dần mộc phát động khắc tỳ thổ gây khối u vùng bụng.",
        "    - Nhìn vào: Dần mộc động cần Kim chế phục; trích xuất năng lượng Kim từ chuông đồng và dao kéo để trấn áp mộc sát.",
        "    - Đối thoại thực tế: Bác sĩ nghi ngờ khối u ác tính chuẩn bị phẫu thuật.",
        "  - **Phương án hóa giải:** Treo chuông đồng hoặc đặt vật phẩm kim khí phương Đông Bắc và Đông để ức chế Dần mộc phát triển.",
        "  - **Ứng nghiệm thực tế:** Khối u teo nhỏ dần, xét nghiệm sinh thiết là u lành tính, phẫu thuật bóc tách thành công mỹ mãn.",
        "- **Quái lệ 4: Nữ chủ tiệm thuốc tây cầu tài hóa giải kinh doanh ế ẩm (Ngày Bính Thân tháng Canh Ngọ)**"
    ] + make_evidence_block(
        figs_dict['fig_23'],
        custom_proof="Quẻ Lý biến Khốn; Thê Tài Tý thủy lâm Nguyệt phá hưu tù; hào Ứng Huynh Đệ Thân kim phát động; dùng 9 chuông đồng kích tài.",
        custom_see="Hào 3 Huynh Đệ Sửu thổ động; hào 5 Huynh Đệ Thân kim lâm Thanh Long; Thê Tài Tý thủy phục tàng."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Tài hào Tý thủy lâm Nguyệt phá tiền tài tiêu tán; may nhờ hào Ứng Thân kim phát động sinh Thủy.",
        "    - Nhìn vào: Kim sinh Thủy; số 9 là số Lão Dương thuộc Kim/Càn; chuông đồng phát âm thanh kim khí kích hoạt tài khí.",
        "    - Đối thoại thực tế: Chủ tiệm thuốc buồn rầu vì mở tiệm mấy tháng vắng khách, nợ tiền thuê nhà.",
        "  - **Phương án hóa giải:** Treo 9 cái chuông đồng nhỏ trước cửa tiệm thuốc phương Tây Bắc để mỗi khi khách ra vào chuông reo kích Kim sinh Thủy.",
        "  - **Ứng nghiệm thực tế:** Tiệm thuốc đột ngột đông khách nườm nượp, doanh thu tăng gấp ba lần ngay trong tháng đó."
    ])
    return "\n".join(lines) + "\n"

def write_ch07():
    # fragments/ch07_chuong_6_hinh_thuc_ton_tai_cua_ngu_hanh_branches.md
    # figs: fig_24, fig_25, fig_26, fig_27, fig_28, fig_29
    lines = [
        "## Chương 6: Hình Thức Tồn Tại Của Ngũ Hành Theo Phương Vị",
        "",
        "- **Không gian phương vị và trường khí Ngũ hành:**",
        "  - Phương vị trong Bát Quái phân định rõ trường khí: Bắc (Khảm - Thủy), Nam (Ly - Hỏa), Đông (Chấn - Mộc), Đông Nam (Tốn - Mộc), Tây (Đoài - Kim), Tây Bắc (Càn - Kim), Đông Bắc (Cấn - Thổ), Tây Nam (Khôn - Thổ).",
        "  - Thay đổi vị trí cư ngụ, giường ngủ, bàn làm việc hoặc hướng di chuyển là phương thức hóa giải quyền năng dựa trên dịch chuyển không gian phương vị.",
        "- **Quái lệ 1: Người phụ nữ xem con gái thi chuyển cấp ba (Ngày Kỷ Dậu tháng Bính Ngọ)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_24'],
        custom_proof="Quẻ Giải biến Đại Súc; Phụ Mẫu Ngọ hỏa lâm Nguyệt kiến cực vượng nhưng hào Thế Thân kim bị khắc; dùng hướng Tây Bắc cứu viện.",
        custom_see="Hào 2 Quan Quỷ Thìn thổ động hóa Thê Tài Dần mộc; hào Thế Huynh Đệ Thân kim."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Phụ Mẫu Ngọ hỏa lệnh tháng thi cử văn bằng sáng chói; nhưng hào Thế Thân kim bị Ngọ hỏa khắc áp lực tâm lý thi cử căng thẳng.",
        "    - Nhìn vào: Cần chuyển dời phương vị ôn tập sang hướng Tây Bắc (Càn Kim) để tỉ hòa trợ Thế.",
        "    - Đối thoại thực tế: Mẹ cháu bé lo lắng con học tài thi phận, sức ép thi trường chuyên quá lớn.",
        "  - **Phương án hóa giải:** Kê bàn học của cháu gái quay về hướng Tây Bắc, phòng thi ngồi góc Tây Bắc.",
        "  - **Ứng nghiệm thực tế:** Cháu gái làm bài thi suôn sẻ, đỗ thủ khoa vào trường trung học trọng điểm.",
        "- **Quái lệ 2: Người đàn ông thuê đất làm trang trại kinh doanh (Ngày Canh Tuất tháng Canh Tuất)**"
    ] + make_evidence_block(
        figs_dict['fig_25'],
        custom_proof="Quẻ Thái biến Đại Súc; Thế hào Thê Tài Tý thủy lâm Mộ khố; hào Ứng Phụ Mẫu Sửu thổ hợp trói; hướng Đông Bắc phá Mộ sinh Tài.",
        custom_see="Hào 2 Thê Tài Dần mộc động hóa Thê Tài Tý thủy; quẻ Địa Thiên Thái."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Đất đai lấy Phụ Mẫu làm Dụng thần, Tài hào nhập Mộ đất đai khó sinh lợi nhuận ngay.",
        "    - Nhìn vào: Chuyển cửa chính trang trại về hướng Đông Bắc để nạp sinh khí Cấn thổ.",
        "    - Đối thoại thực tế: Người thuê đất lo ngại chôn vốn vào mảnh đất hoang hóa.",
        "  - **Phương án hóa giải:** Mở cổng trang trại ở hướng Đông Bắc và quy hoạch khu chuồng trại theo trục Đông Bắc - Tây Nam.",
        "  - **Ứng nghiệm thực tế:** Trang trại phát triển thuận lợi, thu hoạch vụ mùa bội thu ngay năm đầu tiên.",
        "- **Quái lệ 3: Người đàn ông đoán bệnh xuất huyết nội tạng (Ngày Ất Mão tháng Canh Tuất)**"
    ] + make_evidence_block(
        figs_dict['fig_26'],
        custom_proof="Quẻ Truân biến Phục; hào 2 Quan Quỷ Dần mộc vượng; Thê Tài Tị hỏa phục hào sơ lâm Bạch Hổ; dùng hướng Bắc Thủy dưỡng Mộc.",
        custom_see="Hào sơ Tử Tôn Tý thủy động hóa Huynh Đệ Sửu thổ; hào 2 Quan Quỷ Dần mộc."
    ) + [
        "  - **Phán đoán và đối thoại (phần 1 - quẻ Truân biến Phục):**",
        "    - Căn cứ: Quẻ Truân nạn sinh ban đầu; Quan Quỷ lâm Dần mộc mộc vượng khắc tỳ thổ gây xuất huyết.",
        "    - Nhìn vào: Kiểm tra phối hợp quẻ Nhu biến Thái để định rõ phương hướng tị nạn cứu chữa.",
        "    - Đối thoại thực tế: Bệnh nhân đau bụng quằn quại cấp cứu bác sĩ chưa rõ nguyên nhân xuất huyết.",
        "- **Quái lệ 3 (tiếp theo): Quẻ Nhu biến Thái xác định vị trí bệnh viện điều trị**"
    ] + make_evidence_block(
        figs_dict['fig_27'],
        custom_proof="Quẻ Nhu biến Thái; Thê Tài Tý thủy trì Thế; Tử Tôn Thân kim phát động sinh Thế; hướng Tây Nam có danh y cứu mạng.",
        custom_see="Hào 3 Huynh Đệ Thìn thổ động hóa Thê Tài Hợi thủy; hào sơ Thế Thê Tài Tý thủy."
    ) + [
        "  - **Phán đoán và đối thoại (phần 2 - quẻ Nhu biến Thái):**",
        "    - Căn cứ: Tử Tôn Thân kim (thầy thuốc danh y) phát động sinh cho hào Thế Thủy; Thân kim ở phương Tây/Tây Nam.",
        "    - Nhìn vào: Bệnh viện nằm ở phía Tây Nam thành phố sẽ có phác đồ điều trị dứt điểm.",
        "    - Đối thoại thực tế: Gia đình chuyển viện ngay theo lời khuyên của tác giả.",
        "  - **Phương án hóa giải:** Chuyển bệnh nhân sang bệnh viện ở hướng Tây Nam để bác sĩ chuyên khoa phẫu thuật.",
        "  - **Ứng nghiệm thực tế:** Ca mổ thành công ngoài mong đợi, cầm máu kịp thời và bệnh nhân xuất viện sau 10 ngày.",
        "- **Quái lệ 4: Cổ lệ – Đoán gia nô mưu phản hại chủ (Ngày Bính Tý tháng Mùi)**"
    ] + make_evidence_block(
        figs_dict['fig_28'],
        custom_proof="Quẻ Giải biến Chấn; hào sơ Thế Thê Tài Thìn thổ lâm Bạch Hổ; Huynh Đệ Dần mộc động khắc Thế; di chuyển hướng Đông Bắc thoát nạn.",
        custom_see="Hào 4 Thê Tài Ngọ hỏa động hóa Huynh Đệ Dần mộc; hào Thế Thê Tài Thìn thổ."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Gia nô mưu phản lấy Huynh Đệ làm Kỵ thần; Dần mộc động khắc Thế nguy cơ bị ám hại nửa đêm.",
        "    - Nhìn vào: Chạy sang phương Đông Bắc (Cấn Thổ) nương nhờ chỗ quan phủ trấn áp.",
        "    - Đối thoại thực tế: Chủ nhân nghi ngờ gia nô có mưu đồ phản nghịch nhưng chưa có chứng cớ.",
        "  - **Phương án hóa giải:** Đêm đó dời phòng ngủ sang dinh thự phía Đông Bắc của thân thích.",
        "  - **Ứng nghiệm thực tế:** Nửa đêm gia nô vác dao xông vào phòng cũ chém nát giường chiếu, chủ nhân thoát nạn trong gang tấc.",
        "- **Quái lệ 5: Cổ lệ – Lánh giặc cướp thời chiến loạn (Quẻ Càn biến Đại Hữu)**"
    ] + make_evidence_block(
        figs_dict['fig_29'],
        custom_proof="Quẻ Càn biến Đại Hữu; hào 3 Phục thần Huynh Đệ Thân kim động; trốn sang hang núi phương Tây Bắc giữ trọn tính mạng tài sản.",
        custom_see="Hào 3 Phụ Mẫu Thìn thổ động hóa Thê Tài Ngọ hỏa; quẻ Càn Vi Thiên thuần dương."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Giặc cướp hoành hành làng mạc; quẻ thuần Càn cương kiện, Tây Bắc là nơi hiểm trở cao ráo.",
        "    - Nhìn vào: Ẩn náu phương Tây Bắc hợp với quái khí Càn Kim để tị hung.",
        "    - Đối thoại thực tế: Dân làng hoang mang không biết chạy hướng nào để tránh thổ phỉ.",
        "  - **Phương án hóa giải:** Cả gia đình gom góp lương thực trốn lên hẻm núi phương Tây Bắc cắm trại ẩn cư.",
        "  - **Ứng nghiệm thực tế:** Giặc cướp càn quét các hướng Đông và Nam tàn phá khốc liệt, riêng vùng núi Tây Bắc an toàn tuyệt đối."
    ])
    return "\n".join(lines) + "\n"

def write_ch08():
    # fragments/ch08_chuong_7_hinh_thuc_ton_tai_cua_ngu_hanh_branches.md
    # figs: fig_30 to fig_38
    lines = [
        "## Chương 7: Hình Thức Tồn Tại Của Ngũ Hành Theo Thời Gian",
        "",
        "- **Thời gian ngũ hành luân chuyển định đoạt vận số:**",
        "  - Thời gian vận hành tuần hoàn qua 12 canh giờ, 365 ngày, 12 tháng, 24 tiết khí và các chu kỳ hoa giáp ngũ vận lục khí.",
        "  - Chọn thời điểm hành động, xuất hành, khai trương, uống thuốc hoặc đặt vật phẩm hóa giải là chìa khóa mượn thiên thời để hóa giải hung sát.",
        "- **Quái lệ 1: Người phụ nữ Thiên Tân đoán bệnh thận (Ngày Đinh Tị tháng Giáp Thìn)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_30'],
        custom_proof="Quẻ Phong biến Ký Tế; Hào 2 Thế Huynh Đệ Sửu thổ lâm Câu Trần; Thê Tài Hợi thủy Nguyệt phá; giờ Tý Hợi giờ Thủy trợ Thần.",
        custom_see="Hào sơ Phụ Mẫu Mão mộc động hóa Huynh Đệ Sửu thổ; hào 2 Thế Huynh Đệ Sửu thổ."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Thủy chủ thận hư, Hợi thủy Nguyệt phá bị thổ khắc; cần chọn giờ Hợi, Tý (nước vượng) để uống thuốc.",
        "    - Nhìn vào: Mượn thời gian Thủy vượng bổ thận ích tinh giải trừ nhiệt độc.",
        "    - Đối thoại thực tế: Bệnh nhân đau lưng mỏi gối tiểu đêm nhiều lần, thuốc Đông y uống ban ngày không hiệu quả.",
        "  - **Phương án hóa giải:** Uống thuốc bổ thận vào đúng giờ Hợi (21h-23h) và giờ Tý (23h-1h) trước khi ngủ.",
        "  - **Ứng nghiệm thực tế:** Sau 2 tuần chứng đau lưng tiểu đêm dứt hẳn, chức năng thận hồi phục rõ rệt.",
        "- **Quái lệ 2: Đồng nghiệp xem gặp lại bạn cũ thất lạc (Ngày Canh Thìn tháng Giáp Ngọ)**"
    ] + make_evidence_block(
        figs_dict['fig_31'],
        custom_proof="Quẻ Lâm biến Sư; Ứng hào Tử Tôn Dậu kim lâm Huyền Vũ; hào Thế Quan Quỷ Mão mộc; ứng kỳ ngày Dậu tương xung tương kiến.",
        custom_see="Hào 2 Thế Quan Quỷ Mão mộc; hào 6 Ứng Tử Tôn Dậu kim động hóa Huynh Đệ Hợi thủy."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Bạn cũ lấy Huynh Đệ/Ứng hào, Ứng hào Dậu kim động xung Thế; xung là động chạm gặp gỡ bất ngờ.",
        "    - Nhìn vào: Ngày Ất Dậu xung hào Thế Mão mộc là thời khắc gặp mặt.",
        "    - Đối thoại thực tế: Đồng nghiệp bồi hồi nhớ bạn thân thời thơ ấu mất liên lạc 10 năm.",
        "  - **Phương án hóa giải:** Chọn ngày Ất Dậu đi đến khu phố cũ tìm kiếm.",
        "  - **Ứng nghiệm thực tế:** Đúng ngày Ất Dậu hai người tình cờ chạm mặt trên phố, mừng rỡ nối lại tình bạn xưa.",
        "- **Quái lệ 3: Vợ bạn bị mất trộm xe đạp tìm lại (Ngày Quý Mùi tháng Bính Thân)**"
    ] + make_evidence_block(
        figs_dict['fig_32'],
        custom_proof="Quẻ Tùy biến Ký Tế; Thê Tài Thìn thổ trì Thế; Huynh Đệ Dần mộc động đoạt tài; giờ Thân xung Dần bắt kẻ trộm xe.",
        custom_see="Hào sơ Thế Thê Tài Thìn thổ; hào 3 Huynh Đệ Dần mộc động hóa Quan Quỷ Ngọ hỏa."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Xe đạp lấy Thê Tài Thìn thổ, Huynh Đệ Dần mộc động lâm Huyền Vũ là kẻ trộm lẻn lấy cắp.",
        "    - Nhìn vào: Thân kim xung khắc Dần mộc kẻ trộm bị lộ; giờ Thân (15h-17h) là ứng kỳ tìm xe.",
        "    - Đối thoại thực tế: Bạn hớt hải báo xe đạp mới mua bị dắt trộm tại cổng chợ.",
        "  - **Phương án hóa giải:** Báo bảo vệ canh chốt cổng phụ vào giờ Thân.",
        "  - **Ứng nghiệm thực tế:** Đúng 16h bảo vệ bắt quả tang kẻ trộm đang mang xe ra khỏi cổng, thu hồi nguyên vẹn chiếc xe.",
        "- **Quái lệ 4: Nữ sĩ Hồng Kông hỏi về đầu tư bất động sản (Ngày Giáp Tuất tháng Ất Tị)**"
    ] + make_evidence_block(
        figs_dict['fig_33'],
        custom_proof="Quẻ Sư biến Cấu; Phụ Mẫu Dậu kim Không Vong; Quan Quỷ Sửu thổ động; tháng Dậu xuất Không là thời điểm giao dịch.",
        custom_see="Hào 6 Ứng Phụ Mẫu Dậu kim Không Vong; hào 4 Quan Quỷ Sửu thổ động hóa Thê Tài Ngọ hỏa."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Bất động sản lấy Phụ Mẫu làm Dụng thần, Dậu kim Không Vong là hợp đồng chưa ký kết được ngay.",
        "    - Nhìn vào: Tháng 8 âm lịch (tháng Dậu) xuất Không tài vận hanh thông.",
        "    - Đối thoại thực tế: Khách hàng lo lắng thị trường nhà đất đóng băng chôn vốn.",
        "  - **Phương án hóa giải:** Kiên nhẫn chờ đến tháng Dậu mới mở bán chính thức.",
        "  - **Ứng nghiệm thực tế:** Đến tháng Dậu lượng người mua tăng vọt, bán hết dự án với lợi nhuận cao.",
        "- **Quái lệ 5: Dự định về quê ăn Tết và quẻ Hoán biến Mông (Ngày Tân Tị tháng Kỷ Tị)**"
    ] + make_evidence_block(
        figs_dict['fig_34'],
        custom_proof="Quẻ Hoán biến Mông; hào Thế Thê Tài Tị hỏa lâm Chu Tước; Quan Quỷ Dần mộc động; chọn giờ khởi hành tránh tai nạn xe cộ.",
        custom_see="Hào 2 Quan Quỷ Dần mộc động hóa Tử Tôn Thìn thổ; hào 4 Tử Tôn Mùi thổ."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Xuất hành lấy Thế hào và Tử Tôn làm bình an; Dần mộc động khắc hào lộ trình có nguy cơ va quẹt.",
        "    - Nhìn vào: Chọn giờ Ngọ khởi hành Hỏa vượng tiết Mộc an toàn.",
        "    - Đối thoại thực tế: Tác giả tự gieo quẻ kiểm tra chuyến đi đường dài.",
        "- **Quái lệ 5 (tiếp theo): Quẻ Khuê định vị thời gian an toàn**"
    ] + make_evidence_block(
        figs_dict['fig_35'],
        custom_proof="Quẻ Hỏa Trạch Khuê; hào Thế Huynh Đệ Tị hỏa; Tử Tôn Mùi thổ trì hào 2; lùi thời gian xuất phát bảo toàn chuyến đi.",
        custom_see="Quẻ Hỏa Trạch Khuê; hào 2 Tử Tôn Mão mộc; hào 5 Phụ Mẫu Mùi thổ."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Quẻ Khuê chủ trắc trở ban đầu; lùi giờ xuất phát để tránh trùng giờ hung sát trên cao tốc.",
        "    - Nhìn vào: Ứng nghiệm tai nạn giao thông xảy ra trước cung giờ xuất phát.",
        "  - **Phương án hóa giải:** Lùi giờ xuất phát chậm lại 2 tiếng so với kế hoạch ban đầu.",
        "  - **Ứng nghiệm thực tế:** Khi đi qua đoạn đường đèo thì thấy vụ tai nạn liên hoàn vừa xảy ra cách đó 1 tiếng, nếu đi đúng giờ cũ đã vướng vào thảm họa.",
        "- **Quái lệ 6: Cổ lệ – Hoãn thời gian xuất phát tránh phục kích giặc (Quẻ Ích biến Trung Phu)**"
    ] + make_evidence_block(
        figs_dict['fig_36'],
        custom_proof="Quẻ Ích biến Trung Phu; hào 2 Thế Huynh Đệ Dần mộc; hào 3 Quan Quỷ Thìn thổ động; lùi ngày khởi hành tránh phục kích.",
        custom_see="Hào 3 Quan Quỷ Thìn thổ động hóa Huynh Đệ Sửu thổ; quẻ Phong Lôi Ích."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Cổ nhân xem quẻ hành quân thấy Quan Quỷ động khắc lộ trình phục binh mai phục.",
        "    - Nhìn vào: Lùi ngày đi sang ngày Giáp Dần thoát khỏi cạm bẫy.",
        "  - **Phương án hóa giải:** Án binh bất động thêm 3 ngày rồi mới xuất quân.",
        "  - **Ứng nghiệm thực tế:** Quân địch mai phục kiệt sức rút lui, đoàn quân hành tiến an toàn tuyệt đối.",
        "- **Quái lệ 7: Mẹ đoán con trai thi cấp ba (Ngày Quý Sửu tháng Quý Mùi)**"
    ] + make_evidence_block(
        figs_dict['fig_37'],
        custom_proof="Quẻ Cấn Vi Sơn lục xung; Phụ Mẫu Ngọ hỏa lâm hào 2; Tử Tôn Thân kim trì Thế; thiếu điểm chuyển trường kịp thời gian.",
        custom_see="Quẻ thuần Cấn; hào 2 Phụ Mẫu Ngọ hỏa; hào 6 Huynh Đệ Dần mộc."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Thi cử quẻ lục xung bất lợi, thiếu 0.5 điểm vào trường công lập mong muốn.",
        "    - Nhìn vào: Nộp đơn phúc khảo và chuyển nguyện vọng trước giờ Thân ngày Bính Dần.",
        "  - **Phương án hóa giải:** Nộp hồ sơ xét tuyển nguyện vọng 2 đúng khung giờ vàng.",
        "  - **Ứng nghiệm thực tế:** Nhà trường hạ điểm chuẩn đợt 2 đúng 0.5 điểm, cháu bé được tuyển thẳng.",
        "- **Quái lệ 8: Người đàn ông đoán vận đỏ đen cờ bạc (Ngày Kỷ Mão tháng Quý Sửu)**"
    ] + make_evidence_block(
        figs_dict['fig_38'],
        custom_proof="Quẻ Độn biến Cấu; Thê Tài Dần mộc Không Vong; Huynh Đệ Thân kim động đoạt tài; khuyên can dừng bước tránh tán gia bại sản.",
        custom_see="Hào 4 Huynh Đệ Thân kim động hóa Huynh Đệ Dậu kim tiến thần; Thê Tài Dần mộc Không Vong."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Tài hào Không Vong lại gặp Huynh Đệ hóa tiến thần đoạt tài; đi cờ bạc chắc chắn thua sạch túi.",
        "    - Nhìn vào: Can ngăn không nên tham gia vào canh bạc đỏ đen.",
        "    - Đối thoại thực tế: Khách hàng mê muội tin tưởng vận đỏ; tác giả khuyên can rốt ráo.",
        "  - **Phương án hóa giải:** Hủy chuyến đi đánh bạc, ở nhà cùng vợ con.",
        "  - **Ứng nghiệm thực tế:** Người bạn rủ đi đánh bạc bị bắt trọn ổ và mất sạch tiền, đương số thoát nạn trong may mắn."
    ])
    return "\n".join(lines) + "\n"

def write_ch09():
    # fragments/ch09_chuong_8_hinh_thuc_ton_tai_cua_ngu_hanh_branches.md
    # figs: fig_39 to fig_42
    lines = [
        "## Chương 8: Hình Thức Tồn Tại Của Ngũ Hành Theo Màu Sắc",
        "",
        "- **Ý nghĩa trường khí của màu sắc ngũ hành:**",
        "  - Màu sắc là sóng ánh sáng mang tần số năng lượng ngũ hành xác định: Xanh lục/thanh (Mộc), Đỏ/tím/hồng (Hỏa), Vàng/nâu (Thổ), Trắng/bạc/vàng kim (Kim), Đen/xanh lam (Thủy).",
        "  - Ứng dụng màu sắc vào trang phục, rèm cửa, màu tường, vật dụng hàng ngày để điều chỉnh trường sinh học cơ thể.",
        "- **Quái lệ 1: Bệnh nhân hậu phẫu thuật hồi phục sức khỏe (Ngày Mậu Thân tháng Mậu Thân)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_39'],
        custom_proof="Quẻ Lâm biến Sư; hào Thế Mão mộc bị Thân kim song trùng khắc; mặc trang phục màu xanh lá bồi bổ Mộc khí.",
        custom_see="Hào 2 Thế Quan Quỷ Mão mộc lâm Câu Trần; Nhật Nguyệt Thân kim khắc hào Thế."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Hào Thế Mão mộc bị Nhật Nguyệt song Thân kim khắc thương trầm trọng; sau mổ cơ thể suy kiệt xanh xao.",
        "    - Nhìn vào: Cần dùng màu sắc của Mộc (xanh lá cây) và Thủy (xanh lam) để dưỡng Mộc chống lại Kim sát.",
        "    - Đối thoại thực tế: Người nhà bệnh nhân hỏi cách bồi dưỡng hồi phục sau đại phẫu thuật.",
        "  - **Phương án hóa giải:** Cho bệnh nhân mặc áo màu xanh lá cây và trải ga giường màu xanh lá nhạt.",
        "  - **Ứng nghiệm thực tế:** Sắc mặt bệnh nhân hồng hào nhanh chóng, vết mổ liền da đẹp không để lại di chứng.",
        "- **Quái lệ 2: Người cha đoán con trai thi đại học (Ngày Tân Mùi tháng Đinh Mùi)**"
    ] + make_evidence_block(
        figs_dict['fig_40'],
        custom_proof="Quẻ Địa Lôi Phục; Tử Tôn Dần mộc hưu tù; hào Phụ Mẫu Tị hỏa lâm Chu Tước; mặc áo đỏ vào phòng thi kích hoạt Hỏa tinh.",
        custom_see="Quẻ Địa Lôi Phục nhất dương sinh; hào sơ Tử Tôn Tý thủy; hào 2 Huynh Đệ Dần mộc."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Phụ Mẫu Tị hỏa là bài thi bằng cấp lâm Chu Tước; dùng màu đỏ của Hỏa để trợ vượng hỏa quang văn chương.",
        "    - Nhìn vào: Màu đỏ kích hoạt hưng phấn trí não làm bài thi đạt kết quả tối đa.",
        "    - Đối thoại thực tế: Người cha lo lắng tâm lý thi cử của con trai.",
        "  - **Phương án hóa giải:** Cho thí sinh mặc áo thun màu đỏ may mắn trong các ngày thi đại học.",
        "  - **Ứng nghiệm thực tế:** Thí sinh làm bài thi xuất sắc vượt 20 điểm so với dự kiến, trúng tuyển đại học danh tiếng.",
        "- **Quái lệ 3: Phụ nữ hơn 30 tuổi đoán tình duyên hôn nhân bế tắc (Ngày Ất Dậu tháng Ất Mão)**"
    ] + make_evidence_block(
        figs_dict['fig_41'],
        custom_proof="Quẻ Tùy biến Đồng Nhân; hào Thế Thê Tài Thìn thổ hưu tù; Quan Quỷ Ngọ hỏa phục tàng; dùng trang phục màu hồng kích đào hoa.",
        custom_see="Hào 2 Thê Tài Dần mộc động hóa Quan Quỷ Ngọ hỏa; hào sơ Thê Tài Thìn thổ."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Quan Quỷ Ngọ hỏa (người yêu) phục tàng; cung Đoài khuyết thiếu tình cảm; cần Hỏa sinh Thổ trợ Thế.",
        "    - Nhìn vào: Màu hồng và đỏ thuộc Hỏa kích hoạt đào hoa duyên phận phái nữ.",
        "    - Đối thoại thực tế: Đương số muộn màng tình duyên chưa từng có mối tình trọn vẹn, cảm thấy cô đơn tuyệt vọng.",
        "  - **Phương án hóa giải:** Thường xuyên diện váy áo màu hồng phấn và đeo vòng tay thạch anh hồng.",
        "  - **Ứng nghiệm thực tế:** Trong vòng 3 tháng quen được một kỹ sư tài giỏi, hai người nhanh chóng tiến tới hôn nhân hạnh phúc.",
        "- **Quái lệ 4: Phụ nữ xem dự đoán chuyện sinh nở con cái (Ngày Nhâm Thân tháng Đinh Hợi)**"
    ] + make_evidence_block(
        figs_dict['fig_42'],
        custom_proof="Quẻ Ly biến Phục; Tử Tôn Tý thủy lâm Nguyệt kiến cực vượng xung hào Thế; dùng màu vàng Thổ chế Thủy an thai.",
        custom_see="Quẻ Ly Vi Hỏa; hào 2 Thế Quan Quỷ Sửu thổ; hào sơ Phụ Mẫu Mão mộc động."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Tử Tôn Thủy quá vượng khắc hại hào Thế Hỏa, nguy cơ sảy thai hoặc thai nghén hành hạ dữ dội.",
        "    - Nhìn vào: Thổ chế Thủy; dùng màu vàng của Thổ để bảo vệ tử cung an thai dưỡng mạch.",
        "    - Đối thoại thực tế: Sản phụ ốm nghén nặng nề không ăn uống được, dọa sảy thai tuần thứ 8.",
        "  - **Phương án hóa giải:** Mặc váy bầu màu vàng nhạt, bài trí gối đệm màu vàng trong phòng ngủ.",
        "  - **Ứng nghiệm thực tế:** Dứt hẳn triệu chứng ốm nghén dọa sảy, thai nhi phát triển khỏe mạnh đến ngày sinh tròn vuông."
    ])
    return "\n".join(lines) + "\n"

# Write Group 3 files
g3_files = {
    'ch05': ('fragments/ch05_chuong_4_nap_am_cua_can_chi_va_pham_vi_s_branches.md', write_ch05()),
    'ch06': ('fragments/ch06_chuong_5_trich_xuat_thong_tin_ngu_hanh_branches.md', write_ch06()),
    'ch07': ('fragments/ch07_chuong_6_hinh_thuc_ton_tai_cua_ngu_hanh_branches.md', write_ch07()),
    'ch08': ('fragments/ch08_chuong_7_hinh_thuc_ton_tai_cua_ngu_hanh_branches.md', write_ch08()),
    'ch09': ('fragments/ch09_chuong_8_hinh_thuc_ton_tai_cua_ngu_hanh_branches.md', write_ch09()),
}

for cid, (fpath, content) in g3_files.items():
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Wrote {cid} -> {fpath} ({len(content.splitlines())} lines)")
