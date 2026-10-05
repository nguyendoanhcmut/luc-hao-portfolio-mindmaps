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
        # Skip table rows
        if ls.startswith('|') and ls.endswith('|'):
            continue
        # Skip hexagram standalone status rows
        if re.match(r'^(?:KIM|MỘC|THỦY|HỎA|THỔ)?\s*(?:Không Vong|Tuần Không)\s*:', ls, re.IGNORECASE):
            continue
        if re.match(r'^(?:KIM|MỘC|THỦY|HỎA|THỔ)\s*$', ls):
            continue
        if ls.startswith('##### '):
            continue
        out.append(l)
    return '\n'.join(out)

def split_into_sections_and_cases(chunk_id, text, assigned_fids):
    cleaned = clean_lines(text)
    paragraphs = [p.strip() for p in cleaned.split('\n\n') if p.strip()]
    return paragraphs

print("Loaded parser")
