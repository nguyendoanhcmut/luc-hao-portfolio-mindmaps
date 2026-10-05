import json

with open("C:/Users/Admin/.gemini/antigravity/scratch/luc_hao_portfolio_ocr/luc_hao_du_trac_ngo_trung_ngo/wave_plan.json", "r", encoding="utf-8") as f:
    plan = json.load(f)

wave1 = plan["wave1"]
subagents = []
for item in wave1:
    p1 = item["p1"]
    p2 = item["p2"]
    subagents.append({
        "TypeName": "two_page_worker",
        "Role": f"OCR Worker P{p1:04d}-P{p2:04d}",
        "Prompt": f"page_1_number: {p1}, page_2_number: {p2}. Transcribe pages {p1} and {p2} verbatim into page_{p1:04d}.json and page_{p2:04d}.json.",
        "Model": "inherit"
    })

print(f"Total subagents: {len(subagents)}")
dump = json.dumps(subagents)
print(f"Length: {len(dump)}")
