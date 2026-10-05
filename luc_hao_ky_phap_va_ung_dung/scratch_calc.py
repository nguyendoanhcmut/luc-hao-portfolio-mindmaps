
import json, tiktoken

enc = tiktoken.get_encoding('cl100k_base')

# Skeleton
skeleton = [
    {
      'level': 2,
      'title': 'Trang bìa',
      'start_page': 1,
      'end_page': 1,
      'word_count': 17,
      'has_exercises': False,
      'figures': [],
      'children': []
    },
    {
      'level': 2,
      'title': 'Mục lục',
      'start_page': 2,
      'end_page': 2,
      'word_count': 78,
      'has_exercises': False,
      'figures': [],
      'children': []
    },
    {
      'level': 2,
      'title': 'Lời dịch giả: Lý và Tượng trong Lục Hào',
      'start_page': 3,
      'end_page': 4,
      'word_count': 667,
      'has_exercises': False,
      'figures': [],
      'children': [
        {
          'level': 3,
          'title': 'Phân biệt Lý và Tượng trong Luận đoán Bốc Dịch',
          'figures': []
        },
        {
          'level': 3,
          'title': 'Phương pháp Dự đoán Nâng cao của Vương Hổ Ứng',
          'figures': []
        }
      ]
    },
    {
      'level': 2,
      'title': 'Chương 1: Trường sinh mười hai cung bí pháp',
      'start_page': 5,
      'end_page': 8,
      'word_count': 1904,
      'has_exercises': False,
      'figures': [],
      'children': [
        {
          'level': 3,
          'title': 'Ý nghĩa và Tượng ý 12 Cung Trường Sinh',
          'figures': []
        },
        {
          'level': 3,
          'title': 'Ví dụ: Đoán Thai sản (Thiên Trạch Lý biến Thiên Thủy Tụng)',
          'figures': [{'id': 'fig_01', 'file_name': 'assets/page_0007_img_01.png', 'caption': 'Bảng quẻ Thiên Trạch Lý biến Thiên Thủy Tụng'}]
        }
      ]
    },
    {
      'level': 2,
      'title': 'Chương 2: Bí mật của Phi – Phục',
      'start_page': 9,
      'end_page': 11,
      'word_count': 1182,
      'has_exercises': False,
      'figures': [],
      'children': [
        {
          'level': 3,
          'title': 'Nguyên lý Hoạt động của Phi thần và Phục thần',
          'figures': []
        },
        {
          'level': 3,
          'title': 'Ví dụ: Tìm Tung tích Chồng (Hỏa Sơn Lữ biến Bát Thuần Cấn)',
          'figures': [{'id': 'fig_02', 'file_name': 'assets/page_0010_img_01.png', 'caption': 'Bảng quẻ Hỏa Sơn Lữ biến Bát Thuần Cấn'}]
        }
      ]
    },
    {
      'level': 2,
      'title': 'Chương 3: Không vong hoạt dụng',
      'start_page': 12,
      'end_page': 13,
      'word_count': 764,
      'has_exercises': False,
      'figures': [],
      'children': [
        {
          'level': 3,
          'title': 'Biện chứng Chân Không và Giả Không',
          'figures': []
        },
        {
          'level': 3,
          'title': 'Ví dụ: Đoán Cầu hôn Tình cảm (Sơn Thủy Mông biến Thiên Phong Cấu)',
          'figures': [{'id': 'fig_03', 'file_name': 'assets/page_0012_img_01.png', 'caption': 'Sơ đồ quẻ Sơn Thủy Mông biến Thiên Phong Cấu'}]
        }
      ]
    },
    {
      'level': 2,
      'title': 'Chương 4: Quẻ do ai đến gieo!',
      'start_page': 14,
      'end_page': 23,
      'word_count': 5273,
      'has_exercises': False,
      'figures': [],
      'children': [
        {
          'level': 3,
          'title': 'Trường Thông tin Vũ trụ và Phê phán Mật chú',
          'figures': []
        },
        {
          'level': 3,
          'title': 'Ví dụ 1: Gieo Quẻ qua Điện thoại (Thiên Trạch Lý)',
          'figures': [{'id': 'fig_04', 'file_name': 'assets/page_0016_img_01.png', 'caption': 'Bảng quẻ Lục Hào: Thiên Trạch Lý'}]
        },
        {
          'level': 3,
          'title': 'Ví dụ 2: Dự đoán Sư gieo thay Thân chủ (Phong Lôi Ích biến Thủy Trạch Tiết)',
          'figures': [{'id': 'fig_05', 'file_name': 'assets/page_0018_img_01.png', 'caption': 'Sơ đồ quẻ Phong Lôi Ích biến Thủy Trạch Tiết'}]
        },
        {
          'level': 3,
          'title': 'Ví dụ 3: Bạn bè gieo giùm Đoán Hôn nhân (Thiên Phong Cấu biến Phong Địa Quán)',
          'figures': [{'id': 'fig_06', 'file_name': 'assets/page_0019_img_01.png', 'caption': 'Sơ đồ quẻ Thiên Phong Cấu biến Phong Địa Quán'}]
        },
        {
          'level': 3,
          'title': 'Ví dụ 4: Xem Tivi Khởi quẻ Bệnh Thủ tướng Nhật (Thiên Hỏa Đồng Nhân biến Hỏa Phong Đỉnh)',
          'figures': [{'id': 'fig_07', 'file_name': 'assets/page_0022_img_01.png', 'caption': 'Sơ đồ quẻ Thiên Hỏa Đồng Nhân biến Hỏa Phong Đỉnh'}]
        }
      ]
    },
    {
      'level': 2,
      'title': 'Chương 5: Quẻ gián đoán mộng',
      'start_page': 24,
      'end_page': 25,
      'word_count': 1158,
      'has_exercises': False,
      'figures': [],
      'children': [
        {
          'level': 3,
          'title': 'Cơ chế Giải mộng qua Hào vị Giường nằm và Đằng Xà',
          'figures': []
        },
        {
          'level': 3,
          'title': 'Ví dụ: Giải Mộng Ác mộng Đánh nhau (Phong Trạch Trung Phu biến Bát Thuần Tốn)',
          'figures': [{'id': 'fig_08', 'file_name': 'assets/page_0024_img_01.png', 'caption': 'Sơ đồ quẻ Phong Trạch Trung Phu biến Bát Thuần Tốn'}]
        }
      ]
    },
    {
      'level': 2,
      'title': 'Chương 6: Lục hào xạ phúc',
      'start_page': 26,
      'end_page': 27,
      'word_count': 1316,
      'has_exercises': False,
      'figures': [],
      'children': [
        {
          'level': 3,
          'title': 'Kỹ pháp Đoán Vật Ẩn tàng qua Tượng Quái',
          'figures': []
        },
        {
          'level': 3,
          'title': 'Ví dụ 1: Đoán Vật trong Túi (Lôi Thủy Giải biến Trạch Thủy Khốn)',
          'figures': [{'id': 'fig_09', 'file_name': 'assets/page_0026_img_01.png', 'caption': 'Bảng quẻ Lôi Thủy Giải biến Trạch Thủy Khốn'}]
        },
        {
          'level': 3,
          'title': 'Ví dụ 2: Đoán Vật trong Bình Nước (Hỏa Trạch Khuê biến Hỏa Lôi Phệ Hạp)',
          'figures': [{'id': 'fig_10', 'file_name': 'assets/page_0027_img_01.png', 'caption': 'Sơ đồ quẻ Hỏa Trạch Khuê biến Hỏa Lôi Phệ Hạp'}]
        }
      ]
    },
    {
      'level': 2,
      'title': 'Chương 7: Lục hào đoán tướng mạo',
      'start_page': 28,
      'end_page': 30,
      'word_count': 1528,
      'has_exercises': False,
      'figures': [],
      'children': [
        {
          'level': 3,
          'title': 'Hệ thống Hào vị và Lục Thần Đoán Hình thể',
          'figures': []
        },
        {
          'level': 3,
          'title': 'Ví dụ 1: Đoán Tướng mạo Mắt Cận và Sẹo Mũi (Thủy Trạch Tiết)',
          'figures': [{'id': 'fig_11', 'file_name': 'assets/page_0028_img_01.png', 'caption': 'Sơ đồ quẻ Thủy Trạch Tiết'}]
        },
        {
          'level': 3,
          'title': 'Ví dụ 2: Đoán Vóc dáng Ngực Mông Dáng đi (Phong Hỏa Gia Nhân biến Phong Địa Quán)',
          'figures': [{'id': 'fig_12', 'file_name': 'assets/page_0029_img_01.png', 'caption': 'Sơ đồ quẻ Phong Hỏa Gia Nhân biến Phong Địa Quán'}]
        }
      ]
    },
    {
      'level': 2,
      'title': 'Chương 8: Ngàn vạn không thể bổ',
      'start_page': 31,
      'end_page': 32,
      'word_count': 927,
      'has_exercises': False,
      'figures': [],
      'children': [
        {
          'level': 3,
          'title': 'Biện chứng Nội nhiệt Thực chứng và Cấm kỵ Thuốc Bổ',
          'figures': []
        },
        {
          'level': 3,
          'title': 'Ví dụ: Đoán Bệnh Chảy máu Mũi (Thủy Thiên Nhu biến Địa Lôi Phục)',
          'figures': [{'id': 'fig_13', 'file_name': 'assets/page_0031_img_01.png', 'caption': 'Sơ đồ quẻ Thủy Thiên Nhu biến Địa Lôi Phục'}]
        }
      ]
    },
    {
      'level': 2,
      'title': 'Chương 9: Giếng nước nghiên cứu cùng nghiệm chứng luận',
      'start_page': 33,
      'end_page': 36,
      'word_count': 1968,
      'has_exercises': False,
      'figures': [],
      'children': [
        {
          'level': 3,
          'title': 'Khảo cứu và Đính chính Sai lầm Cổ thư về Giếng Nước',
          'figures': []
        },
        {
          'level': 3,
          'title': 'Ví dụ: Tìm Dê Chết Ven Giếng Cạn (Thiên Sơn Độn biến Thiên Địa Bĩ)',
          'figures': [{'id': 'fig_14', 'file_name': 'assets/page_0035_img_01.png', 'caption': 'Sơ đồ quẻ Thiên Sơn Độn biến Thiên Địa Bĩ'}]
        }
      ]
    },
    {
      'level': 2,
      'title': 'Chương 10: Con đường trong Lục hào',
      'start_page': 37,
      'end_page': 40,
      'word_count': 1823,
      'has_exercises': False,
      'figures': [],
      'children': [
        {
          'level': 3,
          'title': 'Kỹ pháp Nhận diện Đường sá qua Bạch Hổ',
          'figures': []
        },
        {
          'level': 3,
          'title': 'Ví dụ 1: Mở đường Phá dỡ Nhà và Hỏa hoạn (Lôi Thiên Đại Tráng)',
          'figures': [{'id': 'fig_15', 'file_name': 'assets/page_0037_img_01.png', 'caption': 'Sơ đồ quẻ Lôi Thiên Đại Tráng'}]
        },
        {
          'level': 3,
          'title': 'Ví dụ 2: Đoán Ngã Gãy Xương Chân trên Đường (Trạch Hỏa Cách biến Trạch Thiên Quải)',
          'figures': [{'id': 'fig_16', 'file_name': 'assets/page_0039_img_01.png', 'caption': 'Sơ đồ quẻ Trạch Hỏa Cách biến Trạch Thiên Quải'}]
        }
      ]
    },
    {
      'level': 2,
      'title': 'Chương 11: Đoán bệnh tất lấy Quan quỷ là bệnh sao?',
      'start_page': 41,
      'end_page': 44,
      'word_count': 1786,
      'has_exercises': False,
      'figures': [],
      'children': [
        {
          'level': 3,
          'title': 'Nguyên lý Chẩn bệnh Toàn diện Vượt qua Quan Quỷ',
          'figures': []
        },
        {
          'level': 3,
          'title': 'Ví dụ 1: U Vòm Họng và Suy Thận (Sơn Thủy Mông biến Địa Thủy Sư)',
          'figures': [{'id': 'fig_17', 'file_name': 'assets/page_0042_img_01.png', 'caption': 'Sơ đồ quẻ Sơn Thủy Mông biến Địa Thủy Sư'}]
        },
        {
          'level': 3,
          'title': 'Ví dụ 2: Bệnh Tắc Ruột và Phẫu thuật (Lôi Thiên Đại Tráng biến Bát Thuần Càn)',
          'figures': [{'id': 'fig_18', 'file_name': 'assets/page_0043_img_01.png', 'caption': 'Sơ đồ quẻ Lôi Thiên Đại Tráng biến Bát Thuần Càn'}]
        }
      ]
    }
]

print('Skeleton tokens (indented):', len(enc.encode(json.dumps(skeleton, ensure_ascii=False, indent=2))))
print('Skeleton tokens (compact):', len(enc.encode(json.dumps(skeleton, ensure_ascii=False))))
