import os
import sys

output_dir = r"C:/Users/Admin/.gemini/antigravity/scratch/luc_hao_portfolio_ocr/luc_hao_kinh_te_du_trac_hoc"
results_dir = f"{output_dir}/page_results"

start_p = int(sys.argv[1]) if len(sys.argv) > 1 else 1
end_p = int(sys.argv[2]) if len(sys.argv) > 2 else 160

existing = set()
if os.path.exists(results_dir):
    for f in os.listdir(results_dir):
        if f.startswith("page_") and f.endswith(".json"):
            try:
                num = int(f.split("_")[1].split(".")[0])
                existing.add(num)
            except Exception:
                pass

missing = [p for p in range(start_p, end_p + 1) if p not in existing]
total = end_p - start_p + 1
done = total - len(missing)

print(f"Range {start_p}-{end_p}: Done {done}/{total} ({done/total*100:.1f}%)")
if missing:
    if len(missing) <= 20:
        print(f"Missing pages: {missing}")
    else:
        print(f"Missing count: {len(missing)} (first 10: {missing[:10]})")
