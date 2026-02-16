# Multi-Agent Debate — Overview

## Corpus Coverage

- **153 papers** in 2025 corpus (debate/deliberation-focused spin-off)
- Focus: multi-LLM/multi-agent debate frameworks aimed at improving answer quality or robustness

## Phase-0 Definition (final)

Candidate retrieval from `ml_research_analysis_2025/` using phrase anchors:

- `multi-agent debate`
- `llm debate`
- `multi-agent deliberation`
- `debate framework`
- `debate-driven`
- `debate-based`

Scope tightening:
- Removed obvious context-only title classes (`survey`, `review`, `position`, `benchmark`, `technical report`, `literature review`) before final insert.
- Deduplicated by `arxiv_id` in `spot_analysis_paper_groups`.

## Phase-0 Quality Gate

- `DB_COUNT`: **153**
- `papers.md` lines: **153**
- `dup_group_ids`: **0**
- `broken_links`: **0**
- `duplicate_arxiv_rows_in_papers`: **1** (join by filepath in Phase 1 keeps export safe)

Scope smoke test: acceptable precision for debate-focused mechanisms with a moderate tail of domain-heavy applications.

## Extraction Status

- Option C: [option_c_extraction.md](option_c_extraction.md)
- Option A: [option_a_refinement.md](option_a_refinement.md)
- Final merged analysis: [../multi_agent_debate.md](../multi_agent_debate.md)

## Paper List

See [papers.md](papers.md).
