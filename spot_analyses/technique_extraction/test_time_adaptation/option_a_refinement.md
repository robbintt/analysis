# TTA Technique Extraction — Option A (LLM Refinement)

**Date:** 2025-02-14  
**Group:** test_time_adaptation (284 papers)  
**Input:** Option C grep-seeded extraction + full core_contribution review

---

## Merged Categories and Sub-structure

After reviewing all 285 core contributions against the grep-seeded categories, the main findings are:

### Categories to Merge

1. **Test-Time Tuning (C6) + Model Update (C8) + Adapter/LoRA (C9) + State Tuning (C10)** → These are all mechanisms for *what parameters to update*. Merge into a single "Parameter Update Strategies" category with sub-categories for scope (full model, specific layers, adapters, state matrices).

2. **Diffusion/Generative (C31) + Diffusion Guidance (C39)** → Merge into "Diffusion/Generative Model Adaptation" covering both using diffusion priors for TTA and adapting diffusion models themselves at test time.

3. **Prototype/Memory (C12) + Experience/Retrieval (C24)** → Merge into "Memory, Cache & Retrieval" — all non-parametric methods that store and retrieve past information.

### Categories to Split

1. **VLM/Foundation Model (C29, 51 papers)** should split into:
   - **CLIP/VLM Zero-shot Adaptation** (~30 papers) — prompt tuning, cache-based, spectral text adaptation
   - **Foundation Model Robustness** (~12 papers) — corruption robustness, adversarial defense, calibration for VLMs
   - **VLM for Domain-Specific Tasks** (~9 papers) — robotics (QueryAdapter), anomaly detection (SSVP), medical

2. **Continual/Online TTA (C25, 34 papers)** should split into:
   - **Continual TTA with Forgetting Prevention** — dual-teacher (SloMo-Fast), EMA anchors (LATTA), reset strategies (RDumb++)
   - **Dynamic Domain Detection** — online domain-diversity scoring (DATTA), martingale shift detection (M-FISHER)
   - **Streaming/Single-sample TTA** — OATTA, single-sample methods for edge deployment

3. **LLM Adaptation (C30, 31 papers)** should split into:
   - **LLM Test-Time Training** — TTT-Discover, MIGRATE, PERK, TTCS, TTC-RL
   - **LLM Inference-time Strategy** — RAG adaptation, policy optimization, prompt transfer
   - **LLM Agent Adaptation** — belief-space agents, multi-agent collaboration, experience injection

### Categories Grep Missed Entirely

4. **Bayesian/Probabilistic Approaches** (≥8 papers)
   - VCoTTA (2402.08182) — variational Bayesian CTTA
   - BTFL (2503.06633) — dual-Bayesian federated TTA
   - CHBR (2503.15886) — Bayesian concept inference for zero-shot
   - OATTA (2601.21012) — recursive Bayesian filtering
   - LatentTrack (2602.00458) — sequential Bayesian filtering in function space
   - M-FISHER (2510.03839) — martingale-based shift detection
   - OptPO (2512.02882) — Bayesian sequential probability ratio tests
   - PPRM (2602.02229) — prediction-powered risk monitoring

5. **Graph-based TTA** (≥4 papers)
   - GrapHoST (2510.22289) — homophily-weighted test graph construction
   - GOODFormer (2508.00304) — invariant graph representations via entropy-guided attention
   - TT-GDA (2510.07762) — LLM-based graph restoration for domain adaptation
   - Graph anomaly detection (2511.07023) — normality shift in GAD

6. **Causal/Invariance Methods** (≥5 papers)
   - TACT (2510.11133) — causal trimming via PCA on augmented data
   - Bias-as-feature (2507.17001) — theoretical framework for beneficial bias
   - GSAC (2510.21427) — causal representation learning for MARL
   - OOD invariance papers using disentanglement

7. **Curriculum/Self-evolution at Test Time** (≥5 papers)
   - TTCS (2601.22628) — co-evolving question synthesizer + solver
   - TTC-RL (2510.04786) — self-selected curriculum for reasoning
   - TTT-Discover (2601.16175) — RL at test time for scientific discovery
   - VDS-TTT (2505.19475) — continuous self-improvement
   - SOAR (2507.14172) — self-improving program synthesis

8. **Embodied Agent Adaptation** (≥8 papers)
   - EVOLVE-VLA (2512.14666) — VLA test-time training with progress estimation
   - EFN (2510.10181) — experience feedback network for frozen VLA
   - WorMI (2509.03956) — world model implantation for domain adaptation
   - TMoW (2601.22647) — mixture of world models at test time
   - BRIC (2511.20431) — bridging motion planners and physics controllers
   - Diffusion-MPC (2510.04234) — diffusion priors for legged locomotion
   - QueryAdapter (2502.18735) — VLM adaptation for robotic manipulation
   - ZeroGUI (2505.23762) — online learning for GUI agents

9. **Adversarial Robustness via TTA** (≥5 papers)
   - TCA (2506.22819) — calibration against adversarial prompts
   - Panda (2511.10481) — negative data augmentation against corruptions
   - COLA, TTC, etc. from defense survey (2601.12443)
   - ACD (2406.16743) — adversarial contrastive decoding for safety
   - Variance collapse analysis (2510.22127) — understanding corruption effects

---

## Refined Taxonomy (Final 18 Categories)

### Core Adaptation Mechanisms

| # | Category | Papers | Representative IDs | Description |
|---|----------|--------|--------------------|-------------|
| 1 | **Entropy Minimization** | ~12 | 2501.13924, 2509.23183, 2505.16441, 2506.11121, 2510.03258 | Minimizing prediction entropy on unlabeled target data. Includes open-set entropy amplification (AEO), ranked entropy (REM), asymmetric Siamese entropy (ZeroSiam). |
| 2 | **Normalization Layer Adaptation** | ~18 | 2506.06782, 2505.16257, 2505.20890, 2509.04977, 2402.08182, 2511.15276 | Updating/replacing BN statistics. Includes BN refresh, alternative normalizations (GN/LN) for stability, normalization-layer MoE (MoETTA 2511.13760), hierarchical (Hi-Vec 2508.09223). |
| 3 | **Prompt-based Adaptation** | ~18 | 2501.16404, 2506.03190, 2506.22819, 2511.11690, 2601.02147, 2601.23253 | Optimizing visual/text prompts at test time. Sub-families: dynamic prompt selection (DynaPrompt), memory-augmented prompts (MINT), debiased optimization (D2TPT), cross-modal generation (SSVP), attribute-aware (TCA). |
| 4 | **Test-Time Training (TTT)** | ~30 | 2512.23675, 2512.13898, 2601.00894, 2507.05221, 2509.26301, 2507.06415 | Self-supervised auxiliary objectives at test time. Sub-families: long-context TTT (TTT-E2E, qTTT), efficient TTT (PonderTTT with adaptive gating), cross-task alignment (CTA), domain-specific TTT (EEG: NeuroTTT, weather: REE-TTT, depth: Re-Depth). |
| 5 | **Parameter Update Strategies** | ~20 | 2503.23257, 2503.20354, 2510.05530, 2510.05635, 2504.05097, 2512.02441 | What/how to update. Sub-families: selective parameters via Fisher info (FIESTA), activation sparsity (SURGEON), Langevin perturbation (LATTA), embedding re-centering (NEO), spectral subspace (BOLT), state tuning for SSMs. |
| 6 | **Pseudo-labeling / Self-training** | ~15 | 2601.20333, 2506.12481, 2511.16218, 2510.03574, 2505.19361 | Generating and using pseudo-labels for adaptation. Includes topological pseudo-labels (TopoOT), audio-assisted pseudo-labels, Dirichlet prior augmentation for label shift, consensus-based. |

### Supporting Techniques

| # | Category | Papers | Representative IDs | Description |
|---|----------|--------|--------------------|-------------|
| 7 | **Memory, Cache & Retrieval** | ~18 | 2503.23388, 2506.03190, 2601.11669, 2512.11458, 2511.18811, 2510.10181 | Non-parametric storage and retrieval. Sub-families: cache-based classifiers (COSMIC, Skeleton-Cache), prototype refinement (IPEC), memory banks (ADC), retrieval-augmented TTA (RATFM 2506.02081), experience feedback (EFN). |
| 8 | **Feature/Distribution Alignment** | ~14 | 2511.03148, 2510.11133, 2503.02170, 2501.03764, 2505.10641 | Aligning test features to source distributions. Sub-families: quantile recalibration (AQR), causal feature trimming (TACT), sensor optimization (Lens), feature redundancy reduction (FRET), Fourier-space (SPA 2504.08010). |
| 9 | **Knowledge Distillation / Teacher-Student** | ~10 | 2511.18468, 2511.18066, 2512.18321, 2504.01707, 2601.20802 | Teacher-student frameworks for stable adaptation. Dual-teacher (SloMo-Fast), class-wise adaptive (pFedBBN), incremental PCA teacher (CTTA-T), self-distillation (SDPO). |
| 10 | **Calibration & Uncertainty** | ~15 | 2512.07390, 2502.02998, 2505.20362, 2512.14420, 2503.10468 | Confidence calibration and uncertainty estimation at test time. Style-invariance calibration (SICL), OOD dictionary (OODD), VLM safety calibration (VSCBench), DISCODE for image captioning. |
| 11 | **Bayesian / Probabilistic** | ~8 | 2402.08182, 2601.21012, 2503.06633, 2602.00458, 2503.15886 | Bayesian approaches to TTA. Variational (VCoTTA), recursive Bayesian filtering (OATTA), dual-Bayesian federated (BTFL), sequential Bayesian in function space (LatentTrack). |

### Scaling & Architecture Approaches

| # | Category | Papers | Representative IDs | Description |
|---|----------|--------|--------------------|-------------|
| 12 | **Training-free / Gradient-free Methods** | ~20 | 2510.05635, 2510.11068, 2601.23253, 2509.25495, 2512.11458 | No backpropagation required. Embedding re-centering (NEO), CMA-ES in latent subspace (ELaTTA), Brownian distance covariance (TaTa), EM-based (EMO-TTA), non-parametric cache (Skeleton-Cache). |
| 13 | **Routing / MoE Adaptation** | ~8 | 2502.20395, 2511.13760, 2601.02144, 2510.14853, 2506.07033 | Dynamic expert routing at test time. Re-routing via gradient descent (R2-T2), normalization-layer MoE (MoETTA), retrieval-augmented routing (kNN-MoE), self-supervised router optimization. |
| 14 | **Model Merging / Fusion** | ~10 | 2505.16524, 2512.02441, 2512.22467, 2406.03280, 2508.09223 | Combining models/weights. CodeMerge in latent space, spectral bases (BOLT), gradient-free unification (GLUE), task vector sharing (Hi-Vec). |

### Problem Settings

| # | Category | Papers | Representative IDs | Description |
|---|----------|--------|--------------------|-------------|
| 15 | **Continual / Online TTA** | ~35 | 2408.08056, 2601.15544, 2511.18468, 2510.03839, 2505.16441 | Streaming non-stationary data. Forgetting prevention: dual-teacher (SloMo-Fast), EMA anchor (LATTA), drift-triggered resets (RDumb++). Domain detection: domain-diversity score (DATTA), martingale (M-FISHER). Edge/streaming: SNAP, OATTA. |
| 16 | **Source-free Adaptation** | ~12 | 2506.05736, 2509.02982, 2511.12491, 2501.07585, 2511.18660 | No source data access. Calibrated source-free (CSFA), BN refresh + entropy (StableSleep), simulated shift (AFTTA), teacher-student without source (MTDA). |

### Model-type / Domain-specific

| # | Category | Papers | Representative IDs | Description |
|---|----------|--------|--------------------|-------------|
| 17 | **VLM / Foundation Model Adaptation** | ~45 | 2503.23388, 2511.11690, 2512.18504, 2507.03458, 2511.09809 | Largest cluster. CLIP adaptation via prompts, caches, spectral subspaces. Foundation model robustness under corruption/adversarial. VLM for specific domains (robotics, anomaly detection, autonomous driving). |
| 18 | **Embodied Agent / RL Adaptation** | ~20 | 2512.14666, 2510.10181, 2601.22647, 2511.20431, 2510.04786, 2601.16175 | Adapting agents/policies at test time. VLA test-time training (EVOLVE-VLA), world model reconfiguration (TMoW), experience feedback (EFN), RL at test time for reasoning (TTT-Discover, TTC-RL), bandit-based expert selection (Red-Bandit). |

---

## Application Domain Clusters

| Domain | Papers | Representative IDs | Notes |
|--------|--------|--------------------|-------|
| **Medical / Healthcare** | ~12 | 2502.08774, 2503.13012, 2512.06652, 2512.15762, 2508.04552, 2601.13919 | Fetal ultrasound, brain segmentation, ICU prediction, sleep staging, clinical triage. Often source-free or few-shot. |
| **Autonomous Driving / Robotics** | ~10 | 2508.12690, 2505.16524, 2502.18735, 2510.04234, 2512.01300 | Driving under weather shifts, robotic manipulation, legged locomotion. |
| **Audio / Speech** | ~8 | 2506.11121, 2506.07078, 2509.25495, 2601.16240, 2511.22030 | ASR with noise, speech emotion recognition, drowsiness EEG. |
| **Time Series / Forecasting** | ~8 | 2501.04970, 2506.23424, 2510.14814, 2602.01635, 2507.01597 | Non-stationarity handling, concept drift, anomaly detection. |
| **Video / Temporal** | ~6 | 2506.12481, 2510.07940, 2511.22188, 2506.15929 | Video TTA with audio cues, compositional video generation, facial expression. |
| **Federated Learning** | ~8 | 2503.06633, 2505.13643, 2507.21494, 2511.18066, 2511.22305 | Test-time personalization/generalization in federated settings, class imbalance handling. |
| **Malware / Cybersecurity** | ~2 | 2505.18734 | Concept drift in malware detection via masked autoencoder TTA. |
| **Graph / Network** | ~5 | 2510.22289, 2508.00304, 2510.07762, 2511.07023, 2502.18188 | Node classification, anomaly detection, cross-graph adaptation. |

---

## Key Observations

1. **VLM/CLIP adaptation dominates** (~45 papers, 16% of corpus). The 2025 surge reflects the community's pivot toward adapting pre-trained foundation models rather than training task-specific architectures.

2. **TTT is experiencing a renaissance** (~30 papers). Originally proposed for robustness (Sun et al., 2020), TTT is now applied to long-context LLMs (TTT-E2E), scientific discovery (TTT-Discover), and even normalizing flows. The key insight driving this: foundation models are globally underparameterized (2509.24510) — TTT specializes them per instance.

3. **Continual TTA is maturing** (~35 papers). The field has moved beyond simple BN adaptation to sophisticated forgetting-prevention mechanisms: dual-teacher architectures, drift detection, and adaptive resets. Edge deployment constraints (memory, latency) are now first-class concerns.

4. **Entropy minimization is being refined, not replaced**. While the basic TENT approach remains widely used, new variants address its failure modes: collapse prevention (ZeroSiam), ranked structure (REM), open-set awareness (AEO), and combination with LM rescoring (SUTA-LM).

5. **Training-free methods are a growing counter-trend** (~20 papers). As TTA moves to edge devices, methods that avoid backpropagation entirely — embedding re-centering (NEO), CMA-ES (ELaTTA), EM-based (EMO-TTA), cache-based retrieval — are becoming competitive alternatives.

6. **Agent/RL adaptation is an emerging frontier** (~20 papers). Test-time RL for reasoning (TTT-Discover, TTC-RL), world model reconfiguration (TMoW), and VLA training (EVOLVE-VLA) represent a fundamentally different TTA paradigm where adaptation means *behavioral* change, not just feature adjustment.

7. **Federated + TTA intersection** (~8 papers) addresses the practical reality that personalization must happen at test time in privacy-preserving settings.

8. **The 49 unmatched papers** fall into: ARC/reasoning benchmarks (6), tangential surveys (5), empty entries (2), domain-specific papers mentioning TTA peripherally (15), and papers using unique vocabulary for TTA-adjacent concepts (21). The tangential fraction (~20%) aligns with expectations per the procedure.
