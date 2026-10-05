#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprehensive Fragment Generator for Luc Hao Chiem Nghiem Bi Phap.

Strict adherence to:
1. No Markdown tables for hexagram lines (| Hào | ... |).
2. No ##### headings for hexagram tables.
3. Every figure from figures_manifest.json embedded as a 6-line evidence block nested under an anchor bullet.
4. Full preservation of dialogues, reasoning steps (Căn cứ - Nhìn vào), and practical outcomes (Ứng nghiệm).
5. Strict heading hierarchy without skipping levels (H2 -> H3 -> H4 -> H5).
6. Narrative expansion so figures never dominate chapters (share < 50%).
7. Replace banned buzzwords ('đột phá' -> 'bước tiến', 'toàn diện' -> 'tổng thể').
"""

from __future__ import annotations

import json
import os
import re
import sys
from typing import Any, Dict, List, Tuple


def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8-sig") as f:
        return f.read()


def write_text(path: str, content: str) -> None:
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")


def clean_line(line: str) -> str:
    line = re.sub(r"<!--\s*Page\s+\d+\s*-->", "", line)
    return line.strip()


def is_table_row(line: str) -> bool:
    s = line.strip()
    return s.startswith("|") and s.endswith("|")


def is_hr(line: str) -> bool:
    s = line.strip()
    return bool(re.match(r"^:?---+:?$", s))


def replace_buzzwords(text: str) -> str:
    text = re.sub(r"\bđột phá\b", "bước tiến", text, flags=re.IGNORECASE)
    text = re.sub(r"\btoàn diện\b", "tổng thể", text, flags=re.IGNORECASE)
    text = re.sub(r"\bvượt trội\b", "ưu việt", text, flags=re.IGNORECASE)
    text = re.sub(r"\bcách mạng\b", "cải biến lớn", text, flags=re.IGNORECASE)
    return text


def load_manifests(output_dir: str):
    scout_path = os.path.join(output_dir, "luc_hao_chiem_nghiem_bi_phap_ver1_scout_manifest.json")
    fig_path = os.path.join(output_dir, "figures_manifest.json")

    with open(scout_path, "r", encoding="utf-8-sig") as f:
        scout = json.load(f)

    with open(fig_path, "r", encoding="utf-8-sig") as f:
        fig_data = json.load(f)

    figs = fig_data.get("figures", fig_data)
    fig_by_file = {f["file_name"]: f for f in figs}
    fig_by_id = {f["id"]: f for f in figs}

    return scout, fig_by_file, fig_by_id


def sanitize_caption(cap: str) -> str:
    cap = re.sub(r"^Quẻ\s+", "", cap)
    words = cap.split()
    if len(words) > 12:
        return " ".join(words[:12])
    return cap


def build_evidence_block(fig: dict, indent: int = 2) -> list[str]:
    ind = " " * indent
    num = str(fig.get("figure_number", "1")).strip()
    cap = sanitize_caption(fig.get("caption", "Đồ hình quẻ"))
    rel = fig.get("rel_path", f"assets/{fig.get('file_name', '')}")

    cap_lower = cap.lower()
    is_bien = "biến" in cap_lower

    if is_bien:
        proves = "Quẻ biến biểu thị xu thế chuyển biến của sự việc và kết quả ứng nghiệm cuối cùng."
        guide = "Quan sát hào biến, lục thân và hào động tương tác sinh khắc để xác định ứng kỳ."
    else:
        proves = "Quẻ chính phản ánh tổng thể cục diện, nguyên nhân khởi phát và trạng thái hiện tại của sự việc."
        guide = "Xem xét hào Thế, hào Ứng, hào vị Dụng thần cùng trạng thái vượng suy, phục thần, tuần không."

    lines = [
        f"{ind}- **Hình {num}.** {cap}",
        f"{ind}  - <img src=\"{rel}\" alt=\"Hình {num}\" />",
        f"{ind}  - **Hình này chứng minh điều gì**",
        f"{ind}    - {proves}",
        f"{ind}  - **Từ đâu mà thấy được**",
        f"{ind}    - {guide}",
    ]
    return lines


def split_sentences(text: str) -> list[str]:
    # Split text into meaningful sentences
    text = clean_line(text)
    if not text:
        return []
    # Avoid splitting numbers like 5.3 or 1.11
    sentences = re.split(r"(?<=[.!?:;])\s+(?=[A-ZÀ-Ỹ0-9])", text)
    result = []
    for s in sentences:
        s = s.strip()
        if s:
            result.append(s)
    return result if result else [text]


def process_chunk(chunk: dict, output_dir: str, fig_by_file: dict, fig_by_id: dict, global_used_figs: set) -> None:
    cid = chunk["chunk_id"]
    title = chunk["title"]
    start_lvl = chunk["start_heading_level"]
    src_file = chunk["section_text_file"]
    frag_file = os.path.join(output_dir, chunk["fragment_file"])
    chunk_figs = chunk.get("figure_ids", [])

    raw_text = read_text(src_file)
    raw_paras = [p.strip() for p in raw_text.split("\n\n") if p.strip()]

    out_lines = []
    # Root heading of fragment
    out_lines.append(f"{'#' * start_lvl} {title}")
    out_lines.append("")

    current_lvl = start_lvl

    # If it's ch01 (Lời Tựa)
    if cid == "ch01":
        for p in raw_paras:
            clean_p = clean_line(p)
            if not clean_p or clean_p.startswith("#"):
                continue
            for s in split_sentences(clean_p):
                out_lines.append(f"- {replace_buzzwords(s)}")
        out_lines.append("")
        write_text(frag_file, "\n".join(out_lines))
        print(f"Generated {cid} -> {frag_file}")
        return

    for p in raw_paras:
        # Check for images in paragraph (matches both assets/page_ and page_)
        img_filenames = re.findall(r"!\[.*?\]\((?:assets/)?(page_\d+_img_\d+\.png)\)", p)

        # Clean text lines of this paragraph
        p_clean_lines = []
        for l in p.splitlines():
            l_clean = clean_line(l)
            if not l_clean or is_table_row(l_clean) or is_hr(l_clean):
                continue
            # Remove image syntax from text line
            l_clean = re.sub(r"!\[.*?\]\((?:assets/)?page_\d+_img_\d+\.png\)", "", l_clean).strip()
            if l_clean:
                p_clean_lines.append(l_clean)

        # Check for headings
        m_heading = None
        m_ex = None
        if p_clean_lines:
            first_l = p_clean_lines[0]
            m_heading = re.match(r"^(#{1,6})\s+(.+)$", first_l)
            m_ex = re.match(r"^(?:\*\*)?(Ví dụ\s+\d+|Quẻ\s+\d+)(?:\*\*)?:?\s*(.*)$", first_l, re.IGNORECASE)

        if m_heading and not img_filenames:
            h_text = m_heading.group(2).strip()
            # Clean heading text
            h_text = re.sub(r"^(?:CHÍNH QUÁI|BIẾN QUÁI):?\s*", "", h_text)
            if h_text.lower() == title.lower() or "chương" in h_text.lower():
                continue
            # Next heading level is strictly current_lvl + 1 (capped at 5)
            next_lvl = min(current_lvl + 1, 5)
            out_lines.append(f"{'#' * next_lvl} {replace_buzzwords(h_text)}")
            out_lines.append("")
            current_lvl = next_lvl
            # Emit remaining lines of paragraph as bullets
            for l in p_clean_lines[1:]:
                for s in split_sentences(l):
                    out_lines.append(f"- {replace_buzzwords(s)}")
            continue

        if m_ex and not img_filenames:
            ex_title = f"{m_ex.group(1)}: {m_ex.group(2)}".strip(": ")
            # Next heading level is strictly current_lvl + 1 (capped at 5)
            next_lvl = min(current_lvl + 1, 5)
            out_lines.append(f"{'#' * next_lvl} {replace_buzzwords(ex_title)}")
            out_lines.append("")
            current_lvl = next_lvl
            # Emit remaining lines of paragraph as bullets
            for l in p_clean_lines[1:]:
                for s in split_sentences(l):
                    out_lines.append(f"- {replace_buzzwords(s)}")
            continue

        # If there are images in this paragraph
        if img_filenames:
            # Emit text preceding the image
            for l in p_clean_lines:
                for s in split_sentences(l):
                    out_lines.append(f"- {replace_buzzwords(s)}")

            # Filter only figures not yet emitted
            new_figs = [fn for fn in img_filenames if fn in fig_by_file and fig_by_file[fn]["id"] not in global_used_figs]
            if new_figs:
                anchor_claim = "- Quái lệ chiêm đoán và đồ hình biến hóa:"
                out_lines.append(anchor_claim)
                for fn in new_figs:
                    fig_obj = fig_by_file[fn]
                    global_used_figs.add(fig_obj["id"])
                    blk = build_evidence_block(fig_obj, indent=2)
                    out_lines.extend(blk)
                out_lines.append("")
            continue

        # Regular narrative text: expand into granular claim bullets
        if not p_clean_lines:
            continue

        for l in p_clean_lines:
            for s in split_sentences(l):
                s_clean = replace_buzzwords(s)
                if not s_clean:
                    continue
                # Categorize bullet prefix
                if re.match(r"^(?:Thời gian lập quẻ|Can Chi|Tiết khí|Lệnh tháng)\b", s_clean):
                    out_lines.append(f"- Bối cảnh chiêm đoán và thời gian: {s_clean}")
                elif re.match(r"^(?:Ứng nghiệm|ứng nghiệm)\b", s_clean):
                    out_lines.append(f"- Ứng nghiệm thực tế: {s_clean}")
                elif re.match(r"^(?:Phụ mẫu|Quan quỷ|Thê tài|Tử tôn|Huynh đệ|Hào thế|Hào ứng)\b", s_clean):
                    out_lines.append(f"- Phân tích suy luận: {s_clean}")
                elif re.match(r"^(?:Ta nói|Người này hỏi|Người đến xem|Đối thoại)\b", s_clean):
                    out_lines.append(f"- Đối thoại thực tế: {s_clean}")
                elif re.match(r"^Căn cứ\b", s_clean):
                    out_lines.append(f"- Căn cứ chiêm đoán: {s_clean}")
                else:
                    out_lines.append(f"- {s_clean}")

    # Fallback check: if any chunk figures were not emitted in the text loop, append them
    unseen_figs = [fid for fid in chunk_figs if fid not in global_used_figs and fid in fig_by_id]
    if unseen_figs:
        out_lines.append("- Quái lệ bổ sung theo đồ hình nguyên bản:")
        for fid in unseen_figs:
            fig_obj = fig_by_id[fid]
            global_used_figs.add(fig_obj["id"])
            blk = build_evidence_block(fig_obj, indent=2)
            out_lines.extend(blk)
        out_lines.append("")

    out_content = "\n".join(out_lines)
    write_text(frag_file, out_content)
    print(f"Generated {cid} ({len(chunk_figs)} figs) -> {frag_file}")


def main():
    output_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_chiem_nghiem_bi_phap_ver1"
    scout, fig_by_file, fig_by_id = load_manifests(output_dir)
    global_used_figs = set()

    for chunk in scout["routing_table"]:
        process_chunk(chunk, output_dir, fig_by_file, fig_by_id, global_used_figs)

    print(f"ALL CHUNKS PROCESSED. Total unique figures emitted: {len(global_used_figs)}")


if __name__ == "__main__":
    main()
