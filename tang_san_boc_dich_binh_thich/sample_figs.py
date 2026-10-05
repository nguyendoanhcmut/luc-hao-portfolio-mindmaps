import glob, re, sys

sys.stdout.reconfigure(encoding="utf-8")

count = 0
for f in sorted(glob.glob("fragments/src/*.txt")):
    text = open(f, encoding="utf-8").read()
    matches = list(re.finditer(r"!\[(.*?)\]\((assets/page_\d+_img_\d+\.png)\)", text))
    if matches:
        for m in matches[:2]:
            start = max(0, m.start() - 200)
            end = min(len(text), m.end() + 200)
            print(f"--- File: {f} ---")
            print(text[start:end])
            print("="*40)
            count += 1
            if count >= 3:
                break
    if count >= 3:
        break
