import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')
m = json.load(open('luc_hao_du_trac_ngo_trung_ngo_scout_manifest.json', encoding='utf-8'))
for c in m['routing_table']:
    src = open(c['section_text_file'], encoding='utf-8').read()
    imgs = re.findall(r'!\[(.*?)\]\((assets/[^\)]+)\)', src)
    print(f"{c['chunk_id']:5s}: {c['title'][:35]:35s} | figs in src: {len(imgs):2d} | manifest figs: {len(c['figure_ids']):2d}")
