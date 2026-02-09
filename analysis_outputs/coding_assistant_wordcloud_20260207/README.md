# Coding Assistant Word Cloud (2026-02-07)

## Output files
- `coding_assistant_wordcloud.png` — rendered word cloud image
- `top_terms.csv` — raw term frequencies
- `top_terms_weighted.csv` — weighted frequencies used for visualization balance
- `selected_sources.txt` — source files/chunks used
- `metadata.json` — corpus statistics and top terms

## Corpus used
- `research_analysis_v2/*.md`
- `research_analysis_bulk_20260203_parts/part_*.txt` (chunked)

## Selection method (topic-focused)
Included paragraphs that mention coding-assistant related signals (e.g., code generation, software engineering, debugging, repository/codebase, SWE-bench, HumanEval, programming/developer terms) plus assistant context (agent/assistant/LLM/tool-use/function-calling).

## Snapshot (top raw terms)
- llm (388)
- agent (275)
- code (158)
- reasoning (124)
- multi_agent (110)
- agentic (89)
- developers (83)
- code_generation (81)
- programming (65)
- execution (64)
- safety (62)
- tools (56)
- autonomous (52)
- repository (42)
- software_engineering (41)
- debugging (25)
- planning (23)
- workflow (22)

