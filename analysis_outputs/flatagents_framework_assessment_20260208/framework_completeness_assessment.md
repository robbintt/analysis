# FlatAgents/FlatMachines Framework Completeness Assessment

Scope reviewed:
- `~/code/flatagents/*.d.ts`
- `~/code/flatagents/sdk/python/flatagents`
- `~/code/flatagents/sdk/python/flatmachines`

Date: 2026-02-08

## Overall assessment

Strong orchestration core, partial production/distributed maturity, and some schema/runtime drift.

Verdict: **good v1 platform**, but **not yet fully complete** for advanced mixed-model / heterogeneous multi-agent production workflows without additional hardening.

---

## What is solid (ready now)

1. **State-machine orchestration is strong**
   - Initial/final states, transitions, conditions, retries, loops, on-error routing.
   - Machine invocation patterns implemented:
     - `machine: child`
     - `machine: [a, b]`
     - `foreach`
     - `launch` (fire-and-forget)

2. **Execution strategy coverage is good**
   - Implemented: `default`, `retry`, `parallel`, `mdap_voting`.

3. **Heterogeneous runtime composition exists**
   - Adapter architecture is clean/extensible.
   - Built-in adapters:
     - `flatagent`
     - `smolagents`
     - `pi-agent`

4. **Model profiles are practical**
   - default/profile/override behavior implemented.
   - profile propagation/fallback patterns supported across machine→agent boundaries.

5. **Checkpoint + resume + outbox semantics exist**
   - Pending launches are checkpointed and resumed.

---

## Partial / important gaps

1. **Schema/runtime drift**
   - `tool_loop` and `sampling` are in schema/types but not materially handled in runtime execution logic.
   - `MachineInput[]` support is partial; per-machine input has an explicit TODO in runtime.

2. **Distributed backend maturity is partial**
   - `QueueInvoker` is abstract and requires subclass implementation (`_enqueue` not implemented).
   - Default result backend is in-memory (fine local, limited distributed by default).
   - Firestore backend exists, but broader distributed backend matrix (Redis/Postgres for all components) is not complete.

3. **Observability defaults are CLI-hostile by default**
   - Metrics enabled by default + console exporter can pollute stdout payloads.
   - Requires explicit environment/runner discipline to keep stdout clean.

4. **Policy/routing governance is mostly DIY**
   - No first-class built-ins for uncertainty-triggered escalation, utility/cost routing policy, verifier budget policy.
   - These are implementable via states/hooks, but not pre-packaged as framework primitives.

5. **Distributed test depth is still limited**
   - Integration tests cover basic operations/smoke behavior, but not deep failure/race/network-partition robustness at production confidence levels.

---

## Fit-to-use-case quick score

- Mixed-model orchestration: **8/10**
- Heterogeneous runtime composition: **7/10**
- Verifier/consensus workflows: **6/10**
- Distributed production robustness: **5/10**
- Safety/control-plane hardening: **4/10**
- Evaluation/benchmarking support: **5/10**

---

## Bottom line

For your mixed-model / heterogeneous multi-agent goals, this framework is a strong base for:
- orchestration patterns,
- adapter-based heterogeneity,
- profile-driven model selection,
- checkpointable workflows.

Primary work needed next is:
1) close schema/runtime drift,
2) harden distributed/runtime backends,
3) tighten observability defaults for machine-readable pipelines,
4) add first-class policy/routing primitives for selective council-style workflows.
