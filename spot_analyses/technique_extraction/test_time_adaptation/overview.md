# Test-Time Adaptation

## Corpus Coverage

- **284 papers** in 2025 corpus (52K total)
- Group defined by: "test-time adaptation", "test-time training", "TTA", "TTT", and related terms
- Disambiguated from test-time compute scaling (separate group, 987 papers)

## Scope

Techniques for adapting model parameters or behavior to handle distribution shift encountered at deployment, without full retraining.

## Techniques

18 technique categories identified via grep-seeded extraction + LLM refinement. Full details in [test_time_adaptation.md](../test_time_adaptation.md).

### Core Adaptation Mechanisms
1. **Entropy Minimization** (~12) — TENT-style with collapse prevention, ranked structure, open-set variants
2. **Normalization Layer Adaptation** (~18) — BN refresh, alternative norms, MoE over normalizations
3. **Prompt-based Adaptation** (~18) — dynamic prompts, memory-augmented, debiased, training-free
4. **Test-Time Training (TTT)** (~30) — self-supervised at inference; renaissance in long-context LLMs, RL, curricula
5. **Parameter Update Strategies** (~20) — selective (Fisher), sparse activations, Langevin, spectral subspaces
6. **Pseudo-labeling / Self-training** (~15) — topological, audio-assisted, consensus-based pseudo-labels

### Supporting Techniques
7. **Memory, Cache & Retrieval** (~18) — caches, prototypes, experience feedback, retrieval-augmented
8. **Feature / Distribution Alignment** (~14) — quantile recalibration, causal trimming, Fourier-space
9. **Knowledge Distillation / Teacher-Student** (~10) — dual-teacher, incremental PCA, self-distillation
10. **Calibration & Uncertainty** (~15) — style-invariance calibration, OOD detection, active labeling
11. **Bayesian / Probabilistic** (~8) — variational, recursive filtering, martingale shift detection

### Scaling & Architecture
12. **Training-free / Gradient-free** (~20) — embedding re-centering, CMA-ES, EM-based, non-parametric
13. **Routing / MoE Adaptation** (~8) — dynamic routing, normalization-layer MoE, retrieval-augmented
14. **Model Merging / Fusion** (~10) — latent-space merging, spectral bases, task vectors

### Problem Settings
15. **Continual / Online TTA** (~35) — forgetting prevention, drift detection, edge/streaming constraints
16. **Source-free Adaptation** (~12) — no source data access; simulated shifts, calibrated adaptation

### Model-type & Domain-specific
17. **VLM / Foundation Model Adaptation** (~45) — CLIP zero-shot, robustness, cross-modal, domain-specific
18. **Embodied Agent / RL Adaptation** (~20) — VLA training, world model reconfiguration, RL at test time

## Key Findings

1. **VLM/CLIP adaptation dominates** (16% of corpus) — the community has pivoted to adapting pre-trained foundation models rather than training task-specific architectures
2. **TTT renaissance** (~30 papers) — originally for robustness, now applied to long-context LLMs, scientific discovery, and normalizing flows
3. **Training-free methods are growing** (~20 papers) — edge deployment drives gradient-free alternatives
4. **Entropy minimization is refined, not replaced** — new variants fix collapse, rank structure, open-set awareness
5. **Agent/RL adaptation is an emerging frontier** (~20 papers) — behavioral adaptation, not just feature adjustment

## Open Questions

- How to select the right TTA strategy per deployment scenario? RTTC (2508.10024) proposes reward-guided selection but this remains under-explored.
- Theoretical foundations: why does TTT work? (2509.24510) proposes global underparameterization but more work needed.
- Continual TTA stability at scale: dual-teacher and reset methods work but add complexity.
- VLM TTA under adversarial conditions: robustness vs. adaptation tradeoff is poorly understood.

## Paper List

See [papers.md](papers.md) (284 papers).

## Extraction Artifacts

- [option_c_extraction.md](option_c_extraction.md) — grep-seeded categories (41 patterns, 82.7% coverage)
- [option_a_refinement.md](option_a_refinement.md) — LLM refinement pass
- [test_time_adaptation.md](../test_time_adaptation.md) — merged final taxonomy with reconciliation
