import os
import json

output_dir = r"C:/Users/Admin/.gemini/antigravity/scratch/luc_hao_portfolio_ocr/luc_hao_nhan_duyen_du_trac_hoc"
results_dir = os.path.join(output_dir, "page_results").replace("\\", "/")
pages_dir = os.path.join(output_dir, "pages").replace("\\", "/")

total_pages = 243

pairs = []
for i in range(1, 123):
    p1 = 2 * i - 1
    p2 = 2 * i
    if p2 <= total_pages:
        pairs.append({
            "pair_id": i,
            "p1": p1,
            "img1": f"{pages_dir}/page_{p1:04d}.png",
            "p2": p2,
            "img2": f"{pages_dir}/page_{p2:04d}.png"
        })
    else:
        pairs.append({
            "pair_id": i,
            "p1": p1,
            "img1": f"{pages_dir}/page_{p1:04d}.png",
            "p2": None,
            "img2": None
        })

def make_subagent_entry(p):
    p1 = p["p1"]
    p2 = p["p2"]
    img1 = p["img1"]
    img2 = p["img2"]
    if p2 is not None:
        prompt = (
            f"page_1_number: {p1}\n"
            f"page_1_image: {img1}\n"
            f"page_2_number: {p2}\n"
            f"page_2_image: {img2}\n"
            f"output_dir: {results_dir}\n"
            f"Transcribe pages {p1} and {p2} verbatim into page_{p1:04d}.json and page_{p2:04d}.json in {results_dir}. Obey two_page_worker system instructions."
        )
        role = f"OCR Worker P{p1:04d}-P{p2:04d}"
    else:
        prompt = (
            f"page_1_number: {p1}\n"
            f"page_1_image: {img1}\n"
            f"output_dir: {results_dir}\n"
            f"Transcribe page {p1} verbatim into page_{p1:04d}.json in {results_dir}. Note: page {p1} is the final single page of the book. Obey two_page_worker system instructions."
        )
        role = f"OCR Worker P{p1:04d}"
    return {
        "TypeName": "two_page_worker",
        "Role": role,
        "Prompt": prompt,
        "Model": "inherit"
    }

w1a = [make_subagent_entry(p) for p in pairs[0:40]]
w1b = [make_subagent_entry(p) for p in pairs[40:80]]
w2 = [make_subagent_entry(p) for p in pairs[80:122]]

with open(os.path.join(output_dir, "wave1a.json"), "w", encoding="utf-8") as f:
    json.dump(w1a, f, indent=2)

with open(os.path.join(output_dir, "wave1b.json"), "w", encoding="utf-8") as f:
    json.dump(w1b, f, indent=2)

with open(os.path.join(output_dir, "wave2.json"), "w", encoding="utf-8") as f:
    json.dump(w2, f, indent=2)

print(f"Created wave plans: w1a={len(w1a)}, w1b={len(w1b)}, w2={len(w2)}, total={len(w1a)+len(w1b)+len(w2)}")
