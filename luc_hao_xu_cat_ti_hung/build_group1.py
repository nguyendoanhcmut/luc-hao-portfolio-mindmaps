import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
from base_generator import figs_dict, make_evidence_block

def write_ch01():
    # fragments/ch01_loi_tua_branches.md
    fig_01 = figs_dict['fig_01']
    lines = [
        "## Lời Tựa",
        "",
        "- **Tư tưởng cốt lõi về số phận và hóa giải:**",
        "  - Trong đời người khó tránh khỏi gian truân trắc trở; bậc trí giả không cam chịu số phận mà chọn thái độ tích cực, dùng trí tuệ Dịch học để phòng tránh và hóa giải tai nạn.",
        "  - Khảo cổ học chứng minh từ thời Tây Hán hơn 2000 năm trước đã thịnh hành trấn trạch, linh phù trừ tà; Trương Đạo Lăng dùng phù thủy trị bệnh lập Ngũ Đấu Mễ Đạo, mở đường cho 'Chúc Do Thập Tam Khoa' trong Trung y.",
        "  - Mục đích tối thượng của thuật dự đoán là mưu cầu cuộc sống tốt đẹp; nhận diện rủi ro trước mắt để chủ động né tránh và chuyển hóa theo chiều hướng tích cực.",
        "- **Sơ đồ Thái Cực Bát Quái – Cội nguồn âm dương ngũ hành:**"
    ]
    lines.extend(make_evidence_block(
        fig_01,
        custom_proof="Thái Cực sinh Lưỡng Nghi, Lưỡng Nghi sinh Tứ Tượng, Tứ Tượng sinh Bát Quái – gốc rễ điều hòa âm dương ngũ hành trong vũ trụ.",
        custom_see="Vòng tròn Thái Cực âm dương tương bão ở trung tâm, bao quanh bởi hệ thống quẻ Càn, Khôn, Cấn, Đoài, Khảm, Ly, Chấn, Tốn."
    ))
    lines.extend([
        "- **Hệ thống Lục Hào hóa giải bí truyền của tác giả Vương Hổ Ứng:**",
        "  - Lục Hào cổ truyền phần lớn chỉ lưu truyền thuật đoán mà khuyết thiếu thuật giải; tác giả dày công nghiên cứu bí truyền dân gian và thực nghiệm để hoàn thiện trọn vẹn học thuyết Lục Hào hóa giải.",
        "  - Thực nghiệm khoa học của học trò Nhật Bản: Xếp hạt giống theo tự dạng Hán tự chứng minh năng lượng ngũ hành có thật (chữ Thủy nảy mầm 90%, chữ Mộc 70%, chữ Kim 30%).",
        "  - Giới hạn và nguyên tắc thực tiễn: Hóa giải không phải vạn năng; năng lượng bất lợi quá lớn hoặc phương pháp chưa phù hợp đòi hỏi phải điều chỉnh linh hoạt, không sa vào mê tín cực đoan."
    ])
    return "\n".join(lines) + "\n"

def write_ch02():
    # fragments/ch02_chuong_1_muc_ich_cua_du_oan_luc_hao_branches.md
    fig_02 = figs_dict['fig_02']
    fig_03 = figs_dict['fig_03']
    lines = [
        "## Chương 1: Mục Đích Của Dự Đoán Lục Hào",
        "",
        "- **Mục đích và nguyên lý Lục Hào dự đoán:**",
        "  - Người xưa sáng tạo Lục Hào nhằm giúp con người nắm bắt cơ hội tốt, lánh xa tai họa để cuộc sống hạnh phúc viên mãn hơn.",
        "  - Cát hung bắt nguồn từ Ngũ hành sinh khắc chế ước vạn vật; do đó vận dụng Ngũ hành sinh khắc hoàn toàn có thể biến đổi cát hung.",
        "  - Tính mềm dẻo của vận mệnh: Vận mệnh chịu ảnh hưởng của thời không vũ trụ, giáo dục, nỗ lực bản thân và di truyền nên không có hai số mệnh hoàn toàn rập khuôn; dự đoán học tìm ra quy luật vận động để cải tạo.",
        "- **Quái lệ 1: Quách Phác đoán bệnh cho Cảnh Tự bằng quẻ Lâm (Ngày Quý Dậu tháng Mùi)**"
    ]
    lines.extend(make_evidence_block(
        fig_02,
        custom_proof="Hào 2 Thế Quan Quỷ Mão mộc hưu tù bị Nhật thần khắc thương; Quách Phác dùng Mão mộc tỉ hòa trợ vượng kết hợp quẻ Khôn (thịt thỏ).",
        custom_see="Thế tại hào 2 Quan Quỷ Mão mộc lâm Thanh Long; quẻ thuộc cung Khôn; hào Ứng Thê Tài Hợi thủy Không Vong."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Cảnh Tự phái em trai đi xem thay nên Dụng thần lấy hào Thế Quan Quỷ Mão mộc chứ không lấy hào Huynh Đệ; hào Thế hưu tù tại tháng Mùi lại bị Nhật Dậu khắc thương là bệnh nặng.",
        "    - Nhìn vào: Kỵ thần Kim không phát động nên chọn phương pháp tỉ vượng Dụng thần; Mão mộc là sao Thiên Y, ứng với loài thỏ; quẻ Địa Trạch Lâm thuộc cung Khôn, Khôn là thịt, gộp lại là thịt thỏ; Thế lâm Thanh Long chủ ăn uống.",
        "    - Đối thoại thực tế: Quách Phác phán bệnh dai dẳng mấy năm muốn lành nhất thiết phải ăn thịt thỏ mới chuyển nguy thành an.",
        "  - **Phương án hóa giải:** Ăn thịt thỏ để trợ vượng hào Thế Quan Quỷ Mão mộc và nạp khí Thiên Y.",
        "  - **Ứng nghiệm thực tế:** Trên đường về em trai Cảnh Tự bắt được con thỏ rừng, Cảnh Tự ăn xong liền khỏi dứt điểm căn bệnh nan y nhiều năm.",
        "- **Quái lệ 2: Quách Phác đoán bệnh thương hàn cho chú viên quan quận Nghĩa Hưng (Ngày Tân Hợi tháng Ngọ)**"
    ] + make_evidence_block(
        fig_03,
        custom_proof="Hào 2 Thế Quan Quỷ Ngọ hỏa hóa Tử Tôn Hợi thủy hồi đầu khắc nguy kịch; Quách Phác dùng Thổ khắc Thủy cứu Hỏa (khắc thần bị khắc).",
        custom_see="Hào 2 Thế Quan Quỷ Ngọ hỏa lâm Huyền Vũ động hóa Tử Tôn Hợi thủy hồi đầu khắc; Thổ hướng Khôn (Sửu thổ) khắc Hợi thủy bảo vệ Ngọ hỏa."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Hào Thế tự hóa hồi đầu khắc tính mạng ngàn cân treo sợi tóc; áp dụng nguyên tắc 'khắc thần bị khắc' (dùng Thổ khắc phục Kỵ thần Thủy để cứu Dụng thần Hỏa).",
        "    - Nhìn vào: Trong các chi Thổ, Tuất là Mộ khố làm suy Hỏa, Mùi tương hợp trói kỵ bệnh mới; Thìn và Sửu không hại Thế; Sửu ứng với trâu, phương Khôn là Tây Nam đại diện cho Thổ và trâu.",
        "    - Đối thoại thực tế: Quách Phác khuyên gia đình phải tìm được trâu ở hướng Khôn dẫn về thì bệnh nhân mới có cơ hội sống sót.",
        "  - **Phương án hóa giải:** Dắt trâu từ phương Khôn (Tây Nam) về lưu lại một đêm để trường khí Thổ phương Khôn trấn áp Thủy sát.",
        "  - **Ứng nghiệm thực tế:** Giữa lúc khó khăn người từ phía Tây Nam dắt trâu đi qua, giữ trâu lại một đêm thì bệnh thương hàn thuyên giảm rồi khỏi hẳn."
    ])
    return "\n".join(lines) + "\n"

def write_ch03_0():
    # fragments/ch03_0_chuong_2_thap_nhi_ia_chi_tiet_lo_thien_c_branches.md
    lines = [
        "## Chương 2: Thập Nhị Địa Chi Tiết Lộ Thiên Cơ",
        "",
        "- **Nguyên lý âm dương mất cân bằng thúc đẩy vận động vũ trụ:**",
        "  - Vũ trụ sinh ra từ sự tương tác giữa âm và dương; chính sự phát triển không cân bằng khiến vũ trụ không ngừng chuyển động và sinh sôi muôn loài.",
        "  - Nếu âm dương đạt tới trạng thái cân bằng tuyệt đối thì vạn vật rơi vào trạng thái tĩnh tịch và ngừng tồn tại.",
        "- **Mật mã 12 loài vật đối ứng 12 Địa Chi:**",
        "  - 12 con giáp được chọn làm mật mã dự đoán do mang vai trò truyền tải trường năng lượng ngũ hành đặc thù của trời đất.",
        "  - Quy luật móng chân chẵn lẻ phân định âm dương: Động vật móng chẵn ứng với Địa Chi âm (Trâu-Sửu, Thỏ-Mão, Dê-Mùi, Gà-Dậu, Lợn-Hợi; Rắn-Tị cực âm không chân); động vật móng lẻ ứng với Địa Chi dương (Hổ-Dần, Rồng-Thìn, Ngựa-Ngọ, Khỉ-Thân, Chó-Tuất).",
        "  - Chuột (Tý) đại diện cho giờ Tý chuyển giao âm dương nên chân trước 4 ngón (chẵn - âm), chân sau 5 ngón (lẻ - dương)."
    ]
    return "\n".join(lines) + "\n"

def write_ch03_1():
    # fragments/ch03_1_loai_ca_con_giap_ky_la_branches.md
    lines = [
        "### Loài Cá Con Giáp Kỳ Lạ",
        "",
        "- **Hiện tượng loài cá Nhuận ngư ở Đông Hải:**",
        "  - Cổ tịch ghi chép loài Nhuận ngư chỉ xuất hiện vào các năm nhuận; hình dạng đầu cá biến đổi tương ứng với Địa Chi năm nhuận (năm Tý nhuận đầu chuột đuôi cá, năm Sửu nhuận đầu trâu đuôi cá).",
        "  - Minh chứng tự nhiên về sự tồn tại hữu hình của trường khí 12 con giáp trong sinh giới.",
        "- **Thiên cơ tiết lộ ở nơi khuyết hãm:**",
        "  - Người xưa đúc kết 'thiên cơ tiết lộ tại bệnh xứ' (bí mật trời đất bộc lộ ở chỗ khiếm khuyết); do đó 12 con giáp được chọn đều mang khiếm khuyết sinh học đặc trưng.",
        "  - 'Thử mục thốn quang': Chuột mắt kém nhìn gần ứng giờ Tý âm dương mờ mịt; Trâu thiếu hàm răng trên, Thỏ hở môi, Rắn không chân, Rồng thiếu thính giác, Gà không bàng quang."
    ]
    return "\n".join(lines) + "\n"

def write_ch03_2():
    # fragments/ch03_2_hien_tuong_sinh_khac_giua_12_loai_vat_branches.md
    lines = [
        "### Hiện Tượng Sinh Khắc Giữa 12 Loài Vật",
        "",
        "- **Quan hệ sinh khắc tự nhiên tương ứng Địa Chi:**",
        "  - Hợi thủy khắc Tị hỏa: Trong thực tế loài lợn ăn thịt rắn, khi bị rắn cắn lợn chỉ sưng nhẹ ngoài da không nguy hiểm tính mạng.",
        "  - Tý thủy khắc Ngọ hỏa: Phân chuột chứa độc tính tự nhiên với loài ngựa, ngựa ăn phải sẽ bị trướng bụng mà chết.",
        "  - Hiện tượng sinh thái khẳng định tính chân thực của quy luật sinh khắc xung hợp giữa 12 Địa Chi khi ứng dụng vào thuật hóa giải."
    ]
    return "\n".join(lines) + "\n"

def write_ch03_3():
    # fragments/ch03_3_y_nghia_tuong_ung_cua_12_ia_chi_trong_ho_branches.md
    lines = [
        "### Ý Nghĩa Tương Ứng Của 12 Địa Chi Trong Hóa Giải",
        "",
        "- **Ý nghĩa biểu tượng và vật phẩm của 12 Địa Chi:**",
        "  - Tý (Thủy): Chuột, chim én, cá quả, con dơi; nước muối, sông hồ, bể nước; người tuổi Tý.",
        "  - Sửu (Thổ): Trâu, con cua, rùa đen; ruộng đất, két sắt, đồ gốm sứ; người tuổi Sửu.",
        "  - Dần (Mộc): Hổ, con mèo, con báo; cây cối, rừng rậm, đồ gỗ, kiến trúc gỗ; người tuổi Dần.",
        "  - Mão (Mộc): Thỏ, con cáo, nhím, hạc trắng; hoa cỏ, đồ tre trúc; người tuổi Mão.",
        "  - Thìn (Thổ): Rồng, thuồng luồng, cá chép, giun đất; đầm nước, ấm trà, vại nước, dụng cụ y tế; người tuổi Thìn.",
        "  - Tị (Hỏa): Rắn, lươn, ve sầu; nến, ánh đèn, đất nung đỏ, dây thừng; người tuổi Tị.",
        "  - Ngọ (Hỏa): Ngựa, con lừa, hươu nai; cây nến, lồng hấp nhiệt; người tuổi Ngọ.",
        "  - Mùi (Thổ): Dê cừu, chim nhạn; sừng dê, chén rượu, bồn cảnh, vườn cây, y dược; người tuổi Mùi.",
        "  - Thân (Kim): Khỉ, con mèo; kim loại, đồ sắt, xe cộ, dao kéo, đinh nhọn, xương cốt; người tuổi Thân.",
        "  - Dậu (Kim): Gà, chim trĩ; gương đồng, la bàn, nam châm, ổ khóa, đồ kim khí; người tuổi Dậu.",
        "  - Tuất (Thổ): Chó, chó sói; ngói gạch, đồ gốm, tràng hạt, bình chữa cháy; người tuổi Tuất.",
        "  - Hợi (Thủy): Lợn, cá quả, gấu; nước đá, băng, mực viết, muối ăn, nước tương; người tuổi Hợi.",
        "- **Nguyên tắc điều phối năng lượng Địa Chi trong hóa giải:**",
        "  - Dụng thần Không Vong: Dùng Xung Không hoặc Thực Không để kích hoạt cát khí.",
        "  - Dụng thần Nguyệt Phá: Ưu tiên dùng Hợp Phá thay vì Thực Phá.",
        "  - Nguyên thần bị hợp: Dùng chi xung Nguyên thần để giải hợp; Kỵ thần phát động: Dùng chi khắc hoặc hợp Kỵ thần.",
        "- **Quái lệ 1: Người đàn ông đoán thăng chức (Ngày Quý Dậu tháng Giáp Dần năm Quý Mùi)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_04'],
        custom_proof="Quan Quỷ Sửu thổ bị Nguyệt khắc lâm hào động hóa Ngọ hỏa hồi đầu sinh; hào Thế Ngọ hỏa động cần trợ lực đầu ngựa hướng vào trong.",
        custom_see="Hào 3 Thế Thê Tài Ngọ hỏa lâm Chu Tước hóa Quan Quỷ Sửu thổ; hào sơ Tử Tôn Dần mộc động khắc hào 2 Quan Quỷ Thìn thổ."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Quan Quỷ làm Dụng thần bị Nguyệt khắc, Tử Tôn Dần mộc động khắc Quan; quẻ Sư là quân đội, Tử Tôn là binh lính lâm Nguyệt kiến báo hiệu có quân nhân xuất ngũ phản đối.",
        "    - Nhìn vào: Quan Quỷ hóa hồi đầu sinh; hào Thế là Ngọ hỏa sinh Quan; Kỵ thần Dần mộc phương Đông Bắc sinh khí bất lợi cho quan vận.",
        "    - Đối thoại thực tế: Đương số rà soát hội đồng không thấy quân nhân xuất ngũ; tác giả khẳng định nếu không hóa giải chắc chắn trượt, khuyên đặt ngựa đỏ.",
        "  - **Phương án hóa giải:** Đặt một con ngựa mỹ nghệ màu đỏ tại phương Đông Bắc trong nhà, đầu ngựa hướng vào phía trong phòng làm việc (tượng hồi đầu sinh).",
        "  - **Ứng nghiệm thực tế:** Hôm sau họp thảo luận bất ngờ bị một cựu hồng quân kịch liệt phản đối, nhưng sau đó chuyển hướng sang người khác, đương số được thăng chức; sau đó nghe bạn xoay đầu ngựa ra ngoài liền bị điều chuyển vị trí nhàn rỗi.",
        "- **Quái lệ 2: Đoán ký hợp đồng chuyển nhượng kỹ thuật (Ngày Canh Dần tháng Bính Dần)**"
    ] + make_evidence_block(
        figs_dict['fig_05'],
        custom_proof="Hào Ứng Phụ Mẫu Mùi thổ lâm Nguyệt khắc; Nguyên thần Tị hỏa nhập Mộ; Kỵ thần Dần mộc xung khắc Thân kim cần chữ Thân giải cứu.",
        custom_see="Hào 5 Huynh Đệ Thân kim động hóa Huynh Đệ Thân kim; hào 2 Quan Quỷ Sửu thổ động hóa Thê Tài Dần mộc."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Hợp đồng lấy Phụ Mẫu làm Dụng thần, Dụng thần Mùi thổ hưu tù; hào 5 Huynh Đệ Thân kim động khắc hợp đồng nhưng hóa thoái; cần củng cố Kim để trợ Thân.",
        "    - Nhìn vào: Chi Thân tương ứng phương Tây Nam; viết chữ Thân (申) bổ khuyết trường khí Kim.",
        "    - Đối thoại thực tế: Khách hàng lo lắng đối tác chần chừ bỏ cuộc; tác giả hướng dẫn viết chữ Thân đặt phương Tây Nam.",
        "  - **Phương án hóa giải:** Viết chữ Thân (申) trên giấy vàng mực chu sa dán tại phương Tây Nam phòng làm việc.",
        "  - **Ứng nghiệm thực tế:** Vài ngày sau đối tác chủ động liên lạc và ký kết hợp đồng chuyển nhượng thuận lợi.",
        "- **Quái lệ 3: Đoán thi cử thăng tiến (Ngày Canh Dần tháng Giáp Tý)**"
    ] + make_evidence_block(
        figs_dict['fig_06'],
        custom_proof="Phụ Mẫu Mão mộc Không Vong; Quan Quỷ Hợi thủy lâm Nguyệt kiến động hóa Tử Tôn Dần mộc tham hợp quên sinh; cần bể nước giải hợp.",
        custom_see="Hào 5 Quan Quỷ Hợi thủy động hóa Tử Tôn Dần mộc; hào 3 Tử Tôn Thìn thổ động hóa Huynh Đệ Ngọ hỏa."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Phụ Mẫu Mão mộc Không Vong cần Xung Không hoặc Thực Không; Quan Quỷ Hợi thủy động hợp Dần mộc (tham hợp quên sinh).",
        "    - Nhìn vào: Hợi thủy tương ứng hướng Tây Bắc và cá quả/bể nước; tăng cường Thủy để sinh Phụ Mẫu Mão mộc.",
        "    - Đối thoại thực tế: Thí sinh hồi hộp vì tỷ lệ chọi cao; tác giả hướng dẫn bài trí bể nước hướng Tây Bắc.",
        "  - **Phương án hóa giải:** Đặt bể nước nuôi cá quả tại góc Tây Bắc phòng học để kích hoạt Quan tinh sinh Phụ.",
        "  - **Ứng nghiệm thực tế:** Thí sinh đạt điểm số xuất sắc và được bổ nhiệm vào vị trí mong muốn.",
        "- **Quái lệ 4: Đoán bệnh viêm đại tràng mãn tính (Ngày Kỷ Hợi tháng Giáp Tý)**"
    ] + make_evidence_block(
        figs_dict['fig_07'],
        custom_proof="Hào 2 Quan Quỷ Sửu thổ lâm Câu Trần vượng; Phụ Mẫu Mão mộc hưu tù bị khắc; cần Mão mộc thỏ phương Đông để sinh Thế trợ thân.",
        custom_see="Quẻ Ly Vi Hỏa lục xung; hào 2 Thế Quan Quỷ Sửu thổ; hào sơ Phụ Mẫu Mão mộc."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Hào 2 là ruột và bụng, lâm Câu Trần chủ sưng trướng đau đớn; Mão mộc hưu tù bị tiết khí nặng.",
        "    - Nhìn vào: Mão mộc đối ứng với loài thỏ và phương Đông; tranh thỏ mang năng lượng Mộc tươi sáng.",
        "    - Đối thoại thực tế: Bệnh nhân đau bụng đi ngoài nhiều năm không khỏi; tác giả khuyên treo tranh thỏ phương Đông.",
        "  - **Phương án hóa giải:** Treo bức tranh vẽ con thỏ tại phương Đông phòng ngủ để bồi bổ Mộc khí.",
        "  - **Ứng nghiệm thực tế:** Sau một tháng các cơn đau quặn bụng dứt hẳn, đại tràng phục hồi bình thường.",
        "- **Quái lệ 5: Đoán mua cổ phiếu đầu tư (Ngày Giáp Tuất tháng Kỷ Mùi)**"
    ] + make_evidence_block(
        figs_dict['fig_08'],
        custom_proof="Thê Tài Ngọ hỏa lâm Tuần Không; Thế hào Thân kim hưu tù; cần tượng ngựa đồng hướng Nam xuất Không tiếp tài.",
        custom_see="Hào 5 Huynh Đệ Thân kim持 Thế; hào 3 Thê Tài Ngọ hỏa Không Vong."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Cầu tài lấy Thê Tài làm Dụng thần; Tài hào Ngọ hỏa Không Vong tức tiền tài chưa tụ; Ngọ lâm Hỏa phương Nam.",
        "    - Nhìn vào: Ngọ là ngựa, chất liệu kim loại đồng hỗ trợ sinh tài trường khí bền vững.",
        "    - Đối thoại thực tế: Nhà đầu tư phân vân không biết cổ phiếu có tăng giá hay sụt giảm.",
        "  - **Phương án hóa giải:** Đặt một tượng ngựa bằng đồng tại phương Nam bàn làm việc để kích tài xuất Không.",
        "  - **Ứng nghiệm thực tế:** Cổ phiếu tăng vọt liên tiếp nhiều phiên, nhà đầu tư chốt lời thu lợi nhuận lớn.",
        "- **Quái lệ 6: Đoán cha bị đột quỵ xuất huyết não (Ngày Canh Ngọ tháng Ất Mão)**"
    ] + make_evidence_block(
        figs_dict['fig_09'],
        custom_proof="Hào 6 Phụ Mẫu Dần mộc vượng; Quan Quỷ Tuất thổ động hóa Dậu kim tiết khí; cần tượng chó phương Tây Bắc giữ vững khí mạch.",
        custom_see="Quẻ Cấn Vi Sơn; hào 2 Quan Quỷ Ngọ hỏa; hào 3 Huynh Đệ Thân kim động hóa Huynh Đệ Mão mộc."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Người cha bị xuất huyết não; hào vị đầu não lâm Quan Quỷ động khắc; Tuất thổ Mộ khố cần củng cố.",
        "    - Nhìn vào: Tuất đối ứng với chó ở phương Tây Bắc; dùng linh khuyển trấn áp tà khí phục hồi sinh cơ.",
        "    - Đối thoại thực tế: Người con trai vô cùng lo lắng cha hôn mê sâu tại bệnh viện.",
        "  - **Phương án hóa giải:** Đặt tượng chó bằng gốm sứ ở phương Tây Bắc giường bệnh nhân để bồi đắp Tuất thổ.",
        "  - **Ứng nghiệm thực tế:** Bệnh nhân tỉnh lại sau 3 ngày và dần bình phục chức năng vận động."
    ])
    return "\n".join(lines) + "\n"

# Write out group 1 fragments
manifest = json.load(open('luc_hao_xu_cat_ti_hung_scout_manifest.json', encoding='utf-8'))
g1_files = {
    'ch01': ('fragments/ch01_loi_tua_branches.md', write_ch01()),
    'ch02': ('fragments/ch02_chuong_1_muc_ich_cua_du_oan_luc_hao_branches.md', write_ch02()),
    'ch03_0': ('fragments/ch03_0_chuong_2_thap_nhi_ia_chi_tiet_lo_thien_c_branches.md', write_ch03_0()),
    'ch03_1': ('fragments/ch03_1_loai_ca_con_giap_ky_la_branches.md', write_ch03_1()),
    'ch03_2': ('fragments/ch03_2_hien_tuong_sinh_khac_giua_12_loai_vat_branches.md', write_ch03_2()),
    'ch03_3': ('fragments/ch03_3_y_nghia_tuong_ung_cua_12_ia_chi_trong_ho_branches.md', write_ch03_3()),
}

for cid, (fpath, content) in g1_files.items():
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Wrote {cid} -> {fpath} ({len(content.splitlines())} lines)")
