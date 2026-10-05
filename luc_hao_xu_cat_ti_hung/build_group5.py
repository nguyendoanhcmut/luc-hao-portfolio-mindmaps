import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
from base_generator import figs_dict, make_evidence_block

def write_ch14_1():
    # fragments/ch14_1_chinh_sua_phong_thuy_branches.md
    # figs: fig_63 to fig_68
    lines = [
        "### Chỉnh Sửa Phong Thủy",
        "",
        "- **Phong thủy môi trường và tác động lập thể tới vận mệnh:**",
        "  - Bất hạnh, tai nạn và bệnh tật của con người thường bắt nguồn từ môi trường sống xung quanh (dương trạch) hoặc phần mộ tổ tiên (âm trạch) tương tác với bát tự.",
        "  - Dương trạch quản nhân đinh và tài vận hiện tại; âm trạch chi phối phúc ấm sâu xa và căn cơ gia tộc lâu dài.",
        "  - Phương pháp 'xem bộ phận' trong Lục Hào: Dự đoán chi tiết từng khu vực nghi ngờ (cổng chính, phòng ngủ, phòng khách, bếp, giếng nước, nhà vệ sinh) để định vị chính xác vị trí phát sinh sát khí.",
        "  - Nguyên tắc chỉnh sửa phong thủy bằng Lục Hào: Không phá dỡ bừa bãi mà kết hợp điều hòa hình thế loan đầu với kích hoạt trường khí lý khí ngũ hành tương sinh.",
        "  - Hào vị tương ứng với kiến trúc nội ngoại thất: Hào 1 nền móng giếng nước, hào 2 bếp và phòng ngủ, hào 3 cửa phòng giường chiếu, hào 4 cửa chính cổng ngõ, hào 5 đường đi phòng khách, hào 6 nóc nhà từ đường.",
        "  - Phối hợp ngũ hành bài trí: Kim suy bổ Kim vật phẩm đồng hồ kim loại, Mộc héo tưới Thủy trồng cây xanh thanh lọc khí trường.",
        "- **Quái lệ 1: Người đàn ông lận đận quan lộ mấy chục năm không thăng tiến (Ngày Mậu Dần tháng Dậu)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_63'],
        custom_proof="Quẻ Sư biến Lâm; hào sơ Tử Tôn Dần mộc động là giếng nước trong sân bị lấp; Quan Quỷ Sửu thổ bị khắc hãm.",
        custom_see="Hào sơ Tử Tôn Dần mộc động hóa Huynh Đệ Tị hỏa; quẻ Địa Thủy Sư."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại (phần 1 - quẻ Sư biến Lâm):**",
        "    - Căn cứ: Tử Tôn Dần mộc động tại hào sơ; hào sơ là giếng nước, nền đất; giếng bị lấp bừa bãi sinh uế khí khắc Quan.",
        "    - Nhìn vào: Kiểm tra tiếp phong thủy phòng làm việc bằng quẻ Đồng Nhân.",
        "    - Đối thoại thực tế: Khách hàng thắc mắc tại sao phấn đấu cống hiến suốt ba mươi năm mà luôn bị cấp trên gạt tên ra khỏi danh sách thăng chức.",
        "- **Quái lệ 1 (tiếp theo): Quẻ Đồng Nhân kiểm tra bàn làm việc cơ quan**"
    ] + make_evidence_block(
        figs_dict['fig_64'],
        custom_proof="Quẻ Đồng Nhân; Thế hào Tử Tôn Ngọ hỏa trì Thế; Phụ Mẫu Sửu thổ lâm Bạch Hổ; dời bàn làm việc tránh sát khí.",
        custom_see="Hào 3 Thế Tử Tôn Ngọ hỏa; quẻ Thiên Hỏa Đồng Nhân."
    ) + [
        "  - **Phán đoán và đối thoại (phần 2 - quẻ Đồng Nhân):**",
        "    - Căn cứ: Bàn làm việc quay lưng về cửa sổ gió lùa phạm hư không, trước mặt bị xà ngang đè đầu.",
        "    - Nhìn vào: Khai thông giếng nước cũ và xoay chuyển bàn làm việc tựa lưng vào tường vững chắc.",
        "  - **Phương án hóa giải:** Khai thông giếng nước phong thủy và sắp xếp lại nội thất phòng làm việc.",
        "  - **Ứng nghiệm thực tế:** Nửa năm sau cơ quan cải tổ, anh được bổ nhiệm làm phó giám đốc sở.",
        "- **Quái lệ 2: Học sĩ tài hoa mấy khoa thi cử đều trượt vỏ chuối (Ngày Kỷ Sửu tháng Tị)**"
    ] + make_evidence_block(
        figs_dict['fig_65'],
        custom_proof="Quẻ Tiểu Quá biến Cấn; Phụ Mẫu Ngọ hỏa Không Vong; Quan Quỷ Dậu kim phục tàng; mộ tổ phía Nam bị rễ cây xuyên qua.",
        custom_see="Hào 3 Huynh Đệ Thân kim động hóa Huynh Đệ Thân kim; quẻ Lôi Sơn Tiểu Quá."
    ) + [
        "  - **Phán đoán và đối thoại (phần 1 - quẻ Tiểu Quá):**",
        "    - Căn cứ: Văn hay chữ tốt nhưng thi cử lận đận; mộ tổ hướng Nam có cây cổ thụ rễ ăn xuyên nắp quan tài.",
        "    - Nhìn vào: Kết hợp quẻ Đại Hữu biến Càn xem xét phần mộ nhánh phụ.",
        "    - Đối thoại thực tế: Sĩ tử than thở bài thi luôn được chấm điểm cao ở vòng đầu nhưng đến vòng quyết định lại gặp sự cố bất ngờ rớt đài.",
        "- **Quái lệ 2 (tiếp theo): Quẻ Đại Hữu biến Càn xem xét sửa sang âm trạch**"
    ] + make_evidence_block(
        figs_dict['fig_66'],
        custom_proof="Quẻ Đại Hữu biến Càn; hào 3 Thế Phụ Mẫu Thìn thổ động hóa Thê Tài Tý thủy; sửa sang âm trạch mở mang văn vận.",
        custom_see="Hào 3 Thế Phụ Mẫu Thìn thổ động hóa Phụ Mẫu Thìn thổ; quẻ Hỏa Thiên Đại Hữu."
    ) + [
        "  - **Phán đoán và đối thoại (phần 2 - quẻ Đại Hữu):**",
        "    - Căn cứ: Âm trạch được thanh tẩy rễ cây, bồi đắp đất mới Càn Kim trợ văn xương.",
        "  - **Phương án hóa giải:** Chặt rễ cây xâm lấn mộ tổ và đắp lại nấm mồ phong thủy hướng Càn.",
        "  - **Ứng nghiệm thực tế:** Khoa thi mùa thu năm sau đỗ cử nhân hạng nhì, vinh quy bái tổ.",
        "- **Quái lệ 3: Nữ đoán bệnh hiểm nghèo cho cháu trai con anh ruột (Ngày Bính Thân tháng Ất Mão)**"
    ] + make_evidence_block(
        figs_dict['fig_67'],
        custom_proof="Quẻ Quy Muội biến Dự; Tử Tôn Hợi thủy bị Nguyệt kiến Mão mộc tiết khí; hào sơ động sát khí góc Tây Bắc nhà ở.",
        custom_see="Hào sơ Huynh Đệ Tý thủy động hóa Thê Tài Mùi thổ; quẻ Lôi Trạch Quy Muội."
    ) + [
        "  - **Phán đoán và đối thoại (phần 1 - quẻ Quy Muội):**",
        "    - Căn cứ: Cháu bé sốt cao co giật co cứng cơ; phong thủy góc Tây Bắc có vật nhọn kim loại đâm thẳng vào giường ngủ.",
        "    - Nhìn vào: Quẻ Ký Tế biến Kiển kiểm tra hồ nước và đường cống sau nhà.",
        "    - Đối thoại thực tế: Người cô ruột nước mắt ngắn dài van xin cứu mạng cháu nhỏ đang nằm thở oxy trong phòng hồi sức cấp cứu.",
        "- **Quái lệ 3 (tiếp theo): Quẻ Ký Tế biến Kiển – Thông cống nghẹt cứu mạng cháu bé**"
    ] + make_evidence_block(
        figs_dict['fig_68'],
        custom_proof="Quẻ Ký Tế biến Kiển; hào 2 Quan Quỷ Sửu thổ; hào 3 Huynh Đệ Hợi thủy động; khai thông đường nước bẩn sau nhà.",
        custom_see="Hào 3 Huynh Đệ Hợi thủy động hóa Huynh Đệ Thân kim; quẻ Thủy Hỏa Ký Tế."
    ) + [
        "  - **Phán đoán và đối thoại (phần 2 - quẻ Ký Tế):**",
        "    - Căn cứ: Cống thoát nước sau nhà bị tắc nghẽn ứ đọng nước bẩn đúng góc Tây Bắc phòng cháu bé.",
        "  - **Phương án hóa giải:** Dọn dẹp vật nhọn và khơi thông đường cống thoát nước ngầm.",
        "  - **Ứng nghiệm thực tế:** Vừa thông cống xong thì cơn co giật của cháu bé dứt hẳn, xuất viện khỏe mạnh sau 3 ngày."
    ])
    return "\n".join(lines) + "\n"

def write_ch14_2():
    lines = [
        "### Hóa Giải Tên Người, Tên Đất",
        "",
        "- **Tác động của âm vận danh xưng và địa danh:**",
        "  - Tên gọi của con người và tên gọi địa danh mang trường sóng năng lượng ngũ hành xác định thông qua âm luật và tượng hình ngữ nghĩa.",
        "  - Khi Dụng thần suy nhược hoặc Kỵ thần quá vượng, việc đổi tên, dùng biệt danh, thêm tên đệm hoặc di chuyển đến vùng đất có tên mang hành tương sinh là phương pháp bổ khuyết trường khí rất hiệu nghiệm.",
        "  - Phân tích tên gọi theo Ngũ hành Hán tự: Chữ có bộ Thủy bổ Thủy, chữ có bộ Mộc bổ Mộc, chữ có bộ Hỏa bổ Hỏa, chữ có bộ Thổ bổ Thổ, chữ có bộ Kim bổ Kim.",
        "- **Quái lệ: Bị dán tờ rơi vu khống nói xấu giám đốc công ty (Ngày Canh Ngọ tháng Quý Mùi)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_69'],
        custom_proof="Quẻ Bí biến Lữ; hào 5 Huynh Đệ Tý thủy động hóa Thê Tài Ngọ hỏa; kẻ xấu mang tên có bộ Thủy hoặc phương Bắc hãm hại.",
        custom_see="Hào 5 Huynh Đệ Tý thủy lâm Chu Tước động; hào Thế Thê Tài Sửu thổ."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Chu Tước lâm Huynh Đệ Tý thủy động là khẩu thiệt thị phi gièm pha nặc danh; kẻ hãm hại tên có liên quan đến Thủy (Hà, Hải, Giang).",
        "    - Nhìn vào: Dùng chữ viết Thổ (tên công ty hoặc phòng ban có chữ Sơn, Thạch) để khắc Thủy dẹp yên thị phi.",
        "    - Đối thoại thực tế: Giám đốc đau đầu vì tin đồn bôi nhọ trước kỳ đại hội cổ đông.",
        "  - **Phương án hóa giải:** Đổi tên đề án kinh doanh sang chữ mang hành Thổ và chuyển văn phòng sang tòa nhà mang tên địa danh Cấn/Khôn.",
        "  - **Ứng nghiệm thực tế:** Kẻ tung tin nặc danh bị phát hiện xử lý kỷ luật, uy tín giám đốc được khôi phục trọn vẹn."
    ])
    return "\n".join(lines) + "\n"

def write_ch14_3():
    lines = [
        "### Hóa Giải Bằng Màu Sắc",
        "",
        "- **Cân bằng sắc thái ngũ hành trong không gian kiến trúc:**",
        "  - Màu sắc tác động trực tiếp vào thị giác và hệ thần kinh giao cảm của con người, sản sinh trường sinh học tương ứng ngũ hành.",
        "  - Sự thiên lệch thái quá của một gam màu trong nhà ở hay văn phòng có thể kích hoạt sát khí của Kỵ thần làm đảo lộn hòa khí và sức khỏe.",
        "  - Phối màu sinh khắc: Cung vị bị Kim vượng thái quá dùng màu xanh lục của Mộc hoặc lam của Thủy để tiết chế, tái lập cân bằng sinh thái.",
        "- **Quái lệ: Xung đột nội bộ công ty tại Bắc Kinh (Ngày Canh Thân tháng Bính Thìn)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_70'],
        custom_proof="Quẻ Tốn biến Cấu; Tốn Mộc bị Kim khắc; văn phòng sơn màu trắng quá nhiều (Kim vượng) gây bất hòa; đổi sang xanh lục dưỡng Mộc.",
        custom_see="Hào sơ Sửu thổ động hóa Tử Tôn Tị hỏa; quẻ thuần Tốn."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Quẻ Tốn Mộc thuần âm bị trường khí Kim bao vây; văn phòng mới cải tạo toàn bộ màu trắng toát làm nhân viên bức bối cãi cọ.",
        "    - Nhìn vào: Sơn lại mảng tường màu xanh lá cây nhạt và trải thảm xanh phối hợp cây xanh.",
        "    - Đối thoại thực tế: Lãnh đạo công ty gọi điện từ Bắc Kinh thắc mắc vì sao chuyển văn phòng mới nhân viên liên tục nghỉ việc.",
        "  - **Phương án hóa giải:** Thay đổi màu rèm cửa và mảng tường điểm nhấn sang màu xanh lục thảo mộc.",
        "  - **Ứng nghiệm thực tế:** Không khí công ty hòa nhã trở lại, các dự án phối hợp ăn ý nhịp nhàng."
    ])
    return "\n".join(lines) + "\n"

def write_ch14_4():
    lines = [
        "### Hóa Giải Bằng Phương Vị",
        "",
        "- **Chiến lược hoán chuyển phương vị không gian:**",
        "  - Phương vị phương hướng là tọa độ vật lý chứa các dòng chảy từ trường Trái Đất và năng lượng Bát Quái vũ trụ.",
        "  - Di chuyển người bị nạn hoặc người cần tìm đến phương vị sinh vượng cho Dụng thần là quy tắc cứu nguy tị hung kinh điển.",
        "  - Ứng dụng trong tìm người lạc, tìm đồ thất lạc, chữa bệnh hiểm nghèo và chuyển dời cơ sở làm ăn.",
        "- **Quái lệ: Mẹ tìm con gái bị lạc đường (Ngày Giáp Dần tháng Giáp Thân)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_71'],
        custom_proof="Quẻ Tốn biến Cấu; Tử Tôn Tị hỏa xuất hiện tại phương Nam; Tốn là Đông Nam; tìm con gái theo trục Đông Nam hướng Nam.",
        custom_see="Hào sơ Sửu thổ động; hào 4 Quan Quỷ Tân dậu kim; quẻ Tốn Vi Phong."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Con gái lấy Tử Tôn Tị hỏa, Tị là Hỏa phương Nam, quẻ Tốn là Đông Nam; cháu bé đi về hướng Đông Nam đến khu vui chơi.",
        "    - Nhìn vào: Hướng dẫn người nhà xuất phát tìm kiếm theo trục Đông Nam.",
        "    - Đối thoại thực tế: Người mẹ khóc lóc hoảng loạn tìm con suốt một ngày.",
        "  - **Phương án hóa giải:** Cử người đi tìm dọc theo công viên và nhà sách phía Đông Nam thành phố.",
        "  - **Ứng nghiệm thực tế:** Tìm thấy cháu bé đang ngồi đọc truyện tại nhà sách phía Đông Nam an toàn."
    ])
    return "\n".join(lines) + "\n"

def write_ch14_5():
    lines = [
        "### Hóa Giải Bằng Thời Gian",
        "",
        "- **Thuận theo thiên thời hoán chuyển cục diện:**",
        "  - Thời gian là chiều kích động biến đổi ngũ hành liên tục theo ngày, giờ, tiết khí và tuần giáp.",
        "  - Đón thời điểm tương xung tương hợp của hào động để thi hành các việc then chốt (đòi nợ, ký hợp đồng, chia tay, hòa giải).",
        "  - Xung khai quẻ hợp để giải quyết dứt điểm các vướng mắc dùng dằng khó tháo gỡ.",
        "- **Quái lệ 1: Đòi món nợ khó đòi lâu năm (Ngày Đinh Hợi tháng Nhâm Thìn)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_72'],
        custom_proof="Quẻ Bí biến Tổn; Thê Tài Tý thủy hưu tù; chọn ngày Tý xung Ngọ hỏa phá đê thu hồi tiền nợ.",
        custom_see="Hào 3 Huynh Đệ Thân kim động hóa Huynh Đệ Sửu thổ; hào Thế Thê Tài Sửu thổ."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại (phần 1 - quẻ Bí biến Tổn):**",
        "    - Căn cứ: Con nợ chây ì không chịu trả; quẻ Khảm biến Sư tiếp tục định rõ thời điểm thu nợ.",
        "- **Quái lệ 1 (tiếp theo): Quẻ Khảm biến Sư thu hồi 1 vạn nguyên đúng ngày Tý**"
    ] + make_evidence_block(
        figs_dict['fig_73'],
        custom_proof="Quẻ Khảm biến Sư; Thê Tài Ngọ hỏa số 2; ngày Tý xung Ngọ thu hồi đúng 1 vạn nguyên một nửa số nợ.",
        custom_see="Hào 3 Huynh Đệ Thìn thổ động hóa Quan Quỷ Mão mộc; quẻ Khảm Vi Thủy."
    ) + [
        "  - **Phán đoán và đối thoại (phần 2 - quẻ Khảm biến Sư):**",
        "    - Căn cứ: Ngày Bính Tý Thủy vượng xung Ngọ hỏa; số 2 chia đôi là 1 vạn nguyên.",
        "  - **Phương án hóa giải:** Đến tận nhà con nợ đòi tiền vào đúng 9h sáng ngày Bính Tý.",
        "  - **Ứng nghiệm thực tế:** Con nợ mở két thanh toán ngay 10.000 nguyên không một lời thoái thác.",
        "- **Quái lệ 2: Nam muốn hủy bỏ hôn ước êm đẹp (Ngày Giáp Thân tháng Nhâm Thìn)**"
    ] + make_evidence_block(
        figs_dict['fig_74'],
        custom_proof="Quẻ Dự biến Hằng; Thế lâm Thanh Long lục hợp; chọn ngày Tuất xung Thìn giải hợp hủy hôn thuận hòa.",
        custom_see="Hào sơ Thê Tài Mùi thổ động hóa Thê Tài Sửu thổ; hào 4 Thế Tử Tôn Ngọ hỏa."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Quẻ lục hợp dùng dằng khó dứt; chọn ngày Tuất xung khai quẻ hợp để nói lời chia tay.",
        "    - Nhìn vào: Tránh cãi vã đền bù tổn thất danh dự hai bên gia đình.",
        "    - Đối thoại thực tế: Chàng trai muốn chia tay vì không hợp tính cách nhưng sợ bị làm ầm ĩ.",
        "  - **Phương án hóa giải:** Hẹn gặp nói chuyện dứt khoát vào chiều ngày Mậu Tuất.",
        "  - **Ứng nghiệm thực tế:** Hai bên chia tay trong hòa bình, thống nhất trả lại sính lễ êm đẹp."
    ])
    return "\n".join(lines) + "\n"

def write_ch14_6():
    lines = [
        "### Hóa Giải Bằng Tu Luyện",
        "",
        "- **Khí công, dưỡng sinh và điều tức nội giới:**",
        "  - Khí huyết và tinh thần là nền tảng trường sinh học của cơ thể con người.",
        "  - Luyện khí công, thiền định đúng phương pháp giúp bổ sung chân khí, đả thông kinh mạch, tiêu trừ bệnh tật và nâng cao trường năng lượng tự vệ trước tà khí.",
        "  - Bế tinh dưỡng khí kiêng cữ phòng dục là chìa khóa phục hồi nguyên khí cho các trường hợp thận hư muộn con.",
        "- **Quái lệ 1: Người đàn ông hiệp hội khí công đoán bệnh nan y (Ngày Bính Dần tháng Ất Mùi)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_75'],
        custom_proof="Quẻ Quy Muội biến Khuê; Quan Quỷ Ngọ hỏa thiêu đốt; luyện khí công Thái Cực dưỡng âm thanh nhiệt phục hồi tạng phủ.",
        custom_see="Hào 3 Huynh Đệ Sửu thổ động hóa Tử Tôn Dần mộc; hào Thế Thê Tài Mão mộc."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Hỏa vượng thiêu tỳ vị; người tập khí công dùng công pháp dẫn khí hạ đan điền.",
        "    - Nhìn vào: Điều hòa hơi thở sâu kết hợp tĩnh tọa giờ Tý.",
        "  - **Phương án hóa giải:** Mỗi ngày thiền định 45 phút vào giờ Tý và giờ Ngọ.",
        "  - **Ứng nghiệm thực tế:** Bệnh nan y thuyên giảm kỳ diệu, xét nghiệm chỉ số máu trở lại bình thường.",
        "- **Quái lệ 2: Người đàn ông nhiều vợ nhưng muộn đường con cái (Ngày Đinh Sửu tháng Thân)**"
    ] + make_evidence_block(
        figs_dict['fig_76'],
        custom_proof="Quẻ Cách biến Quải; Tử Tôn Tý thủy Không Vong bị Thổ khắc; tu luyện dưỡng tinh khí túc sinh quý tử.",
        custom_see="Hào 4 Quan Quỷ Ngọ hỏa động hóa Quan Quỷ Ngọ hỏa; hào Thế Huynh Đệ Hợi thủy."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Hào Tử Tôn Không Vong do tinh khí suy kiệt vì sắc dục quá độ.",
        "    - Nhìn vào: Bế tinh dưỡng khí kiêng cữ phòng dục 100 ngày kết hợp luyện nội công.",
        "  - **Phương án hóa giải:** Kiêng phòng sự 3 tháng và tập bài tập bồi bổ thận khí.",
        "  - **Ứng nghiệm thực tế:** Sau 4 tháng người vợ chính thức mang thai và sinh hạ con trai kháu khỉnh."
    ])
    return "\n".join(lines) + "\n"

def write_ch14_7():
    lines = [
        "### Hóa Giải Bằng Mượn Vận",
        "",
        "- **Cộng hưởng trường khí từ người vượng vận:**",
        "  - Khi bản thân đang trong chu kỳ suy vi bại vận, năng lượng từ trường cá nhân bị suy thoái dễ dẫn đến quyết định sai lầm và thua lỗ.",
        "  - 'Đồng thanh tương ứng, đồng khí tương cầu': Mượn vận người có phúc khí, mạng vượng hoặc tuổi tương hợp với Dụng thần để đứng tên, ký kết hoặc đồng hành cùng hành sự.",
        "  - Giúp né tránh mũi nhọn hung sát và hưởng lây sinh khí cát tường của đối tác.",
        "- **Quái lệ: Người phụ nữ xem vận năm gặp suy hạn (Ngày Bính Tuất tháng Quý Sửu)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_77'],
        custom_proof="Quẻ Kiển biến Cấn; hào Thế Huynh Đệ Thìn thổ hưu tù; hào Ứng Thê Tài Tý thủy vượng; mượn vận người sinh năm Tý làm ăn.",
        custom_see="Hào 5 Quan Quỷ Thân kim động hóa Huynh Đệ Tuất thổ; hào Thế Huynh Đệ Thìn thổ."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Thế lâm hào Kiển gian nan; hào Ứng Tý thủy mang tài lộc vượng.",
        "    - Nhìn vào: Hợp tác làm ăn đứng tên chung với người tuổi Tý để mượn vận hanh thông.",
        "    - Đối thoại thực tế: Khách hàng buôn bán thua lỗ triền miên mất hết vốn liếng.",
        "  - **Phương án hóa giải:** Nhờ người em gái tuổi Giáp Tý đứng tên đại diện pháp luật cửa hàng.",
        "  - **Ứng nghiệm thực tế:** Việc buôn bán đổi chiều khởi sắc, thu hồi toàn bộ vốn và sinh lời lớn."
    ])
    return "\n".join(lines) + "\n"

def write_ch14_8():
    lines = [
        "### Hóa Giải Bằng Ngoại Ứng",
        "",
        "- **Cơ chế cảm ứng tâm vật và thiên cơ ngoại ứng:**",
        "  - Vũ trụ là một toàn thể hữu cơ; trong thời khắc gieo quẻ và dự đoán, vạn vật xung quanh xuất hiện ngẫu nhiên đều mang thông điệp vi tế tương thích với sự việc.",
        "  - Phân loại ngoại ứng: Ngoại ứng thị giác (hình ảnh, màu sắc, động vật, xe cộ); ngoại ứng thính giác (tiếng còi, tiếng chuông, tiếng chim, lời nói tình cờ); ngoại ứng sự kiện (hiến máu, làm từ thiện, gặp gỡ ngẫu nhiên).",
        "  - Chủ động tạo ngoại ứng: Dùng hành động có ý nghĩa tương đương (như hiến máu ứng với huyết quang, quyên tiền ứng với phá tài) để triệt tiêu tai họa thực tế.",
        "  - Quy luật bắt mạch thiên cơ: Ngoại ứng phát sinh đúng khoảnh khắc tâm niệm vừa khởi sẽ mang tính ứng nghiệm cao nhất.",
        "  - Chuyển di năng lượng hung sát: Biến hung thành cát bằng cách chủ động gánh chịu một phần tổn thất tượng trưng trước khi biến cố thật sự ập đến.",
        "- **Quái lệ 1: Hiến máu nhân đạo giải đại hạn phá tài (Quẻ Lữ biến Tấn)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_78'],
        custom_proof="Quẻ Lữ biến Tấn; Huynh Đệ Dần mộc động đoạt tài lâm Bạch Hổ; chủ động hiến máu bệnh viện hóa giải đại hạn phá tài huyết quang.",
        custom_see="Hào 4 Quan Quỷ Ngọ hỏa động hóa Thê Tài Dậu kim; hào sơ Huynh Đệ Mão mộc."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Quẻ báo sắp gặp đại nạn mất tiền và chảy máu; thấy xe hiến máu đỗ trước cửa làm ngoại ứng.",
        "    - Nhìn vào: Chủ động hiến máu (ứng huyết quang) và quyên tiền (ứng phá tài) để tiêu trừ nghiệp chướng.",
        "    - Đối thoại thực tế: Đương số linh cảm thấy điều chẳng lành, trong lòng bồn chồn đứng ngồi không yên.",
        "  - **Phương án hóa giải:** Đi hiến máu nhân đạo 200ml và công đức vào quỹ từ thiện.",
        "  - **Ứng nghiệm thực tế:** Tháng đó bình an vô sự, chỉ bị phạt giao thông nhẹ 50 ngàn đồng thay vì mất bạc triệu.",
        "- **Quái lệ 2: Tương lai cháu trai (Quẻ Tiểu Súc)**"
    ] + make_evidence_block(
        figs_dict['fig_79'],
        custom_proof="Quẻ Phong Thiên Tiểu Súc; Tử Tôn Tý thủy lâm hào Ứng; ngoại ứng nhìn thấy trẻ con cầm cờ dẫn đầu thành công sau này.",
        custom_see="Quẻ Phong Thiên Tiểu Súc; hào Thế Thê Tài Thìn thổ; hào Ứng Tử Tôn Tý thủy."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Cháu bé học hành thông minh nhưng hiếu động; ngoại ứng đứa trẻ vẫy cờ đỏ đi qua.",
        "    - Nhìn vào: Hình ảnh cờ đỏ tượng trưng cho bảng vàng đề danh và chức vụ lãnh đạo dẫn dắt tập thể.",
        "    - Đối thoại thực tế: Người bà lo lắng hỏi về tương lai của đứa cháu trai thông minh nhưng nghịch ngợm.",
        "  - **Phương án hóa giải:** Định hướng cháu theo ngành sư phạm hoặc quản trị công vụ.",
        "  - **Ứng nghiệm thực tế:** Cháu đỗ đại học sư phạm và trở thành giảng viên ưu tú.",
        "- **Quái lệ 3: Xem mộ tổ (Quẻ Tụy biến Hoán)**"
    ] + make_evidence_block(
        figs_dict['fig_80'],
        custom_proof="Quẻ Tụy biến Hoán; hào sơ Thế Mùi thổ động hóa Tị hỏa; Thủy triều rút cạn lộ xương cốt tổ tiên cần cải táng.",
        custom_see="Hào sơ Thế Thê Tài Mùi thổ động hóa Tử Tôn Tị hỏa; quẻ Trạch Địa Tụy."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Âm trạch bị ngập úng trũng; tiếng còi tàu hỏa hú dài làm ngoại ứng chỉ hướng Tây Bắc cao ráo.",
        "    - Nhìn vào: Âm thanh còi tàu rền vang thuộc Càn Kim báo hiệu địa hình gò đồi vượng khí phía xa.",
        "    - Đối thoại thực tế: Người nhà trăn trở nghi ngờ phần mộ dòng họ bị sụt lún ngập nước.",
        "  - **Phương án hóa giải:** Quy tập mộ phần về sườn đồi phía Tây Bắc.",
        "  - **Ứng nghiệm thực tế:** Gia tộc con cháu làm ăn phát đạt, sinh nhiều đinh quý.",
        "- **Quái lệ 4: Xem bệnh chồng (Quẻ Thăng & Quẻ Đại Hữu biến Đỉnh)**"
    ] + make_evidence_block(
        figs_dict['fig_81'],
        custom_proof="Quẻ Thăng; Quan Quỷ Dậu kim Không Vong; ngoại ứng nghe thấy tiếng chim gõ kiến mổ cây trừ sâu bệnh.",
        custom_see="Quẻ Địa Phong Thăng; hào 3 Quan Quỷ Dậu kim Không Vong."
    ) + [
        "  - **Phán đoán và đối thoại (phần 1 - quẻ Thăng):**",
        "    - Căn cứ: Chồng mắc bệnh gan mật mệt mỏi; kết hợp quẻ Đại Hữu biến Đỉnh kiểm tra bài thuốc.",
        "    - Đối thoại thực tế: Người vợ vừa khóc vừa kể bệnh viện lớn đã trả về, bác sĩ lắc đầu.",
        "- **Quái lệ 4 (tiếp theo): Quẻ Đại Hữu biến Đỉnh bài trừ bệnh tật**"
    ] + make_evidence_block(
        figs_dict['fig_82'],
        custom_proof="Quẻ Đại Hữu biến Đỉnh; hào 3 Thế Phụ Mẫu Thìn thổ; Tử Tôn Dần mộc động; dùng thảo dược Mộc trị dứt bệnh gan.",
        custom_see="Hào 3 Thế Phụ Mẫu Thìn thổ động hóa Quan Quỷ Hợi thủy; quẻ Hỏa Thiên Đại Hữu."
    ) + [
        "  - **Phán đoán và đối thoại (phần 2):**",
        "    - Căn cứ: Ngoại ứng chén trà xanh mang lại thanh nhiệt giải độc.",
        "    - Nhìn vào: Mộc khí sinh vượng từ thảo dược giải độc gan phục hồi chức năng tạng phủ.",
        "  - **Phương án hóa giải:** Dùng nhân trần và diệp hạ châu sắc uống thay nước lọc.",
        "  - **Ứng nghiệm thực tế:** Men gan hạ về mức an toàn sau 3 tuần uống thuốc.",
        "- **Quái lệ 5: Xem bệnh phổi (Quẻ Tốn biến Tiểu Súc)**"
    ] + make_evidence_block(
        figs_dict['fig_83'],
        custom_proof="Quẻ Tốn biến Tiểu Súc; hào 2 Thế Quan Quỷ Dậu kim động hóa Huynh Đệ Dần mộc; ngoại ứng tiếng chuông reo báo lành.",
        custom_see="Hào 2 Thế Quan Quỷ Dậu kim động hóa Huynh Đệ Dần mộc; quẻ Tốn Vi Phong."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Phổi có nốt mờ nghi u; tiếng chuông điện thoại báo tin lành là ngoại ứng hoán cải số mệnh.",
        "    - Đối thoại thực tế: Bệnh nhân ho kéo dài tức ngực khó thở, tinh thần hoang mang cực độ.",
        "  - **Phương án hóa giải:** Tập hít thở sâu ngoài trời vào lúc bình minh phương Đông.",
        "  - **Ứng nghiệm thực tế:** Chụp CT lại nốt mờ chỉ là ổ viêm cũ vôi hóa, sức khỏe bình an.",
        "- **Quái lệ 6: Mộ phần cha mẹ (Quẻ Cổ biến Đại Súc)**"
    ] + make_evidence_block(
        figs_dict['fig_84'],
        custom_proof="Quẻ Cổ biến Đại Súc; Phụ Mẫu Tý thủy lâm Nguyệt phá; ngoại ứng người lái xe tải chạy ngang chỉ rõ vị trí long mạch.",
        custom_see="Hào 3 Huynh Đệ Thân kim động hóa Huynh Đệ Tuất thổ; quẻ Sơn Phong Cổ."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Mộ tổ bị đường giao thông mới mở cắt ngang long mạch.",
        "    - Nhìn vào: Xe chở đá cuội chạy qua ngụ ý cần xếp đá kè đất vững chắc cản ngăn bụi khí.",
        "  - **Phương án hóa giải:** Trồng hàng thông xanh phong thủy chắn bụi và ngăn sát khí đường xá.",
        "  - **Ứng nghiệm thực tế:** Gia đạo an ổn trở lại, công việc làm ăn thoát khỏi bế tắc."
    ])
    return "\n".join(lines) + "\n"

# Write Group 5 files
g5_files = {
    'ch14_1': ('fragments/ch14_1_chinh_sua_phong_thuy_branches.md', write_ch14_1()),
    'ch14_2': ('fragments/ch14_2_hoa_giai_ten_nguoi_ten_at_branches.md', write_ch14_2()),
    'ch14_3': ('fragments/ch14_3_hoa_giai_bang_mau_sac_branches.md', write_ch14_3()),
    'ch14_4': ('fragments/ch14_4_hoa_giai_bang_phuong_vi_branches.md', write_ch14_4()),
    'ch14_5': ('fragments/ch14_5_hoa_giai_bang_thoi_gian_branches.md', write_ch14_5()),
    'ch14_6': ('fragments/ch14_6_hoa_giai_bang_tu_luyen_branches.md', write_ch14_6()),
    'ch14_7': ('fragments/ch14_7_hoa_giai_bang_muon_van_branches.md', write_ch14_7()),
    'ch14_8': ('fragments/ch14_8_hoa_giai_bang_ngoai_ung_branches.md', write_ch14_8()),
}

for cid, (fpath, content) in g5_files.items():
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Wrote {cid} -> {fpath} ({len(content.splitlines())} lines)")
