import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("te_thuyet_luc_hao_du_trac_hoc_scout_manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

with open("te_thuyet_luc_hao_du_trac_hoc_branches.md", "r", encoding="utf-8") as f:
    text = f.read()

lexicon = manifest.get('global_lexicon', {})
key_terms = lexicon.get('key_terms', [])
key_entities = lexicon.get('key_entities', [])

print(f"Total key_terms: {len(key_terms)}")
print(f"Total key_entities: {len(key_entities)}")

resolved_terms = []
unresolved_terms = []

for kt in key_terms:
    term_str = kt['term'] if isinstance(kt, dict) else kt
    # Count occurrences in text (case-insensitive)
    matches = len(re.findall(re.escape(term_str), text, re.IGNORECASE))
    if matches > 0:
        resolved_terms.append({'term': term_str, 'count': matches})
    else:
        unresolved_terms.append(term_str)

resolved_entities = []
unresolved_entities = []

for ke in key_entities:
    entity_str = ke['entity'] if isinstance(ke, dict) else ke
    matches = len(re.findall(re.escape(entity_str), text, re.IGNORECASE))
    if matches > 0:
        resolved_entities.append({'entity': entity_str, 'count': matches})
    else:
        unresolved_entities.append(entity_str)

print(f"\nResolved key terms: {len(resolved_terms)} / {len(key_terms)}")
if unresolved_terms:
    print("Unresolved terms:", unresolved_terms)

print(f"Resolved key entities: {len(resolved_entities)} / {len(key_entities)}")
if unresolved_entities:
    print("Unresolved entities:", unresolved_entities)

print("\nSample resolved terms counts:")
for item in resolved_terms[:10]:
    print(f"  {item['term']}: {item['count']} matches")

print("\nSample resolved entities counts:")
for item in resolved_entities:
    print(f"  {item['entity']}: {item['count']} matches")
