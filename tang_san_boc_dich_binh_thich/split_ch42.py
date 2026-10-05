import json, os, sys

sys.stdout.reconfigure(encoding="utf-8")

output_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\tang_san_boc_dich_binh_thich"

with open(os.path.join(output_dir, "fragments", "src", "ch42.txt"), "r", encoding="utf-8") as f:
    lines = f.readlines()

split_idx = 1208
part1_lines = lines[:split_idx]
part2_lines = lines[split_idx:]

with open(os.path.join(output_dir, "fragments", "src", "ch42_part1.txt"), "w", encoding="utf-8") as f:
    f.writelines(part1_lines)

with open(os.path.join(output_dir, "fragments", "src", "ch42_part2.txt"), "w", encoding="utf-8") as f:
    f.writelines(part2_lines)

with open("figures_manifest.json", "r", encoding="utf-8") as f:
    fig_man = json.load(f)
fig_map = {f["id"]: f for f in fig_man.get("figures", [])}

with open("tang_san_boc_dich_binh_thich_scout_manifest.json", "r", encoding="utf-8") as f:
    scout = json.load(f)
ch42_entry = next(c for c in scout["routing_table"] if c["chunk_id"] == "ch42")

part1_text = "".join(part1_lines)
part2_text = "".join(part2_lines)

part1_figs = []
part2_figs = []

for fid in ch42_entry["figure_ids"]:
    fg = fig_map[fid]
    fnum = fg["figure_number"]
    # Check by figure number or caption keywords
    cap = fg.get("caption", "")
    info = {
        "num": fnum,
        "cap": cap,
        "src": fg.get("rel_path", f"assets/{fg.get('file_name','')}")
    }
    if int(fnum) <= 280:
        part1_figs.append(info)
    else:
        part2_figs.append(info)

print(f"Part 1: {len(part1_lines)} lines, {len(part1_figs)} figures (fig {part1_figs[0]['num']} to {part1_figs[-1]['num']})")
print(f"Part 2: {len(part2_lines)} lines, {len(part2_figs)} figures (fig {part2_figs[0]['num']} to {part2_figs[-1]['num']})")
