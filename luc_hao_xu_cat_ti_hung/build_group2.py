import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
from base_generator import figs_dict, make_evidence_block

def write_ch04_0():
    return (
        "## Chương 3: Ý Nghĩa Ẩn Tàng Trong Bát Quái\n\n"
        "- **Ý nghĩa ẩn tàng đa tầng của Bát Quái trong Lục Hào:**\n"
        "  - Bát Quái không chỉ chứa đựng tượng quẻ cơ bản mà còn ẩn tàng trường thông tin vô cùng phong phú về nhân vật, thân thể, không gian, đồ vật, âm thanh, chữ viết.\n"
        "  - Trích xuất thông tin quái cung là nền tảng cốt yếu để xác định chính xác phương án hóa giải Lục Hào có hiệu quả rõ ràng và bền vững.\n"
    )

def write_trigram(level, trigram_name, nature, weather, geo, people, body, animal, static, char, food):
    lines = [
        f"### Ý Nghĩa Ẩn Tàng Trong Quẻ {trigram_name}",
        "",
        f"- **Tính chất:** {nature}",
        f"- **Thiên tượng:** {weather}",
        f"- **Địa lý:** {geo}",
        f"- **Nhân vật:** {people}",
        f"- **Thân thể:** {body}",
        f"- **Động vật:** {animal}",
        f"- **Tĩnh vật:** {static}",
        f"- **Chữ viết:** {char}",
        f"- **Ẩm thực:** {food}"
    ]
    return "\n".join(lines) + "\n"

def write_ch04_8():
    lines = [
        "### Ý Nghĩa Ẩn Tàng Trong Quẻ Đoài",
        "",
        "- **Ý nghĩa ẩn tàng của quẻ Đoài:**",
        "  - Tính chất: Khuyết thiếu, tan vỡ, tổn hại, sứt mẻ, vui vẻ, khẩu thiệt.",
        "  - Thiên tượng: Mưa nhỏ, trăng non, các vì sao tinh tú.",
        "  - Địa lý: Phương Tây, đầm lầy, ao hồ, nơi trũng ngập nước.",
        "  - Nhân vật: Thiếu nữ, người có tài ăn nói, bà đồng, phiên dịch viên, ca sĩ.",
        "  - Thân thể: Miệng, lưỡi, răng, phổi, thanh quản, khí quản, ruột.",
        "  - Động vật: Con dê.",
        "  - Tĩnh vật: Đồ vật có miệng, đồ kim khí sắc bén, nhạc cụ, phế liệu, kim loại.",
        "  - Chữ viết: Chữ bộ Kim (金), chữ mang nghĩa kim khí hoặc khuyết thiếu.",
        "  - Ẩm thực: Đồ ăn cay nồng, cơm Tây.",
        "- **Quy luật phán đoán tai họa theo quái cung:** Càn (chùa chiền, quan chức, kim loại); Đoài (tranh chấp khẩu thiệt, ao hồ, thiếu nữ); Khảm (sông biển, trộm cắp, thủy nạn); Ly (hỏa hoạn, văn thư); Chấn (xe cộ, rừng cây, tức giận); Tốn (đồ gỗ, phụ nữ); Khôn (ruộng đất, bà cụ, núi rừng); Cấn (khoáng vật, phần mộ).",
        "- **Quái lệ 1: Bạn học nữ gầy yếu đoán bệnh máu cô đặc (Ngày Đinh Mùi tháng Bính Thìn)**"
    ]
    lines.extend(make_evidence_block(
        figs_dict['fig_10'],
        custom_proof="Hào 2 Thế Quan Quỷ Ngọ hỏa nhập Mộ ở Tuất thổ; cung Càn (xương) + Thê Tài Dần mộc (máu) lâm Câu Trần (cô đặc) -> suy tủy giảm sinh máu.",
        custom_see="Hào 2 Thế Quan Quỷ Ngọ hỏa [phục Thê Tài Dần mộc]; hào 6 Phụ Mẫu Tuất thổ động; hào 3 Huynh Đệ Thân kim."
    ))
    lines.extend([
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Hào 2 Thế Ngọ hỏa nhập Mộ ở Tuất thổ mất tự do (ở lì trong nhà không ra ngoài); Ngọ hỏa số 2, 7 -> thể trọng chỉ 70 cân (35 kg); năm 1995 Ất Hợi Thế bị khắc bắt đầu mắc bệnh, 1996 Bính Tý xung Thế bệnh trầm trọng.",
        "    - Nhìn vào: Quẻ Độn thuộc cung Càn (xương); Nguyên thần Thê Tài Dần mộc phục hào 2 nhập Mộ ở Nhật, lâm Câu Trần chủ chậm chạp kết khối -> tủy xương rối loạn tạo máu, máu cô đặc không chảy được.",
        "    - Đối thoại thực tế: Đương số kinh ngạc xác nhận bị bệnh từ 1995, năm 1996 liệt giường không ra khỏi cửa; máu cô đặc đến mức bác sĩ cắm kim không rút được máu; thể trọng đúng 70 cân, ở nhà lầu tầng 2.",
        "  - **Phương án hóa giải:** Mỗi ngày ăn hai lạng thịt ngựa (Càn là thịt ngựa, Ngọ hỏa số 2); đặt vôi sống dưới gầm giường (hào 2) để hút Thủy sát Kỵ thần và trợ vượng Hỏa, 7 ngày (hợp ngũ hành) thay vôi một lần.",
        "  - **Ứng nghiệm thực tế:** Không lâu sau thể trọng tăng nhanh, bệnh tủy xương khỏi hoàn toàn; năm 1999 yêu đương và năm 2001 kết hôn thuận lợi.",
        "- **Quái lệ 2: Người đàn ông đoán đau chân và phong thấp (Ngày Nhâm Tý tháng Mậu Ngọ)**"
    ] + make_evidence_block(
        figs_dict['fig_11'],
        custom_proof="Cừu thần Phụ Mẫu Tý thủy hào sơ độc phát khắc thương Nguyên thần; cung Tốn (đùi) + hào sơ (chân) + Thủy lâm Huyền Vũ -> phong thấp chân.",
        custom_see="Hào sơ Phụ Mẫu Tý thủy động hóa Thê Tài Mùi thổ hồi đầu khắc; hào 5 Thế Thê Tài Mùi thổ; Nguyệt kiến Ngọ hỏa."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Quẻ Phệ Hạp thuộc cung Tốn (đùi), Cừu thần Phụ Mẫu Tý thủy động tại hào sơ (bàn chân) lâm Huyền Vũ chủ phong thấp dịch ẩm; quẻ biến du hồn bệnh lan rộng.",
        "    - Nhìn vào: Cừu thần Tý thủy hóa Thê Tài Mùi thổ hồi đầu khắc nhưng sức Mùi thổ yếu, cần tăng cường Mùi thổ; Tốn là cây cỏ, Mùi hào sơ là rễ cây, lâm Huyền Vũ màu đen ánh đỏ -> rễ cà tím.",
        "    - Đối thoại thực tế: Đương số xác nhận đau chân phong thấp kinh niên chữa khắp nơi không khỏi, thỉnh cầu Lục Hào cứu giải.",
        "  - **Phương án hóa giải:** Lấy rễ cây cà tím kết hợp ớt đỏ (Mùi thổ hợp Nguyệt Ngọ hỏa màu đỏ) sắc nước sôi ngâm rửa chân hằng ngày.",
        "  - **Ứng nghiệm thực tế:** Sau một thời gian kiên trì ngâm rửa, chứng đau nhức phong thấp ở chân tiêu biến hoàn toàn.",
        "- **Quái lệ 3: Tăng San Bốc Dịch – Bài học không tuân thủ hóa giải dẫn đến đại họa**"
    ] + make_evidence_block(
        figs_dict['fig_12'],
        custom_proof="Quẻ Ích biến Trung Phu; Dụng thần hưu tù phát động gặp hung; dự trắc sư chỉ dẫn hóa giải nhưng đương số coi nhẹ không nghe theo.",
        custom_see="Hào 2 Thê Tài Dần mộc động hóa Thê Tài Dần mộc; hào 3 Huynh Đệ Thìn thổ động hóa Huynh Đệ Sửu thổ."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Tăng San Bốc Dịch ghi chép quẻ biến xuất hiện hung sát hiển hiện; dự trắc sư dặn dò kỹ lưỡng thời khắc và phương vị phải lánh nạn.",
        "    - Nhìn vào: Người coi bói chủ quan ỷ lại nghĩ là chuyện nhỏ không thi hành phương án.",
        "    - Đối thoại thực tế: Lời cảnh báo bị bỏ ngoài tai, đến kỳ hạn hung thần phát động ứng nghiệm chuẩn xác.",
        "  - **Phương án hóa giải:** Đáng lẽ phải dùng vật phẩm chế sát và chuyển đổi chỗ ở theo hướng dẫn.",
        "  - **Ứng nghiệm thực tế:** Đương số gặp tai nạn thảm khốc, chứng minh quy luật nhân quả và tầm quan trọng của việc nghiêm túc chấp hành hóa giải.",
        "- **Quái lệ 4: Dự đoán và hóa giải bệnh dịch hô hấp SARS năm 2003**"
    ] + make_evidence_block(
        figs_dict['fig_13'],
        custom_proof="Quẻ Đỉnh biến Hằng; Kim hào đại diện phế khí bị Hỏa khắc mạnh; trích xuất thông tin Tốn Mộc và Ly Hỏa để điều tiết phòng dịch.",
        custom_see="Hào 3 Tử Tôn Dậu kim bị Nguyệt kiến khắc; hào 4 Quan Quỷ Cửu tứ động."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Bệnh dịch SARS năm 2003 thuộc phế nhiệt hô hấp, kim bị hỏa khắc gay gắt; cung Ly chủ sốt cao viêm nhiệt.",
        "    - Nhìn vào: Vận dụng cơ chế sinh khắc của Bát Quái và Lục Hào để tìm phương thức thanh nhiệt nhuận phế.",
        "    - Đối thoại thực tế: Tác giả cảnh báo nguy cơ lây lan diện rộng qua đường hô hấp và đề xuất các biện pháp phòng ngừa phong thủy.",
        "  - **Phương án hóa giải:** Tăng cường Thủy khí phương Bắc để dập tắt Hỏa nhiệt, bảo vệ Kim phế âm.",
        "  - **Ứng nghiệm thực tế:** Dự báo trùng khớp diễn biến dịch tễ, giúp người áp dụng tránh được lây nhiễm trong mùa cao điểm dịch bệnh.",
        "- **Quái lệ 5: Dự đoán hôn nhân trắc trở (Ngày Canh Thìn tháng Mùi)**"
    ] + make_evidence_block(
        figs_dict['fig_14'],
        custom_proof="Quẻ Trung Phu biến Tụng; hào Thế Thê Tài Mão mộc hưu tù Không Vong; Quan Quỷ Tị hỏa lâm Chu Tước khẩu thiệt tranh chấp.",
        custom_see="Hào 3 Huynh Đệ Thìn thổ động hóa Quan Quỷ Ngọ hỏa; hào Thế Thê Tài Mão mộc Không Vong."
    ) + [
        "  - **Phán đoán và đối thoại:**",
        "    - Căn cứ: Thế lâm Thê Tài Không Vong là tình cảm trống rỗng bất an; hào Ứng Quan Quỷ xung khắc Thế lâm Chu Tước hay cãi vã thị phi.",
        "    - Nhìn vào: Phương Đoài khuyết thiếu làm tổn hại gia đạo; cần dùng Mộc tỉ hòa và Thủy sinh Mộc để cứu vãn.",
        "    - Đối thoại thực tế: Người vợ đau khổ vì vợ chồng lục đục trên bờ vực ly hôn, xin cứu vãn mái ấm.",
        "  - **Phương án hóa giải:** Bài trí cây xanh phong thủy phương Đông và đặt bình nước hoa hợp mệnh tại phòng ngủ.",
        "  - **Ứng nghiệm thực tế:** Vợ chồng hóa giải mâu thuẫn, tình cảm hòa thuận trở lại sau hai tháng."
    ])
    return "\n".join(lines) + "\n"

# Generate Group 2 files
g2_files = {
    'ch04_0': ('fragments/ch04_0_chuong_3_y_nghia_an_tang_trong_bat_quai_branches.md', write_ch04_0()),
    'ch04_1': ('fragments/ch04_1_y_nghia_an_tang_trong_que_can_branches.md', write_trigram(3, "Càn", "Vĩ đại, dũng cảm, quyết đoán, cao lớn, hình tròn.", "Trời quang, mưa đá, băng giá, khí lạnh.", "Tây Bắc, thủ đô, cao nguyên, nơi cao ráo.", "Lãnh đạo, giám đốc, cha, bậc trưởng bối, người nhà nước.", "Đầu, xương, phổi, đại tràng, khuôn mặt.", "Ngựa, thiên nga, sư tử, voi.", "Vàng bạc, ngọc ngà, gương tròn, kính mắt, mũ nón.", "Chữ bộ Kim (金) (như Ngân, Châm, Đinh, Cương, Tiền).", "Thịt ngựa, thịt dính xương, quả táo, đồ khô.")),
    'ch04_2': ('fragments/ch04_2_y_nghia_an_tang_trong_que_khon_branches.md', write_trigram(3, "Khôn", "Bao dung, nhu thuận, tĩnh lặng, vuông vức, tối tăm.", "Mây mù, sương mù, khí âm u.", "Tây Nam, đồng bằng, ruộng đất, bãi đất trống.", "Mẹ, bà cụ, nông dân, quần chúng nhân dân.", "Bụng, dạ dày, lá lách, da thịt.", "Bò sữa, trâu, kiến.", "Vải vóc, đồ gốm sứ, đồ vuông, xi măng.", "Chữ bộ Thổ (土) (như Địa, Điền, Khang, Thạch).", "Thịt bò, đồ ngọt, ngũ cốc, khoai lang.")),
    'ch04_3': ('fragments/ch04_3_y_nghia_an_tang_trong_que_chan_branches.md', write_trigram(3, "Chấn", "Chuyển động, phấn phát, kinh sợ, giận dữ, âm vang.", "Sấm sét, sấm mùa xuân, chớp giật.", "Phương Đông, đường cái, sân vận động, rừng cây.", "Trưởng nam, quân nhân, cảnh sát, người lái xe.", "Chân, bàn chân, gan, thanh đới, dây thần kinh.", "Rồng, rắn, chim ưng.", "Xe cộ, chuông báo, nhạc cụ gõ, đồ gỗ lớn.", "Chữ bộ Mộc (木) mang ý nghĩa chuyển động.", "Thịt rồng, đồ chua, măng tre, rau xanh.")),
    'ch04_4': ('fragments/ch04_4_y_nghia_an_tang_trong_que_ton_branches.md', write_trigram(3, "Tốn", "Thẩm thấu, thuận tòng, lưu động, do dự, thanh mảnh.", "Gió lốc, gió xuân, mây bay.", "Đông Nam, vườn hoa, bưu điện, sân bay.", "Trưởng nữ, tăng ni, giáo viên, thương nhân.", "Đùi, mông, hệ thần kinh, khí quản, tóc.", "Gà, chim trĩ, bướm, côn trùng.", "Dây thừng, quạt máy, đồ tre trúc mảnh mai, thư từ.", "Chữ bộ Thảo (艹) hoặc Mộc mảnh mai.", "Thịt gà, rau thơm, trà, quả dâu tằm.")),
    'ch04_5': ('fragments/ch04_5_y_nghia_an_tang_trong_que_kham_branches.md', write_trigram(3, "Khảm", "Hiểm trở, trắc trở, gian nan, trí tuệ, chìm đắm.", "Mưa rào, tuyết, sương đêm, mặt trăng.", "Phương Bắc, sông hồ, biển cả, giếng nước, quán rượu.", "Trung nam, thủy thủ, trộm đạo, gián điệp.", "Thận, bàng quang, máu, tai, cơ quan bài tiết.", "Lợn, cá, chuột, sinh vật dưới nước.", "Rượu bia, chất lỏng, dầu nhớt, bút mực, bánh xe.", "Chữ bộ Thủy (氵) (như Giang, Hà, Hải, Hồ).", "Cá biển, canh súp, muối ăn, đồ ướp lạnh.")),
    'ch04_6': ('fragments/ch04_6_y_nghia_an_tang_trong_que_ly_branches.md', write_trigram(3, "Ly", "Quang minh, rực rỡ, bám víu, nóng nảy, trống rỗng bên trong.", "Mặt trời, ánh nắng, cầu vồng, sao băng.", "Phương Nam, thư viện, trường học, trạm phát sóng, rạp phim.", "Trung nữ, học giả, nghệ sĩ, người mẫu, binh sĩ.", "Mắt, tim, huyết áp, tiểu tràng.", "Chim công, chim trĩ, gà lôi, rùa, con cua.", "Sách vở, tranh ảnh, máy vi tính, tivi, bóng đèn.", "Chữ bộ Hỏa (火) (như Quang, Viêm, Huy, Xích).", "Thịt chim, đồ nướng chiên, quả hạnh cay đắng.")),
    'ch04_7': ('fragments/ch04_7_y_nghia_an_tang_trong_que_can_branches.md', write_trigram(3, "Cấn", "Đình chỉ, ngăn trở, ổn định, vững chắc, cao vút.", "Mây núi, sương mù trên đỉnh núi.", "Đông Bắc, đồi núi, gò đống, bức tường thành, nghĩa trang.", "Thiếu nam, người gác cổng, bảo vệ, ẩn sĩ.", "Mũi, lưng, ngón tay, xương sườn, khớp xương.", "Chó, hổ, gấu, cáo, chim gõ kiến.", "Bàn ghế đá, hòn non bộ, đồ điêu khắc đá, két sắt.", "Chữ bộ Sơn (山) (như Nham, Phong, Lĩnh, Khâu).", "Thịt thú rừng, măng khô, củ khoai củ cải.")),
    'ch04_8': ('fragments/ch04_8_y_nghia_an_tang_trong_que_oai_branches.md', write_ch04_8()),
}

for cid, (fpath, content) in g2_files.items():
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Wrote {cid} -> {fpath} ({len(content.splitlines())} lines)")
