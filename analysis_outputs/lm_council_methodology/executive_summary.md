# Executive Summary: LM-Council Methodologies and Evidence Fit

## Bottom line
The evidence **does not support a universal “LM council everywhere” strategy**. It supports a **conditional strategy**:
- default to strong single-agent execution,
- escalate to multi-agent council methods only for high-depth/high-stakes cases,
- enforce strict cost/latency/safety guardrails.

## What is strongly supported
1. **Conditional multi-agent use** (SAS→MAS routing) improves outcome-per-cost in mixed workloads.  
2. **Disagreement-triggered debate** is better than always-on debate.  
3. **Depth-sensitive deployment** matters: multi-agent methods help most on deep sequential reasoning.  
4. **Dynamic routing/topology/model assignment** outperforms static fixed workflows.  
5. **Verifier-centric selection** (multi-verifier consensus) is a strong lever for correctness.  
6. **Critical-path optimization** is essential for latency in parallel agent systems.

## What is strongly not supported
1. **Static MAS by default** on frontier models (often poor ROI).  
2. **High-overhead coordination** without limits (failure rates increase when over-coordinated).  
3. **Homogeneous MAS as automatic win** (strong single-agent simulation can match cheaper).  
4. **One-size-fits-all topology** (beneficial topologies are sparse and task-dependent).  
5. **Context-only scaling** as primary strategy (bounded returns).  
6. **Single-agent safety metrics alone** for MAS security assessment.

## Use-case fit (confirm / deny / conditional)
- **Confirmed**: high-depth reasoning, counterfactual/causal analysis, mixed-complexity routing scenarios, correctness-critical verification pipelines, latency-sensitive parallel orchestration.  
- **Denied**: blanket LM-council deployment for all tasks; always-on debate/refinement; uniform model assignment for all modules.  
- **Conditional**: heterogeneous teams, debate-heavy protocols, and hybrid architectures—beneficial only with measured boundaries and monitoring.

## Required governance before deployment
- Quality + cost + latency measured together.
- Round caps, consensus early stop, and token budgets.
- Coordination overhead guardrails (avoid over-coordination).
- Drift and adversarial weak-link checks for long-horizon workflows.

## Decision posture
Adopt a **“selective council” policy**: multi-agent deliberation is a specialized tool, not a default architecture.
