import os
import re

target_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\giai_dap_nghi_van"
frag_dir = os.path.join(target_dir, "fragments")

buzzword_fixes = {
    "đột phá": "sâu sắc",
    "toàn diện": "đầy đủ",
    "vượt trội": "nổi bật",
    "cách mạng": "cải tiến",
}

for f in os.listdir(frag_dir):
    if f.endswith("_branches.md"):
        path = os.path.join(frag_dir, f)
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Replace buzzwords
        for bw, repl in buzzword_fixes.items():
            content = content.replace(bw, repl)
            content = content.replace(bw.capitalize(), repl.capitalize())
        
        # If ch01, remove the second Hình 1 block inside Dữ kiện
        if "ch01" in f:
            # remove lines 59 to 65
            lines = content.splitlines()
            cleaned = []
            skip = False
            for l in lines:
                if "- **Minh chứng quẻ chiêm (Sơ đồ quẻ Quy Muội biến Càn)**" in l:
                    skip = True
                    cleaned.append("  - Sơ đồ quẻ: Tra cứu chi tiết tại **Hình 1** ở trên.")
                    continue
                if skip:
                    if l.strip().startswith("- Nhìn vào:") or l.strip().startswith("- **Quy tắc"):
                        skip = False
                        cleaned.append(l)
                    continue
                cleaned.append(l)
            content = "\n".join(cleaned) + "\n"

        with open(path, "w", encoding="utf-8") as file:
            file.write(content)

print("Cleaned buzzwords and duplicate embed in ch01.")
