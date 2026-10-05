import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open("tang_san_boc_dich_binh_thich_scout_manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

rt = manifest.get("routing_table", [])
print(f"Total chunks: {len(rt)}")
batch_size = 15
batches = [rt[i:i + batch_size] for i in range(0, len(rt), batch_size)]
print(f"Total batches of ~15: {len(batches)}")
for b_idx, batch in enumerate(batches):
    ids = [c["chunk_id"] for c in batch]
    figs = sum(len(c.get("figure_ids", [])) for c in batch)
    print(f"Batch {b_idx+1:02d} ({len(batch)} chunks, {figs} figs): {ids[0]} -> {ids[-1]}")
