import json
import os

output_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\giai_dap_nghi_van"
skill_dir = r"C:\Users\Admin\.gemini\config\skills\branches"

with open(os.path.join(output_dir, "giai_dap_nghi_van_scout_manifest.json"), "r", encoding="utf-8") as f:
    manifest = json.load(f)

figures_manifest_path = os.path.join(output_dir, "figures_manifest.json")
global_context_pack = manifest.get("global_context_pack", "")
rule_index = manifest.get("rule_index", [])

subagents = []
for c in manifest["routing_table"]:
    cid = c["chunk_id"]
    title = c["title"]
    start_lvl = c["start_heading_level"]
    src_file = c["section_text_file"]
    frag_file = os.path.join(output_dir, c["fragment_file"])
    fig_ids = c["figure_ids"]
    exercises = c["exercises"]
    
    prompt = f"""You are branch_driller.
Read-scope rule: read only your prompt, parameter files, and script outputs. Do not open other skill files. Do not lint JSON.

Parameters:
- section_text_file: {src_file}
- section_title: {title}
- start_level: {start_lvl}
- max_heading_level: 5
- drill_threshold_words: 1500
- figures_manifest: {figures_manifest_path}
- assigned_figures: {json.dumps(fig_ids)}
- exercises: {json.dumps(exercises, ensure_ascii=False)}
- domain: luc_hao
- rule_index: {json.dumps(rule_index, ensure_ascii=False)}
- global_context_pack: {global_context_pack}
- skill_dir: {skill_dir}
- output_file: {frag_file}

Instructions:
1. Turn the assigned section into a structured Markdown subtree at start_level ({start_lvl}).
2. Under each heading, write claim bullets for findings, rules, and theoretical explanations.
3. Every figure in assigned_figures MUST be embedded:
   - **Hình {{figure_number}}** {{Short caption}}
     - <img src="assets/{{filename}}" alt="Hình {{figure_number}}" />
     - **Hình này chứng minh điều gì**
       - {{bullet}}
     - **Từ đâu mà thấy được**
       - {{bullet}}
4. In luc_hao domain, for each exercise in exercises, preserve the author-querent dialog flow, step-by-step reasoning (Căn cứ - Nhìn vào), and real-world verified outcomes:
   ### {{exercise_title}}
   - **Đề bài**: {{tóm tắt câu hỏi của người hỏi và nghi vấn}}
   - **Dữ kiện**
     - Ngày tháng, can chi, tuần không, quẻ chủ, quẻ biến, hào động
     - <img src="assets/{{chart}}" alt="Sơ đồ quẻ" />
     - Nhìn vào: {{hào, vị trí, lục thân, lục thú}}
   - **Quy tắc áp dụng**
     - {{quy tắc lục hào}}
   - **Lời giải**
     - **Bước 1**: {{phân tích dụng thần / nguyệt hợp / động biến}}
       - Căn cứ: {{quy tắc}}
       - Nhìn vào: {{hào, cột, bảng quẻ}}
     - **Bước 2**: ...
   - **Đối thoại giải đáp nghi vấn**: {{phân tích chuyên sâu giải đáp thắc mắc giữa người hỏi và Vương Hổ Ứng}}
   - **Kết quả**: {{kết luận dự đoán và thực chứng ngoài đời}}
   - **Kiểm tra lại**: {{đối chiếu dữ kiện với kết quả}}
5. Write the final fragment directly to output_file ({frag_file}) in UTF-8.
6. Verify lineage and syntax. Ensure no unrendered FIG tags remain.
7. Send parent: "Driller done. {frag_file}. Headings: {{H}}. Figures: {{F}}. Exercises: {{E}} ({{passed}} passed). FV: {{score}}. Open: none."
"""
    subagents.append({
        "TypeName": "branch_driller",
        "Role": f"Driller {cid}",
        "Prompt": prompt,
        "Model": "flash"
    })

print(f"Prepared {len(subagents)} subagents.")
with open(os.path.join(output_dir, "driller_subagents_spec.json"), "w", encoding="utf-8") as f:
    json.dump(subagents, f, indent=2, ensure_ascii=False)
