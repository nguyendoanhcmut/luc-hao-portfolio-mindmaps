import json

with open("C:/Users/Admin/.gemini/antigravity/scratch/luc_hao_portfolio_ocr/luc_hao_du_trac_ngo_trung_ngo/wave_plan.json", "r", encoding="utf-8") as f:
    plan = json.load(f)

w1 = plan["wave1"]
items = []
results_dir = "C:/Users/Admin/.gemini/antigravity/scratch/luc_hao_portfolio_ocr/luc_hao_du_trac_ngo_trung_ngo/page_results"
for p in w1:
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
    items.append({
        "TypeName": "two_page_worker",
        "Role": f"OCR Worker P{p1:04d}-P{p2:04d}",
        "Prompt": prompt,
        "Model": "inherit"
    })

dump = json.dumps(items)
print(f"Count: {len(items)}")
print(f"Total chars: {len(dump)}")
print(f"Estimated tokens: {len(dump) // 4}")

with open("C:/Users/Admin/.gemini/antigravity/scratch/luc_hao_portfolio_ocr/luc_hao_du_trac_ngo_trung_ngo/wave1_subagents.json", "w", encoding="utf-8") as f:
    json.dump(items, f, indent=2)
