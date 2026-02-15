# TTA Technique Extraction — Final Analysis

**Date:** 2025-02-14  
**Group:** test_time_adaptation (284 papers, 2025 corpus)  
**Grep Coverage:** 235/284 (82.7%)  
**Sources:** [Option C (grep-seeded)](test_time_adaptation/option_c_extraction.md) · [Option A (LLM refinement)](test_time_adaptation/option_a_refinement.md)

---

## Method Summary

Option C cast 41 grep patterns across core_contribution summaries, producing raw category counts with known overlaps. Option A reviewed all 285 summaries to merge overlapping categories, split oversized ones, and identify technique families grep missed entirely. This document reconciles both into a final taxonomy.

---

## Final Taxonomy: 18 Technique Categories

### I. Core Adaptation Mechanisms (6 categories)

#### 1. Entropy Minimization (~12 papers)
**Agreement:** Both extractions identify this as a foundational, well-delineated category.

Minimizing prediction entropy on unlabeled test data. The base technique (TENT-style) remains widely used but 2025 papers focus on fixing its failure modes:
- **Collapse prevention:** Asymmetric Siamese alignment avoids trivial one-hot outputs (ZeroSiam, 2509.23183)
- **Ranked entropy:** Maintaining rank-ordered entropy structure across masking ratios (REM, 2505.16441)
- **Open-set awareness:** Amplifying entropy gap between known/unknown classes (AEO, 2501.13924)
- **Integration with downstream:** Entropy minimization compatible with LM rescoring (SUTA-LM, 2506.11121)

Key papers: 2501.13924, 2505.16441, 2509.23183, 2510.03258, 2506.11121

#### 2. Normalization Layer Adaptation (~18 papers)
**Agreement:** Both identify this clearly. Option A adds the MoE-over-normalizations sub-family.

Updating normalization statistics (BN/GN/LN) to match target distribution. The 2025 literature reveals a maturation arc:
- **Classic BN refresh:** Still the simplest TTA baseline; analyzed theoretically via Edgeworth expansion (2505.16257)
- **Instance-level partitioning:** FIND (2506.06782) partitions feature maps within BN layers by instance statistics
- **Alternative normalizations:** Group/Layer norm shown more stable than BN for TTA (2509.04977)
- **MoE over normalizations:** MoETTA (2511.13760) routes samples to structurally decoupled expert branches within LayerNorm
- **Frequency-aware:** CoDA (2505.20890) combines frequency-aware BN with quantization for on-device deployment
- **Threshold modulation for SNNs:** TM (2505.05375) adapts firing thresholds as a normalization analogue for neuromorphic hardware

Key papers: 2506.06782, 2505.16257, 2509.04977, 2511.13760, 2402.08182, 2511.15276

#### 3. Prompt-based Adaptation (~18 papers)
**Agreement:** Both identify this. Option A reveals rich sub-structure.

Optimizing visual/textual prompts while keeping model weights frozen. Dominant in VLM settings:
- **Dynamic prompt management:** Adaptive selection and growth of prompt pools (DynaPrompt 2501.16404)
- **Memory-augmented prompts:** Key-value prompt banks that accumulate test-time knowledge (MINT 2506.03190)
- **Debiased optimization:** Correcting entropy-driven optimization bias via retrieval and cross-modal consistency (D2TPT 2511.11690)
- **Attribute-aware initialization:** LLM-extracted visual attributes for prompt seeding (TCA 2506.22819)
- **Cross-modal generation:** Vision-conditioned prompt generation for anomaly detection (SSVP 2601.09147)
- **Bilateral debiasing:** Joint visual and textual prompt optimization (BiPrompt 2601.02147)
- **Training-free prompts:** Brownian distance covariance without backprop (TaTa 2601.23253)
- **Backpropagation-free for speech:** Lightweight prompt tuning for speech foundation models (E-BATS 2506.07078)

Key papers: 2501.16404, 2506.03190, 2511.11690, 2601.02147, 2601.23253

#### 4. Test-Time Training (TTT) (~30 papers)
**Agreement:** Both identify this as a major, growing category. Option A reveals the renaissance narrative.

Self-supervised auxiliary objectives applied during inference. The 2025 surge reflects application to new model classes:
- **Long-context LLM TTT:** Compressing context into weights via next-token prediction (TTT-E2E 2512.23675), query-only TTT for attention score dilution (qTTT 2512.13898)
- **Efficient/adaptive TTT:** Using reconstruction loss as gating signal for compute allocation (PonderTTT 2601.00894)
- **TTT + ICL synergy:** Theory showing TTT reduces ICL sample complexity under distribution shift (2503.11842, 2509.25741)
- **RL-based TTT:** Test-time RL for scientific discovery (TTT-Discover 2601.16175), mixed-policy GRPO (MIGRATE 2508.08641)
- **Curriculum-based TTT:** Co-evolving question synthesizer + solver (TTCS 2601.22628), self-selected curricula (TTC-RL 2510.04786)
- **Domain-specific TTT:** EEG (NeuroTTT 2509.26301), weather radar (REE-TTT 2601.01605), depth (Re-Depth 2512.17908), audio (2507.15523), recommendation (T2ARec 2504.01489)
- **Cross-task alignment:** Contrastive alignment between supervised and self-supervised encoders (CTA 2507.05221)
- **Theoretical grounding:** Foundation models as globally underparameterized; TTT specializes per instance (2509.24510)

Key papers: 2512.23675, 2512.13898, 2601.00894, 2601.16175, 2601.22628, 2509.24510

#### 5. Parameter Update Strategies (~20 papers)
**Option A merge:** Combines grep categories C6 (test-time tuning), C8 (model update), C9 (adapter/LoRA), C10 (state tuning). These share the question: *which parameters to update and how*.

- **Selective via Fisher information:** Updating only critical parameters based on importance (FIESTA 2503.23257)
- **Activation sparsity:** Pruning activations during adaptation to reduce memory (SURGEON 2503.20354)
- **Langevin perturbation:** SGLD-inspired weight exploration + EMA anchor (LATTA 2510.05530)
- **Embedding re-centering:** Hyperparameter-free, shifting embeddings to origin (NEO 2510.05635)
- **Spectral bases:** Orthogonal task-informed subspaces with diagonal coefficients (BOLT 2512.02441)
- **State tuning:** Optimizing internal state matrices in RNN/SSM architectures (2504.05097)
- **Low-rank adaptation:** LoRA/adapter modules as the adaptation substrate
- **Gradient-free ODE:** HyperFlow (2504.15323) replaces gradient-based optimization with ODE solving
- **Energy-based:** Residual energy function with preference optimization (2505.19607)

Key papers: 2503.23257, 2503.20354, 2510.05530, 2510.05635, 2512.02441

#### 6. Pseudo-labeling / Self-training (~15 papers)
**Agreement:** Both identify this, with Option A adding nuance on label generation strategies.

Generating and leveraging pseudo-labels for adaptation:
- **Topological pseudo-labels:** Persistence diagram-based supervision for anomaly segmentation (TopoOT 2601.20333)
- **Audio-assisted pseudo-labels:** Using audio cues from video to generate visual labels (2506.12481)
- **Label shift handling:** Dirichlet prior augmentation for unknown test-time class distributions (2511.16218)
- **Consensus-based:** Aggregating augmented views for pseudo-label generation (2510.03574)
- **Consistency-based abduction:** Multi-model consistency for error detection (2505.19361)

Key papers: 2601.20333, 2506.12481, 2510.03574, 2505.19361

---

### II. Supporting Techniques (5 categories)

#### 7. Memory, Cache & Retrieval (~18 papers)
**Option A merge:** Combines grep categories C12 (prototype/memory) and C24 (experience/retrieval).

Non-parametric methods that store and retrieve information:
- **Cache-based classification:** Dual semantics graph with clique-guided querying (COSMIC 2503.23388)
- **Skeleton descriptor caches:** Non-parametric action recognition (Skeleton-Cache 2512.11458)
- **Prototype refinement:** Incremental prototype updates from high-confidence queries (IPEC 2601.11669)
- **Diversity caches:** Class-specific caches for long-tail HOI detection (ADC 2511.18811)
- **Experience feedback:** Retrieving prior trajectories for residual corrections (EFN 2510.10181)
- **Retrieval-augmented:** RAG for time series anomaly detection (RATFM 2506.02081), TTT on nearest neighbors (2511.16691)
- **Memory prompt banks:** Accumulating key-value prompt pairs (MINT 2506.03190)

Key papers: 2503.23388, 2512.11458, 2601.11669, 2510.10181, 2506.02081

#### 8. Feature / Distribution Alignment (~14 papers)
**Agreement:** Both identify this, with Option A adding causal methods.

Aligning test-time feature distributions to source:
- **Quantile recalibration:** Nonparametric quantile transforms across normalization types (AQR 2511.03148)
- **Causal trimming:** PCA-based removal of non-causal feature directions (TACT 2510.11133)
- **Sensor optimization:** Optimizing camera parameters to reduce domain shift at capture time (Lens 2503.02170)
- **Feature redundancy reduction:** GCN + contrastive to eliminate redundant features (FRET 2505.10641)
- **Fourier-space:** Self-bootstrapping from Fourier-deteriorated views (SPA 2504.08010)
- **Spectral text adaptation:** SVD of text embeddings for zero-shot VLM adaptation (2511.09809)
- **Multi-modal re-alignment:** Progressive unimodal-then-crossmodal alignment (BriMPR 2511.22862)

Key papers: 2511.03148, 2510.11133, 2503.02170, 2505.10641, 2504.08010

#### 9. Knowledge Distillation / Teacher-Student (~10 papers)
**Agreement:** Both identify this.

Teacher-student architectures for stable adaptation:
- **Dual-teacher:** Fast-teacher for adaptation + slow-teacher for retention (SloMo-Fast 2511.18468)
- **Class-wise adaptive:** Per-class BN statistics with confidence-filtered distillation (pFedBBN 2511.18066)
- **Incremental PCA teacher:** Domain-aware teacher with cross-domain PCA accumulation (CTTA-T 2512.18321)
- **Context distillation:** Transferring in-context knowledge to permanent parameters (InfiniteICL 2504.01707)
- **Self-distillation:** Using current model as self-teacher with feedback-driven credit assignment (SDPO 2601.20802)

Key papers: 2511.18468, 2512.18321, 2504.01707

#### 10. Calibration & Uncertainty (~15 papers)
**Agreement:** Both identify this.

Confidence calibration and uncertainty estimation at test time:
- **Style-invariance calibration:** Measuring prediction consistency across style-altered variants (SICL 2512.07390)
- **OOD detection dictionary:** Priority queue of OOD features accumulated during testing (OODD 2503.10468)
- **Uncertainty in CTTA:** Addressing pseudo-label uncertainty in continual settings (2502.02998)
- **Adaptive scoring:** Gaussian prior for robust evaluation scores (DISCODE 2512.14420)
- **Binary feedback:** Using correct/incorrect feedback for guided adaptation (BiTTA 2505.18514)
- **Active labeling:** Minimal annotation for long-term TTA stability (EATTA 2503.14564)

Key papers: 2512.07390, 2503.10468, 2502.02998, 2505.18514

#### 11. Bayesian / Probabilistic (~8 papers)
**Grep missed this entirely.** Option A identified it as a coherent family.

Probabilistic frameworks for TTA:
- **Variational Bayesian CTTA:** Modeling uncertainty in continual adaptation (VCoTTA 2402.08182)
- **Recursive Bayesian filtering:** Temporal prior via transition matrix (OATTA 2601.21012)
- **Dual-Bayesian federated:** Beta-Bernoulli interpolation for personalization (BTFL 2503.06633)
- **Sequential filtering in function space:** Latent state tracking via hypernetwork (LatentTrack 2602.00458)
- **Bayesian concept inference:** Importance sampling over infinite concept space (CHBR 2503.15886)
- **Martingale shift detection:** Statistical tests for distribution change (M-FISHER 2510.03839)
- **Sequential probability ratio:** Adaptive rollout budgets (OptPO 2512.02882)

Key papers: 2402.08182, 2601.21012, 2503.06633, 2602.00458

---

### III. Scaling & Architecture Approaches (3 categories)

#### 12. Training-free / Gradient-free Methods (~20 papers)
**Agreement:** Both identify this as a significant counter-trend.

Methods avoiding backpropagation, critical for edge deployment:
- **Embedding operations:** Re-centering (NEO 2510.05635), Brownian distance covariance (TaTa 2601.23253)
- **Evolutionary optimization:** CMA-ES in principal latent subspace (ELaTTA 2510.11068)
- **EM-based:** Incremental class-conditional statistics update (EMO-TTA 2509.25495)
- **Non-parametric retrieval:** Cache-based classification without parameter updates (Skeleton-Cache 2512.11458)
- **Sensor-level:** Optimizing image capture quality as a proxy for adaptation (Lens 2503.02170)
- **Prompt transfer:** PromptBridge (2512.01420) maps prompts across models without re-optimization
- **Gradient-free ODE:** Replacing gradient-based fine-tuning with numerical integration (HyperFlow 2504.15323)

Key papers: 2510.05635, 2510.11068, 2509.25495, 2601.23253, 2512.11458

#### 13. Routing / MoE Adaptation (~8 papers)
**Agreement:** Both identify this, with Option A adding papers.

Dynamic expert routing at test time:
- **Gradient-based re-routing:** Neighborhood optimization of routing weights (R2-T2 2502.20395)
- **Normalization-layer MoE:** Structurally decoupled expert branches within LayerNorm (MoETTA 2511.13760)
- **Retrieval-augmented routing:** Memory of optimal expert assignments (kNN-MoE 2601.02144)
- **Self-supervised routing:** In-context loss for router logit optimization (2510.14853)
- **Expert aggregation:** Test-time self-supervised aggregation for imbalanced regression (MATI 2506.07033)
- **Attention routing:** Elastic attention with head-level sparse/full routing (2601.17367)

Key papers: 2502.20395, 2511.13760, 2601.02144, 2510.14853

#### 14. Model Merging / Fusion (~10 papers)
**Agreement:** Both identify this.

Combining model weights at test time:
- **Latent-space merging:** Compact codebook representation for efficient merging (CodeMerge 2505.16524)
- **Spectral bases:** Orthogonal task-informed subspaces (BOLT 2512.02441)
- **Gradient-free unification:** GLUE (2512.22467) avoids full-gradient optimization for expert combination
- **Task vector sharing:** Hierarchical adapted weight propagation (Hi-Vec 2508.09223)
- **Benchmark:** FusionBench (2406.03280) for systematic evaluation of fusion techniques

Key papers: 2505.16524, 2512.02441, 2512.22467, 2406.03280

---

### IV. Problem Settings (2 categories)

#### 15. Continual / Online TTA (~35 papers)
**Agreement:** Largest setting category. Option A reveals three clear sub-families.

Adaptation over streaming, non-stationary data:
- **Forgetting prevention:** Dual-teacher (SloMo-Fast 2511.18468), EMA anchors (LATTA 2510.05530), ranked entropy structure (REM 2505.16441), drift-triggered resets (RDumb++ 2601.15544)
- **Domain detection:** Domain-diversity scoring (DATTA 2408.08056), martingale shift detection (M-FISHER 2510.03839), entropy/KL-based drift detection (RDumb++ 2601.15544)
- **Edge/streaming constraints:** Memory-efficient BN adaptation (2502.20677), sparse adaptation (SNAP 2511.15276), single-sample filtering (OATTA 2601.21012)
- **Benchmarking:** BoTTA (2504.10149) for practical mobile constraints, DHAuDS (2511.18421) for audio domain shifts

Key papers: 2408.08056, 2511.18468, 2510.05530, 2601.15544, 2510.03839

#### 16. Source-free Adaptation (~12 papers)
**Agreement:** Both identify this.

No source data available during adaptation:
- **Calibrated source-free:** CSFA (2506.05736) for evolving streams with concept drift and class evolution
- **BN + entropy:** StableSleep (2509.02982) with entropy gate and EMA reset for safety
- **Simulated shift:** AFTTA (2511.12491) uses off-the-shelf domain transformations to simulate potential shifts
- **Teacher-student without source:** MTDA (2501.07585) for computation offloading in MEC systems
- **Open-set source-free:** PAF+KIP (2508.18751) for stabilizing adaptation with open-set samples

Key papers: 2506.05736, 2509.02982, 2511.12491, 2501.07585

---

### V. Model-type & Domain-specific (2 categories)

#### 17. VLM / Foundation Model Adaptation (~45 papers)
**Agreement:** Both identify this as the largest cluster. Option A proposes splitting but given the interconnections, keeping as one category with clear sub-families is preferable.

Largest technique cluster, reflecting 2025's focus on adapting pre-trained models:
- **CLIP zero-shot adaptation:** Prompt tuning (DynaPrompt, D2TPT, BiPrompt), cache-based (COSMIC), spectral text adaptation (2511.09809), pseudo-word synthesis (GTMA 2512.18504)
- **Foundation model robustness:** Variance collapse analysis (2510.22127), negative data augmentation (Panda 2511.10481), adversarial defense (2601.12443 survey), receptive field recalibration (D&D 2507.03458)
- **VLM for specific domains:** Robotics (QueryAdapter 2502.18735), anomaly detection (SSVP 2601.09147, RAP 2508.10556), medical (HyperWalker 2601.13919), autonomous driving (RoboDriveBench 2512.01300)
- **Cross-modal TTA:** Multi-modal TTA under complex noise (2503.02616), progressive re-alignment (BriMPR 2511.22862), attention-based warping (AttWarp 2510.09741)
- **Survey:** Comprehensive taxonomy of unsupervised VLM adaptation (2508.05547)

Key papers: 2503.23388, 2511.11690, 2512.18504, 2507.03458, 2510.22127

#### 18. Embodied Agent / RL Adaptation (~20 papers)
**Grep partially captured this across reinforcement (C33) and autonomous (C35). Option A identified it as a coherent emerging family.**

Test-time behavioral adaptation for agents:
- **VLA test-time training:** Learning from environment interaction with progress estimation (EVOLVE-VLA 2512.14666)
- **World model reconfiguration:** Multi-granular prototype routing for world model mixtures (TMoW 2601.22647)
- **Experience feedback:** Residual corrections from retrieved trajectories (EFN 2510.10181)
- **Diffusion priors for control:** Diffusion-MPC for legged locomotion (2510.04234)
- **RL at test time:** Scientific discovery (TTT-Discover 2601.16175), curriculum for reasoning (TTC-RL 2510.04786), online GRPO for black-box optimization (MIGRATE 2508.08641)
- **Bandit-based selection:** Multi-armed bandit over LoRA attack experts (Red-Bandit 2510.07239)
- **Reward-guided strategy:** Selecting between direct inference, RAG, and TTT per query (RTTC 2508.10024)
- **Multi-agent:** Test-time experience injection with credit assignment (MATTRL 2601.09667)
- **Meta-RL for safety:** Adaptive policy refinement in constrained MDPs (2601.21845)

Key papers: 2512.14666, 2601.22647, 2510.10181, 2601.16175, 2510.04786

---

## Application Domain Summary

| Domain | ~Papers | Key Theme |
|--------|---------|-----------|
| Medical / Healthcare | 12 | Source-free adaptation across scanner/modality shifts; morphological priors for segmentation |
| Autonomous / Robotics | 10 | Weather/condition robustness; VLM adaptation for manipulation |
| Audio / Speech | 8 | Noise adaptation for ASR; emotion recognition under speaker variability |
| Time Series | 8 | Non-stationarity; concept drift; parameter-efficient forecasting adaptation |
| Federated Learning | 8 | Privacy-preserving test-time personalization; class imbalance handling |
| Graph / Network | 5 | Node classification under structure shift; anomaly detection |
| Video / Temporal | 6 | Audio-visual pseudo-labels; compositional generation |

---

## Where the Extractions Agree (High Confidence)

These categories are well-supported by both grep frequency and semantic review:
- Entropy Minimization (core, refined)
- Normalization Layer Adaptation (core, well-studied)
- Prompt-based Adaptation (large, rich sub-structure)
- TTT (large, growing, well-delineated)
- Continual/Online TTA (large setting category)
- VLM/Foundation Model (largest cluster)
- Training-free Methods (clear counter-trend)

## What the LLM Added

- **Bayesian/Probabilistic** as a coherent family (8 papers grep couldn't catch)
- **Embodied Agent/RL Adaptation** as a unified emerging category spanning grep's reinforcement + autonomous
- **Sub-family structure** within TTT (long-context, curriculum, RL-based), prompts (debiased, memory-augmented), and continual TTA (forgetting prevention, drift detection, edge constraints)
- **Merges:** Parameter update strategies (4 grep categories → 1), Memory/Cache/Retrieval (2 → 1)

## What the LLM Disagrees With

- **Grep's domain_shift category (66 papers):** This is a problem description, not a technique. Dropped as a standalone category; domain shift is the *motivation* for all 18 technique categories.
- **Grep's video_temporal (48 papers):** Inflated by broad temporal patterns. Most papers are better classified by their *technique* (TTT, prompt, etc.) with video/temporal as an application note.
- **Grep's separate diffusion categories:** Merged into a sub-family within TTT (diffusion-based TTT) and parameter update strategies (diffusion guidance), not a standalone technique category at this corpus size.

---

## Coverage Reconciliation

| | Count |
|---|---|
| Total papers in group | 284 |
| Grep-matched (Option C) | 235 (82.7%) |
| Semantically classifiable (Option A) | ~250 (88%) |
| Clearly tangential | ~25 (9%) |
| Empty/malformed entries | ~4 (1.5%) |
| Unique vocabulary, partially classifiable | ~5 (1.5%) |
