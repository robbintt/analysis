# TTA Technique Extraction — Option C (Grep-Seeded)

**Date:** 2025-02-14
**Group:** test_time_adaptation (284 papers)
**Coverage:** 235/284 matched (82.7%)
**Unmatched:** 49 papers — predominantly tangential (ARC benchmarks, surveys, drug discovery, molecular generation, fake news detection, drone racing) that mention TTA in passing but don't propose TTA techniques.

---

## Core Adaptation Mechanisms

### 1. Entropy Minimization (8 papers)
Minimizes prediction entropy on unlabeled target data to encourage confident predictions. Classic TTA baseline (TENT, etc.).

### 2. Pseudo-labeling / Self-training (18 papers)
Generates pseudo-labels from model predictions on target data, then uses them as supervision for adaptation. Includes self-supervised variants and noisy label handling.

### 3. Batch Normalization Adaptation (12 papers)
Updates batch normalization statistics (running mean/variance) to match target distribution. Lightweight — no gradient computation required for basic variants.

### 4. Test-Time Training (TTT) (29 papers)
Self-supervised auxiliary tasks at test time (e.g., rotation prediction, masked reconstruction). Distinct from general TTA by requiring a training-time auxiliary head.

### 5. Prompt-based Adaptation (10 papers)
Optimizes or adapts prompts (visual or textual) at test time while keeping model weights frozen. Strong in VLM/foundation model settings.

### 6. Test-Time Tuning / Fine-tuning (24 papers)
Broader category covering methods that tune model parameters at test time, beyond the specific mechanisms above. Includes test-time policy adaptation for agents.

### 7. Selective Parameter Update (5 papers)
Identifies and updates only critical parameters (e.g., via Fisher information, gradient importance). Reduces computational cost and catastrophic forgetting.

### 8. Model Update / Weight Adaptation (26 papers)
General weight/parameter updates at test time — normalizations, layer-specific updates, fine-tuning specific layers. Overlaps with categories 3, 6, 7.

### 9. Adapter / LoRA-based Adaptation (3 papers)
Uses parameter-efficient modules (LoRA, adapters) as the adaptation substrate. Keeps base model frozen, tunes only the lightweight module.

### 10. State Tuning (1 paper)
Optimizes internal state matrices (e.g., in RNN/SSM architectures) while keeping weights fixed.

---

## Supporting Techniques

### 11. Contrastive / Consistency Learning (3 papers)
Enforces consistency between augmented views or contrastive objectives during adaptation.

### 12. Prototype / Memory-based (14 papers)
Stores prototypes, feature banks, or nearest-neighbor indices; adapts by matching test samples to stored representations. Includes retrieval-augmented approaches.

### 13. Sample Selection / Reliability Filtering (7 papers)
Filters unreliable test samples before adaptation to prevent error accumulation. Uses confidence, entropy, or other reliability scores.

### 14. Feature Alignment (11 papers)
Aligns feature distributions between source and target domains at test time. Includes style transfer and distribution matching.

### 15. Knowledge Distillation / Teacher-Student (7 papers)
Uses teacher-student frameworks (mean teacher, self-distillation) during adaptation to stabilize updates.

### 16. Calibration / Uncertainty Estimation (18 papers)
Calibrates model confidence or estimates uncertainty at test time. Often combined with OOD detection. Not always adaptation per se — some are diagnostic.

### 17. Energy-based Methods (1 paper)
Uses energy functions or energy-based models for adaptation objectives.

---

## Scaling & Efficiency Approaches

### 18. Training-free Methods (24 papers)
Methods requiring no gradient computation at test time — typically use heuristic adjustments, retrieval, or architectural properties.

### 19. Ensemble / Multi-model (9 papers)
Combines multiple models or predictions for adaptation. Includes model selection at test time.

### 20. Model Merging / Fusion (12 papers)
Merges or interpolates weights from multiple models. Task vectors, model soups, weight averaging.

### 21. Routing / MoE Adaptation (4 papers)
Dynamically adjusts routing in mixture-of-experts architectures at test time.

### 22. Iterative Refinement (3 papers)
Iteratively refines predictions through feedback loops at test time.

### 23. Active Labeling (1 paper)
Requests minimal human labels during test-time to anchor adaptation.

### 24. Experience / Retrieval-based (5 papers)
Retrieves prior trajectories or experiences to guide test-time behavior.

---

## Adaptation Settings (Problem Framing)

### 25. Continual / Online TTA (34 papers)
Adaptation over streaming, potentially non-stationary data. Handles forgetting and evolving distributions.

### 26. Source-free Domain Adaptation (11 papers)
No access to source training data during adaptation. Must adapt using only the pre-trained model and target data.

### 27. Domain Shift (66 papers)
Broad category — papers explicitly addressing distribution/domain shift. Most other categories are *mechanisms* for handling this *problem*.

### 28. OOD Generalization (9 papers)
Focuses on generalization to out-of-distribution data, often via invariant representations.

---

## Model-Type Specific

### 29. VLM / Foundation Model Adaptation (51 papers)
Adapting vision-language models (CLIP, etc.) or other foundation models at test time. Largest single technique cluster.

### 30. LLM Adaptation (31 papers)
Test-time adaptation specific to large language models — prompt transfer, policy adaptation, agent adaptation.

### 31. Diffusion / Generative Model Adaptation (10 papers)
Using or adapting diffusion/generative models at test time. Includes guidance mechanisms and score-based methods. (3 diffusion_generative + 7 diffusion_guidance, some overlap)

### 32. Meta-learning (14 papers)
Learning to adapt — meta-training for fast test-time adaptation. MAML-style and few-shot adaptation.

### 33. Reinforcement / Reward-based (15 papers)
Uses RL objectives or reward signals for test-time adaptation.

---

## Domain-Specific Applications

### 34. Medical / Healthcare (6 papers)
Medical image segmentation, clinical adaptation.

### 35. Autonomous / Robotics (13 papers)
Self-driving, navigation, embodied agents.

### 36. Video / Temporal (48 papers)
Video understanding, temporal adaptation, sequence-level shifts.

### 37. Multimodal (5 papers)
Cross-modal adaptation beyond VLM-specific work.

### 38. Federated Learning (5 papers)
TTA in federated settings — personalization and generalization at test time.

### 39. Anomaly Detection (4 papers)
Adapting anomaly detection models at test time, often post-hoc score adjustment.

---

## Overlaps & Notes

- **Heavy overlap** between categories 6 (test-time tuning), 8 (model update), and 4 (TTT). These represent a spectrum from specific (TTT with auxiliary tasks) to general (any parameter update).
- **Category 27 (domain shift)** is a problem statement, not a technique — most papers in other categories also address domain shift. It captures the large set of papers that frame the problem explicitly.
- **Category 29 (VLM/foundation)** overlaps with 5 (prompt-based) and 6 (test-time tuning) — many VLM papers use prompts or tuning as the mechanism.
- **Categories 18 (training-free)** and 3 (batch norm) overlap — BN adaptation is often the simplest training-free method.
- Papers often span 2–3 categories (e.g., a paper doing entropy minimization + batch norm adaptation in a continual online setting = categories 1, 3, 25).
- The 49 unmatched papers include ~15 clearly tangential papers, ~10 with empty/malformed core_contributions, and ~24 that use unique vocabulary not captured by any pattern.
