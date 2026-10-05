import json, re, sys, subprocess
sys.stdout.reconfigure(encoding='utf-8')

md_path = 'tang_san_boc_dich_binh_thich_branches.md'
html_path = 'tang_san_boc_dich_binh_thich_branches.html'

md_lines = open(md_path, encoding='utf-8').readlines()
headings = [l for l in md_lines if l.strip().startswith('#')]
H = len(headings)

img_pat = re.compile(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]|!\[[^\]]*\]\(([^)\s]+)\)')
figs = set()
for l in md_lines:
    for m in img_pat.finditer(l):
        figs.add(m.group(1) or m.group(2))
F = len(figs)

mf = json.load(open('tang_san_boc_dich_binh_thich_scout_manifest.json', encoding='utf-8'))
total_exercises = 0
for c in mf['routing_table']:
    total_exercises += len(c.get('exercises', []))
E = total_exercises

# Run verify_lineage to get warnings count
proc = subprocess.run(['python', r'C:\Users\Admin\.gemini\config\skills\branches\scripts\verify_lineage.py', '.'], capture_output=True, text=True, encoding='utf-8')
warn_lines = [l for l in proc.stdout.splitlines() if l.startswith('[WARN]')]
fail_lines = [l for l in proc.stdout.splitlines() if l.startswith('[FAIL]')]
N = len(warn_lines)

print(f"Headings (H): {H}")
print(f"Figures (F): {F}")
print(f"Exercises (E): {E}")
print(f"Failures: {len(fail_lines)}")
print(f"Warnings (N): {N}")
