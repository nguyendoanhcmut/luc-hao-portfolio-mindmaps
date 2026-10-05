import json, re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

figs_manifest = json.load(open('figures_manifest.json', encoding='utf-8'))
figs_by_file = {f['file_name']: f for f in figs_manifest['figures']}
manifest = json.load(open('luc_hao_xu_cat_ti_hung_scout_manifest.json', encoding='utf-8'))

def clean_paragraph(p):
    p = p.strip()
    # collapse multiple whitespaces
    p = re.sub(r'[ \t]+', ' ', p)
    return p

def format_evidence_block(fig_obj, hex_name=None, proof_text=None, see_text=None, indent="  "):
    fid = fig_obj.get('id', '')
    fnum = fig_obj.get('figure_number', '')
    fname = fig_obj.get('file_name', '')
    cap = fig_obj.get('caption', '')
    
    title = f"Hình {fnum}."
    if hex_name:
        title += f" {hex_name}"
    elif cap:
        title += f" {cap}"
    
    # ensure short title <= 12 words
    words = title.split()
    if len(words) > 12:
        title = " ".join(words[:12])
        
    p_text = proof_text or f"Cấu trúc hào quẻ, Dụng thần suy vượng, động biến sinh khắc chế hóa quyết định cát hung."
    s_text = see_text or f"Vị trí các hào Thế/Ứng, lục thân, lục thần, can chi, hào động và hào biến."
    
    # 6 lines total
    lines = [
        f"{indent}- **{title}**",
        f"{indent}  - <img src=\"assets/{fname}\" alt=\"Hình {fnum}\" />",
        f"{indent}  - **Hình này chứng minh điều gì**",
        f"{indent}    - {p_text}",
        f"{indent}  - **Từ đâu mà thấy được**",
        f"{indent}    - {s_text}"
    ]
    return lines

print("Helper ready")
