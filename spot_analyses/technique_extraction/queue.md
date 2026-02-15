# Technique Extraction Queue

Tracks planned, in-progress, and completed extractions. See [topic_selection_and_scoping.md](topic_selection_and_scoping.md) for how topics are chosen and scoped, and [technique_extraction_procedure.md](technique_extraction_procedure.md) for how extractions are executed.

---

## Completed

| Group | Papers | Scope | Notes |
|---|---|---|---|
| `test_time_compute_scaling` | 987 | Techniques for allocating additional compute at inference to improve output quality — reasoning budgets, search strategies, verification, self-consistency. | 20 grep categories → 3-tier taxonomy, 76.4% coverage. Artifacts: [analysis](test_time_compute_scaling.md), [papers](test_time_compute_scaling/papers.md), [option C](test_time_compute_scaling/option_c_extraction.md), [option A](test_time_compute_scaling/option_a_refinement.md). |
| `test_time_adaptation` | 284 | Techniques for adapting model parameters or behavior at deployment to handle distribution shift without full retraining. | 41 grep patterns (Option C), 82.7% coverage (235/284), merged into 18-category final taxonomy. Artifacts: [analysis](test_time_adaptation.md), [papers](test_time_adaptation/papers.md), [option C](test_time_adaptation/option_c_extraction.md), [option A](test_time_adaptation/option_a_refinement.md). Separate from TTC scaling despite shared "test-time" prefix. |

## In Progress

(none)

## Queued

Priority order. Top = next.

### 1. `multi_agent_debate`

- **Scope:** Multi-LLM debate/deliberation frameworks for improving output quality through structured argumentation.
- **Est. papers:** ~170
- **Source:** Decomposed from "agentic orchestration" investigation. Also identified as a Tier 1 TTC technique in `test_time_compute_scaling` extraction.
- **Dependencies:** None (but extends TTC analysis).
- **Decomposition notes:** "Agentic orchestration" (~1040 LLM papers) split into 3 groups: this one, `agentic_workflow_design`, and `multi_agent_collaboration`. Debate is the cleanest and most technique-focused.

### 2. `agentic_workflow_design`

- **Scope:** Designing, generating, and optimizing agent workflow graphs — conductor models, planner-executor patterns, auto-MAS design, workflow generation.
- **Est. papers:** ~250
- **Source:** Decomposed from "agentic orchestration" investigation.
- **Dependencies:** None, but contrast with `multi_agent_debate` (debate is a specific technique; workflows are the meta-layer).
- **Decomposition notes:** May need further scoping. "Workflow" is broad — check whether it splits into "workflow generation/optimization" (the technique) vs. "workflow applications" (domain).

### 3. `process_reward_models`

- **Scope:** Step-level reward signals for evaluating intermediate reasoning steps — PRM training, PRM-guided search, PRM scaling.
- **Est. papers:** ~32 (from TTC grep), likely more with expanded terms.
- **Source:** Sub-category of `test_time_compute_scaling` verification cluster (435 papers).
- **Dependencies:** Builds on `test_time_compute_scaling`.
- **Decomposition notes:** The TTC extraction found 32 papers via core_contribution grep. Full-text search will likely surface 80-150+.

### 4. `reasoning_distillation`

- **Scope:** Compressing expensive test-time compute reasoning into smaller/faster models — teacher-student for reasoning, CoT distillation, reasoning compression.
- **Est. papers:** ~45 (from TTC grep), likely more.
- **Source:** Tier 2 enabling technique in `test_time_compute_scaling`.
- **Dependencies:** Builds on `test_time_compute_scaling`.

### 5. `adaptive_compute_allocation`

- **Scope:** Dynamic inference compute budgeting — overthinking mitigation, query-adaptive allocation, early exit, difficulty routing, compute scaling laws.
- **Est. papers:** ~50 (from TTC grep), likely more.
- **Source:** Tier 1 technique in `test_time_compute_scaling`.
- **Dependencies:** Builds on `test_time_compute_scaling`.

### 6. `multi_agent_collaboration`

- **Scope:** Teams of specialized LLM agents coordinating on tasks — role-based agents, agent teaming, cooperative multi-agent LLM systems.
- **Est. papers:** ~300
- **Source:** Decomposed from "agentic orchestration" investigation.
- **Dependencies:** After `multi_agent_debate` and `agentic_workflow_design` to avoid overlap.
- **Decomposition notes:** Likely needs further decomposition — bleeds into RL multi-agent and robotics. Restrict to LLM-based collaboration.

### 7. `continual_online_tta`

- **Scope:** Continual and online test-time adaptation under non-stationary streams — drift detection, forgetting prevention, reset strategies, streaming constraints.
- **Est. papers:** ~35 in parent extraction, likely 60–120 standalone.
- **Source:** **Spin-off from `test_time_adaptation` extraction** (18-category final taxonomy).
- **Dependencies:** Builds on `test_time_adaptation`.
- **Decomposition notes:** Keep focus on adaptation mechanics; exclude generic continual learning papers without explicit test-time adaptation.

### 8. `vlm_tta`

- **Scope:** Test-time adaptation for vision-language/foundation models — prompt tuning, cache/retrieval, calibration, corruption robustness.
- **Est. papers:** ~45 in parent extraction, likely 80–150 standalone.
- **Source:** **Spin-off from `test_time_adaptation` extraction**.
- **Dependencies:** Builds on `test_time_adaptation`.
- **Decomposition notes:** High overlap with prompt and training-free methods. Consider whether to keep as umbrella or split into `vlm_prompt_tta` and `vlm_cache_tta` after Phase 0 sampling.

### 9. `prompt_based_tta`

- **Scope:** Prompt-centric test-time adaptation across modalities — dynamic prompt tuning, memory prompts, debiased prompt optimization, test-time prompt transfer.
- **Est. papers:** ~18 in parent extraction, likely 35–80 standalone.
- **Source:** **Spin-off from `test_time_adaptation` extraction**.
- **Dependencies:** Builds on `test_time_adaptation`; overlaps with `vlm_tta`.
- **Decomposition notes:** Keep this technique-first (prompt mechanism), not model-family-first.

### 10. `training_free_tta`

- **Scope:** Training-free or gradient-free test-time adaptation — embedding transforms, EM updates, CMA-ES/subspace search, cache/prototype adaptation.
- **Est. papers:** ~20 in parent extraction, likely 40–90 standalone.
- **Source:** **Spin-off from `test_time_adaptation` extraction**.
- **Dependencies:** Builds on `test_time_adaptation`.
- **Decomposition notes:** Distinguish from lightweight gradient methods; include only methods explicitly avoiding backprop at deployment.

---

## Parking Lot

Topics noted but not yet scoped or volume-checked.

- **Diffusion language models** — DLLMs as an alternative architecture for reasoning. ~15 papers in TTC extraction, possibly more in full corpus.
- **Latent/implicit reasoning** — Models that reason without explicit token generation. ~8 papers in TTC, niche but growing.
- **Speculative decoding for reasoning** — Draft-verify pipelines specifically for reasoning (not just speed). ~12 papers.
- **RL for reasoning** — Broad (102 in TTC), but worth isolating GRPO/PPO-specific techniques.
- **Retrieval-augmented reasoning** — RAG specifically for reasoning tasks (not general RAG). Needs disambiguation.
- **Code generation agents** — ~173 papers. Domain application but large enough for extraction.
- **Web/GUI agents** — ~296 papers. Domain application.
- **Scientific research agents** — ~144 papers. Domain application.
