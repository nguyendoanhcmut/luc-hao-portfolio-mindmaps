import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("portfolio_manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

for i, book in enumerate(manifest["books"], 1):
    print(f"{i:2d}. {book['file']}: {book['total_pages']} pages -> {book['worker_pairs']} worker pairs")
