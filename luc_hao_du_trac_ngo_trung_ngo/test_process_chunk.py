import sys
import os
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

m = json.load(open('luc_hao_du_trac_ngo_trung_ngo_scout_manifest.json', encoding='utf-8'))
fm = json.load(open('figures_manifest.json', encoding='utf-8'))
fdict = {f['id']: f for f in fm['figures']}

def clean_paragraph(p):
    p = p.strip()
    p = re.sub(r'\s+', ' ', p)
    # Remove markdown table lines
    if p.startswith('|') or '|' in p and '---' in p:
        return ''
    # Remove running headers or footnotes
    if p.startswith('---') or p.startswith('LOIHOAPHONG.COM'):
        return ''
    # Remove figure markdown embeds since we will insert evidence blocks
    if re.match(r'^!\[.*?\]\(.*?\)$', p):
        return ''
    return p

def process_chunk(chunk_id):
    c = next(x for x in m['routing_table'] if x['chunk_id'] == chunk_id)
    raw = open(c['section_text_file'], encoding='utf-8').read()
    title = c['title']
    fig_ids = c['figure_ids']
    
    print(f"Processing {chunk_id}: {title} with {len(fig_ids)} figures")

process_chunk('ch02')
