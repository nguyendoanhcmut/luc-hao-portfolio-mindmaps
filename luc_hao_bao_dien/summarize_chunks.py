import json

with open("scratch_manifest_test.json", "r", encoding="utf-8") as f:
    mf = json.load(f)

chunks = mf.get("routing_table", [])
print(f"Total chunks: {len(chunks)}")

with open("scratch_chunks_summary.txt", "w", encoding="utf-8") as out:
    for c in chunks:
        cid = c["chunk_id"]
        title = c["title"]
        parents = " > ".join(c.get("parent_titles", []))
        figs = len(c.get("figure_ids", []))
        exs = len(c.get("exercises", []))
        # Get word count from section_text_file
        w_cnt = 0
        try:
            with open(c["section_text_file"], "r", encoding="utf-8") as tf:
                w_cnt = len(tf.read().split())
        except Exception:
            pass
        out.write(f"[{cid:8s}] ({w_cnt:5d}w | {figs:2d} figs | {exs:2d} exs) {parents + ' > ' if parents else ''}{title}\n")
