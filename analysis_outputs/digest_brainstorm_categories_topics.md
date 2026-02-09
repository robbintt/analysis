# Brainstorm: Digest Categories & Topics for Mixed-Model / Heterogeneous Multi-Agent Workflows

Generated from `codebase_ripper` pass over this repository (2 iterations).

## 1) Orchestration & Coordination Strategies (Tier 1)
**Why critical:** Core control logic for when/why to invoke multi-agent workflows.

**Topic candidates**
- SAS-first vs MAS-default policy
- Escalation triggers (complexity, uncertainty, disagreement, risk)
- Conditional debate vs always-on debate
- Topology selection (fixed templates vs dynamic search)
- Parallel vs sequential execution and critical-path optimization
- Over-coordination detection (efficiency cliffs)

**Primary source files**
- `lm_council_methodology/standalone_technical_report.md`
- `lm_council_methodology/decision_rules_checklist.md`
- `lm_council_methodology/methodology_do_dont_matrix.md`
- `agents_are_mas_rebranded.md`

---

## 2) Role Specialization & Team Composition (Tier 1)
**Why critical:** Mixed-model systems depend on explicit role boundaries.

**Topic candidates**
- Router / Planner / Spec-Gen / Validator / Ranker / Compressor split
- Heterogeneous role assignment by capability
- Judge-free vs judge-centric debate structures
- Candidate generation diversity policies
- Role handoff schemas and failure fallback

**Primary source files**
- `agents_for_speculative_diffs.md`
- `lm_council_methodology/candidate_methodology_set.md`
- `lm_council_methodology/methodology_do_dont_matrix.md`

---

## 3) Model Routing & Capability Allocation (Tier 1)
**Why critical:** Determines cost/quality frontier in heterogeneous workflows.

**Topic candidates**
- SLM vs LLM routing rules
- Module-wise model assignment (weak planner + strong executor patterns)
- Utility-cost routing objectives
- Confidence/uncertainty-based escalation
- Routing observability and calibration

**Primary source files**
- `lm_council_methodology/implementation_guide_1000_tokens.md`
- `agents_for_speculative_diffs.md`
- `research_analysis_v1/2501.05465_small-language-models-slms-can-still-pack-a-punch-a-survey_20260126_162306.md`

---

## 4) Verification, Consensus, and Selection (Tier 1)
**Why critical:** Main defense against hallucination and weak candidates.

**Topic candidates**
- Multi-verifier consensus vs simple majority
- Verifier-count scaling vs candidate-count scaling under fixed budget
- List-wise verification/merging
- Ranker rubrics (compatibility, schema fidelity, style)
- Confidence-triggered re-try/re-refine loops

**Primary source files**
- `lm_council_methodology/standalone_technical_report.md`
- `lm_council_methodology/method_claim_table.md`
- `agents_for_speculative_diffs.md`
- `grades.md`

---

## 5) Memory & Context Architecture (Tier 1)
**Why critical:** Long-horizon multi-agent systems fail without memory policy discipline.

**Topic candidates**
- Working/episodic/semantic memory splits (Minsky-style references)
- Rolling summaries vs full transcript retention
- Context compression and turn-level pruning
- Drift detection in long debates
- Retrieval-trigger policies (when to re-open evidence)

**Primary source files**
- `OrKa_vs_flatagents.md`
- `lm_council_methodology/decision_rules_checklist.md`
- `agents_for_speculative_diffs.md`
- `research_analysis_v1/2501.05475_retrieval-augmented-generation-by-evidence-retroactivity-in-llms_20260201_162112.md`

---

## 6) Tooling Protocols & MCP Abstractions (Tier 2)
**Why critical:** Reusable tool interfaces are key for model portability and distillation.

**Topic candidates**
- MCP template design patterns
- Tool registry, schema validation, and capability discovery
- Tool-to-agent retrieval patterns
- MCP-Box as reusable capability layer

**Primary source files**
- `agents_for_speculative_diffs.md`
- `MCP_BOX_PLAN.md`

---

## 7) Distillation, Merging, and Knowledge Transfer (Tier 2)
**Why critical:** Enables cheap agents to inherit expensive-agent competence.

**Topic candidates**
- Teacher→student workflows for agent behaviors
- MCP-Box distillation pipeline
- Model merging methods (task vectors, TIES, DARE)
- Reward distillation in model-based control loops

**Primary source files**
- `MCP_BOX_PLAN.md`
- `research_analysis_v1/2408.07666_model-merging-in-llms-a-survey_20260131_170104.md`
- `research_analysis_v1/2501.05329_...`

---

## 8) Safety, Security, and Robustness (Tier 1)
**Why critical:** Control-plane vulnerabilities can collapse routing integrity.

**Topic candidates**
- Control-plane integrity attacks (Confounder Gadgets)
- Router hardening and anomaly detection
- Adversarial weak-link diagnostics across agent chains
- MAS-specific risk taxonomy and governance checks

**Primary source files**
- `research_analysis_v1/2501.01818_we-first-define-llm-control-plane-integrity-i_20260127_211904.md`
- `lm_council_methodology/decision_rules_checklist.md`
- `research_analysis_v1/2511.10949_...`

---

## 9) Retrieval & Knowledge Integration (Tier 2)
**Why critical:** Knowledge freshness and revision quality drive planning accuracy.

**Topic candidates**
- Retroactive reasoning (RetroRAG)
- Evidence revision/redirection loops
- Graph-based retrieval (AST-derived vs extracted KG)
- Enterprise KG integration patterns (RDF/OWL/JSON-LD)

**Primary source files**
- `research_analysis_v1/2501.05475_retrieval-augmented-generation-by-evidence-retroactivity-in-llms_20260201_162112.md`
- `research_analysis_v1/2501.03566_...`
- `research_analysis_v1/2601.08773_...`

---

## 10) Infrastructure & Production Patterns (Tier 2)
**Why critical:** Execution reliability and operability determine real-world viability.

**Topic candidates**
- YAML/state-machine workflow design
- Distributed worker patterns and checkpointing
- Retry/error normalization and idempotency
- Telemetry: token/cost/latency tracking

**Primary source files**
- `OrKa_vs_flatagents.md`
- `agents_for_speculative_diffs.md`
- `frenbot_flatagents_for_dummies.md`

---

## 11) Evaluation Methodology & Benchmarks (Tier 1)
**Why critical:** Prevents cargo-cult MAS adoption.

**Topic candidates**
- Depth vs width task decomposition metrics
- ROI gates (quality delta vs token/cost multiplier)
- Coordination overhead bands (useful vs harmful)
- Test-time scaling in context/batch/turn dimensions

**Primary source files**
- `lm_council_methodology/method_claim_table.md`
- `lm_council_methodology/standalone_technical_report.md`
- `grades.md`

---

## 12) Anti-Patterns / Gotchas Catalog (Tier 1)
**Why critical:** Fastest way to avoid expensive failures.

**Topic candidates**
- MAS-by-default overuse
- Debate on shallow/low-depth tasks
- Over-coordination (> high overhead regimes)
- Sequential assumptions in parallel systems
- Ignoring context drift over long sessions

**Primary source files**
- `lm_council_methodology/method_claim_table.md`
- `lm_council_methodology/methodology_do_dont_matrix.md`
- `lm_council_methodology/decision_rules_checklist.md`

---

## Suggested initial digest build order
1. Orchestration & coordination
2. Role specialization & routing
3. Verification/consensus
4. Safety/control-plane integrity
5. Memory/context management
6. Evaluation + anti-patterns

These six should be the first tranche for 250/500/750/1000/1250/1500-token digest variants.