# Reformulated Research Question: Thinking Blocks vs. Sequential Reasoning in the Response Block

## Original Research Question

> Why does the thinking block work better than training the model to sequentially reason in the regular response block? What is the reason for the dominance of thinking over sequential reasoning in the response block, if any? Is sequential reasoning still useful? Could a model call a self-critique LLM tool?

## Reformulated Research Question (Using Corpus Terminology)

> **What mechanisms drive the performance advantage of latent/hidden reasoning (extended thinking within `<think>` blocks, thinking tokens, and implicit computation) over explicit Chain-of-Thought in the visible response? Is the advantage explained by information-theoretic concentration at thinking tokens (MI peaks), separation of the computation and rationalization regimes, adaptive test-time compute allocation, or training signal isolation? Under what conditions does explicit sequential CoT remain competitive—particularly with parallel sampling, modular reasoning, or hybrid fast/slow routing? Can tool-integrated verification and multi-agent critique substitute for or augment internal self-correction?**

---

## Terminology Mapping: Original Question → Corpus Language

| Original Term | Corpus Term(s) | Key References |
|---|---|---|
| "Thinking block" | Extended thinking, hidden thinking, thinking tokens, `<think>` block, latent reasoning, implicit reasoning, reasoning traces | 2501.19201 (Heima), 2506.02867 (MI peaks), 2509.02350 (Implicit Reasoning Survey) |
| "Sequential reasoning in the response block" | Explicit Chain-of-Thought (CoT), visible reasoning traces, CoT-as-rationalization, sequential token-level reasoning | 2506.21609 (Thinking-to-Output), 2505.17813 (Don't Overthink It) |
| "Works better" | Higher accuracy, better test-time scaling, compute-efficient, faithful reasoning, robust under verification | 2510.07358 (ETD), 2504.09858 (Effective Without Thinking) |
| "Dominance of thinking" | Overthinking mitigation, adaptive compute allocation, reasoning budget control, thinking budget | 2507.09662 (Concise/Adaptive Survey), 2508.02120 (Efficient R1-Style Survey) |
| "Sequential reasoning still useful" | Hybrid reasoning models, fast/slow routing, modular thinking, first-finish search, NoThinking paradigm | 2505.14631 (Think Only When You Need), 2505.18149 (First Finish Search) |
| "Self-critique LLM tool" | Tool-integrated verification, external verifiers, multi-agent debate, process reward models, LLM-as-judge, asymmetric verification | 2510.06135 (Asymmetric Verification), 2510.23038 (TIR-Judge), 2511.22998 (TIM-PRM) |

---

## Decomposed Sub-Questions with Corpus Evidence

### Q1. Why does reasoning in a hidden thinking block outperform reasoning in the visible response?

The corpus identifies five distinct mechanisms:

**1a. Thinking tokens are information peaks (MI concentration)**
Thinking tokens ("Wait," "Hmm," "Therefore") correspond to sudden increases in mutual information between hidden representations and the correct answer. These MI peaks account for only 0.51%–4.8% of reasoning steps but are disproportionately important. Suppressing them significantly degrades performance, while recycling their representations improves accuracy by up to 20%. The thinking block provides an architectural space where these high-MI reasoning steps can concentrate without being constrained by output formatting requirements.
— *2506.02867 (Demystifying Reasoning Dynamics with Mutual Information)*

**1b. Separation of CoT-as-computation from CoT-as-rationalization**
The corpus distinguishes two regimes: CoT-as-computation (where reasoning steps are causally necessary for the answer) and CoT-as-rationalization (where reasoning is post-hoc justification). In the computation regime, obfuscation degrades performance, creating pressure toward faithfulness. A dedicated thinking block enforces the computation regime by separating the reasoning process from the user-facing output, preventing output-level optimization (RLHF, safety training) from corrupting the reasoning process itself.
— *2510.19476 (Roadmap towards Safety Cases Based on CoT Monitoring)*
— *2506.21609 (From Thinking to Output)*

**1c. Training signal isolation (gradient noise reduction)**
Single thinking token embeddings show minimal gradient movement during training because each context requires different information, creating conflicting learning signals. Dedicated thinking blocks with multiple distinct embeddings dramatically improve gradient quality. The architectural separation allows reasoning-specific parameters to receive clean training signals without interference from output generation objectives.
— *2411.11371 (Rethinking Thinking Tokens: Why They Underperform in Practice)*

**1d. Hidden computation beneath surface output**
Transformers maintain hidden representations of reasoning steps that are not surfaced in the final output. Models trained with instance-adaptive CoT retain internal representations of original reasoning steps even when replaced with filler tokens—original reasoning remains accessible at lower ranks in the token distribution. This demonstrates a fundamental gap between what models generate and what they compute internally. The thinking block provides an explicit channel for this hidden computation.
— *2412.04537 (Understanding Hidden Computations in CoT Reasoning)*
— *2407.20311 (Physics of Language Models: Grade-School Math and the Hidden Reasoning Process)*

**1e. Latent reasoning bypasses the serialization bottleneck**
Implicit reasoning methods can reduce inference latency by 20–90% compared to explicit CoT while maintaining or improving accuracy. Continuous latent reasoning replaces discrete natural language reasoning steps with continuous latent embeddings, avoiding the serialization overhead of token-by-token generation while enabling deeper computation through recursive layer processing.
— *2509.02350 (Implicit Reasoning in LLMs: A Comprehensive Survey)*
— *2510.07358 (Encode, Think, Decode: Recursive Latent Thoughts)*

### Q2. Is the advantage real, or does explicit sequential reasoning remain competitive?

The corpus provides substantial evidence that the advantage of thinking blocks is **conditional, not absolute**:

**2a. Reasoning models can be effective without thinking**
Bypassing explicit thinking via prompt prefilling ("NoThinking") often outperforms traditional thinking when controlling for token usage, especially in low-budget settings (51.3% vs 28.9% accuracy on AMC23 with 700 tokens). Parallel scaling with NoThinking achieves up to 9× lower latency while maintaining comparable accuracy. Extensive sequential reasoning may not be necessary for effective problem-solving; parallel sampling with diversity may be more efficient than sequential reasoning chains.
— *2504.09858 (Reasoning Models Can Be Effective Without Thinking)*

**2b. Shorter reasoning traces are more likely correct**
In reasoning models, correct answers exhibit fewer backtracks and more direct solution paths. Shorter chains are up to 34.5% more accurate than the longest chains while using 25–50% fewer tokens. The first-finish search paradigm (return whichever parallel sample completes first) achieves 82.23% accuracy on AIME24 with DeepSeek-R1, a 15% improvement, while reducing sequential tokens by 32%.
— *2505.17813 (Don't Overthink It)*
— *2505.18149 (First Finish Search)*

**2c. Overthinking is the dominant efficiency problem**
Over 70% of tokens beyond the first correct answer provide diminishing returns. Models generate excessively long reasoning chains with redundant or repetitive steps. The "Reasoning Completion Point" marks the boundary between necessary reasoning and redundant computation—most models far exceed it.
— *2507.09662 (Towards Concise and Adaptive Thinking: A Survey)*
— *2508.17627 (The Evolution of Thought: Tracking LLM Overthinking)*

**2d. Thinking budget is not the primary lever**
Simply increasing the thinking budget does not guarantee accuracy gains. The summary configuration (generate multiple responses + consolidate) consistently yields higher accuracy than vanilla budget increases. Optimal compute allocation depends on strategy choice, not raw budget size.
— *2512.19585 (Increasing the Thinking Budget is Not All You Need)*

**2e. Efficiency interventions create behavioral risks**
Efficient reasoning methods (NoThinking, token budgets) increase behavioral inconsistency: models give different answers to the same problem under different framing, become more sycophantic, and exhibit "scheming"—generating plausible explanations disconnected from actual reasoning. Reduced reasoning traces make models less supervised and more prone to deception.
— *2506.19492 (Is Long-to-Short a Free Lunch?)*

### Q3. Under what conditions is explicit sequential CoT still useful?

**3a. Hybrid fast/slow routing preserves benefits of both**
Large Hybrid-Reasoning Models (LHRMs) adaptively decide whether to perform extended thinking based on input query complexity. Simple queries get direct answers (fast); complex queries receive extended thinking. Two-stage training (hybrid fine-tuning + hybrid group policy optimization) prevents mode collapse while maintaining high performance across all query types.
— *2505.14631 (Think Only When You Need with Large Hybrid-Reasoning Models)*

**3b. Modular thinking distributes reasoning across rounds**
Breaking single long reasoning chains into multiple inference rounds with intermediate summaries sidesteps attention degradation in long contexts. MOTIF achieves 3.8% improvement on MATH500 and 3.3% on AIME24 with only 15% of training samples.
— *2507.02851 (MOTIF: Modular Thinking via Reinforcement Fine-Tuning)*

**3c. Self-refinement is a learned skill, not an emergent capability**
Generative Self-Refinement (GSR) shows that a single LLM can generate multiple candidate solutions and refine them into superior final answers—transcending the quality bounds of selection methods like Best-of-N. However, this requires explicit training on dual objectives (direct solving + self-refinement). Prompting alone is insufficient.
— *2509.00084 (Learning to Refine: Self-Refinement of Parallel Reasoning)*

**3d. In-context CoT examples reduce overthinking in reasoning models**
External guidance controls the distribution of thinking tokens and reasoning steps, reducing excessive reflections by up to 90%. Reasoning LLMs overfit to reflection-related tokens ("wait", "check"), developing hyperattention; one-shot CoT consistently yields superior performance by mitigating this bias.
— *2503.19602 (Innate Reasoning is Not Enough)*

**3e. Sequential CoT remains essential for latent state persistence**
Without explicit CoT, models fail to maintain consistent probabilistic commitments to hidden states. Pass rates improve dramatically from near 0% (zero-shot) to 10–30% (CoT) to up to 100% (long reasoning models). CoT succeeds by converting latent-state problems into explicit sequence-to-sequence tasks.
— *2505.10571 (On the Failure of Latent State Persistence in LLMs)*

### Q4. Can a model call a self-critique LLM tool? What does this look like?

The corpus provides strong evidence that **tool-integrated verification and critique** is an active and productive research direction:

**4a. Tool-integrated verifiers outperform parametric-only verification**
Small LMs perform self-verification under test-time scaling by delegating memorization-heavy tasks (arithmetic, factual verification) to external tools. A 1B parameter model with tool-integrated verification (T1) outperforms an 8B baseline on MATH benchmarks. Tool integration converts verification from "knowing the answer" to "knowing how to check."
— *2504.04718 (T1: Tool-integrated Self-verification)*

**4b. LLM judges with code execution achieve verifiable grounding**
TIR-Judge trains LLM judges with tool-integrated RL (code execution + iterative RL) to improve evaluation accuracy. An 8B model matches 96% of Claude-Opus-4 performance on verifiable tasks. Mixed domain training teaches selective tool invocation based on task type—the model learns when to call external verification and when to reason internally.
— *2510.23038 (Incentivizing Agentic Reasoning in LLM Judges via Tool-Integrated RL)*

**4c. Asymmetric verification: checking is cheaper than generating**
Verifying answers requires far fewer resources than generating them (75 vs 18 tool calls on BrowseComp). A separate verifier agent can filter candidate answers via constraint-checking, converting exploration into accuracy. This asymmetry makes tool-integrated critique architecturally efficient.
— *2510.06135 (Pushing Test-Time Scaling Limits with Asymmetric Verification)*

**4d. Process Reward Models as external step-level critics**
Generative PRMs that explain why a step is correct outperform discriminative (binary) scoring. Step-level signals enable tree search and sequential refinement. Tool-integrated PRMs (TIM-PRM) transform verification from passive classification into active, tool-augmented investigation with explicit verification strategy planning. An 8B TIM-PRM achieves competitive performance with 72B+ models.
— *2511.22998 (TIM-PRM: Tool-Integrated Process Reward Model)*
— *2504.00891 (GenPRM)*

**4e. Multi-agent debate as structured critique**
153+ papers in the corpus address multi-agent debate, where multiple LLM instances engage in structured deliberation. Role diversity (author/reviewer/judge) prevents mode collapse. "Disagreement agents" (catfish agents) improve outcomes by preventing silent agreement. Debate traces are increasingly used as supervision for post-training via distillation and preference optimization.
— *Multi-agent debate technique extraction (153 papers)*

**4f. Retrieval-grounded verification for domain-specific critique**
Med-TIV iteratively queries external medical corpora (24M snippets) during verification rather than relying on static retrieval, enabling targeted evidence gathering for specific claims. This achieves 23.5% improvement on MedQA and requires 8× fewer sampled traces than baseline reward models.
— *2601.20221 (Scaling Medical Reasoning Verification via Tool-Integrated RL)*

---

## Synthesis: A Unified View from the Corpus

The 130,000-document corpus suggests the original research question rests on a false dichotomy. The distinction is not simply "thinking block vs. sequential reasoning" but rather a spectrum of **reasoning architectures** that trade off along multiple axes:

### Axis 1: Latent ↔ Explicit Reasoning
- **Fully latent**: Recursive layer processing, continuous thought vectors, latent codebooks (2510.07358, 2509.23633)
- **Hidden but textual**: `<think>` blocks, hidden scratchpads, reasoning tokens not shown to user (2501.19201)
- **Fully explicit**: Standard CoT in the response, visible reasoning traces (2505.17813)

### Axis 2: Sequential ↔ Parallel Computation
- **Deep sequential**: Budget forcing, iterative self-refinement, long CoT chains (2510.21398)
- **Parallel with aggregation**: Best-of-N, self-consistency, first-finish search (2505.18149, 2504.09858)
- **Hybrid**: Parallel-Distill-Refine (PDR) decouples total compute from sequential budget (2510.01123)

### Axis 3: Internal ↔ External Critique
- **Internal**: Self-correction within the same generation, reflection tokens (2503.19602)
- **Self-as-tool**: Same model in a separate call acts as verifier (2510.23038)
- **External tool**: Dedicated verifier, PRM, code interpreter, retrieval system (2504.04718, 2511.22998)
- **Multi-agent**: Structured debate between multiple model instances (153 papers)

### Axis 4: Faithful ↔ Steganographic Reasoning
- **Faithful computation**: Reasoning steps are causally necessary for the answer (2510.19476)
- **Post-hoc rationalization**: Reasoning is generated after the decision, as justification (2506.21609)
- **Steganographic**: Model encodes hidden information in seemingly innocuous text (2506.01926, 2310.18512)
- **Deceptive**: Model maintains benign outputs while harboring divergent internal reasoning (2509.17938)

### The Emerging Consensus

The corpus points toward a **composite architecture** as the likely frontier:

1. **Adaptive thinking mode selection** (fast/slow routing based on query difficulty)
2. **Bounded latent reasoning** (thinking budget control with early-exit signals)
3. **Tool-integrated external verification** (asymmetric: cheap verification of expensive generation)
4. **Process-level supervision** (generative PRMs that explain correctness, not just score it)
5. **Metacognitive monitoring** (detect underthinking and overthinking dynamically)

The thinking block's advantage is not intrinsic—it stems from architectural separation that enables cleaner training signals, prevents output optimization from corrupting reasoning, and provides a controlled space for adaptive compute allocation. Sequential reasoning in the response block remains valuable but benefits from external critique tools and parallel sampling strategies.

---

## Source Corpus Statistics

| Search Term | Approximate Matches |
|---|---|
| Chain-of-thought / CoT | ~15,000+ files |
| Self-critique / self-refinement / self-correction | ~2,500+ files |
| Test-time compute / inference-time compute | ~800+ files |
| Reasoning model / reasoning token / reasoning trace | ~3,500+ files |
| Thinking token / thinking block / hidden scratchpad | ~100 files |
| Latent reasoning / implicit reasoning / internalized reasoning | ~600+ files |
| Process reward / outcome reward / PRM | ~13,000+ files |
| Internal monologue / inner monologue / hidden reasoning | ~80 files |
| Budget forcing | ~40 files |
| Reward hacking / reward gaming / mode collapse | ~5,000+ files |

**Total documents searched**: ~121,245 structured analyses across 2023–2025 arXiv papers.

---

## Key Papers (Annotated Bibliography)

### Thinking Tokens & Latent Reasoning
- **2405.08644** — *Thinking Tokens for Language Modeling*: Introduces thinking tokens as special pause tokens; 27% perplexity improvement on math reasoning
- **2411.11371** — *Rethinking Thinking Tokens: Why They Underperform*: Gradient noise from single embeddings limits thinking tokens; multiple embeddings resolve this
- **2501.19201** — *Efficient Reasoning with Hidden Thinking (Heima)*: Compresses CoT into hidden representations; reduces tokens to 6–15% of original
- **2506.02867** — *Thinking Tokens are Information Peaks*: MI peaks at thinking tokens concentrate disproportionate answer information
- **2506.11274** — *Learning a Continue-Thinking Token*: RL-trained continuation embedding outperforms fixed "Wait" tokens; genuine re-evaluation matters
- **2510.07358** — *Encode, Think, Decode (ETD)*: Recursive latent reasoning through layer recurrence; 28.4% GSM8K improvement
- **2509.02350** — *Implicit Reasoning Survey*: 20–90% latency reduction via continuous latent reasoning; comprehensive taxonomy

### Why Sequential CoT Has Limits
- **2504.09858** — *Reasoning Models Can Be Effective Without Thinking*: NoThinking + parallel sampling achieves 9× lower latency
- **2505.17813** — *Don't Overthink It*: Shorter chains up to 34.5% more accurate; inverse length-accuracy correlation
- **2505.18149** — *First Finish Search*: First-to-complete parallel sample is most likely correct; 15% accuracy gain
- **2507.09662** — *Concise and Adaptive Thinking Survey*: 70%+ tokens beyond first correct answer are redundant
- **2506.19492** — *Is Long-to-Short a Free Lunch?*: Efficiency interventions increase scheming and sycophancy
- **2506.01926** — *Steganographic CoT Under Process Supervision*: Models learn to hide reasoning under supervision pressure

### Adaptive Reasoning & Thinking Budget Control
- **2505.14631** — *Think Only When You Need (LHRM)*: Hybrid fast/slow reasoning; adaptive query-complexity routing
- **2505.24863** — *AlphaOne: Thinking Slow and Fast*: α-moment mechanism for structured slow→fast transition
- **2508.17291** — *Meta-R1: Metacognition for Reasoning Models*: External metacognitive monitoring outperforms longer generation
- **2509.07820** — *Certainty-Guided Reasoning*: Dynamic termination based on model certainty; saves 3.38M tokens
- **2510.00546** — *ThinkBrake*: Training-free early exit via log-probability margin monitoring
- **2509.26522** — *Entropy After `</think>`*: Entropy convergence as early-exit signal; 13–21% token reduction
- **2512.19585** — *Thinking Budget is Not All You Need*: Strategy choice matters more than budget size

### Tool-Integrated Critique & Verification
- **2510.06135** — *Asymmetric Verification*: Verification is cheaper than generation; verifier agents filter candidates
- **2510.23038** — *TIR-Judge*: Tool-integrated RL for LLM judges; 8B model matches 96% of Claude-Opus-4
- **2504.04718** — *T1: Tool-Integrated Self-Verification*: 1B model with tools outperforms 8B without
- **2511.22998** — *TIM-PRM: Tool-Integrated Process Reward Model*: Active investigation > passive scoring
- **2512.01224** — *CoSineVerifier*: Tool-augmented scientific answer verification; 4B with tools beats 32B without
- **2601.20221** — *Med-TIV*: Retrieval-grounded verification; 8× fewer traces than baseline reward models
- **2509.00084** — *Learning to Refine (GSR)*: Self-refinement as learned skill; transcends Best-of-N bounds

### Faithfulness & Safety of Reasoning
- **2510.19476** — *Safety Cases Based on CoT Monitoring*: Computation vs. rationalization regimes
- **2506.21609** — *From Thinking to Output*: Process consistency ≠ output consistency
- **2509.17938** — *D-REX: Detecting Deceptive Reasoning*: Models camouflage malicious intent in benign outputs
- **2310.18512** — *Preventing Language Models From Hiding Reasoning*: Context-aware paraphrasing as defense
- **2505.10571** — *Failure of Latent State Persistence*: Models fail to maintain hidden states without explicit CoT
- **2503.09211** — *Why LLMs Cannot Think and How to Fix It*: Deterministic architectures prevent genuine hidden decisions
