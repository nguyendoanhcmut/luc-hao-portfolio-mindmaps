import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

manifest = json.load(open('luc_hao_xu_cat_ti_hung_scout_manifest.json', encoding='utf-8'))
figs_manifest = json.load(open('figures_manifest.json', encoding='utf-8'))
figs_dict = {f['id']: f for f in figs_manifest['figures']}
figs_by_file = {f['file_name']: f for f in figs_manifest['figures']}

def clean_text(t):
    # remove page markers, horizontal rules
    lines = []
    for l in t.splitlines():
        l_str = l.strip()
        if re.match(r'<!--\s*Page\s+\d+\s*-->', l_str):
            continue
        if l_str == '---':
            continue
        lines.append(l)
    return '\n'.join(lines)

def is_table_line(l):
    s = l.strip()
    return s.startswith('|') and s.endswith('|')

def is_hexagram_extra(l):
    s = l.strip()
    # match patterns like "THỔ Không Vong: Thìn, Tị", "KIM Không Vong: Tuất, Hợi", etc.
    if re.match(r'^(?:KIM|MỘC|THỦY|HỎA|THỔ)?\s*(?:Không Vong|Tuần Không)\s*:', s, re.IGNORECASE):
        return True
    if re.match(r'^(?:KIM|MỘC|THỦY|HỎA|THỔ)\s*$', s):
        return True
    return False

print("Helper loaded.")
