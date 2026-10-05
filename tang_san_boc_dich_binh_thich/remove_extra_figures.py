import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

mf = json.load(open('tang_san_boc_dich_binh_thich_scout_manifest.json', encoding='utf-8'))
fmf = json.load(open('figures_manifest.json', encoding='utf-8'))
by_id = {f['id']: f['rel_path'] for f in fmf['figures']}
routing = {c['chunk_id']: c for c in mf['routing_table']}

targets = ['ch22_0', 'ch22_1', 'ch22_3', 'ch23', 'ch30', 'ch31', 'ch34', 'ch35_0', 'ch37', 'ch38', 'ch40', 'ch41_1', 'ch41_3']

for cid in targets:
    sec = routing[cid]
    ff = sec['fragment_file']
    assigned = [by_id[fid] for fid in sec.get('figure_ids', []) if fid in by_id]
    
    lines = open(ff, encoding='utf-8').readlines()
    new_lines = []
    i = 0
    removed_count = 0
    
    while i < len(lines):
        line = lines[i]
        # Check if line starts a figure block: e.g. "  - **Hình N.**" or "- **Hình N.**"
        m_fig = re.match(r'^(\s*)-\s*\*\*Hình\s+\d+\.\*\*', line)
        if m_fig:
            indent_len = len(m_fig.group(1))
            # collect all lines of this figure block
            fig_lines = [line]
            j = i + 1
            while j < len(lines):
                next_line = lines[j]
                if not next_line.strip():
                    fig_lines.append(next_line)
                    j += 1
                    continue
                next_indent_len = len(next_line) - len(next_line.lstrip())
                # If next line is deeper indent, it belongs to figure block
                if next_indent_len > indent_len:
                    fig_lines.append(next_line)
                    j += 1
                else:
                    break
            
            fig_text = "".join(fig_lines)
            # check image src in fig_text
            m_img = re.search(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', fig_text)
            img_src = m_img.group(1) if m_img else None
            
            if img_src and img_src not in assigned:
                # This is an extra figure! Remove it.
                print(f"[{cid}] Removing extra figure: {img_src}")
                removed_count += 1
                # If previous line in new_lines was a standalone anchor line introducing only this figure, e.g. "- Minh họa ...:\n"
                if len(new_lines) > 0:
                    prev = new_lines[-1].strip()
                    if re.match(r'^-\s*(Minh họa|Sơ đồ|Tương tác|Hình ảnh).*:$', prev, re.IGNORECASE):
                        print(f"[{cid}] Also removing anchor line: {prev}")
                        new_lines.pop()
                i = j
                continue
            else:
                new_lines.extend(fig_lines)
                i = j
                continue
        else:
            new_lines.append(line)
            i += 1
            
    open(ff, 'w', encoding='utf-8').writelines(new_lines)
    print(f"[{cid}] Done. Removed {removed_count} figures.")

