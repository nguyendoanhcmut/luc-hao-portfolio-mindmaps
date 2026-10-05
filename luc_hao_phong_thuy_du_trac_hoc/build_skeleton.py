import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

TXT_PATH = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_phong_thuy_du_trac_hoc\luc_hao_phong_thuy_du_trac_hoc.txt"
OUTPUT_DIR = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_phong_thuy_du_trac_hoc"

with open(TXT_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines in source text: {len(lines)}")

# 1. Map each line to exact page number using page_results
pages_data = {}
for i in range(1, 349):
    pfile = os.path.join(OUTPUT_DIR, "page_results", f"page_{i:04d}.json")
    if os.path.exists(pfile):
        with open(pfile, "r", encoding="utf-8") as pf:
            pages_data[i] = json.load(pf).get("markdown", "")

line_to_page = {}
cur_p = 1
for l_idx, line in enumerate(lines):
    s = line.strip()
    if not s:
        line_to_page[l_idx] = cur_p
        continue
    for p in range(cur_p, min(cur_p + 15, 349)):
        if s in pages_data.get(p, ""):
            cur_p = p
            break
    line_to_page[l_idx] = cur_p

print(f"Page mapping complete. Max page: {max(line_to_page.values())}")

# 2. Extract Figures
FIG_MANIFEST = os.path.join(OUTPUT_DIR, "figures_manifest.json")
drop_figures = ["fig_01", "fig_02", "fig_03", "fig_187"]
figure_ids = {}

# 3. Build Sections
# We want clean, hierarchical sections:
# Level 2 for chapters / Lời tựa
# Level 3 for chapter sub-topics
# Level 4 for individual case studies under Quẻ Dịch sections (to ensure ~400-800 word chunks)

sections = []

def add_sec(line, level, title):
    sections.append({
        "line": line,
        "level": level,
        "title": title
    })

# Front matter & Chapter 1
add_sec(36, 2, "MỤC LỤC")
add_sec(69, 2, "LỜI TỰA")
add_sec(85, 2, "CHƯƠNG 1: Ý NGHĨA CỦA LỤC HÀO DỰ ĐOÁN PHONG THỦY")

# Chapter 2
add_sec(145, 2, "CHƯƠNG 2: KIẾN THỨC LỤC HÀO CĂN BẢN ỨNG DỤNG TRONG DỰ ĐOÁN PHONG THỦY")
add_sec(149, 3, "1. DỤNG THẦN TRONG DỰ ĐOÁN PHONG THỦY")
add_sec(186, 3, "2. CÁCH DÙNG HÀO VỊ TRONG DỰ ĐOÁN PHONG THỦY")
add_sec(373, 3, "3. Ý NGHĨA CỦA LỤC THÂN TRONG DỰ ĐOÁN PHONG THỦY")
add_sec(425, 3, "4. THỦ TƯỢNG LỤC THẦN TRONG DỰ ĐOÁN PHONG THỦY")
add_sec(584, 3, "5. THỦ TƯỢNG BÁT QUÁI TRONG DỰ ĐOÁN PHONG THỦY")
add_sec(631, 3, "6. THỦ TƯỢNG NGŨ HÀNH TRONG DỰ ĐOÁN PHONG THỦY")
add_sec(678, 3, "7. LỤC THÂN HỖ HÓA TRONG DỰ ĐOÁN PHONG THỦY")
add_sec(740, 3, "8. Ý NGHĨA CỦA DỤNG THẦN LƯỠNG HIỆN")
add_sec(754, 3, "9. Ý NGHĨA CỦA DỤNG THẦN PHỤC TÀNG")
add_sec(774, 3, "10. Ý NGHĨA CỦA TIẾN THẦN VÀ THOÁI THẦN")
add_sec(788, 3, "11. Ý NGHĨA CỦA NGUYỆT PHÁ")
add_sec(865, 3, "12. Ý NGHĨA CỦA KHÔNG VONG")
add_sec(948, 3, "13. Ý NGHĨA CỦA LỤC XUNG VÀ LỤC HỢP")
add_sec(1009, 3, "14. Ý NGHĨA CỦA PHẢN NGÂM VÀ PHỤC NGÂM")
add_sec(1056, 3, "15. Ý NGHĨA CỦA DU HỒN VÀ QUY HỒN")
add_sec(1091, 3, "16. ỨNG DỤNG CỦA 12 TRẠNG THÁI NGŨ HÀNH SINH DIỆT TRONG DỰ ĐOÁN PHONG THỦY")

# Chapter 3
add_sec(1152, 2, "CHƯƠNG 3: PHÁN ĐOÁN CHI TIẾT TRONG DỰ ĐOÁN PHONG THỦY")
add_sec(1159, 3, "1. PHƯƠNG PHÁP PHÁN ĐOÁN ĐƯỜNG ĐI")
add_sec(1234, 3, "2. PHƯƠNG PHÁP PHÁN ĐOÁN CẦU")
add_sec(1287, 3, "3. PHƯƠNG PHÁP PHÁN ĐOÁN SÔNG NGÒI")
add_sec(1301, 3, "4. PHƯƠNG PHÁP PHÁN ĐOÁN VẬT KIẾN TRÚC")
add_sec(1331, 3, "5. PHƯƠNG PHÁP PHÁN ĐOÁN NÚI")
add_sec(1366, 3, "6. PHƯƠNG PHÁP PHÁN ĐOÁN HOA CỎ CÂY CỐI")
add_sec(1380, 3, "7. PHƯƠNG PHÁP PHÁN ĐOÁN ĐÁ")
add_sec(1414, 3, "8. TỔNG LUẬN PHONG THỦY")

# Chapter 4
add_sec(1513, 2, "CHƯƠNG 4: DỰ ĐOÁN PHONG THỦY NƠI Ở")
add_sec(1533, 3, "1. NỀN NHÀ")
add_sec(1604, 3, "2. GIẾNG NƯỚC")
add_sec(1622, 3, "3. HÀNG XÓM")
add_sec(1638, 3, "4. SÂN")
add_sec(1677, 3, "5. PHÒNG BẾP")
add_sec(1732, 3, "6. PHÒNG NGỦ")
add_sec(1744, 3, "7. BÀN THỜ")
add_sec(1781, 3, "8. CỬA")
add_sec(1828, 3, "9. TƯỜNG")
add_sec(1842, 3, "10. MÁI NHÀ")
add_sec(1875, 3, "11. GIƯỜNG")
add_sec(1928, 3, "12. NHÀ VỆ SINH")
add_sec(1961, 3, "QUẺ DỊCH VỀ PHONG THỦY DƯƠNG TRẠCH")

# Chapter 5
add_sec(5277, 2, "CHƯƠNG 5: DỰ ĐOÁN PHONG THỦY ÂM TRẠCH")
add_sec(5280, 3, "1. LONG MẠCH")
add_sec(5290, 3, "2. SA")
add_sec(5298, 3, "3. THỦY")
add_sec(5333, 3, "4. MINH ĐƯỜNG")
add_sec(5343, 3, "5. LONG HỔ")
add_sec(5351, 3, "6. PHÁN ĐOÁN HUYỆT VÀ ĐIỂM HUYỆT")
add_sec(5402, 3, "7. PHẦN MỘ")
add_sec(5431, 3, "8. THỦY KHẨU")
add_sec(5445, 3, "9. ÁN SƠN")
add_sec(5474, 3, "10. ĐẮC ĐỊA")
add_sec(5492, 3, "ÁN LỆ PHONG THỦY ÂM TRẠCH CỔ ĐẠI")
add_sec(5576, 3, "QUẺ DỊCH VỀ PHONG THỦY ÂM TRẠCH")

# Chapter 6
add_sec(6276, 2, "CHƯƠNG 6: PHONG THỦY THƯƠNG NGHIỆP")
add_sec(6279, 3, "1. CỬA HÀNG")
add_sec(6321, 3, "2. QUẦY THU NGÂN")
add_sec(6337, 3, "3. KHÁCH HÀNG")
add_sec(6386, 3, "4. NGƯỜI LÀM THUÊ")
add_sec(6406, 3, "QUẺ DỊCH VỀ PHONG THỦY THƯƠNG NGHIỆP")

# Now let's extract all worked examples (exercises)
# and also add the case study examples under QUẺ DỊCH as level 4 sections!

pat_vd = re.compile(r'^(?:#{1,4}\s+)?(?:\*\*)?(Ví dụ(?:\s+\d+(?:\s*\([^\)]+\))?)?)\s*[:\.]\s*(.*)', re.IGNORECASE)
pat_pure_vd = re.compile(r'^(?:#{1,4}\s+)?(?:\*\*)?(Ví dụ\s+\d+)\b\s*[:\.]?\s*(.*)', re.IGNORECASE)

all_exercises = []
ex_counter = 0

for i, line in enumerate(lines):
    s = line.strip()
    if not s:
        continue
    # Special case: line 101
    if "Xin đưa ra một ví dụ:" in s:
        ex_counter += 1
        all_exercises.append({
            "line": i,
            "exercise_id": f"vd{ex_counter:03d}",
            "title": "Ví dụ: Ngày Giáp Thìn tháng Mão, được Chấn Vi Lôi biến Lôi Phong Hằng",
            "start_page": line_to_page[i],
            "end_page": line_to_page[min(i + 40, len(lines) - 1)]
        })
        continue

    m = pat_vd.match(s)
    if m:
        label = m.group(1).strip()
        rest = m.group(2).strip().replace('*', '').strip()
        if label.lower() == 'ví dụ như':
            continue
        
        # Clean up title
        full_title = f"{label}: {rest}".strip().rstrip(':')
        ex_counter += 1
        start_p = line_to_page[i]
        # estimate end_page (look ahead up to next example or +35 lines)
        end_p = start_p
        for fwd in range(i + 1, min(i + 60, len(lines))):
            fwd_s = lines[fwd].strip()
            if pat_vd.match(fwd_s) or fwd_s.startswith('#'):
                end_p = line_to_page[fwd - 1]
                break
        end_p = max(start_p, end_p)

        all_exercises.append({
            "line": i,
            "exercise_id": f"vd{ex_counter:03d}",
            "title": full_title[:120],
            "start_page": start_p,
            "end_page": end_p
        })

        # If this example is inside QUẺ DỊCH sections, add it as level 4 section!
        # Dương Trạch cases: 1961 < i < 5277
        # Âm Trạch cổ đại: 5492 <= i < 5576
        # Âm Trạch cases: 5576 <= i < 6276
        # Thương nghiệp cases: 6406 <= i < 7157
        if (1961 < i < 5277) or (5492 <= i < 6276) or (6406 <= i < 7157):
            # Short clean title for the section
            sec_title = full_title
            if len(sec_title) > 90:
                sec_title = sec_title[:87] + "..."
            add_sec(i, 4, sec_title)

# Sort sections by line
sections.sort(key=lambda s: s["line"])

print(f"Total sections: {len(sections)}")
print(f"Total exercises: {len(all_exercises)}")

# Build Rule Index
rule_index = [
    {"title": "Dụng thần trong dự đoán phong thủy", "page": 11},
    {"title": "Cách dùng hào vị trong dự đoán phong thủy", "page": 13},
    {"title": "Phân bố lục thân cho hào vị", "page": 15},
    {"title": "Phân bố kết cấu căn nhà cho hào vị", "page": 16},
    {"title": "Phân bố bộ vị cơ thể cho hào vị", "page": 17},
    {"title": "Phân bố nội tạng cơ thể cho hào vị", "page": 18},
    {"title": "Phân bố khu vực hành chính cho hào vị", "page": 19},
    {"title": "Phân bố chức vụ cho hào vị", "page": 20},
    {"title": "Tổ hợp thông tin hào vị", "page": 20},
    {"title": "Ý nghĩa lục thân trong dự đoán phong thủy", "page": 20},
    {"title": "Thủ tượng lục thần trong dự đoán phong thủy", "page": 22},
    {"title": "Tổ hợp lục thần và ngũ hành", "page": 25},
    {"title": "Thủ tượng bát quái trong dự đoán phong thủy", "page": 30},
    {"title": "Thủ tượng ngũ hành trong dự đoán phong thủy", "page": 32},
    {"title": "Lục thân hỗ hóa trong dự đoán phong thủy", "page": 35},
    {"title": "Ý nghĩa Dụng thần lưỡng hiện", "page": 37},
    {"title": "Ý nghĩa Dụng thần phục tàng", "page": 38},
    {"title": "Ý nghĩa Tiến thần và Thoái thần", "page": 39},
    {"title": "Ý nghĩa Nguyệt phá", "page": 39},
    {"title": "Ý nghĩa Không Vong", "page": 41},
    {"title": "Ý nghĩa lục xung và lục hợp", "page": 43},
    {"title": "Ý nghĩa phản ngâm và phục ngâm", "page": 45},
    {"title": "Ý nghĩa du hồn và quy hồn", "page": 47},
    {"title": "Ứng dụng 12 trạng thái ngũ hành sinh diệt", "page": 48},
    {"title": "Phương pháp phán đoán đường đi", "page": 52},
    {"title": "Phương pháp phán đoán cầu", "page": 55},
    {"title": "Phương pháp phán đoán sông ngòi", "page": 57},
    {"title": "Phương pháp phán đoán vật kiến trúc", "page": 57},
    {"title": "Phương pháp phán đoán núi", "page": 58},
    {"title": "Phương pháp phán đoán hoa cỏ cây cối", "page": 60},
    {"title": "Phương pháp phán đoán đá", "page": 60},
    {"title": "Tổng luận phong thủy", "page": 62},
    {"title": "Phương pháp phán đoán nền nhà", "page": 67},
    {"title": "Phương pháp phán đoán giếng nước", "page": 70},
    {"title": "Phương pháp phán đoán hàng xóm", "page": 71},
    {"title": "Phương pháp phán đoán sân", "page": 72},
    {"title": "Phương pháp phán đoán phòng bếp", "page": 74},
    {"title": "Phương pháp phán đoán phòng ngủ", "page": 76},
    {"title": "Phương pháp phán đoán bàn thờ", "page": 77},
    {"title": "Phương pháp phán đoán cửa", "page": 79},
    {"title": "Phương pháp phán đoán tường", "page": 81},
    {"title": "Phương pháp phán đoán mái nhà", "page": 81},
    {"title": "Phương pháp phán đoán giường", "page": 83},
    {"title": "Phương pháp phán đoán nhà vệ sinh", "page": 84},
    {"title": "Phương pháp phán đoán Long mạch âm trạch", "page": 251},
    {"title": "Phương pháp phán đoán Sa âm trạch", "page": 251},
    {"title": "Phương pháp phán đoán Thủy âm trạch", "page": 252},
    {"title": "Phương pháp phán đoán Minh đường âm trạch", "page": 253},
    {"title": "Phương pháp phán đoán Long Hổ âm trạch", "page": 254},
    {"title": "Phán đoán huyệt và điểm huyệt", "page": 254},
    {"title": "Phương pháp phán đoán phần mộ", "page": 257},
    {"title": "Phương pháp phán đoán thủy khẩu", "page": 258},
    {"title": "Phương pháp phán đoán án sơn", "page": 259},
    {"title": "Phương pháp phán đoán đắc địa", "page": 260},
    {"title": "Phán đoán phong thủy cửa hàng thương nghiệp", "page": 303},
    {"title": "Phán đoán quầy thu ngân", "page": 305},
    {"title": "Phán đoán khách hàng", "page": 306},
    {"title": "Phán đoán người làm thuê", "page": 308}
]

# Global Lexicon
global_lexicon = {
    "core_thesis": "Hệ thống lý luận và thực chiến Lục Hào Phong Thủy Dự Trắc Học của Vương Hổ Ứng và Lưu Thiết Khanh, kết hợp hào vị, lục thân, lục thần, bát quái, ngũ hành, 12 trạng thái ngũ hành sinh diệt và thần sát để chẩn đoán chính xác thực trạng phong thủy và đề xuất phương án cải tạo tối ưu cho Dương Trạch (nhà ở), Âm Trạch (mồ mả) và Phong Thủy Thương Nghiệp (kinh doanh, cửa hàng).",
    "key_terms": [
        {
            "term": "Dụng thần",
            "definition": "Hào đại diện cho đối tượng phong thủy cần chiêm đoán: Hào Thế (bản thân gia chủ), Hào 2 (trạch hào - căn nhà), Phụ Mẫu (kiến trúc, nhà đất, mồ mả), Thê Tài (tiền bạc, phòng bếp), Quan Quỷ (sát khí, tai họa, quỷ thần, âm hồn), Tử Tôn (lối đi, nước giếng, sự an lành), Huynh Đệ (tường vách, cửa nẻo, sự tiêu tán)."
        },
        {
            "term": "Hào vị",
            "definition": "Hệ thống 6 bậc hào tương ứng không gian trạch xá: Hào 1 (nền móng, giếng nước), Hào 2 (phòng bếp, nhà ở, lân cận), Hào 3 (cửa trong, giường nằm), Hào 4 (cửa ngoài, cổng ngõ), Hào 5 (đường đi, chủ nhà), Hào 6 (tường bao, mái nhà, không gian trên cao)."
        },
        {
            "term": "Trạch hào",
            "definition": "Vị trí hào 2 trong quẻ, tiêu điểm biểu thị trực tiếp ngôi nhà, trạng thái an nguy, khí trường và sự thoải mái của gia cư."
        },
        {
            "term": "Lục thần",
            "definition": "Sáu linh thần phối hợp ngũ hành phụ họa thông tin phong thủy: Thanh Long (mới mẻ, tươi tốt, hướng Đông), Chu Tước (bếp lửa, âm thanh, tiếng ồn, hướng Nam), Câu Trần (nhà cũ, tu sửa, bế tắc, trung cung), Đằng Xà (dị vật, sâu bọ, uốn lượn, hoảng sợ), Bạch Hổ (đường lộ lớn, xung sát, đổ gãy, hướng Tây), Huyền Vũ (mương nước bẩn, ẩm thấp, ám muội, hướng Bắc)."
        },
        {
            "term": "Lục hợp",
            "definition": "Tượng trưng cho sự gắn kết chặt chẽ, nhà nhiều tầng lầu, tàng phong tụ khí, kiên cố, êm ấm."
        },
        {
            "term": "Lục xung",
            "definition": "Tượng trưng cho phi sa tẩu thạch, tán khí, xung xạ hung hiểm, gió lùa, thường xuyên biến động hoặc đổ vỡ."
        },
        {
            "term": "Nguyệt phá",
            "definition": "Hào bị chi tháng xung phá, chủ hư hỏng, rạn nứt, bong tróc tường vách, kiến trúc suy tàn hoặc chất lượng công trình kém."
        },
        {
            "term": "Không Vong",
            "definition": "Hào tuần không, biểu thị phòng ốc bỏ trống, thiếu ánh sáng, thiếu sinh khí, hư vô, hoặc tinh thần gia chủ hoang mang bất an."
        },
        {
            "term": "Phản ngâm / Phục ngâm",
            "definition": "Phản ngâm chủ phản phúc, thay đổi, cải tạo nhiều lần; Phục ngâm chủ ngột ngạt, rên rỉ, bệnh tật kéo dài, khó khăn đình trệ."
        },
        {
            "term": "12 Cung Trường Sinh",
            "definition": "Vòng sinh diệt ngũ hành biểu thị chu kỳ sinh suy của khí trường và sự vật: Trường Sinh (cội nguồn), Mộc Dục (ẩm bẩn), Quan Đới (trang nghiêm), Lâm Quan / Đế Vượng (thịnh vượng, cao lớn), Suy / Bệnh / Tử (suy tàn, hư hại), Mộ (mồ mả, cất giấu), Tuyệt (cạn kiệt), Thai / Dưỡng (thai nghén, bồi đắp)."
        },
        {
            "term": "Dương Trạch",
            "definition": "Phong thủy nhà ở nhân gian, khảo sát 12 hạng mục trọng yếu: Nền nhà, Giếng nước, Hàng xóm, Sân, Phòng bếp, Phòng ngủ, Bàn thờ, Cửa, Tường, Mái nhà, Giường, Nhà vệ sinh."
        },
        {
            "term": "Âm Trạch",
            "definition": "Phong thủy mồ mả tổ tiên, khảo sát 10 quy tắc: Long mạch, Sa, Thủy, Minh đường, Long Hổ, Huyệt vị, Phần mộ, Thủy khẩu, Án sơn, Đắc địa."
        },
        {
            "term": "Phong Thủy Thương Nghiệp",
            "definition": "Phong thủy ứng dụng trong kinh doanh buôn bán, tập trung vào 4 trọng điểm: Cửa hàng, Quầy thu ngân, Khách hàng, Người làm thuê."
        }
    ],
    "key_entities": [
        "Vương Hổ Ứng",
        "Lưu Thiết Khanh",
        "Trần Phương"
    ]
}

# Global Context Pack
global_context_pack = """# BỐI CẢNH VĂN BẢN: LỤC HÀO PHONG THỦY DỰ TRẮC HỌC
**Nguyên tác:** Vương Hổ Ứng & Lưu Thiết Khanh | **Dịch giả:** Trần Phương | **Ngôn ngữ xuất lực:** vi (Tiếng Việt) | **Lĩnh vực:** Lục Hào Dự Trắc Học (luc_hao) - Chuyên khảo Phong Thủy Toàn Tập

## 1. Luận điểm Cốt lõi (Core Thesis)
Lục Hào Phong Thủy Dự Trắc Học là sự kết hợp nhuần nhuyễn giữa Chu Dịch học và Phong Thủy học cổ truyền (Hình pháp kết hợp Khí pháp). Thông qua hệ thống đa tầng gồm Dụng thần, Hào vị (từ móng đến nóc), Lục thân, Lục thần (Thanh Long đến Huyền Vũ), Bát quái, Ngũ hành, 12 Trạng thái sinh diệt và thần sát, phương pháp này cho phép chẩn đoán chính xác thực trạng địa khí, kiến trúc, bố cục trong ngoài của nhà ở (Dương Trạch), mồ mả (Âm Trạch) và nơi kinh doanh (Thương Nghiệp), đồng thời đưa ra các giải pháp hóa giải, cải tạo phong thủy thực chứng đạt hiệu quả cao mà không cần trực tiếp khảo sát hiện trường.

## 2. Hệ thống Thuật ngữ và Phương pháp Luận
- **Dụng thần & Hào vị:** Hào Thế (gia chủ), Hào 2 (trạch hào - ngôi nhà), Phụ Mẫu (kiến trúc, nhà cửa, mồ mả), Thê Tài (tiền bạc, phòng bếp), Quan Quỷ (sát khí, bệnh tật, thần phật, âm hồn), Tử Tôn (đường đi, giếng nước, sự thông thoáng), Huynh Đệ (cửa nẻo, vách tường, hao tổn tài sản).
- **Phân bố Hào vị Trạch xá:** Hào 1 (nền móng, giếng nước) -> Hào 2 (phòng bếp, không gian sống chính, trạch hào) -> Hào 3 (cửa trong, giường ngủ) -> Hào 4 (cửa ngoài, cổng ngõ) -> Hào 5 (đường lộ lớn, chủ nhà) -> Hào 6 (tường bao, mái nhà, không gian lân cận phía trên).
- **Lục thần Phụ họa:** Thanh Long (mới mẻ, tươi mát, cây cối, phương Đông); Chu Tước (bếp lửa, âm thanh ồn ào, tiếng hót, phương Nam); Câu Trần (nhà cũ, tu bổ, đất đai, bế tắc); Đằng Xà (dị vật, sâu bọ, uốn lượn, kinh hãi); Bạch Hổ (đường lớn, xung sát, gãy nứt, thương tích, phương Tây); Huyền Vũ (rãnh nước bẩn, ẩm mốc, ám muội, phương Bắc).
- **Quy luật Động biến:** Lục hợp chủ tàng phong tụ khí, kiên cố, nhà lầu nhiều tầng; Lục xung chủ tán khí, xung xạ hung hiểm; Nguyệt phá chủ mục nát, rạn nứt nứt tường; Không vong chủ trống rỗng, hư hao, thiếu ánh sáng; Phản phục ngâm chủ phản phúc, rên rỉ, cải tạo liên miên.

## 3. Tổng quan Hệ thống 6 Chương
- **Chương 1:** Ý nghĩa của Lục Hào dự đoán phong thủy (tính khoa học, từ trường địa cầu, năng động chủ quan, khắc phục điểm yếu của phong thủy thụ động).
- **Chương 2:** Kiến thức lục hào căn bản ứng dụng phong thủy (16 chuyên đề: Dụng thần, Hào vị, Lục thân, Lục thần, Bát quái, Ngũ hành, Hỗ hóa, Lưỡng hiện, Phục tàng, Tiến thoái, Nguyệt phá, Không vong, Hợp xung, Phản phục ngâm, Du quy hồn, 12 Trạng thái sinh diệt).
- **Chương 3:** Phán đoán chi tiết hoàn cảnh ngoại vi (8 chuyên mục: Đường đi, Cầu cống, Sông ngòi, Vật kiến trúc xung quanh, Núi non, Hoa cỏ cây cối, Đá, Tổng luận phong thủy).
- **Chương 4:** Dự đoán phong thủy Dương Trạch nơi ở (12 bộ phận nhà ở: Nền nhà, Giếng nước, Hàng xóm, Sân, Phòng bếp, Phòng ngủ, Bàn thờ, Cửa, Tường, Mái nhà, Giường, Nhà vệ sinh; kèm 116 quẻ dịch thực chiến chi tiết).
- **Chương 5:** Dự đoán phong thủy Âm Trạch mồ mả (10 tiêu chí: Long mạch, Sa, Thủy, Minh đường, Long Hổ, Huyệt vị, Phần mộ, Thủy khẩu, Án sơn, Đắc địa; cùng 4 án lệ cổ đại và 21 quẻ dịch âm trạch thời nay).
- **Chương 6:** Dự đoán phong thủy Thương Nghiệp (4 hạng mục: Cửa hàng, Quầy thu ngân, Khách hàng, Người làm thuê; cùng 25 quẻ dịch kinh doanh buôn bán).
"""

skeleton = {
    "doc_slug": "luc_hao_phong_thuy_du_trac_hoc",
    "doc_title": "Lục Hào Phong Thủy Dự Trắc Học",
    "doc_type": "book",
    "domain": "luc_hao",
    "max_heading_level": 5,
    "sections": sections,
    "figure_ids": figure_ids,
    "drop_figures": drop_figures,
    "exercises": all_exercises,
    "rule_index": rule_index,
    "global_lexicon": global_lexicon,
    "global_context_pack": global_context_pack
}

out_skel_path = os.path.join(OUTPUT_DIR, "skeleton.json")
with open(out_skel_path, "w", encoding="utf-8") as f:
    json.dump(skeleton, f, indent=2, ensure_ascii=False)

print(f"Wrote skeleton.json to {out_skel_path}")
