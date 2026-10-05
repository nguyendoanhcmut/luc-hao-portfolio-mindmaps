#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepare figures_manifest.json for books in luc_hao_portfolio_ocr."""

import os
import re
import json
import glob
from PIL import Image

IMG_MD_REGEX = re.compile(r"!\[(.*?)\]\((assets/[^)]+)\)")

def process_book(book_dir: str):
    book_dir = os.path.abspath(book_dir)
    book_slug = os.path.basename(book_dir)
    full_md_path = os.path.join(book_dir, f"{book_slug}_full.md")
    assets_dir = os.path.join(book_dir, "assets")
    
    if not os.path.exists(full_md_path):
        return
        
    with open(full_md_path, "r", encoding="utf-8-sig") as f:
        full_text = f.read()
        
    figures = []
    seen_files = set()
    
    # 1. Match from markdown image tags
    for match in IMG_MD_REGEX.finditer(full_text):
        caption = match.group(1).strip()
        rel_path = match.group(2).strip().replace("\\", "/")
        file_name = os.path.basename(rel_path)
        abs_path = os.path.join(book_dir, rel_path.replace("/", os.sep))
        
        if not os.path.exists(abs_path):
            continue
            
        page_num = 1
        page_m = re.search(r"page_(\d+)", file_name)
        if page_m:
            page_num = int(page_m.group(1))
            
        # Get dimensions
        w, h = 800, 600
        try:
            with Image.open(abs_path) as img:
                w, h = img.size
        except Exception:
            pass
            
        fig_id = f"fig_{len(figures) + 1:02d}"
        fig_num = str(len(figures) + 1)
        
        # Context mentions: extract sentence or paragraph around the figure
        start_pos = max(0, match.start() - 200)
        end_pos = min(len(full_text), match.end() + 200)
        context = full_text[start_pos:end_pos].strip()
        
        figures.append({
            "id": fig_id,
            "file_name": file_name,
            "rel_path": f"assets/{file_name}",
            "abs_path": abs_path,
            "page": page_num,
            "caption": caption if caption else f"Đồ hình trang {page_num}",
            "figure_number": fig_num,
            "width": w,
            "height": h,
            "context_mentions": [context]
        })
        seen_files.add(file_name)
        
    # 2. Add any remaining assets not directly in markdown
    if os.path.exists(assets_dir):
        for img_path in sorted(glob.glob(os.path.join(assets_dir, "*.*"))):
            fname = os.path.basename(img_path)
            if fname.lower().endswith((".png", ".jpg", ".jpeg")) and fname not in seen_files:
                page_num = 1
                page_m = re.search(r"page_(\d+)", fname)
                if page_m:
                    page_num = int(page_m.group(1))
                w, h = 800, 600
                try:
                    with Image.open(img_path) as img:
                        w, h = img.size
                except Exception:
                    pass
                fig_id = f"fig_{len(figures) + 1:02d}"
                figures.append({
                    "id": fig_id,
                    "file_name": fname,
                    "rel_path": f"assets/{fname}",
                    "abs_path": os.path.abspath(img_path),
                    "page": page_num,
                    "caption": f"Đồ hình bổ sung trang {page_num}",
                    "figure_number": str(len(figures) + 1),
                    "width": w,
                    "height": h,
                    "context_mentions": []
                })
                seen_files.add(fname)
                
    manifest = {
        "doc_source": book_dir,
        "total_figures": len(figures),
        "figures": figures
    }
    
    out_manifest = os.path.join(book_dir, "figures_manifest.json")
    with open(out_manifest, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        
    # Also write to branches/ if it exists or create branches/
    branches_dir = os.path.join(book_dir, "branches")
    os.makedirs(branches_dir, exist_ok=True)
    with open(os.path.join(branches_dir, "figures_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        
    print(f"[{book_slug}] Cataloged {len(figures)} figures.")

if __name__ == "__main__":
    import sys
    portfolio_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr"
    if len(sys.argv) > 1:
        target = sys.argv[1]
        process_book(target)
    else:
        for entry in sorted(os.listdir(portfolio_dir)):
            full_p = os.path.join(portfolio_dir, entry)
            if os.path.isdir(full_p) and os.path.exists(os.path.join(full_p, f"{entry}_full.md")):
                process_book(full_p)
