import os
import json

results_dir = r"C:/Users/Admin/.gemini/antigravity/scratch/luc_hao_portfolio_ocr/luc_hao_du_trac_ngo_trung_ngo/page_results"
pages_dir = r"C:/Users/Admin/.gemini/antigravity/scratch/luc_hao_portfolio_ocr/luc_hao_du_trac_ngo_trung_ngo/pages"

def page_exists(p):
    f = os.path.join(results_dir, f"page_{p:04d}.json")
    return os.path.exists(f)

missing_pairs = []
for i in range(1, 108):
    p1 = 2 * i - 1
    p2 = 2 * i
    if not (page_exists(p1) and page_exists(p2)):
        missing_pairs.append({
            "pair_id": i,
            "p1": p1,
            "img1": f"{pages_dir}/page_{p1:04d}.png",
            "p2": p2,
            "img2": f"{pages_dir}/page_{p2:04d}.png",
        })

print(f"Total missing pairs: {len(missing_pairs)}")
wave1 = missing_pairs[:80]
wave2 = missing_pairs[80:]

print(f"Wave 1: {len(wave1)} pairs (pair {wave1[0]['pair_id']} pages {wave1[0]['p1']}-{wave1[0]['p2']} to pair {wave1[-1]['pair_id']} pages {wave1[-1]['p1']}-{wave1[-1]['p2']})")
print(f"Wave 2: {len(wave2)} pairs (pair {wave2[0]['pair_id']} pages {wave2[0]['p1']}-{wave2[0]['p2']} to pair {wave2[-1]['pair_id']} pages {wave2[-1]['p1']}-{wave2[-1]['p2']})")

plan_file = r"C:/Users/Admin/.gemini/antigravity/scratch/luc_hao_portfolio_ocr/luc_hao_du_trac_ngo_trung_ngo/wave_plan.json"
with open(plan_file, "w", encoding="utf-8") as f:
    json.dump({"wave1": wave1, "wave2": wave2}, f, indent=2)
print("Saved wave plan to", plan_file)
