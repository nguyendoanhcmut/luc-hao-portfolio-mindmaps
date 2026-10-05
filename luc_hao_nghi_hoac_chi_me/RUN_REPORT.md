# RUN_REPORT: Lục Hào Nghi Hoặc Chỉ Mê (luc_hao_nghi_hoac_chi_me)

## Execution Summary

- **Document Title**: Lục Hào Nghi Hoặc Chỉ Mê
- **Document Slug**: `luc_hao_nghi_hoac_chi_me`
- **Document Type**: `book`
- **Domain**: `luc_hao`
- **Output Language**: `vi`
- **Max Heading Level**: 5

## Pipeline Phases & Timings

1. **Extract & Assets Preparation**:
   - Source text loaded: 68,725 words across 216 pages.
   - Text normalized with continuous `<!-- Page N -->` markers.
   - 234 figures cataloged in `figures_manifest.json`.
   - 9 decorative front/back cover graphics placed in `drop_figures`.
   - 225 active hexagram charts retained and indexed.

2. **Scout Phase**:
   - `branch_scout` invoked (`1c6b24cb-2e53-4d1f-b66a-26cdbc4f33c9`).
   - Skeleton defined: 63 sections (Lời nói đầu + 6 Chương + 56 Câu hỏi).
   - Routing table generated: 57 chunks routed to `fragments/src/`.
   - Manifest created: `luc_hao_nghi_hoac_chi_me_scout_manifest.json`.

3. **Drill Phase**:
   - Generated 57 fragment files in `fragments/`.
   - Strictly enforced all user-mandated rules:
     - 0 Markdown hexagram tables (`| Hào | Can Chi | ...`).
     - 0 `#####` subheadings.
     - Direct `<img>` embedding from `assets/` with exact 6-line evidence blocks.
     - 225 figures consecutively numbered `Hình 1.` through `Hình 225.`.
     - Preserved author-querent dialogues, deduction rationale (Căn cứ - Nhìn vào), and real-world outcomes.

4. **Merge Phase**:
   - Merged via `scripts/merge_fragments.py`.
   - Output tree: `luc_hao_nghi_hoac_chi_me_branches.md` (4,851 lines, 64 headings).
   - Single H1 root: `# Lục Hào Nghi Hoặc Chỉ Mê`.

5. **Audit Phase**:
   - `verify_lineage.py`: **LINEAGE PASSED** (0 errors, 9 non-blocking warnings for dropped cover assets).
   - `branch_verifier` (`f8404568-c988-44d0-ab61-71eb4d66b8b8`): **Score: 1.0** (PASSED).
     - Section coverage: 1.0 (63/63 skeleton headings matched).
     - Depth: 1.0 (3,497 claim bullets across 63 sections).
     - Grounding: 1.0 (225/225 figures embedded under valid anchor claims).
     - Lexicon: 1.0 (16/16 key terms resolved).

6. **Render Phase**:
   - Compiled with `scripts/compile_mindmap.js`.
   - Output HTML: `luc_hao_nghi_hoac_chi_me_branches.html` (240 KB, 3,581 nodes).
   - Verified components: `katex.min.js`, `markmap-view`, `id="theme-toggle"`.

## Metrics Table

| Metric | Value |
|---|---|
| Total Headings | 64 |
| Total Nodes (Mindmap) | 3,581 |
| Active Figures Embedded | 225 |
| Dropped Decorative Figures | 9 |
| Exercises | 0 |
| Completeness Score | 1.00 |
| Lineage Verification | PASSED |
| Warnings | 9 (dropped cover assets) |
