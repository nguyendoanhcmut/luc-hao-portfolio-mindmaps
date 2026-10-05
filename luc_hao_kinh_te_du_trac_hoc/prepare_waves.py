import os
import json

output_dir = r"C:/Users/Admin/.gemini/antigravity/scratch/luc_hao_portfolio_ocr/luc_hao_kinh_te_du_trac_hoc"
results_dir = f"{output_dir}/page_results"
pages_dir = f"{output_dir}/pages"

os.makedirs(results_dir, exist_ok=True)

total_pages = 371
total_pairs = (total_pages + 1) // 2 # 186 pairs

def make_entry(i):
    p1 = 2 * i - 1
    p2 = 2 * i if (2 * i <= total_pages) else None
    img1 = f"{pages_dir}/page_{p1:04d}.png"
    
    if p2 is not None:
        img2 = f"{pages_dir}/page_{p2:04d}.png"
        prompt = (
            f"Transcribe the following 2 pages:\n"
            f"- page_1_number: {p1}\n"
            f"- page_1_image: \"{img1}\"\n"
            f"- page_2_number: {p2}\n"
            f"- page_2_image: \"{img2}\"\n"
            f"- output_dir: \"{results_dir}\"\n\n"
            f"Follow your operational instructions:\n"
            f"1. View image 1 and transcribe verbatim into \"{results_dir}/page_{p1:04d}.json\".\n"
            f"2. View image 2 and transcribe verbatim into \"{results_dir}/page_{p2:04d}.json\".\n"
            f"3. Extract diagram bounding boxes if present.\n"
            f"4. Send completion message back to the caller agent when done."
        )
        role = f"OCR Worker P{p1:04d}-P{p2:04d}"
    else:
        prompt = (
            f"Transcribe the following page:\n"
            f"- page_1_number: {p1}\n"
            f"- page_1_image: \"{img1}\"\n"
            f"- output_dir: \"{results_dir}\"\n\n"
            f"Follow your operational instructions:\n"
            f"1. View image 1 and transcribe verbatim into \"{results_dir}/page_{p1:04d}.json\".\n"
            f"2. Extract diagram bounding boxes if present.\n"
            f"3. Send completion message back to the caller agent when done."
        )
        role = f"OCR Worker P{p1:04d}"
        
    return {
        "TypeName": "two_page_worker",
        "Role": role,
        "Prompt": prompt,
        "Model": "flash"
    }

pairs = [make_entry(i) for i in range(1, total_pairs + 1)]

wave1 = pairs[0:80]
wave2 = pairs[80:160]
wave3 = pairs[160:186]

wave1a = pairs[0:40]
wave1b = pairs[40:80]
wave2a = pairs[80:120]
wave2b = pairs[120:160]

with open(f"{output_dir}/wave1.json", "w", encoding="utf-8") as f:
    json.dump(wave1, f, indent=2)

with open(f"{output_dir}/wave2.json", "w", encoding="utf-8") as f:
    json.dump(wave2, f, indent=2)

with open(f"{output_dir}/wave3.json", "w", encoding="utf-8") as f:
    json.dump(wave3, f, indent=2)

with open(f"{output_dir}/wave1a.json", "w", encoding="utf-8") as f:
    json.dump(wave1a, f, indent=2)

with open(f"{output_dir}/wave1b.json", "w", encoding="utf-8") as f:
    json.dump(wave1b, f, indent=2)

with open(f"{output_dir}/wave2a.json", "w", encoding="utf-8") as f:
    json.dump(wave2a, f, indent=2)

with open(f"{output_dir}/wave2b.json", "w", encoding="utf-8") as f:
    json.dump(wave2b, f, indent=2)

print(f"Generated waves successfully. Total pairs: {len(pairs)}")
print(f"Wave 1: {len(wave1)} pairs (1a: {len(wave1a)}, 1b: {len(wave1b)})")
print(f"Wave 2: {len(wave2)} pairs (2a: {len(wave2a)}, 2b: {len(wave2b)})")
print(f"Wave 3: {len(wave3)} pairs")
