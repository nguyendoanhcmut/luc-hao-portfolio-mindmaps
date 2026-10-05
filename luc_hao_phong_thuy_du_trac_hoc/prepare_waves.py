import os
import json

output_dir = r"C:/Users/Admin/.gemini/antigravity/scratch/luc_hao_portfolio_ocr/luc_hao_phong_thuy_du_trac_hoc"
results_dir = f"{output_dir}/page_results"
pages_dir = f"{output_dir}/pages"

total_pages = 348
total_pairs = 174

def make_entry(i):
    p1 = 2 * i - 1
    p2 = 2 * i
    img1 = f"{pages_dir}/page_{p1:04d}.png"
    img2 = f"{pages_dir}/page_{p2:04d}.png"
    prompt = (
        f"page_1_number: {p1}\n"
        f"page_1_image: {img1}\n"
        f"page_2_number: {p2}\n"
        f"page_2_image: {img2}\n"
        f"output_dir: {results_dir}\n"
        f"Transcribe pages {p1} and {p2} verbatim into page_{p1:04d}.json and page_{p2:04d}.json in {results_dir}. Obey two_page_worker system instructions."
    )
    return {
        "TypeName": "two_page_worker",
        "Role": f"OCR Worker P{p1:04d}-P{p2:04d}",
        "Prompt": prompt,
        "Model": "inherit"
    }

pairs = [make_entry(i) for i in range(1, total_pairs + 1)]

# Split into waves:
# Wave 1 (pairs 1-80): wave1a (1-40), wave1b (41-80)
# Wave 2 (pairs 81-160): wave2a (81-120), wave2b (121-160)
# Wave 3 (pairs 161-174): wave3 (161-174)

wave1a = pairs[0:40]
wave1b = pairs[40:80]
wave2a = pairs[80:120]
wave2b = pairs[120:160]
wave3 = pairs[160:174]

with open(f"{output_dir}/wave1a.json", "w", encoding="utf-8") as f:
    json.dump(wave1a, f, indent=2)

with open(f"{output_dir}/wave1b.json", "w", encoding="utf-8") as f:
    json.dump(wave1b, f, indent=2)

with open(f"{output_dir}/wave2a.json", "w", encoding="utf-8") as f:
    json.dump(wave2a, f, indent=2)

with open(f"{output_dir}/wave2b.json", "w", encoding="utf-8") as f:
    json.dump(wave2b, f, indent=2)

with open(f"{output_dir}/wave3.json", "w", encoding="utf-8") as f:
    json.dump(wave3, f, indent=2)

print(f"Generated wave chunks: wave1a={len(wave1a)}, wave1b={len(wave1b)}, wave2a={len(wave2a)}, wave2b={len(wave2b)}, wave3={len(wave3)}")
