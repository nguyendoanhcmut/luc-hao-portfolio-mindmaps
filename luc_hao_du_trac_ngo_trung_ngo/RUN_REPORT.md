# RUN REPORT: Lục Hào Dự Trắc Ngộ Trung Ngộ

- **Document Slug**: `luc_hao_du_trac_ngo_trung_ngo`
- **Document Title**: `Lục Hào Dự Trắc Ngộ Trung Ngộ`
- **Domain**: `luc_hao`
- **Document Type**: `book`
- **Output Language**: `vi`
- **Max Heading Level**: 5

## Timings & Phases

1. **Extract**:
   - Source: `luc_hao_du_trac_ngo_trung_ngo_full.md` (489,562 bytes, 214 pages).
   - Figures Manifest: 174 total extracted assets in `assets/`.
   - Status: PASSED (completed deterministic seam repair).

2. **Page Images**:
   - 214 rasterized page images in `pages/` (page_0001.png - page_0214.png).
   - Status: PASSED.

3. **Scout**:
   - Candidates scan & skeleton definition: 37 clean sections (Lời Tựa + 36 Chương).
   - Routing table: 37 chunks (`ch01` to `ch37`), 172 hexagram figures routed.
   - Status: PASSED.

4. **Drill (Parallel)**:
   - 37 fragments generated in `fragments/`.
   - Banned markdown hexagram tables: Completely removed per user instructions.
   - Evidence blocks: All 172 figures embedded with `<img src="assets/..." />`, `Hình này chứng minh điều gì`, `Từ đâu mà thấy được`.
   - Dialogues & Reasoning: Full preservation of dialogues, deduction steps (Căn cứ - Nhìn vào), and actual verified outcomes.
   - Status: PASSED.

5. **Merge**:
   - Script: `merge_fragments.py`.
   - Output: `luc_hao_du_trac_ngo_trung_ngo_branches.md` (4,585 lines, 230 headings).
   - Status: PASSED.

6. **Audit**:
   - Verification script: `verify_lineage.py`.
   - Lineage Gate: PASSED (0 errors, 2 expected decorative asset warnings).
   - Completeness Score: 1.00 (100% of chapters, cases, and figures routed).

7. **Render**:
   - Compiler: `compile_mindmap.js`.
   - Output: `luc_hao_du_trac_ngo_trung_ngo_branches.html` (197,369 bytes).
   - Node count: 4,218 nodes.
   - Verifications: Katex math, markmap-view runtime, theme toggle verified.
   - Status: PASSED.

## Final Metrics

- **Headings**: 230
- **Figures**: 172
- **Exercises**: 0 (0 passed)
- **Completeness**: 1.00
- **Lineage**: PASSED
- **Warnings**: 2 (Unused decorative cover assets fig_01, fig_02)
