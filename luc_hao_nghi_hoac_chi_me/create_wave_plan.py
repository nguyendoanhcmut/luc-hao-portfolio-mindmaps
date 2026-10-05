import os
import json

output_dir = r"C:/Users/Admin/.gemini/antigravity/scratch/luc_hao_portfolio_ocr/luc_hao_nghi_hoac_chi_me"
results_dir = os.path.join(output_dir, "page_results")
pages_dir = os.path.join(output_dir, "pages").replace("\\", "/")

total_pages = 216
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

wave1 = pairs[:80]
wave2 = pairs[80:]

print(f"Total pairs: {len(pairs)}")
print(f"Wave 1 count: {len(wave1)} (pairs 1 to {len(wave1)}, pages {wave1[0]['p1']}-{wave1[-1]['p2']})")
print(f"Wave 2 count: {len(wave2)} (pairs {wave2[0]['pair_id']} to {wave2[-1]['pair_id']}, pages {wave2[0]['p1']}-{wave2[-1]['p2']})")

plan_file = os.path.join(output_dir, "wave_plan.json")
with open(plan_file, "w", encoding="utf-8") as f:
    json.dump({"wave1": wave1, "wave2": wave2}, f, indent=2)

print("Saved wave plan to", plan_file)

# Prepare wave 1 subagents payload
w1_subagents = []
for p in wave1:
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
    w1_subagents.append({
        "TypeName": "two_page_worker",
        "Role": f"OCR Worker P{p1:04d}-P{p2:04d}",
        "Prompt": prompt,
        "Model": "inherit"
    })

w1_file = os.path.join(output_dir, "wave1_subagents.json")
with open(w1_file, "w", encoding="utf-8") as f:
    json.dump(w1_subagents, f, indent=2)
print("Saved wave 1 subagents to", w1_file)

# Prepare wave 2 subagents payload
w2_subagents = []
for p in wave2:
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
    w2_subagents.append({
        "TypeName": "two_page_worker",
        "Role": f"OCR Worker P{p1:04d}-P{p2:04d}",
        "Prompt": prompt,
        "Model": "inherit"
    })

w2_file = os.path.join(output_dir, "wave2_subagents.json")
with open(w2_file, "w", encoding="utf-8") as f:
    json.dump(w2_subagents, f, indent=2)
print("Saved wave 2 subagents to", w2_file)
