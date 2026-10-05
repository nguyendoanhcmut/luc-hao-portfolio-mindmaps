import os
import json

output_dir = r"C:/Users/Admin/.gemini/antigravity/scratch/luc_hao_portfolio_ocr/luc_hao_chiem_nghiem_bi_phap_ver1"
results_dir = f"{output_dir}/page_results"
pages_dir = f"{output_dir}/pages"

total_pages = 238
total_pairs = total_pages // 2

def make_item(i):
    p1 = 2 * i - 1
    p2 = 2 * i
    return {
        "TypeName": "two_page_worker",
        "Role": f"Worker P{p1:04d}-P{p2:04d}",
        "Prompt": f"page_1_number: {p1}, page_2_number: {p2}, pages_dir: {pages_dir}, output_dir: {results_dir}. Transcribe pages {p1} and {p2} verbatim into page_{p1:04d}.json and page_{p2:04d}.json.",
        "Model": "inherit"
    }

w1 = [make_item(i) for i in range(1, 81)] # pairs 1 to 80
w2 = [make_item(i) for i in range(81, 120)] # pairs 81 to 119

with open(f"{output_dir}/wave1_compact.json", "w", encoding="utf-8") as f:
    json.dump(w1, f)

with open(f"{output_dir}/wave2_compact.json", "w", encoding="utf-8") as f:
    json.dump(w2, f)

print(f"Generated wave1: {len(w1)} items ({os.path.getsize(f'{output_dir}/wave1_compact.json')} bytes)")
print(f"Generated wave2: {len(w2)} items ({os.path.getsize(f'{output_dir}/wave2_compact.json')} bytes)")
