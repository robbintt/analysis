# Phase 0 Notes — Agentic Workflows / Pipeline Design

## Candidate Terms (2025 hit counts)

- agentic workflow (244)
- agent workflow (161)
- agent pipeline (231)
- multi-agent pipeline (121)
- workflow orchestrat* (44)
- planner-executor (27)
- plan-and-execute (15)
- orchestrator agent (40)
- meta-agent (34)
- agent routing (34)
- workflow generation (30)
- workflow design (30)

## Disambiguation

Broad full-text terms pulled many false positives:
- generic "pipeline design" mentions (not agentic orchestration techniques)
- benchmark/survey papers mentioning workflows in passing
- domain application papers where the main novelty is domain adaptation, not workflow design

To improve precision, group membership is defined using `papers.core_contribution` phrase constraints plus LLM gating.

## Final Group Definition (SQL logic)

Include papers whose `core_contribution` mentions one or more mechanism terms:
- agentic workflow / agent workflow / agent pipeline / multi-agent pipeline
- workflow orchestration / workflow generation / workflow design
- planner-executor / plan-and-execute
- orchestrator agent / meta-agent / agent routing / agent scheduler
- OR (multi-agent framework/architecture/agentic framework + workflow/pipeline/orchestration/planner/executor/routing signals)

And require LLM context in `core_contribution`:
- llm / language model / large language model / foundation model

## Result

- 92 unique papers in `spot_analysis_paper_groups` for `agentic_workflow_pipeline_design`
- `papers.md` generated and link-validated
