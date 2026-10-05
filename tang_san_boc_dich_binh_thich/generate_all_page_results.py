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
print(f"Total pages: {total_pages}")

def normalize(text):
    return unicodedata.normalize('NFC', text)

def format_que_table(que_blocks, pw, ph):
    """
    Format a sequence of blocks containing a hexagram chart into a clean Markdown table.
    """
    # First block is usually title/quẻ names (e.g. "Ly \n Đại Hữu")
    # Remaining blocks are the 6 lines and footer
    return None

def process_page(doc, pnum):
    page = doc[pnum - 1]
    pw, ph = page.rect.width, page.rect.height
    
    # 1. Special Page 1 (Cover)
    if pnum == 1:
        md = normalize(
            "# TĂNG SAN BỐC DỊCH BÌNH THÍCH\n\n"
            "**Tác giả:** Dã Hạc lão nhân\n\n"
            "**Bình thích:** Vương Hổ Ứng\n\n"
            "**Giám định:** Lý Ngã Bình\n\n"
            "**Tăng san:** Lý Văn Huy (hiệu Giác Tử)\n\n"
            "**Hiệu đính:** Trần Văn Cát (hiệu Mậu Sinh) và Như Chi (hiệu Sơn Tú)\n"
        )
        images = [{
            "filename": "page_0001_img_01.png",
            "box_2d": [0, 0, 1000, 1000],
            "caption": "Bìa sách Tăng San Bốc Dịch Bình Thích"
        }]
        return {"page": pnum, "markdown": md, "images": images}
        
    # 2. Special Page 2 (Title page)
    if pnum == 2:
        raw_text = page.get_text().strip()
        lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
        md = normalize("# " + "\n\n".join(lines))
        return {"page": pnum, "markdown": md, "images": []}
        
    # 3. Special Page 3 (Blank page)
    if pnum == 3:
        return {"page": pnum, "markdown": normalize("*(Trang để trắng)*"), "images": []}
        
    # 4. Standard text & diagram extraction
    raw_blocks = page.get_text("blocks")
    
    # Filter out page numbers at margins
    clean_blocks = []
    for b in raw_blocks:
        t = b[4].strip()
        # Check if block is just digits at top (<10% h) or bottom (>85% h)
        if re.match(r"^\d+$", t) and (b[1] > ph * 0.82 or b[3] < ph * 0.10):
            continue
        clean_blocks.append(b)
        
    # Detect image clusters on this page
    rects = []
    for img in page.get_images():
        for r in page.get_image_rects(img[0]):
            rects.append(r)
            
    images = []
    if rects:
        rects.sort(key=lambda r: r.y0)
        clusters = []
        for r in rects:
            if not clusters or r.y0 - clusters[-1][-1].y1 > 35:
                clusters.append([r])
            else:
                clusters[-1].append(r)
                
        for idx, cluster in enumerate(clusters, 1):
            min_y = min(r.y0 for r in cluster)
            max_y = max(r.y1 for r in cluster)
            min_x = min(r.x0 for r in cluster)
            max_x = max(r.x1 for r in cluster)
            
            # Find quẻ title from text blocks near this cluster
            caption_title = "Quẻ Lục Hào"
            for b in clean_blocks:
                t = b[4].strip()
                # If block is above or within this diagram cluster
                if b[3] <= min_y + 35 and b[1] >= min_y - 70:
                    lines = [l.strip() for l in t.splitlines() if l.strip()]
                    if lines:
                        first_line = lines[0]
                        if len(first_line) < 60 and not re.match(r"^\d+$", first_line):
                            caption_title = " ".join(first_line.split())
                            break
                        
            # Normalize bounding box [ymin, xmin, ymax, xmax]
            ymin = max(0, int((min_y - 25) / ph * 1000))
            ymax = min(1000, int((max_y + 25) / ph * 1000))
            xmin = max(0, int((min_x - 35) / pw * 1000))
            xmax = min(1000, int((max_x + 35) / pw * 1000))
            
            # For wide hexagram charts, encompass the labels
            if xmax - xmin > 200:
                xmin = max(20, min(xmin, 50))
                xmax = min(980, max(xmax, 950))
                
            images.append({
                "filename": f"page_{pnum:04d}_img_{idx:02d}.png",
                "box_2d": [ymin, xmin, ymax, xmax],
                "caption": f"Sơ đồ quẻ {caption_title}" if caption_title != "Quẻ Lục Hào" else "Sơ đồ quẻ Lục Hào"
            })
            
    # Process text blocks into markdown
    md_parts = []
    i = 0
    while i < len(clean_blocks):
        b = clean_blocks[i]
        t = b[4].strip()
        if not t:
            i += 1
            continue
            
        # Check if block is a chapter heading
        m_ch = re.match(r"^CHƯƠNG\s+(\d+)[:.]?\s*(.*)$", t, re.IGNORECASE)
        if m_ch:
            ch_num = m_ch.group(1)
            ch_title = m_ch.group(2).strip()
            if ch_title:
                md_parts.append(f"# CHƯƠNG {ch_num}: {ch_title}\n")
            else:
                md_parts.append(f"# CHƯƠNG {ch_num}\n")
            i += 1
            continue
            
        # Check if block starts with Ví dụ
        if re.match(r"^Ví dụ(?:\s+\d+)?[:.]?", t):
            # Bold or h3
            lines = t.splitlines()
            first = lines[0].strip()
            rest = "\n".join(lines[1:]).strip()
            if rest:
                md_parts.append(f"### {first}\n\n{rest}\n")
            else:
                md_parts.append(f"### {first}\n")
            i += 1
            continue
            
        # Check if block starts with Tân bình thích
        if t.startswith("Tân bình thích:"):
            body = t[len("Tân bình thích:"):].strip()
            md_parts.append(f"**Tân bình thích:** {body}\n")
            i += 1
            continue
            
        # Check if block starts with Dã Hạc bàn rằng
        if t.startswith("Dã Hạc bàn rằng:"):
            body = t[len("Dã Hạc bàn rằng:"):].strip()
            md_parts.append(f"**Dã Hạc bàn rằng:** {body}\n")
            i += 1
            continue
            
        # Check if block starts with Lý Ngã Bình bàn rằng
        if t.startswith("Lý Ngã Bình bàn rằng:"):
            body = t[len("Lý Ngã Bình bàn rằng:"):].strip()
            md_parts.append(f"**Lý Ngã Bình bàn rằng:** {body}\n")
            i += 1
            continue
            
        # Check if block is a hexagram line block (contains Lục Thần or Lục Thân)
        has_luc_than = any(k in t for k in ['Chu Tước', 'Thanh Long', 'Huyền Vũ', 'Bạch Hổ', 'Đằng Xà', 'Câu Trần'])
        has_kinship = any(k in t for k in ['Huynh Đệ', 'Tử Tôn', 'Thê Tài', 'Quan Quỷ', 'Phụ Mẫu'])
        
        # If this block is part of a quẻ table layout
        if has_luc_than or (has_kinship and ('T\n' in t or 'Ư\n' in t or 'T ' in t or 'Ư ' in t)):
            # Format clean table row or table lines
            lines = [l.strip() for l in t.splitlines() if l.strip()]
            line_str = " | ".join(lines)
            md_parts.append(line_str)
            i += 1
            continue
            
        # Regular paragraph
        md_parts.append(t)
        i += 1
        
    full_md = "\n\n".join(md_parts).strip()
    return {
        "page": pnum,
        "markdown": normalize(full_md),
        "images": images
    }

print("Running batch extraction for all 476 pages...")
for p in range(1, total_pages + 1):
    res = process_page(doc, p)
    out_file = os.path.join(results_dir, f"page_{p:04d}.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=2)

print(f"Extraction complete! Generated {total_pages} JSON files in {results_dir}.")
