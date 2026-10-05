import json, os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

manifest = json.load(open('luc_hao_xu_cat_ti_hung_scout_manifest.json', encoding='utf-8'))
figs_manifest = json.load(open('figures_manifest.json', encoding='utf-8'))
figs_dict = {f['id']: f for f in figs_manifest['figures']}
figs_by_file = {f['file_name']: f for f in figs_manifest['figures']}

def clean_lines(text):
    out = []
    for l in text.splitlines():
        ls = l.strip()
        if re.match(r'<!--\s*Page\s+\d+\s*-->', ls) or ls == '---':
            continue
        if ls.startswith('|') and ls.endswith('|'):
            continue
        if re.match(r'^(?:KIM|MỘC|THỦY|HỎA|THỔ)?\s*(?:Không Vong|Tuần Không)\s*:', ls, re.IGNORECASE):
            continue
        if re.match(r'^(?:KIM|MỘC|THỦY|HỎA|THỔ)\s*$', ls):
            continue
        if ls.startswith('##### '):
            continue
        out.append(l)
    return '\n'.join(out)

def make_evidence_block(fig_obj, default_hex=None, custom_proof=None, custom_see=None, indent="  "):
    fnum = fig_obj.get('figure_number', '')
    fname = fig_obj.get('file_name', '')
    cap = fig_obj.get('caption', '')
    
    # Clean caption for title
    cap_clean = cap.replace("Sơ đồ quẻ ", "Quẻ ").replace("Sơ đồ ", "")
    title = f"Hình {fnum}. {cap_clean}"
    words = title.split()
    if len(words) > 12:
        title = " ".join(words[:12])
        
    p_text = custom_proof or f"Dụng thần và hào Thế/Ứng suy vượng, động biến sinh khắc chế hóa quyết định phương án hóa giải."
    s_text = custom_see or f"Hào quẻ gốc biến quẻ biến, can chi nạp âm, lục thân, lục thú, hào vị và trạng thái động tĩnh."
    
    return [
        f"{indent}- **{title}**",
        f"{indent}  - <img src=\"assets/{fname}\" alt=\"Hình {fnum}\" />",
        f"{indent}  - **Hình này chứng minh điều gì**",
        f"{indent}    - {p_text}",
        f"{indent}  - **Từ đâu mà thấy được**",
        f"{indent}    - {s_text}"
    ]

print("Base generator loaded")
