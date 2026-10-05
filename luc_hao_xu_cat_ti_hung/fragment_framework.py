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

def format_bullet(text, max_len=180):
    text = " ".join(text.split())
    if not text:
        return ""
    # if it already has bold prefix
    if text.startswith('**'):
        return f"- {text}"
    # find first colon or period to make key bold
    m = re.match(r'^([^:.]+[:.])\s*(.*)$', text)
    if m and len(m.group(1)) <= 40:
        return f"- **{m.group(1).strip()}** {m.group(2).strip()}"
    return f"- {text}"

print("Framework initialized")
