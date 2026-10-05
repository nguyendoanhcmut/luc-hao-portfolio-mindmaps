import json, os, sys, shutil

sys.stdout.reconfigure(encoding="utf-8")

with open("tang_san_boc_dich_binh_thich_scout_manifest.json", "r", encoding="utf-8") as f:
    scout = json.load(f)

output_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\tang_san_boc_dich_binh_thich"
rt = scout.get("routing_table", [])

existing = []
missing = []

all_files = os.listdir(os.path.join(output_dir, "fragments"))

for c in rt:
    frag_rel = c["fragment_file"]
    frag_abs = os.path.join(output_dir, frag_rel) if not os.path.isabs(frag_rel) else frag_rel
    base = os.path.basename(frag_abs)
    
    # Check if exact file exists
    if os.path.exists(frag_abs) and os.path.getsize(frag_abs) > 50:
        existing.append(c)
        continue
    
    # Check if a file matching chunk_id exists
    chunk_matches = [f for f in all_files if f.startswith(c["chunk_id"] + "_") and f.endswith(".md")]
    if chunk_matches:
        src = os.path.join(output_dir, "fragments", chunk_matches[0])
        if os.path.getsize(src) > 50:
            shutil.copyfile(src, frag_abs)
            print(f"Copied alias {chunk_matches[0]} -> {base}")
            existing.append(c)
            continue
            
    missing.append(c)

print(f"Existing valid fragments: {len(existing)}")
print(f"Missing fragments: {len(missing)}")
