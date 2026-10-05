with open("luc_hao_bao_dien.txt", "r", encoding="utf-8-sig") as f:
    lines = [l.rstrip("\r\n") for l in f]

with open("scratch_phuluc2.txt", "w", encoding="utf-8") as out:
    for idx in range(7144, 7573):
        line = lines[idx].strip()
        if line.startswith("#") or (line and line[0].isdigit() and ("," in line[:4] or "." in line[:4])):
            out.write(f"Line {idx:5d}: {line[:100]}\n")
