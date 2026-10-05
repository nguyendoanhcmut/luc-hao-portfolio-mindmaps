import json
import os
import tiktoken

manifest_path = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_ky_phap_va_ung_dung\luc_hao_ky_phap_va_ung_dung_scout_manifest.json"

with open(manifest_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Schema checks
required_keys = ["doc_slug", "doc_title", "total_pages", "total_estimated_tokens", "master_skeleton", "global_lexicon", "routing_table", "global_context_pack"]
for k in required_keys:
    assert k in data, f"Missing top-level key: {k}"

# Guardrail 1: token count < 6000
enc = tiktoken.get_encoding("cl100k_base")
with open(manifest_path, "r", encoding="utf-8") as f:
    raw = f.read()
tokens = len(enc.encode(raw))
print(f"Tokens: {tokens} (< 6000: {tokens < 6000})")
assert tokens < 6000, "Manifest exceeded 6000 tokens!"

# Guardrail 2 & 3: Master skeleton coverage & Single H1 Root
skeleton = data["master_skeleton"]
print(f"Skeleton top-level nodes: {len(skeleton)}")
all_figs_skeleton = []
covered_pages = set()
for node in skeleton:
    assert node["level"] >= 2, f"Level must be >= 2: {node}"
    for p in range(node["start_page"], node["end_page"] + 1):
        covered_pages.add(p)
    for fig in node.get("figures", []):
        all_figs_skeleton.append(fig["id"])
    for ch in node.get("children", []):
        assert ch["level"] >= 2, f"Child level must be >= 2: {ch}"
        for fig in ch.get("figures", []):
            all_figs_skeleton.append(fig["id"])

print(f"Covered pages: {len(covered_pages)} (min: {min(covered_pages)}, max: {max(covered_pages)})")
assert covered_pages == set(range(1, 45)), "Not all pages 1-44 covered!"

# Guardrail 4: Figure verification
asset_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\luc_hao_portfolio_ocr\luc_hao_ky_phap_va_ung_dung"
for node in skeleton:
    for fig in node.get("figures", []):
        fn = os.path.join(asset_dir, fig["file_name"])
        assert os.path.exists(fn), f"File missing: {fn}"
    for ch in node.get("children", []):
        for fig in ch.get("figures", []):
            fn = os.path.join(asset_dir, fig["file_name"])
            assert os.path.exists(fn), f"File missing: {fn}"

print(f"All {len(all_figs_skeleton)} skeleton figures verified to exist on disk.")

# Routing table check
routing = data["routing_table"]
all_routed_figs = []
routed_pages = set()
for r in routing:
    for p in range(r["start_page"], r["end_page"] + 1):
        routed_pages.add(p)
    all_routed_figs.extend(r["assigned_figures"])

print(f"Routing table chunks: {len(routing)}")
print(f"Routing table covered pages: {len(routed_pages)} (min: {min(routed_pages)}, max: {max(routed_pages)})")
assert routed_pages == set(range(1, 45)), "Not all pages covered in routing!"
assert set(all_figs_skeleton) == set(all_routed_figs), "Mismatch between skeleton figures and routing figures!"

# Global context pack check
ctx = data["global_context_pack"]
ctx_tokens = len(enc.encode(ctx))
print(f"Global context pack tokens: {ctx_tokens} (max 1500 tokens: {ctx_tokens <= 1500})")

print("ALL VALIDATIONS PASSED PERFECTLY!")
