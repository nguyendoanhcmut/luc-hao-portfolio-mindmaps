import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')
m = json.load(open('luc_hao_du_trac_ngo_trung_ngo_scout_manifest.json', encoding='utf-8'))
fm = json.load(open('figures_manifest.json', encoding='utf-8'))
fdict = {f['id']: f for f in fm['figures']}

def inspect_chunk(chunk_id):
    c = next(x for x in m['routing_table'] if x['chunk_id'] == chunk_id)
    raw = open(c['section_text_file'], encoding='utf-8').read()
    print(f"=== CHUNK {chunk_id}: {c['title']} ===")
    
    # Split text by images
    parts = re.split(r'!\[.*?\]\(assets/[^\)]+\)', raw)
    imgs = re.findall(r'!\[(.*?)\]\((assets/[^\)]+)\)', raw)
    print(f"Found {len(parts)} text parts and {len(imgs)} images")
    for i, img in enumerate(imgs):
        fid = c['figure_ids'][i]
        finfo = fdict[fid]
        print(f"\n--- Image {i+1} [fid={fid}, fnum={finfo.get('figure_number')}]: {img[0]} ({img[1]}) ---")
        part_text = parts[i].strip()
        lines = [l for l in part_text.splitlines() if not l.strip().startswith('|') and l.strip()]
        print("Pre-text summary (first 3 lines):")
        for l in lines[:3]:
            print("  ", l[:80])
        print("Pre-text summary (last 3 lines):")
        for l in lines[-3:]:
            print("  ", l[:80])

inspect_chunk('ch02')
