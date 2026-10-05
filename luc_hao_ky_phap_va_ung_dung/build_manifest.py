import json
import os
import tiktoken

manifest = {
  "doc_slug": "luc_hao_ky_phap_va_ung_dung",
  "doc_title": "Lục Hào Kỹ Pháp và Ứng Dụng",
  "total_pages": 44,
  "total_estimated_tokens": 42838,
  "master_skeleton": [
    {
      "level": 2,
      "title": "Trang bìa",
      "start_page": 1,
      "end_page": 1,
      "word_count": 17,
      "has_exercises": False,
      "figures": [],
      "children": []
    },
    {
      "level": 2,
      "title": "Mục lục",
      "start_page": 2,
      "end_page": 2,
      "word_count": 78,
      "has_exercises": False,
      "figures": [],
      "children": []
    },
    {
      "level": 2,
      "title": "Lời dịch giả: Lý và Tượng trong Lục Hào",
      "start_page": 3,
      "end_page": 4,
      "word_count": 667,
      "has_exercises": False,
      "figures": [],
      "children": [
        {
          "level": 3,
          "title": "Lý và Tượng trong Luận đoán Bốc Dịch",
          "figures": []
        },
        {
          "level": 3,
          "title": "Kỹ pháp Đoán Tượng của Vương Hổ Ứng",
          "figures": []
        }
      ]
    },
    {
      "level": 2,
      "title": "Chương 1: Trường sinh mười hai cung bí pháp",
      "start_page": 5,
      "end_page": 8,
      "word_count": 1904,
      "has_exercises": False,
      "figures": [],
      "children": [
        {
          "level": 3,
          "title": "Tượng ý 12 Cung Trường Sinh",
          "figures": []
        },
        {
          "level": 3,
          "title": "Ví dụ: Thai sản (Thiên Trạch Lý - Thiên Thủy Tụng)",
          "figures": [
            {
              "id": "fig_01",
              "file_name": "assets/page_0007_img_01.png",
              "caption": "Bảng quẻ Thiên Trạch Lý biến Thiên Thủy Tụng"
            }
          ]
        }
      ]
    },
    {
      "level": 2,
      "title": "Chương 2: Bí mật của Phi – Phục",
      "start_page": 9,
      "end_page": 11,
      "word_count": 1182,
      "has_exercises": False,
      "figures": [],
      "children": [
        {
          "level": 3,
          "title": "Nguyên lý Phi thần và Phục thần",
          "figures": []
        },
        {
          "level": 3,
          "title": "Ví dụ: Tìm Tung tích Chồng (Hỏa Sơn Lữ - Bát Thuần Cấn)",
          "figures": [
            {
              "id": "fig_02",
              "file_name": "assets/page_0010_img_01.png",
              "caption": "Bảng quẻ Hỏa Sơn Lữ biến Bát Thuần Cấn"
            }
          ]
        }
      ]
    },
    {
      "level": 2,
      "title": "Chương 3: Không vong hoạt dụng",
      "start_page": 12,
      "end_page": 13,
      "word_count": 764,
      "has_exercises": False,
      "figures": [],
      "children": [
        {
          "level": 3,
          "title": "Biện chứng Chân Không và Giả Không",
          "figures": []
        },
        {
          "level": 3,
          "title": "Ví dụ: Đoán Cầu hôn (Sơn Thủy Mông - Thiên Phong Cấu)",
          "figures": [
            {
              "id": "fig_03",
              "file_name": "assets/page_0012_img_01.png",
              "caption": "Sơ đồ quẻ Sơn Thủy Mông biến Thiên Phong Cấu"
            }
          ]
        }
      ]
    },
    {
      "level": 2,
      "title": "Chương 4: Quẻ do ai đến gieo!",
      "start_page": 14,
      "end_page": 23,
      "word_count": 5273,
      "has_exercises": False,
      "figures": [],
      "children": [
        {
          "level": 3,
          "title": "Trường Thông tin Vũ trụ và Phê phán Mật chú",
          "figures": []
        },
        {
          "level": 3,
          "title": "Ví dụ 1: Gieo Quẻ qua Điện thoại (Thiên Trạch Lý)",
          "figures": [
            {
              "id": "fig_04",
              "file_name": "assets/page_0016_img_01.png",
              "caption": "Bảng quẻ Lục Hào: Thiên Trạch Lý"
            }
          ]
        },
        {
          "level": 3,
          "title": "Ví dụ 2: Thầy gieo thay Thân chủ (Phong Lôi Ích - Thủy Trạch Tiết)",
          "figures": [
            {
              "id": "fig_05",
              "file_name": "assets/page_0018_img_01.png",
              "caption": "Sơ đồ quẻ Phong Lôi Ích biến Thủy Trạch Tiết"
            }
          ]
        },
        {
          "level": 3,
          "title": "Ví dụ 3: Bạn gieo giùm Đoán Hôn nhân (Thiên Phong Cấu - Phong Địa Quán)",
          "figures": [
            {
              "id": "fig_06",
              "file_name": "assets/page_0019_img_01.png",
              "caption": "Sơ đồ quẻ Thiên Phong Cấu biến Phong Địa Quán"
            }
          ]
        },
        {
          "level": 3,
          "title": "Ví dụ 4: Xem Tivi Đoán Bệnh Thủ tướng Nhật (Đồng Nhân - Đỉnh)",
          "figures": [
            {
              "id": "fig_07",
              "file_name": "assets/page_0022_img_01.png",
              "caption": "Sơ đồ quẻ Thiên Hỏa Đồng Nhân biến Hỏa Phong Đỉnh"
            }
          ]
        }
      ]
    },
    {
      "level": 2,
      "title": "Chương 5: Quẻ gián đoán mộng",
      "start_page": 24,
      "end_page": 25,
      "word_count": 1158,
      "has_exercises": False,
      "figures": [],
      "children": [
        {
          "level": 3,
          "title": "Cơ chế Giải mộng qua Hào vị và Đằng Xà",
          "figures": []
        },
        {
          "level": 3,
          "title": "Ví dụ: Giải Ác mộng Đánh nhau (Trung Phu - Tốn)",
          "figures": [
            {
              "id": "fig_08",
              "file_name": "assets/page_0024_img_01.png",
              "caption": "Sơ đồ quẻ Phong Trạch Trung Phu biến Bát Thuần Tốn"
            }
          ]
        }
      ]
    },
    {
      "level": 2,
      "title": "Chương 6: Lục hào xạ phúc",
      "start_page": 26,
      "end_page": 27,
      "word_count": 1316,
      "has_exercises": False,
      "figures": [],
      "children": [
        {
          "level": 3,
          "title": "Kỹ pháp Đoán Vật Ẩn tàng qua Tượng Quái",
          "figures": []
        },
        {
          "level": 3,
          "title": "Ví dụ 1: Đoán Vật trong Túi (Giải - Khốn)",
          "figures": [
            {
              "id": "fig_09",
              "file_name": "assets/page_0026_img_01.png",
              "caption": "Bảng quẻ Lôi Thủy Giải biến Trạch Thủy Khốn"
            }
          ]
        },
        {
          "level": 3,
          "title": "Ví dụ 2: Đoán Vật trong Bình Nước (Khuê - Phệ Hạp)",
          "figures": [
            {
              "id": "fig_10",
              "file_name": "assets/page_0027_img_01.png",
              "caption": "Sơ đồ quẻ Hỏa Trạch Khuê biến Hỏa Lôi Phệ Hạp"
            }
          ]
        }
      ]
    },
    {
      "level": 2,
      "title": "Chương 7: Lục hào đoán tướng mạo",
      "start_page": 28,
      "end_page": 30,
      "word_count": 1528,
      "has_exercises": False,
      "figures": [],
      "children": [
        {
          "level": 3,
          "title": "Phân bổ Hào vị và Lục Thần Đoán Hình thể",
          "figures": []
        },
        {
          "level": 3,
          "title": "Ví dụ 1: Đoán Mặt Cận và Sẹo Mũi (Thủy Trạch Tiết)",
          "figures": [
            {
              "id": "fig_11",
              "file_name": "assets/page_0028_img_01.png",
              "caption": "Sơ đồ quẻ Thủy Trạch Tiết"
            }
          ]
        },
        {
          "level": 3,
          "title": "Ví dụ 2: Đoán Vóc dáng Ngực Mông Dáng đi (Gia Nhân - Quán)",
          "figures": [
            {
              "id": "fig_12",
              "file_name": "assets/page_0029_img_01.png",
              "caption": "Sơ đồ quẻ Phong Hỏa Gia Nhân biến Phong Địa Quán"
            }
          ]
        }
      ]
    },
    {
      "level": 2,
      "title": "Chương 8: Ngàn vạn không thể bổ",
      "start_page": 31,
      "end_page": 32,
      "word_count": 927,
      "has_exercises": False,
      "figures": [],
      "children": [
        {
          "level": 3,
          "title": "Nội nhiệt Thực chứng và Cấm kỵ Thuốc Bổ",
          "figures": []
        },
        {
          "level": 3,
          "title": "Ví dụ: Đoán Bệnh Chảy máu Mũi (Nhu - Phục)",
          "figures": [
            {
              "id": "fig_13",
              "file_name": "assets/page_0031_img_01.png",
              "caption": "Sơ đồ quẻ Thủy Thiên Nhu biến Địa Lôi Phục"
            }
          ]
        }
      ]
    },
    {
      "level": 2,
      "title": "Chương 9: Giếng nước nghiên cứu cùng nghiệm chứng luận",
      "start_page": 33,
      "end_page": 36,
      "word_count": 1968,
      "has_exercises": False,
      "figures": [],
      "children": [
        {
          "level": 3,
          "title": "Khảo cứu và Đính chính Cổ thư về Giếng Nước",
          "figures": []
        },
        {
          "level": 3,
          "title": "Ví dụ: Tìm Dê Chết Ven Giếng Cạn (Độn - Bĩ)",
          "figures": [
            {
              "id": "fig_14",
              "file_name": "assets/page_0035_img_01.png",
              "caption": "Sơ đồ quẻ Thiên Sơn Độn biến Thiên Địa Bĩ"
            }
          ]
        }
      ]
    },
    {
      "level": 2,
      "title": "Chương 10: Con đường trong Lục hào",
      "start_page": 37,
      "end_page": 40,
      "word_count": 1823,
      "has_exercises": False,
      "figures": [],
      "children": [
        {
          "level": 3,
          "title": "Kỹ pháp Nhận diện Đường sá qua Bạch Hổ",
          "figures": []
        },
        {
          "level": 3,
          "title": "Ví dụ 1: Mở đường Phá dỡ Nhà (Lôi Thiên Đại Tráng)",
          "figures": [
            {
              "id": "fig_15",
              "file_name": "assets/page_0037_img_01.png",
              "caption": "Sơ đồ quẻ Lôi Thiên Đại Tráng"
            }
          ]
        },
        {
          "level": 3,
          "title": "Ví dụ 2: Đoán Ngã Gãy Xương Chân (Cách - Quải)",
          "figures": [
            {
              "id": "fig_16",
              "file_name": "assets/page_0039_img_01.png",
              "caption": "Sơ đồ quẻ Trạch Hỏa Cách biến Trạch Thiên Quải"
            }
          ]
        }
      ]
    },
    {
      "level": 2,
      "title": "Chương 11: Đoán bệnh tất lấy Quan quỷ là bệnh sao?",
      "start_page": 41,
      "end_page": 44,
      "word_count": 1786,
      "has_exercises": False,
      "figures": [],
      "children": [
        {
          "level": 3,
          "title": "Chẩn bệnh Toàn diện Vượt qua Quan Quỷ",
          "figures": []
        },
        {
          "level": 3,
          "title": "Ví dụ 1: U Vòm Họng và Suy Thận (Mông - Sư)",
          "figures": [
            {
              "id": "fig_17",
              "file_name": "assets/page_0042_img_01.png",
              "caption": "Sơ đồ quẻ Sơn Thủy Mông biến Địa Thủy Sư"
            }
          ]
        },
        {
          "level": 3,
          "title": "Ví dụ 2: Bệnh Tắc Ruột và Phẫu thuật (Đại Tráng - Càn)",
          "figures": [
            {
              "id": "fig_18",
              "file_name": "assets/page_0043_img_01.png",
              "caption": "Sơ đồ quẻ Lôi Thiên Đại Tráng biến Bát Thuần Càn"
            }
          ]
        }
      ]
    }
  ],
  "global_lexicon": {
    "core_thesis": "Lục Hào Kỹ Pháp và Ứng Dụng kết hợp Lý (ngũ hành sinh khắc) và Tượng (hình ảnh trực quan, hào vị cơ thể, phương vị, vật thể). Công trình xác nhận trường thông tin vũ trụ khách quan (không cần mật chú) và chuẩn hóa các kỹ pháp chuyên sâu: 12 cung trường sinh, phi phục thần, không vong, giải mộng, xạ phúc, đoán tướng mạo, đường sá và chẩn bệnh toàn diện.",
    "key_terms": [
      {
        "term": "Lý và Tượng",
        "definition": "Lý là ngũ hành sinh khắc định cát hung; Tượng là hình ảnh trực quan, hào vị và lục thần định hình thái chi tiết và ứng kỳ."
      },
      {
        "term": "Trường sinh 12 cung",
        "definition": "12 trạng thái chu kỳ của địa chi (Trường sinh đến Dưỡng), định lượng sức sống và hình thái sự việc."
      },
      {
        "term": "Phi thần - Phục thần",
        "definition": "Phi thần là hào lộ diện trên quẻ; Phục thần là hào ẩn tàng mượn từ quẻ Bát thuần bản cung."
      },
      {
        "term": "Không vong hoạt dụng",
        "definition": "Phân biệt Chân không và Giả không, xác định thời điểm ứng nghiệm qua xung không hoặc thực không."
      },
      {
        "term": "Trường thông tin vũ trụ",
        "definition": "Nguyên lý bốc dịch phi nghi thức: quẻ phản ánh thông tin qua Dụng thần bất kể ai gieo quẻ."
      },
      {
        "term": "Xạ phúc",
        "definition": "Thuật đoán đồ vật ẩn giấu trong hộp, túi hoặc tay qua hào vị, ngũ hành và lục thần."
      },
      {
        "term": "Đoán tướng mạo",
        "definition": "Kỹ pháp suy đoán diện mạo, vóc dáng và trang phục qua phân bổ hào vị từ 1 đến 6 kết hợp lục thần."
      },
      {
        "term": "Bạch Hổ chủ đạo lộ",
        "definition": "Kỹ pháp xác định Bạch Hổ lâm hào đại diện cho đường sá, lộ trình, ngã ba và tai nạn giao thông."
      },
      {
        "term": "Chẩn bệnh bất duy Quan quỷ",
        "definition": "Bệnh tật biểu hiện qua tạng phủ suy kiệt (suy, mộ, tuyệt) chứ không chỉ ở Quan quỷ; cấm kỵ thuốc bổ khi nhiệt thịnh."
      }
    ],
    "key_entities": [
      "Vương Hổ Ứng (Tác giả, bậc thầy Lục hào Dịch học)",
      "Đoạn Kiến Nghiệp (Chuyên gia Dịch học, bậc thầy Manh phái Mệnh lý)",
      "Vương Khai Vũ (Dịch hữu nghiên cứu và nghiệm chứng)",
      "Vương Dịch (Dịch hữu tham gia thực nghiệm)",
      "Hàn tiên sinh (Thân chủ ví dụ gieo quẻ từ xa)",
      "Thôi nữ sĩ (Thân chủ ví dụ tìm chồng qua Phi Phục)",
      "Obuchi Keizo (Thủ tướng Nhật Bản trong ví dụ đoán bệnh)"
    ]
  },
  "routing_table": [
    {
      "chunk_id": "chunk_01",
      "chapters": [
        "Trang bìa",
        "Mục lục",
        "Lời dịch giả: Lý và Tượng trong Lục Hào",
        "Chương 1: Trường sinh mười hai cung bí pháp",
        "Chương 2: Bí mật của Phi – Phục",
        "Chương 3: Không vong hoạt dụng"
      ],
      "start_page": 1,
      "end_page": 13,
      "estimated_tokens": 9996,
      "start_heading_level": 2,
      "depth_budget": 4,
      "assigned_figures": ["fig_01", "fig_02", "fig_03"]
    },
    {
      "chunk_id": "chunk_02",
      "chapters": [
        "Chương 4: Quẻ do ai đến gieo!"
      ],
      "start_page": 14,
      "end_page": 23,
      "estimated_tokens": 10951,
      "start_heading_level": 2,
      "depth_budget": 4,
      "assigned_figures": ["fig_04", "fig_05", "fig_06", "fig_07"]
    },
    {
      "chunk_id": "chunk_03",
      "chapters": [
        "Chương 5: Quẻ gián đoán mộng",
        "Chương 6: Lục hào xạ phúc",
        "Chương 7: Lục hào đoán tướng mạo"
      ],
      "start_page": 24,
      "end_page": 30,
      "estimated_tokens": 8113,
      "start_heading_level": 2,
      "depth_budget": 4,
      "assigned_figures": ["fig_08", "fig_09", "fig_10", "fig_11", "fig_12"]
    },
    {
      "chunk_id": "chunk_04",
      "chapters": [
        "Chương 8: Ngàn vạn không thể bổ",
        "Chương 9: Giếng nước nghiên cứu cùng nghiệm chứng luận",
        "Chương 10: Con đường trong Lục hào",
        "Chương 11: Đoán bệnh tất lấy Quan quỷ là bệnh sao?"
      ],
      "start_page": 31,
      "end_page": 44,
      "estimated_tokens": 13797,
      "start_heading_level": 2,
      "depth_budget": 4,
      "assigned_figures": ["fig_13", "fig_14", "fig_15", "fig_16", "fig_17", "fig_18"]
    }
  ],
  "global_context_pack": "This document is an advanced manual on Liu Yao divination by Master Wang Hu Ying.\nThe text teaches how to combine two primary elements: Li (principles) and Xiang (imagery).\nTraditional manuals focus on Li, which is five-element interaction.\nThis manual adds advanced methods that use Xiang, which shows shapes, body parts, directions, and timing.\n\nThe document contains eleven technical chapters:\n1. Twelve Life Stages: Defines symbolic meanings of the twelve stages from Birth to Nurture to determine physical states and events.\n2. Flying and Hidden Spirits: Explains interactions between visible and concealed lines, and conditions for hidden lines to emerge.\n3. Emptiness: Separates True Emptiness from False Emptiness, and identifies trigger dates when emptiness fills or receives a clash.\n4. Information Field and Divination Mechanics: Proves that anyone can cast hexagrams without rituals, prayers, or secret mantras.\n5. Dream Divination: Connects nightmares and sleep symptoms to line positions, the Flying Serpent spirit, and internal organ conditions.\n6. Guessing Hidden Objects (She Fu): Deduces hidden items in containers or pockets using trigrams, lines, and spirits.\n7. Physical Appearance: Maps lines 1 through 6 to human anatomy to identify face shapes, eyes, scars, breasts, and posture.\n8. Medical Rules on Tonics: Forbids tonic medications for excess internal fire conditions.\n9. Water Well Research: Corrects historical errors in ancient texts through empirical hexagram analysis.\n10. Roads in Liu Yao: Proves that the White Tiger spirit denotes roads, intersections, traffic events, and house demolition.\n11. Disease Diagnosis: Shows that illness appears in weakened organs and clashes, not only in the Guan Gui line."
}

out_path = "C:/Users/Admin/.gemini/antigravity/scratch/luc_hao_portfolio_ocr/luc_hao_ky_phap_va_ung_dung/luc_hao_ky_phap_va_ung_dung_scout_manifest.json"

with open(out_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

enc = tiktoken.get_encoding("cl100k_base")
with open(out_path, "r", encoding="utf-8") as f:
    content = f.read()

tokens = len(enc.encode(content))
print(f"Manifest written to: {out_path}")
print(f"File size: {len(content)} characters, {len(content.encode('utf-8'))} bytes")
print(f"Total cl100k_base tokens: {tokens}")
print(f"Guardrail satisfied (< 6000 tokens): {tokens < 6000}")
