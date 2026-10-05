import os
import json

output_dir = r"C:/Users/Admin/.gemini/antigravity/scratch/luc_hao_portfolio_ocr/luc_hao_chiem_nghiem_bi_phap_ver1"
results_dir = os.path.join(output_dir, "page_results").replace("\\", "/")
pages_dir = os.path.join(output_dir, "pages").replace("\\", "/")

total_pages = 238
total_pairs = total_pages // 2

pairs = []
for i in range(1, total_pairs + 1):
    p1 = 2 * i - 1
    p2 = 2 * i
    pairs.append({
        "pair_id": i,
        "p1": p1,
        "img1": f"{pages_dir}/page_{p1:04d}.png",
        "p2": p2,
        "img2": f"{pages_dir}/page_{p2:04d}.png"
    })

def make_subagent_entry(p):
    p1 = p["p1"]
    p2 = p["p2"]
    img1 = p["img1"]
    img2 = p["img2"]
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

w1a = [make_subagent_entry(p) for p in pairs[0:40]]
w1b = [make_subagent_entry(p) for p in pairs[40:80]]
w2 = [make_subagent_entry(p) for p in pairs[80:119]]

with open(os.path.join(output_dir, "wave1a.json"), "w", encoding="utf-8") as f:
    json.dump(w1a, f, indent=2)

with open(os.path.join(output_dir, "wave1b.json"), "w", encoding="utf-8") as f:
    json.dump(w1b, f, indent=2)

with open(os.path.join(output_dir, "wave2.json"), "w", encoding="utf-8") as f:
    json.dump(w2, f, indent=2)

print(f"Created wave plans: w1a={len(w1a)}, w1b={len(w1b)}, w2={len(w2)}")
