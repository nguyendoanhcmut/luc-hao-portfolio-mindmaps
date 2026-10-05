import os
import sys
import re
import json
import unicodedata
import pymupdf

pdf_path = r"C:/Users/Admin/Downloads/drive-download-20260908T061604Z-1-001/VƯƠNG HỔ ỨNG - TĂNG SAN BỐC DỊCH BÌNH THÍCH.pdf"
output_dir = r"C:/Users/Admin/.gemini/antigravity/scratch/luc_hao_portfolio_ocr/tang_san_boc_dich_binh_thich"
results_dir = os.path.join(output_dir, "page_results")
os.makedirs(results_dir, exist_ok=True)

doc = pymupdf.open(pdf_path)
total_pages = len(doc)
print(f"Total pages in doc: {total_pages}")

def normalize_text(text):
    return unicodedata.normalize('NFC', text)

def get_page_image_rects(page):
    rects = []
    w, h = page.rect.width, page.rect.height
    for img_info in page.get_images():
        xref = img_info[0]
        for r in page.get_image_rects(xref):
            rects.append(r)
    return rects

def detect_que_name_and_bounds(page, text_blocks):
    w, h = page.rect.height, page.rect.width # Note: page.rect.width, page.rect.height
    pw, ph = page.rect.width, page.rect.height
    img_rects = get_page_image_rects(page)
    
    # Check if this page has hexagram elements
    has_luc_than = False
    luc_than_keywords = ['Chu Tước', 'Thanh Long', 'Huyền Vũ', 'Bạch Hổ', 'Đằng Xà', 'Câu Trần']
    kinship_keywords = ['Huynh Đệ', 'Tử Tôn', 'Thê Tài', 'Quan Quỷ', 'Phụ Mẫu']
    
    full_text = page.get_text()
    if any(k in full_text for k in luc_than_keywords) or any(k in full_text for k in kinship_keywords):
        has_luc_than = True
        
    if not img_rects and not has_luc_than:
        return None, []
        
    images = []
    if img_rects:
        min_x = min(r.x0 for r in img_rects)
        max_x = max(r.x1 for r in img_rects)
        min_y = min(r.y0 for r in img_rects)
        max_y = max(r.y1 for r in img_rects)
        
        # Look for quẻ title near top of diagram
        que_title = "Quẻ Lục Hào"
        for b in text_blocks:
            t = b[4].strip()
            # If block is above or within diagram region and short
            if b[3] <= min_y + 30 and b[1] >= min_y - 60 and len(t) < 50:
                clean_t = " ".join(t.split())
                if clean_t and not clean_t.isdigit():
                    que_title = clean_t
                    break
                    
        # Expand box to include quẻ labels and names
        ymin = max(0, int((min_y - 25) / ph * 1000))
        xmin = max(0, int((min_x - 30) / pw * 1000))
        ymax = min(1000, int((max_y + 25) / ph * 1000))
        xmax = min(1000, int((max_x + 30) / pw * 1000))
        
        # If the diagram is wide (two hexagrams side by side), ensure good x coverage
        if xmax - xmin > 200:
            xmin = max(20, min(xmin, 60))
            xmax = min(980, max(xmax, 940))
            
        images.append({
            "filename": f"page_{page.number + 1:04d}_img_01.png",
            "box_2d": [ymin, xmin, ymax, xmax],
            "caption": f"Sơ đồ quẻ {que_title}" if que_title != "Quẻ Lục Hào" else "Sơ đồ quẻ Lục Hào"
        })
    return images

# Test run on page 45
p45 = doc[44]
blocks_45 = p45.get_text('blocks')
imgs_45 = detect_que_name_and_bounds(p45, blocks_45)
print("Page 45 detected images:", imgs_45)
