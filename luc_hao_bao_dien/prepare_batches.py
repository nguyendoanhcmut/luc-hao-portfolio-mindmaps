import json
import os

manifest_path = r'C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_bao_dien\luc_hao_bao_dien_scout_manifest.json'
with open(manifest_path, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

chunks = manifest['routing_table']
output_dir = r'C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_bao_dien'
skill_dir = r'C:\Users\Admin\.gemini\config\skills\branches'
fig_manifest_path = os.path.join(output_dir, 'figures_manifest.json')

with open(fig_manifest_path, 'r', encoding='utf-8') as f:
    fig_man = json.load(f)
fig_lookup = {f['id']: f for f in fig_man.get('figures', [])}

batches = []
batch_size = 20

for i in range(0, len(chunks), batch_size):
    batch_chunks = chunks[i:i + batch_size]
    subagents = []
    for c in batch_chunks:
        frag_file = os.path.join(output_dir, c['fragment_file']) if not os.path.isabs(c['fragment_file']) else c['fragment_file']
        
        # Build concise figure list with relative paths and captions
        figs_info = []
        for fid in c.get('figure_ids', []):
            if fid in fig_lookup:
                fg = fig_lookup[fid]
                figs_info.append(f"{fid} ({fg.get('figure_number')}): {fg.get('rel_path')} - {fg.get('caption')}")
            else:
                figs_info.append(fid)
        figs_str = "\n".join(figs_info) if figs_info else "None"
        
        # Build exercises info
        exs_info = []
        for ex in c.get('exercises', []):
            exs_info.append(f"{ex.get('exercise_id')}: {ex.get('title')}")
        exs_str = "\n".join(exs_info) if exs_info else "None"

        prompt = (
            f"Chunk ID: {c['chunk_id']}\n"
            f"Title: {c['title']}\n"
            f"Start heading level: {c['start_heading_level']}\n"
            f"Source file: {c['section_text_file']}\n"
            f"Output fragment: {frag_file}\n"
            f"Assigned figures:\n{figs_str}\n"
            f"Assigned exercises:\n{exs_str}\n\n"
            f"TASKS & RULES:\n"
            f"1. Read {c['section_text_file']}.\n"
            f"2. Write fragment starting with {'#' * c['start_heading_level']} {c['title']}.\n"
            f"3. Under headings, write claim bullets (- ...). Sub-points nested under claims.\n"
            f"4. BỎ 100% bảng vẽ hào Markdown (| Hào |...) và KHÔNG dùng ##### cho quẻ.\n"
            f"5. Với mỗi quẻ/hình có ảnh, BẮT BUỘC chèn evidence block lồng dưới claim bullet cha:\n"
            f"   - {{Claim bullet luận giải quẻ / kết luận}}\n"
            f"     - **Hình N.** {{Tên quẻ}}\n"
            f"       - <img src=\"assets/page_XXXX_img_YY.png\" alt=\"Hình N\" />\n"
            f"       - **Hình này chứng minh điều gì**\n"
            f"         - ...\n"
            f"       - **Từ đâu mà thấy được**\n"
            f"         - ...\n"
            f"   (Evidence block dài tối đa 10 dòng; mỗi ảnh nhúng 1 lần; thụt lề 2 spaces dưới bullet cha).\n"
            f"6. Bảo toàn đối thoại thực tế, suy luận chi tiết (Căn cứ - Nhìn vào) và ứng nghiệm thực tế.\n"
            f"7. Ghi fragment vào {frag_file} (UTF-8). Send message when done: Driller done. {frag_file}."
        )
        subagents.append({
            "TypeName": "branch_driller",
            "Role": f"Driller {c['chunk_id']}",
            "Model": "flash",
            "Prompt": prompt
        })
    batches.append(subagents)

for idx, b in enumerate(batches):
    batch_file = os.path.join(output_dir, f'drillers_batch_{idx+1}.json')
    with open(batch_file, 'w', encoding='utf-8') as f:
        json.dump(b, f, indent=2, ensure_ascii=False)
    print(f"Batch {idx+1}: {len(b)} subagents -> {batch_file}")
