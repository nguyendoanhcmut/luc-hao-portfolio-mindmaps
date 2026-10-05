import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
from base_generator import figs_dict, make_evidence_block

def write_ch14_9():
    lines = [
        "### Hóa Giải Bằng Thế Thân",
        "",
        "- **Phép dùng hình nhân thế thân giải hạn ách hiểm nghèo:**",
        "  - Khi đương số rơi vào đại hạn hung sát đe dọa tính mạng mà các phương pháp hóa giải thông thường bất khả thi, thuật Lục Hào vận dụng hình nhân thế thân để gánh thay tai kiếp.",
        "  - Chất liệu chế tác hình nhân: Dùng giấy hoàng chỉ, cỏ rơm sạch hoặc đất sét tinh khiết nặn thành hình người đủ đầu mình tứ chi.",
        "  - Nghi thức nạp linh lực: Ghi rõ họ tên, năm tháng ngày giờ sinh của đương số, cắt một lọn tóc hoặc mẫu móng tay bỏ vào bên trong hình nhân để kết nối trường sinh học.",
        "  - Thời điểm và phương vị tống tiễn: Làm lễ tống tiễn vào giờ Tý tại ngã ba đường hoặc phương vị lâm Kỵ thần để chuyển giao tai ách cho hư không.",
        "- **Quái lệ: Bệnh nhân nguy kịch dùng thế thân trừ tai (Quẻ Tổn biến Bác)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_85'],
        custom_proof="Quẻ Tổn biến Bác; hào 2 Quan Quỷ Mão mộc động hóa Thê Tài Tý thủy; dùng người nộm giấy thế thân gánh hạn chết chóc.",
        custom_see="Hào 2 Quan Quỷ Mão mộc động hóa Thê Tài Tý thủy; quẻ Sơn Trạch Tổn."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Bệnh nhân thập tử nhất sinh, hào Thế hưu tù Quan Quỷ lâm Bạch Hổ động khắc; bác sĩ tiên lượng xấu.",
        "    - Nhìn vào: Làm hình nhân thế thân bằng giấy vàng ghi họ tên bát tự đem đốt tại ngã ba đường phương Đông.",
        "    - Đối thoại thực tế: Gia quyến chuẩn bị hậu sự, khẩn cầu tác giả ra tay cứu vãn một tia hy vọng mong manh.",
        "  - **Phương án hóa giải:** Chế tác hình nhân thế thân bằng rơm và giấy hoàng chỉ, làm lễ tống tiễn giờ Tý phương Đông.",
        "  - **Ứng nghiệm thực tế:** Ngay sau đêm làm lễ thế thân, bệnh nhân bất ngờ hồi tỉnh, qua khỏi cơn nguy kịch và dần bình phục hoàn toàn."
    ])
    return "\n".join(lines) + "\n"

def write_ch14_10():
    lines = [
        "### Hóa Giải Bằng Gương Thái Cực Bát Quái",
        "",
        "- **Uy lực khúc xạ và hóa giải của Gương Thái Cực Bát Quái:**",
        "  - Gương Thái Cực Bát Quái là pháp khí phong thủy thượng thừa kết hợp đồ hình Tiên Thiên Bát Quái với mặt gương đồng âm dương.",
        "  - Phân loại và công năng: Gương lồi (khúc xạ và tán xạ sát khí bên ngoài bắn tới); gương lõm (thu nạp và hội tụ cát khí cát tường); gương phẳng (phản xạ cân bằng trường khí âm dương).",
        "  - Các loại hình sát khí cần gương Bát Quái: Tiêm giác sát (góc nhọn nhà đối diện), Thương sát (đường đâm thẳng cổng), Lộ xung sát, Hỏa sát (trạm biến áp, cột điện cao thế), Âm sát (nhà đối diện nghĩa trang, bệnh viện).",
        "  - Cấm kỵ phong thủy: Tuyệt đối không treo gương Bát Quái chiếu thẳng vào cửa chính hoặc cửa sổ nhà hàng xóm để tránh gây xung đột trường khí.",
        "  - Thời điểm treo gương Bát Quái: Nên chọn ngày giờ hoàng đạo, giờ Tý hoặc giờ Ngọ lúc dương khí thịnh vượng nhất để điểm nhãn khai quang gương.",
        "  - Phối hợp ngũ hành chất liệu gương: Gương đồng thuộc Kim hóa giải sát khí thuộc Mộc và Hỏa; gương viền gỗ đào trừ tà khí phương Đông.",
        "- **Quái lệ 1: Nhà đối diện góc nhọn mái đình đâm thẳng vào cửa (Quẻ Tụng & Quẻ Vô Vọng biến Lý)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_86'],
        custom_proof="Quẻ Thiên Thủy Tụng; hào Thế Huynh Đệ Ngọ hỏa bị Quan Quỷ Hợi thủy khắc; sát khí góc nhọn nhà đối diện bắn vào.",
        custom_see="Quẻ Thiên Thủy Tụng; hào 3 Huynh Đệ Ngọ hỏa; quẻ ngoại Càn nội Khảm."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại (phần 1 - quẻ Tụng):**",
        "    - Căn cứ: Góc nhọn mái đình đâm thẳng cửa chính tạo tiêm giác sát làm người trong nhà hay cãi cọ ốm đau.",
        "    - Đối thoại thực tế: Gia chủ lo sợ vì góc nhọn đình làng chĩa thẳng vào cửa nhà khiến các thành viên trong gia đình thường xuyên bất hòa.",
        "- **Quái lệ 1 (tiếp theo): Quẻ Vô Vọng biến Lý – Treo gương lồi Bát Quái**"
    ] + make_evidence_block(
        figs_dict['fig_87'],
        custom_proof="Quẻ Vô Vọng biến Lý; hào sơ Tử Tôn Tý thủy động; treo gương lồi Thái Cực Bát Quái tán xạ góc nhọn.",
        custom_see="Hào sơ Tử Tôn Tý thủy động hóa Thê Tài Dần mộc; quẻ Thiên Lôi Vô Vọng."
    ) + [
        "  - **Phán đoán và đối thoại (phần 2):**",
        "    - Căn cứ: Gương lồi phản xạ và phân tán trường khí xung sát ra hai bên bảo vệ minh đường.",
        "    - Nhìn vào: Cung Khảm Thủy chế ngự hỏa sát góc nhọn khôi phục cân bằng âm dương.",
        "  - **Phương án hóa giải:** Treo gương lồi Bát Quái đồng trước cửa chính hướng thẳng vào góc nhọn đối diện.",
        "  - **Ứng nghiệm thực tế:** Gia đạo bình an trở lại, không còn tiếng cãi vã và các vụ tai nạn vặt biến mất.",
        "- **Quái lệ 2: Cửa sổ đối diện trạm biến áp điện lực (Quẻ Lữ biến Đỉnh)**"
    ] + make_evidence_block(
        figs_dict['fig_88'],
        custom_proof="Quẻ Lữ biến Đỉnh; Hỏa vượng thiêu Kim; trạm biến áp điện lực tạo hỏa sát cực mạnh; gương Bát Quái Thủy hóa Hỏa sát.",
        custom_see="Hào sơ Huynh Đệ Sửu thổ động hóa Phụ Mẫu Mão mộc; quẻ Hỏa Sơn Lữ."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Hỏa sát trạm biến áp làm người nhà đau đầu mất ngủ, huyết áp tăng vọt.",
        "    - Nhìn vào: Trạm biến áp phóng từ trường cực mạnh làm nhiễu loạn sóng não của gia chủ.",
        "    - Đối thoại thực tế: Khách hàng kêu ca đêm nào cũng trằn trọc mất ngủ từ khi trạm điện đối diện nhà đi vào hoạt động.",
        "  - **Phương án hóa giải:** Treo gương Thái Cực Bát Quái lõm kết hợp bình phong thủy tinh chứa nước tại ban công.",
        "  - **Ứng nghiệm thực tế:** Nhiệt độ và điện từ trường cảm nhận dịu hẳn, giấc ngủ của các thành viên sâu và ngon.",
        "- **Quái lệ 3: Cha xem bệnh cho con (Quẻ Tấn biến Đỉnh)**"
    ] + make_evidence_block(
        figs_dict['fig_89'],
        custom_proof="Quẻ Tấn biến Đỉnh; hào sơ Thê Tài Mùi thổ động hóa Quan Quỷ Tị hỏa; bệnh tật dai dẳng cần trấn sát bằng gương Thái Cực.",
        custom_see="Hào sơ Thê Tài Mùi thổ động; hào 4 Quan Quỷ Dậu kim; quẻ Hỏa Địa Tấn."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Con trai sốt co giật không rõ căn nguyên sau khi gia đình sửa cổng.",
        "    - Nhìn vào: Cổng mới mở kích động sát khí loan đầu làm nhiễu loạn nguyên khí trẻ nhỏ.",
        "    - Đối thoại thực tế: Người cha hoang mang đưa con đi khám khắp nơi xét nghiệm không ra bệnh.",
        "  - **Phương án hóa giải:** Treo gương phẳng Thái Cực Bát Quái trước cổng mới để ổn định từ trường.",
        "  - **Ứng nghiệm thực tế:** Cháu bé hạ sốt ngay trong ngày, sức khỏe phục hồi trọn vẹn.",
        "- **Quái lệ 4: Nữ đoán bệnh bản thân suy nhược (Quẻ Tụy biến Quải)**"
    ] + make_evidence_block(
        figs_dict['fig_90'],
        custom_proof="Quẻ Tụy biến Quải; hào 2 Quan Quỷ Tị hỏa động hóa Thê Tài Dần mộc; tà khí từ nghĩa trang đối diện xâm lấn nhà ở.",
        custom_see="Hào 2 Quan Quỷ Tị hỏa động hóa Thê Tài Dần mộc; quẻ Trạch Địa Tụy."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Nhà nhìn ra nghĩa trang âm khí nặng nề làm phụ nữ suy nhược thần kinh ảo giác.",
        "    - Nhìn vào: Âm khí từ nghĩa trang tạo trường năng lượng lạnh lẽo tích tụ lâu ngày làm suy kiệt dương khí.",
        "    - Đối thoại thực tế: Đương số thường xuyên giật mình hoảng sợ lúc nửa đêm và nghe thấy âm thanh kỳ lạ.",
        "  - **Phương án hóa giải:** Treo gương Thái Cực Bát Quái mặt đồng phía sau nhà quay về hướng nghĩa trang.",
        "  - **Ứng nghiệm thực tế:** Không còn cảm giác ớn lạnh rùng mình, tinh thần tỉnh táo hoạt bát."
    ])
    return "\n".join(lines) + "\n"

def write_ch14_11():
    lines = [
        "### Hóa Giải Bằng Bùa Hộ Mệnh",
        "",
        "- **Cơ chế vận hành của Linh phù và Bùa hộ mệnh:**",
        "  - Linh phù là đồ hình mật mã kết nối trường năng lượng tâm thức người tu luyện với linh khí trời đất.",
        "  - Quy chuẩn chế tác: Dùng mực chu sa tự nhiên (thuộc dương Hỏa cực đại) vẽ trên giấy hoàng chỉ (thuộc âm Thổ trung hòa) vào khung giờ Tý thanh tịnh.",
        "  - Đóng dấu triện Bát Quái hoặc triện Đạo gia để niêm phong năng lượng; gấp thành hình tam giác bỏ vào túi gấm mang theo bên mình tạo từ trường bảo hộ cá nhân liên tục 24/7.",
        "- **Quái lệ 1: Phụ nữ lớn tuổi xuất ngoại thăm con (Quẻ Kiển biến Đồng Nhân)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_91'],
        custom_proof="Quẻ Kiển biến Đồng Nhân; hào Thế Huynh Đệ Thìn thổ; hào sơ Thê Tài Thìn thổ động; đeo linh phù bình an xuất ngoại.",
        custom_see="Hào sơ Thê Tài Thìn thổ động hóa Quan Quỷ Tị hỏa; quẻ Thủy Sơn Kiển."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Tuổi cao đi máy bay đường dài qua nửa vòng trái đất lo sợ huyết áp và rủi ro hàng không.",
        "  - **Phương án hóa giải:** Viết linh phù Bình An độ mạng chu sa bỏ vào túi vải gấm vàng đeo trước ngực.",
        "  - **Ứng nghiệm thực tế:** Chuyến bay êm thuận, thủ tục hải quan nhanh chóng, sang Mỹ đoàn tụ con cháu vui vẻ.",
        "- **Quái lệ 2: Bạn học xem vận khí năm tuổi (Quẻ Thủy Lôi Truân)**"
    ] + make_evidence_block(
        figs_dict['fig_92'],
        custom_proof="Quẻ Thủy Lôi Truân; hào sơ Huynh Đệ Tý thủy; Quan Quỷ Dần mộc hưu tù; đeo linh phù Thái Tuế nghênh cát tị hung.",
        custom_see="Quẻ Thủy Lôi Truân; hào sơ Tử Tôn Tý thủy; hào 2 Quan Quỷ Dần mộc."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Quẻ Truân vạn sự khởi đầu nan, năm tuổi dễ gặp thị phi trở ngại bất ngờ.",
        "  - **Phương án hóa giải:** Đeo bùa Thái Tuế phù hộ mạng trong suốt năm.",
        "  - **Ứng nghiệm thực tế:** Cả năm hanh thông, công tác thuận lợi và tránh được nhiều bẫy rập tiểu nhân.",
        "- **Quái lệ 3: Đoán tài vận làm ăn (Quẻ Bĩ biến Tấn)**"
    ] + make_evidence_block(
        figs_dict['fig_93'],
        custom_proof="Quẻ Bĩ biến Tấn; hào sơ Thê Tài Mão mộc động hóa Huynh Đệ Tị hỏa; mang bùa Chiêu Tài tiến bảo kích hoạt kinh doanh.",
        custom_see="Hào sơ Thê Tài Mão mộc động hóa Huynh Đệ Tị hỏa; quẻ Thiên Địa Bĩ."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Bĩ cực thái lai, tài vận chuyển từ bế tắc sang sáng sủa nhưng cần linh phù trợ lực khai thông.",
        "  - **Phương án hóa giải:** Viết bùa Ngũ Lộ Thần Tài đặt trong ví tiền.",
        "  - **Ứng nghiệm thực tế:** Ký kết được 3 hợp đồng lớn, tiền bạc thu hồi đầy đủ.",
        "- **Quái lệ 4: Phụ nữ quản lý dịch vụ đoán tránh kiện tụng (Quẻ Thái biến Tiểu Quá)**"
    ] + make_evidence_block(
        figs_dict['fig_94'],
        custom_proof="Quẻ Thái biến Tiểu Quá; hào 3 Huynh Đệ Thìn thổ động hóa Quan Quỷ Ngọ hỏa; dùng bùa Tiêu Tai giải trừ quan phi kiện tụng.",
        custom_see="Hào 3 Huynh Đệ Thìn thổ động hóa Quan Quỷ Ngọ hỏa; quẻ Địa Thiên Thái."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Quan Quỷ động khắc Thế, nguy cơ bị điều tra pháp luật phạt tiền lớn.",
        "  - **Phương án hóa giải:** Đeo phù Tiêu Tai trừ quan phi bên người và nộp phạt hành chính sớm giải tỏa vụ việc.",
        "  - **Ứng nghiệm thực tế:** Vụ việc được giải quyết êm thấm mức phạt nhẹ nhất, không bị truy cứu hình sự."
    ])
    return "\n".join(lines) + "\n"

def write_ch14_12():
    lines = [
        "### Hóa Giải Bằng Chú Thuật",
        "",
        "- **Phát âm chân ngôn và chú thuật cổ truyền:**",
        "  - Chú ngữ (thần chú) là tổ hợp âm thanh mang tần số cộng hưởng vũ trụ đặc biệt, có khả năng kích hoạt trường năng lượng nội tại và xua đuổi tà khí ngoại lai.",
        "  - Căn bản trì chú: Giữ thân khẩu ý thanh tịnh, quán tưởng ánh sáng quang minh bao phủ thân tâm khi tụng niệm.",
        "  - Ứng dụng trì tụng thần chú lục tự Đại Minh, chú Bát Nhã hoặc các mật chú Đạo gia trong các khung giờ thanh tịnh để thanh tẩy trược khí và tăng cường chính khí."
    ]
    return "\n".join(lines) + "\n"

def write_ch14_13():
    lines = [
        "### Hóa Giải Bằng Trang Phục",
        "",
        "- **Y phục phong thủy và trường khí cá nhân:**",
        "  - Quần áo bao bọc cơ thể suốt cả ngày lẫn đêm, đóng vai trò như lớp màng lọc từ trường sinh học trung gian giữa cơ thể và vũ trụ.",
        "  - Chất liệu sợi và ngũ hành: Vải bông cotton thuộc Mộc nhu hòa; lụa tơ tằm thuộc Hỏa rực rỡ; đồ da thuộc Thủy uyển chuyển; len dạ thuộc Thổ ấm áp; lanh sợi bóng thuộc Kim tinh khiết.",
        "  - Phối hợp màu sắc trang phục hợp mệnh trong các dịp đàm phán quan trọng, phỏng vấn, thi cử, kết hôn để tăng cường tối đa vận khí của Dụng thần.",
        "- **Quái lệ: Nữ công chức dự đoán thăng chức (Quẻ Giải biến Thăng)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_95'],
        custom_proof="Quẻ Giải biến Thăng; Quan Quỷ Dậu kim Không Vong; mặc trang phục màu trắng nạp Kim xuất Không đắc quan.",
        custom_see="Hào 2 Quan Quỷ Thìn thổ động hóa Thê Tài Dần mộc; hào 3 Huynh Đệ Ngọ hỏa."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Quan tinh Dậu kim Không Vong cần kim khí trợ lực trong ngày phỏng vấn bổ nhiệm.",
        "  - **Phương án hóa giải:** Mặc áo vest trắng tinh khôi kết hợp hoa cài áo bằng kim loại sáng bóng.",
        "  - **Ứng nghiệm thực tế:** Buổi phỏng vấn gây ấn tượng xuất sắc với ban giám khảo, nhận quyết định bổ nhiệm ngay tuần sau."
    ])
    return "\n".join(lines) + "\n"

def write_ch14_14():
    lines = [
        "### Hóa Giải Bằng Giường Ngủ",
        "",
        "- **Vị trí và hướng kê giường ngủ quyết định sinh mệnh con người:**",
        "  - Giường ngủ là nơi cơ thể nghỉ ngơi và nạp dưỡng năng lượng trong suốt 1/3 cuộc đời; trạng thái vô thức khi ngủ khiến trường sinh học dễ bị tổn thương nhất trước sát khí.",
        "  - Cấm kỵ giường ngủ: Đầu giường tựa cửa sổ (thiếu chỗ dựa), đầu giường hướng vào nhà vệ sinh (uế khí xung hại), gương chiếu thẳng giường (phản xạ loạn thần), xà ngang đè đầu (áp bức tâm lý).",
        "  - Gầm giường phải luôn thông thoáng sạch sẽ, cấm kỵ chứa đồ kim khí cũ gỉ sét, phế liệu hôi ẩm làm phát sinh âm sát hại sức khỏe phụ nữ và trẻ nhỏ.",
        "  - Quy luật từ trường định vị đầu giường: Đầu quay về hướng cát phương tương sinh với bản mệnh và Thế hào của quẻ bản mệnh.",
        "  - Chất liệu giường ngủ ngũ hành: Giường gỗ tự nhiên điều hòa mộc khí ôn nhu; kiêng kỵ giường sắt kim khí sắc nhọn dẫn dụ từ trường hỗn loạn.",
        "- **Quái lệ 1: Đoán phong thủy nhà ở (Quẻ Cấn biến Bác & Quẻ Tụng biến Cấu)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_96'],
        custom_proof="Quẻ Tụng biến Cấu; hào 2 Thế Quan Quỷ Dần mộc; đầu giường kê ngay dưới xà ngang phạm sát khí đè đầu.",
        custom_see="Hào 2 Thế Quan Quỷ Dần mộc động hóa Tử Tôn Tị hỏa; quẻ Thiên Thủy Tụng."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại (phần 1 - quẻ Tụng biến Cấu):**",
        "    - Căn cứ: Đầu giường ngủ bị xà ngang đè, đối diện gương lớn làm gia chủ đau đầu ác mộng liên tục.",
        "    - Nhìn vào: Xà ngang bê tông nặng nề đè trúng vị trí đầu giường gây hiện tượng bóng đè và đau nửa đầu.",
        "    - Đối thoại thực tế: Gia chủ tâm sự mỗi lần nằm xuống giường là cảm thấy tức ngực khó thở và thường xuyên gặp ác mộng.",
        "- **Quái lệ 1 (tiếp theo): Quẻ Cấn biến Bác – Dời giường ngủ đổi vận**"
    ] + make_evidence_block(
        figs_dict['fig_97'],
        custom_proof="Quẻ Cấn biến Bác; hào 2 Phụ Mẫu Ngọ hỏa; hào 3 Thê Tài Thân kim động; dời giường ngủ sang cung sinh khí.",
        custom_see="Hào 3 Thê Tài Thân kim động hóa Huynh Đệ Mão mộc; quẻ Cấn Vi Sơn."
    ) + [
        "  - **Phán đoán và đối thoại (phần 2):**",
        "    - Căn cứ: Dời giường tránh xa xà ngang và xoay đầu giường về hướng Cát tinh.",
        "    - Nhìn vào: Cung Cấn Thổ tĩnh tại an định giúp ổn định thần phách.",
        "  - **Phương án hóa giải:** Kê lại giường ngủ tựa lưng vào tường đặc, tránh đối diện cửa ra vào và gương soi.",
        "  - **Ứng nghiệm thực tế:** Sau khi kê lại giường giấc ngủ sâu không mộng mị, sức khỏe hồi phục kỳ diệu.",
        "- **Quái lệ 2: Đoán bệnh của vợ (Quẻ Bĩ biến Mông)**"
    ] + make_evidence_block(
        figs_dict['fig_98'],
        custom_proof="Quẻ Bĩ biến Mông; Thê Tài Mão mộc bị Kim khắc nặng; gầm giường chứa đồ kim khí cũ gỉ sét phát sinh sát khí.",
        custom_see="Hào 2 Thê Tài Tị hỏa động hóa Quan Quỷ Mão mộc; quẻ Thiên Địa Bĩ."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Người vợ đau ốm quanh năm uống thuốc không khỏi; kiểm tra gầm giường phát hiện đống đồ sắt vụn dao kéo cũ tích tụ nhiều năm.",
        "    - Nhìn vào: Đồ sắt vụn và dao kéo cũ dưới gầm giường tạo từ trường Kim sát cắt đứt Mộc khí tạng can tỳ.",
        "    - Đối thoại thực tế: Người chồng xót xa vì vợ ốm liệt giường nhiều năm chạy chữa tốn kém khắp nơi không khỏi.",
        "  - **Phương án hóa giải:** Dọn sạch toàn bộ đồ đạc dưới gầm giường, lau chùi sạch sẽ thông thoáng.",
        "  - **Ứng nghiệm thực tế:** Sau khi dọn sạch gầm giường, người vợ khỏe mạnh hồng hào, dứt hẳn căn bệnh phụ khoa mãn tính."
    ])
    return "\n".join(lines) + "\n"

def write_ch14_15():
    lines = [
        "### Hóa Giải Bằng Thay Đổi Ý Đồ",
        "",
        "- **Tâm niệm và ý thức quyết định quỹ đạo vận mệnh:**",
        "  - 'Vạn pháp duy tâm tạo': Ý đồ và tâm thức con người là nguồn phát sóng năng lượng định hướng mạnh mẽ nhất trong vũ trụ.",
        "  - Nhiều tai ách hiểm nghèo xuất phát từ sự cố chấp mù quáng vào một mục tiêu sai lầm; chủ động đổi hướng, từ bỏ ý định mạo hiểm chính là đỉnh cao của thuật xu cát tị hung.",
        "  - Chuyển hướng nghề nghiệp, thay đổi lộ trình, buông bỏ thù hằn tâm lý giúp giải trừ hung sát mà không cần tốn kém vật phẩm phong thủy.",
        "  - Bản chất của việc đổi ý: Ý nghĩ dẫn dắt hành động; khi ý đồ thay đổi thì chuỗi nhân quả của tương lai tức khắc chuyển hướng sang quỹ đạo mới an toàn hơn.",
        "  - Năng lực tự cứu của tâm thức: Biết buông bỏ lòng tham và sự cố chấp mù quáng là chìa khóa tiêu tai diệt nạn vi diệu nhất trong Chu Dịch.",
        "- **Quái lệ 1: Cháu xem vận năm tại quê nhà (Quẻ Kiển biến Khiêm & Quẻ Vị Tế biến Lữ)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_99'],
        custom_proof="Quẻ Kiển biến Khiêm; hào 2 Thế Quan Quỷ Dần mộc; hào 5 Thê Tài Thân kim động; thay đổi ý định đầu tư kinh doanh mạo hiểm.",
        custom_see="Hào 5 Thê Tài Thân kim động hóa Huynh Đệ Tuất thổ; quẻ Thủy Sơn Kiển."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại (phần 1 - quẻ Kiển biến Khiêm):**",
        "    - Căn cứ: Cháu định gom tiền buôn bán xe máy cũ; quẻ Kiển hiểm trở phía trước chắc chắn lỗ vốn.",
        "    - Đối thoại thực tế: Người cháu phân vân định vay mượn thêm vốn lớn để mở đại lý xe máy cũ.",
        "- **Quái lệ 1 (tiếp theo): Quẻ Vị Tế biến Lữ định hướng nghề nghiệp an toàn**"
    ] + make_evidence_block(
        figs_dict['fig_100'],
        custom_proof="Quẻ Vị Tế biến Lữ; Thê Tài Tị hỏa trì Thế; từ bỏ kinh doanh mạo hiểm chuyển sang học nghề sửa chữa điện tử.",
        custom_see="Hào 3 Huynh Đệ Dậu kim động hóa Tử Tôn Thân kim; quẻ Hỏa Thủy Vị Tế."
    ) + [
        "  - **Phán đoán và đối thoại (phần 2):**",
        "    - Căn cứ: Hỏa vượng sinh tài từ kỹ thuật chuyên môn; từ bỏ ý định buôn xe chuyển sang học nghề.",
        "    - Nhìn vào: Tử Tôn sinh trợ Dụng thần bền vững, tích lũy tay nghề lâu dài an toàn.",
        "  - **Phương án hóa giải:** Thay đổi ý đồ kinh doanh, đăng ký học khóa sửa chữa thiết bị điện tử.",
        "  - **Ứng nghiệm thực tế:** Mở cửa hàng sửa chữa điện tử đông khách, thu nhập ổn định làm giàu bền vững.",
        "- **Quái lệ 2: Giám đốc công ty du lịch xem tiền đồ doanh nghiệp (Quẻ Tiệm biến Tấn)**"
    ] + make_evidence_block(
        figs_dict['fig_101'],
        custom_proof="Quẻ Tiệm biến Tấn; Quan Quỷ Thân kim trì Thế; Huynh Đệ Dần mộc động; thay đổi hướng mở rộng tuyến điểm du lịch.",
        custom_see="Hào 3 Tử Tôn Thân kim động hóa Quan Quỷ Ngọ hỏa; quẻ Phong Sơn Tiệm."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Tuyến du lịch miền núi đang ế ẩm nguy cơ lỗ nặng; thay đổi ý định chuyển sang khai thác tuyến ven biển.",
        "    - Nhìn vào: Cung Đoài Thủy sinh vượng kích hoạt tài nguyên biển đảo đem lại nguồn thu lớn.",
        "    - Đối thoại thực tế: Giám đốc đau đầu vì tour leo núi liên tục bị hủy do thời tiết xấu đe dọa phá sản.",
        "  - **Phương án hóa giải:** Hủy bỏ tuyến miền núi, tập trung nguồn lực quảng bá tuyến biển đảo.",
        "  - **Ứng nghiệm thực tế:** Tour du lịch biển cháy vé, công ty thu lãi lớn qua mùa hè.",
        "- **Quái lệ 3: Họp lớp hè năm 1995 (Quẻ Phục biến Chấn)**"
    ] + make_evidence_block(
        figs_dict['fig_102'],
        custom_proof="Quẻ Phục biến Chấn; hào 4 Huynh Đệ Sửu thổ động hóa Tử Tôn Thân kim; thay đổi ý định đi lại tránh tai nạn giao thông.",
        custom_see="Hào 4 Huynh Đệ Sửu thổ động hóa Tử Tôn Thân kim; quẻ Địa Lôi Phục."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Dự định đi xe máy về quê họp lớp; quẻ báo lộ trình gặp tai nạn va chạm.",
        "    - Nhìn vào: Xe cộ đường bộ lâm Bạch Hổ phát động báo trước tai nạn lở đất nguy hiểm.",
        "    - Đối thoại thực tế: Nhóm bạn rủ rê phượt xe máy đường đèo mạo hiểm trong mùa mưa bão.",
        "  - **Phương án hóa giải:** Thay đổi ý định đi xe máy, chuyển sang mua vé tàu hỏa.",
        "  - **Ứng nghiệm thực tế:** Chuyến tàu an toàn, trong khi đoạn đường quốc lộ cũ xảy ra sạt lở xe cộ tê liệt.",
        "- **Quái lệ 4: Phụ nữ tìm bà đồng xem bói hiệu quả ra sao (Quẻ Đại Quá biến Nhu)**"
    ] + make_evidence_block(
        figs_dict['fig_103'],
        custom_proof="Quẻ Đại Quá biến Nhu; Thế hào Dậu kim Nguyệt phá; bà đồng bịa đặt lừa đảo tốn tiền; từ bỏ mê tín chuyển sang khám bác sĩ.",
        custom_see="Hào 3 Quan Quỷ Dậu kim động hóa Huynh Đệ Dần mộc; quẻ Trạch Phong Đại Quá."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Bà đồng dọa ma quỷ đòi 5 triệu làm lễ trừ tà; quẻ Đại Quá cột nhà lung lay lừa đảo rõ ràng.",
        "    - Nhìn vào: Thế phá Kỵ suy chỉ rõ tà thuyết bịa đặt không có thực chất huyền học chân chính.",
        "    - Đối thoại thực tế: Khách hàng hoang mang định vay nóng tiền để nộp cho thầy cúng giải vong.",
        "  - **Phương án hóa giải:** Thay đổi ý định, dứt khoát không đưa tiền cho bà đồng và vào bệnh viện lớn khám chuyên khoa.",
        "  - **Ứng nghiệm thực tế:** Bệnh viện chẩn đoán thiếu canxi gây chuột rút, uống thuốc 1 tuần khỏi hẳn, không tốn tiền oan.",
        "- **Quái lệ 5: Dự đoán thay đổi công việc (Quẻ Tốn biến Hoán)**"
    ] + make_evidence_block(
        figs_dict['fig_104'],
        custom_proof="Quẻ Tốn biến Hoán; Quan Quỷ Dậu kim trì Thế; Huynh Đệ Sửu thổ động; thay đổi ý định nhảy việc ở lại thăng tiến.",
        custom_see="Hào 2 Quan Quỷ Dậu kim động hóa Thê Tài Hợi thủy; quẻ Tốn Vi Phong."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Định bỏ việc công ty cũ vì bất mãn; quẻ báo ở lại cơ quan cũ sắp có cơ hội cất nhắc.",
        "    - Nhìn vào: Quan tinh trì Thế phát sinh sinh lực, cơ quan cũ chính là mảnh đất dụng võ tốt nhất.",
        "    - Đối thoại thực tế: Đương sự nộp đơn xin thôi việc nhưng thầy Vương khuyên hãy nín nhịn chờ thời cơ.",
        "  - **Phương án hóa giải:** Từ bỏ ý định nộp đơn xin nghỉ, tập trung hoàn thành tốt đề án hiện tại.",
        "  - **Ứng nghiệm thực tế:** Đúng 2 tháng sau sếp cũ chuyển công tác, anh được bổ nhiệm vào ghế trưởng phòng trống.",
        "- **Quái lệ 6: Người đàn ông kinh doanh dự đoán tài vận (Quẻ Tụy biến Bĩ)**"
    ] + make_evidence_block(
        figs_dict['fig_105'],
        custom_proof="Quẻ Tụy biến Bĩ; Thê Tài Mão mộc Không Vong; Huynh Đệ Mùi thổ vượng; thay đổi mặt hàng kinh doanh thoát phá sản.",
        custom_see="Hào sơ Thê Tài Mùi thổ động hóa Quan Quỷ Ngọ hỏa; quẻ Trạch Địa Tụy."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Cửa hàng bán đồ gia dụng tồn kho nặng; đổi sang bán thực phẩm sạch sinh tài nhanh.",
        "    - Nhìn vào: Hào Tài Không Vong chuyển dịch sang mặt hàng thiết yếu dòng tiền nhanh chóng hồi sinh.",
        "    - Đối thoại thực tế: Chủ tiệm đứng ngồi không yên vì nợ tiền ngân hàng đến hạn thanh toán.",
        "  - **Phương án hóa giải:** Chuyển đổi mô hình kinh doanh sang hàng tiêu dùng thiết yếu.",
        "  - **Ứng nghiệm thực tế:** Hàng hóa bán chạy, quay vòng vốn nhanh chóng thu lợi nhuận ổn định.",
        "- **Quái lệ 7: Đồng nghiệp sưng mặt đau đớn (Quẻ Vô Vọng)**"
    ] + make_evidence_block(
        figs_dict['fig_106'],
        custom_proof="Quẻ Thiên Lôi Vô Vọng; hào 5 Phụ Mẫu Thân kim trì Thế; Quan Quỷ Dần mộc động; đổi tâm thế tha thứ buông bỏ thù hằn.",
        custom_see="Quẻ Thiên Lôi Vô Vọng; hào 5 Phụ Mẫu Thân kim; hào sơ Huynh Đệ Tý thủy."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Mặt sưng vù không rõ nguyên nhân sau cơn tức giận uất hận với người khác; tâm hỏa thượng nghịch.",
        "    - Nhìn vào: Dần Mộc động khắc chế Tỳ Thổ vùng mặt; tâm hỏa hạ nhiệt khi xả bỏ uất kết nội tâm.",
        "    - Đối thoại thực tế: Đồng nghiệp tâm sự vừa cãi nhau kịch liệt với cấp trên xong thì một bên má sưng to đau nhức.",
        "  - **Phương án hóa giải:** Thay đổi thái độ, chủ động làm hòa và tha thứ cho đối phương.",
        "  - **Ứng nghiệm thực tế:** Sau khi gọi điện hòa giải xong thì vết sưng trên mặt tiêu giảm kỳ diệu sau một giấc ngủ."
    ])
    return "\n".join(lines) + "\n"

def write_ch15():
    # fragments/ch15_chuong_14_phuong_phap_chon_ngay_tot_bang_branches.md
    # figs: fig_107 to fig_115
    lines = [
        "## Chương 14: Phương Pháp Chọn Ngày Tốt Bằng Lục Hào",
        "",
        "- **Nguyên tắc chọn ngày tốt bằng Lục Hào khác biệt hoàng đạo thông thường:**",
        "  - Hạn chế của phương pháp xem lịch vạn niên truyền thống: Lịch thông thường chỉ xét chung theo can chi hoàng đạo đại trà, không phản ánh được tương tác cá nhân hóa giữa đương số với sự việc cụ thể.",
        "  - Bản chất của trạch nhật Lục Hào: Gieo quẻ hỏi về sự việc dự định (khai trương, chuyển nhà, kết hôn, động thổ, xuất hành, cải táng) nhằm đo lường tương tác giữa Dụng thần, Thế hào của chủ thể với trường khí thời không vũ trụ.",
        "  - Tiêu chí vàng chọn ngày hoàng đạo cá nhân: Dụng thần và Thế hào phải vượng tướng, đắc sinh phù từ Nguyệt lệnh và Nhật thần, tuyệt đối tránh ngày Tuần Không hoặc Nguyệt Phá.",
        "  - Quy tắc phân loại Dụng thần chuẩn xác theo từng loại hình sự việc:",
        "    - Khai trương kinh doanh buôn bán, ký kết hợp đồng thương mại: Lấy hào Thê Tài làm Dụng thần số một.",
        "    - Thăng quan nhậm chức, thi cử tuyển dụng, yết kiến lãnh đạo: Lấy hào Quan Quỷ làm Dụng thần trợ uy quyền.",
        "    - Động thổ xây dựng, chuyển nhà nhập trạch, mua bán bất động sản: Lấy hào Phụ Mẫu đại diện trạch xá phối hợp Thế hào.",
        "    - Hôn nhân cưới hỏi, đính hôn rước dâu: Lấy Thê Tài và hào Ứng làm trung tâm đối chiếu tương sinh tương hợp với Thế hào.",
        "    - Chữa bệnh nan y, phẫu thuật cứu người: Lấy hào Tử Tôn làm Dụng thần giải trừ ách tật.",
        "  - Quy tắc Ngũ Bất Chọn trong trạch nhật Dịch học: Tránh ngày Tuần Không của Dụng thần, tránh ngày Nguyệt phá, tránh ngày Lục xung toàn quẻ, tránh ngày Kỵ thần trì Thế lâm Nhật kiến, tránh ngày Thể dụng tương hình.",
        "  - Bí pháp kích hoạt cát khí: Khi Dụng thần hưu tù, chọn ngày lâm trường sinh hoặc tam hợp cục trợ lực để biến nhược thành cường.",
        "- **Quái lệ 1: Chọn ngày khai trương cửa hàng kinh doanh (Ngày Mậu Tuất tháng Tân Hợi)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_107'],
        custom_proof="Quẻ Thiên Địa Bĩ; Thê Tài Mão mộc hưu tù; chọn ngày Dần hoặc Mão Mộc vượng khai trương sinh tài đại phát.",
        custom_see="Hào sơ Thê Tài Mão mộc; hào 2 Quan Quỷ Tị hỏa; quẻ Thiên Địa Bĩ."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Khai trương lấy Thê Tài làm Dụng thần; Thê Tài Mão mộc cần ngày Dần Mão tỉ hòa trợ vượng.",
        "    - Nhìn vào: Mão Mộc đắc Nguyệt sinh nhưng bị Nhật Tuất hợp trói; cần ngày Dần Mộc xung phá hợp hoặc trợ lực trường sinh.",
        "    - Đối thoại thực tế: Khách hàng hỏi chọn ngày hoàng đạo trên lịch nhưng thầy Vương khuyên hãy căn cứ quẻ Dịch để tránh phá tài.",
        "  - **Phương án hóa giải:** Chọn ngày Giáp Dần lúc 9h sáng cắt băng khai trương.",
        "  - **Ứng nghiệm thực tế:** Ngày khai trương khách đông chật kín, buôn may bán đắt lâu dài.",
        "- **Quái lệ 2 & 3: Chọn ngày chuyển nhà an cư lạc nghiệp (Ngày Nhâm Tuất tháng Canh Tý)**"
    ] + make_evidence_block(
        figs_dict['fig_108'],
        custom_proof="Quẻ Khốn biến Đoài; Phụ Mẫu Sửu thổ động hóa Thê Tài Hợi thủy; chọn ngày Thìn hợp Dậu an cư vững bền.",
        custom_see="Hào 2 Quan Quỷ Hợi thủy động hóa Huynh Đệ Dậu kim; quẻ Trạch Thủy Khốn."
    ) + [
        "  - **Phán đoán và đối thoại (phần 1 - quẻ Khốn biến Đoài):**",
        "    - Căn cứ: Chuyển nhà lấy Phụ Mẫu làm nhà, Thế hào làm người; kiểm tra quẻ Khốn biến Cách định giờ nhập trạch.",
        "    - Đối thoại thực tế: Gia chủ muốn chọn ngày cuối tuần để con cái được nghỉ học nhưng lo sợ phạm ngày hung.",
        "- **Quái lệ 2 & 3 (tiếp theo): Quẻ Khốn biến Cách định ngày nhập trạch**"
    ] + make_evidence_block(
        figs_dict['fig_109'],
        custom_proof="Quẻ Khốn biến Cách; hào sơ Thế Huynh Đệ Dần mộc; chọn ngày Thìn xung Tuất mở cửa nhập trạch vượng tài.",
        custom_see="Hào sơ Huynh Đệ Dần mộc động hóa Quan Quỷ Tị hỏa; quẻ Trạch Thủy Khốn."
    ) + [
        "  - **Phán đoán và đối thoại (phần 2):**",
        "    - Căn cứ: Ngày Bính Thìn Thổ vượng Phụ Mẫu sáng sủa, người nhà khỏe mạnh tài lộc hanh thông.",
        "    - Nhìn vào: Thìn Tuất tương xung kích hoạt khố tài mở ra mang lại hưng thịnh cho trạch xá mới.",
        "  - **Phương án hóa giải:** Nhập trạch vào đúng giờ Tị ngày Bính Thìn.",
        "  - **Ứng nghiệm thực tế:** Chuyển nhà suôn sẻ thuận buồm xuôi gió, gia đình an cư phát tài.",
        "- **Quái lệ 4: Nữ chọn ngày dọn nhà mới (Ngày Bính Thìn tháng Giáp Thìn)**"
    ] + make_evidence_block(
        figs_dict['fig_110'],
        custom_proof="Quẻ Quy Muội; Phụ Mẫu Tị hỏa lâm hào 2; chọn ngày Tị hoặc Ngọ hỏa vượng dọn nhà đắc sinh khí.",
        custom_see="Hào 2 Phụ Mẫu Tị hỏa; hào 3 Huynh Đệ Sửu thổ; quẻ Lôi Trạch Quy Muội."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Phụ Mẫu hào 2 là trạch xá; chọn ngày Đinh Tị mang lửa ấm vào nhà mới.",
        "    - Nhìn vào: Hỏa vượng sinh Thổ trợ trạch, hào 2 đắc địa chi hòa hợp chủ về gia đạo an khang thịnh vượng.",
        "    - Đối thoại thực tế: Nữ thí chủ muốn chuyển nhà gấp trước rằm để kịp ngày giỗ đầu của mẹ chồng.",
        "  - **Phương án hóa giải:** Mang bếp lửa và bình nước đun sôi đầu tiên vào nhà mới ngày Đinh Tị.",
        "  - **Ứng nghiệm thực tế:** Gia đình hòa thuận, công việc suôn sẻ sau khi về nhà mới.",
        "- **Quái lệ 5: Nữ dọn nhà quẻ Phục biến Chấn (Ngày Tân Mão tháng Canh Thân)**"
    ] + make_evidence_block(
        figs_dict['fig_111'],
        custom_proof="Quẻ Phục biến Chấn; hào Thế Tý thủy được Nguyệt sinh; chọn ngày Thân hợp Tý nạp tài nhập trạch cát khánh.",
        custom_see="Hào 4 Huynh Đệ Sửu thổ động hóa Tử Tôn Thân kim; quẻ Địa Lôi Phục."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Hào Thế Tý thủy vượng; chọn ngày Giáp Thân kim sinh thủy vượng trạch.",
        "    - Nhìn vào: Thân Tý bán hợp Thủy cục bồi đắp nguồn năng lượng dồi dào cho bản mệnh nữ gia chủ.",
        "    - Đối thoại thực tế: Chị lo lắng vì căn hộ mới hướng Tây Bắc bị người khác chê là hướng xấu.",
        "  - **Phương án hóa giải:** Tiến hành dọn đồ đạc vào giờ Thìn ngày Giáp Thân.",
        "  - **Ứng nghiệm thực tế:** Mọi sự tốt lành, gia chủ thăng quan tiến chức sau khi dọn nhà.",
        "- **Quái lệ 6: Nam dỡ bỏ nhà cũ xây biệt thự mới (Ngày Canh Thân tháng Quý Tị)**"
    ] + make_evidence_block(
        figs_dict['fig_112'],
        custom_proof="Quẻ Đỉnh biến Lữ; hào 3 Tử Tôn Dậu kim động; chọn ngày Dậu động thổ dỡ nhà vạn sự bình an.",
        custom_see="Hào 3 Tử Tôn Dậu kim động hóa Huynh Đệ Thân kim; quẻ Hỏa Phong Đỉnh."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Động thổ dỡ nhà cần Tử Tôn an định phúc thần; ngày Ất Dậu cát tinh tương trợ.",
        "    - Nhìn vào: Dậu kim động trì thế Tử Tôn xua tan âm khí đất cũ bảo hộ thợ thuyền thi công an toàn.",
        "    - Đối thoại thực tế: Chủ thầu xây dựng yêu cầu chọn đúng ngày phạt mộc để tránh xui xẻo nghề nghiệp.",
        "  - **Phương án hóa giải:** Làm lễ phạt mộc hạ ngói vào giờ Thìn ngày Ất Dậu.",
        "  - **Ứng nghiệm thực tế:** Quá trình thi công xây dựng an toàn tuyệt đối không xảy ra tai nạn.",
        "- **Quái lệ 7: Chọn ngày cưới hỏi hôn lễ con trai (Ngày Đinh Dậu tháng Bính Thìn)**"
    ] + make_evidence_block(
        figs_dict['fig_113'],
        custom_proof="Quẻ Giải biến Dự; Thê Tài Ngọ hỏa vượng; hào Ứng tương sinh Thế; chọn ngày Đinh Mùi cưới gả bách niên giai lão.",
        custom_see="Hào 2 Thê Tài Ngọ hỏa động hóa Huynh Đệ Dần mộc; quẻ Lôi Thủy Giải."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Hôn nhân lấy Thê Tài làm Dụng thần; ngày Đinh Mùi tương hợp với Ngọ hỏa đại cát đại lợi.",
        "    - Nhìn vào: Ngọ Mùi lục hợp Hỏa Thổ tương sinh tượng trưng cho vợ chồng hòa thuận sắt son trăm năm.",
        "    - Đối thoại thực tế: Hai bên thông gia xem nhiều thầy phong thủy khác nhau nhưng mỗi nơi phán một ngày gây tranh cãi.",
        "  - **Phương án hóa giải:** Tổ chức hôn lễ rước dâu vào giờ Tị ngày Đinh Mùi.",
        "  - **Ứng nghiệm thực tế:** Đám cưới long trọng vui tươi, đôi vợ chồng trẻ sống hạnh phúc thuận hòa.",
        "- **Quái lệ 8: Khai trương siêu thị điện máy (Ngày Bính Tý tháng Tân Mão)**"
    ] + make_evidence_block(
        figs_dict['fig_114'],
        custom_proof="Quẻ Cách biến Gia Nhân; hào sơ Quan Quỷ Tị hỏa động; chọn ngày Bính Dần khai trương buôn bán phát đạt.",
        custom_see="Hào sơ Quan Quỷ Tị hỏa động hóa Thê Tài Mão mộc; quẻ Trạch Hỏa Cách."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Siêu thị điện máy thuộc Hỏa Kim; ngày Bính Dần Hỏa Mộc tương sinh đại vượng tài khí.",
        "    - Nhìn vào: Dần Mộc sinh trợ Tị Hỏa hào sơ khởi động guồng máy kinh doanh mã đáo thành công.",
        "    - Đối thoại thực tế: Ban giám đốc chuẩn bị mở chi nhánh thứ mười mong muốn ngày khai trương bùng nổ doanh số.",
        "  - **Phương án hóa giải:** Khai trương mở cửa đón khách lúc 8h sáng ngày Bính Dần.",
        "  - **Ứng nghiệm thực tế:** Siêu thị đông nghẹt khách hàng, doanh số ngày đầu phá kỷ lục chi nhánh.",
        "- **Quái lệ 9: Nữ chọn ngày cải táng phần mộ cha mẹ (Ngày Đinh Mùi tháng Ất Mão)**"
    ] + make_evidence_block(
        figs_dict['fig_115'],
        custom_proof="Quẻ Cấn biến Tỉnh; Phụ Mẫu Ngọ hỏa lâm hào 2; chọn ngày Kỷ Tị thanh minh sang cát yên nghỉ vĩnh hằng.",
        custom_see="Hào 3 Thê Tài Thân kim động hóa Huynh Đệ Tý thủy; quẻ Cấn Vi Sơn."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Cải táng âm trạch cần Phụ Mẫu an định, Thổ khí thanh tĩnh; ngày Kỷ Tị cát nhật an táng.",
        "    - Nhìn vào: Tị Hỏa sinh Thổ bồi bổ long mạch, che chở hài cốt tiền nhân được ấm êm muôn đời.",
        "    - Đối thoại thực tế: Con gái trưởng chịu trách nhiệm việc họ tộc lo lắng thời tiết mưa gió ảnh hưởng lễ sang cát.",
        "  - **Phương án hóa giải:** Tiến hành cất bốc cải táng vào giờ Thìn ngày Kỷ Tị.",
        "  - **Ứng nghiệm thực tế:** Xương cốt tổ tiên nguyên vẹn sạch sẽ sắc vàng đẹp, con cháu đời sau thịnh vượng phát tài."
    ])
    return "\n".join(lines) + "\n"

# Write Group 6 files
g6_files = {
    'ch14_9': ('fragments/ch14_9_hoa_giai_bang_the_than_branches.md', write_ch14_9()),
    'ch14_10': ('fragments/ch14_10_hoa_giai_bang_guong_thai_cuc_bat_quai_branches.md', write_ch14_10()),
    'ch14_11': ('fragments/ch14_11_hoa_giai_bang_bua_ho_menh_branches.md', write_ch14_11()),
    'ch14_12': ('fragments/ch14_12_hoa_giai_bang_chu_thuat_branches.md', write_ch14_12()),
    'ch14_13': ('fragments/ch14_13_hoa_giai_bang_trang_phuc_branches.md', write_ch14_13()),
    'ch14_14': ('fragments/ch14_14_hoa_giai_bang_giuong_ngu_branches.md', write_ch14_14()),
    'ch14_15': ('fragments/ch14_15_hoa_giai_bang_thay_oi_y_o_branches.md', write_ch14_15()),
    'ch15': ('fragments/ch15_chuong_14_phuong_phap_chon_ngay_tot_bang_branches.md', write_ch15()),
}

for cid, (fpath, content) in g6_files.items():
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Wrote {cid} -> {fpath} ({len(content.splitlines())} lines)")
