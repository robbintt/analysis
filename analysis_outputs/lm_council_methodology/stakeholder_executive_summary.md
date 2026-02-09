# Stakeholder Executive Summary: When to Use “LM Council”

## Decision in one line
Use LM-council methods **selectively**, not by default.

## Why this matters
Our research review shows that multi-agent council workflows can improve quality on hard tasks, but they can also add major cost and delay when used everywhere.

## Where evidence says to use it
| Good fit | Why |
|---|---|
| Complex, multi-step reasoning | Council-style cross-checking helps on deeper tasks |
| Causal/counterfactual analysis | Debate-based methods show strong gains |
| High-stakes outputs (accuracy-critical) | Multi-verifier review improves reliability |
| Mixed workload systems | Route easy requests to single-agent, hard ones to council |
| Latency-sensitive parallel systems (with proper orchestration) | Critical-path optimization can cut response time significantly |

## Where evidence says **not** to use it
| Poor fit | Why |
|---|---|
| “Use council for everything” strategy | Often low incremental quality for high cost |
| Always-on debate/refinement loops | Expensive and frequently unnecessary |
| Simple/low-depth tasks | Overhead often outweighs benefits |
| Fixed one-size-fits-all topology | Best structure varies by task |
| Uniform model assignment across all modules | Usually leaves quality on the table |

## Practical operating policy
1. **Default to single-agent.**
2. **Escalate to council only when needed** (hard task, disagreement, high risk).
3. **Apply hard controls**: token budget, round cap, early stop on consensus.
4. **Track cost + quality + latency together** in all evaluations.
5. **Add safety checks** for long sessions and adversarial prompts.

## Business takeaway
A targeted “selective council” approach is the best risk-adjusted strategy: it preserves quality gains where they are real and avoids unnecessary compute spend where they are not.
