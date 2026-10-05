import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("driller_wave6.json", "r", encoding="utf-8") as f:
    data = json.load(f)

start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
end = int(sys.argv[2]) if len(sys.argv) > 2 else len(data)

for i in range(start, min(end, len(data))):
    d = data[i]
    print(f"--- ITEM {i}: {d['Role']} ---")
    print(d['Prompt'])
