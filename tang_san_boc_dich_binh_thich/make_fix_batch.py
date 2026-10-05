import json, os

mf = json.load(open('tang_san_boc_dich_binh_thich_scout_manifest.json', encoding='utf-8'))
fig_mf = json.load(open('figures_manifest.json', encoding='utf-8'))
by_id = {f['id']: f for f in fig_mf.get('figures', [])}

workspace_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\tang_san_boc_dich_binh_thich"

subagents = []
for cid in ['ch35_2', 'ch36']:
    sec = [s for s in mf['routing_table'] if s['chunk_id'] == cid][0]
    figs = [{'num': f['id'].replace('fig_', ''), 'cap': f.get('caption', ''), 'src': 'assets/' + f.get('file_name', '')} for f in [by_id[fid] for fid in sec['figure_ids']]]
    
    src_file = os.path.join(workspace_dir, sec['section_text_file'])
    out_file = os.path.join(workspace_dir, sec['fragment_file'])
    
    figs_json = json.dumps(figs, ensure_ascii=False)
    
    prompt = f"""READ-SCOPE RULE: Read ONLY your assigned section_text_file:
{src_file}

Parameters:
- chunk_id: {cid}
- section_title: {sec['title']}
- start_level: {sec['start_heading_level']}
- max_heading_level: 5
- output_file: {out_file}
- assigned_figures: {figs_json}

Tuân thủ triệt để system prompt branch_driller:
- Tiêu đề '{sec['title']}' ở cấp {'##' if sec['start_heading_level']==2 else '###'}, các mục con sâu hơn (max cấp 5 #####), claim bullets (- ...) dưới headings.
- BỎ 100% bảng vẽ hào markdown.
- BẮT BUỘC nhúng ĐẦY ĐỦ toàn bộ các hình ảnh trong assigned_figures ({len(figs)} hình) dưới anchor claim bullet:
  - {{Anchor claim bullet}}
    - **Hình N.** {{Tên/Caption}}
      - <img src="assets/..." alt="Hình N" />
      - **Hình này chứng minh điều gì**
        - ...
      - **Từ đâu mà thấy được**
        - ...
  Đảm bảo block hình <= 10 dòng và thẻ img tự đóng hợp lệ. KHÔNG nhúng bất kỳ ảnh nào ngoài assigned_figures.
- Bảo toàn trọn vẹn luồng đối thoại thực tế Dã Hạc/Vương Hổ Ứng, lập luận Căn cứ - Nhìn vào, lời bình và ứng nghiệm thực tế.
- Ghi output_file (Overwrite=true), send_message báo hoàn thành."""

    subagents.append({
        'TypeName': 'branch_driller',
        'Role': f'Driller {cid}',
        'Model': 'flash',
        'Prompt': prompt,
        'Workspace': 'inherit'
    })

with open('batch_fix_2.json', 'w', encoding='utf-8') as f:
    json.dump(subagents, f, ensure_ascii=False, indent=2)

print(f"Created batch_fix_2.json with {len(subagents)} subagents.")
