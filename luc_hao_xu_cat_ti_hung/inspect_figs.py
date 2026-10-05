import json

d = json.load(open('figures_manifest.json', encoding='utf-8'))
with open('fig_list.txt', 'w', encoding='utf-8') as f:
    for fig in d.get('figures', []):
        f.write(f"{fig['id']}: page {fig.get('page')}, num={fig.get('figure_number')}, file={fig.get('file_name')}, caption={fig.get('caption')}\n")
print(f"Exported {len(d.get('figures', []))} figures to fig_list.txt")
