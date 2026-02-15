# Concrete Acceleration Brainstorm (Architect + Engineer, start now)

Purpose: immediate, practical actions to speed delivery of mixed-model / heterogeneous multi-agent workflows using current Python SDKs + specs.

## 0) Guiding principle
Ship a **thin, reliable golden path** first (few patterns, very hard reliability guarantees), then expand feature surface.

---

## 1) Actions to start today (0–48 hours)

### A. Architect actions
1. **Define the “golden path” contract (1 page)**
   - Required runtime features: state transitions, retry, parallel machine invoke, launch, checkpoint/resume.
   - Explicitly out-of-scope for v1 path: anything not runtime-backed.
2. **Freeze a v1 feature gate list**
   - Mark schema fields as: `supported`, `experimental`, `blocked`.
   - Publish in docs + validator warnings.
3. **Set reliability SLOs for workflow runs**
   - e.g., “95% runs complete without manual intervention under normal load.”
4. **Define one canonical distributed topology**
   - checker → workers → reaper (single blessed pattern).
5. **Define strict stdout/stderr policy**
   - stdout = payload only; stderr = logs/metrics.

### B. Engineer actions
6. **Add runtime guard: reject unsupported state fields at startup**
   - Fast-fail on fields that exist in schema but not runtime.
7. **Implement per-machine input support for `MachineInput[]`**
   - Remove current TODO and add tests.
8. **Add CLI-safe defaults in runners**
   - metrics off by default, noisy logs suppressed, stdout clean JSON only.
9. **Add a parity test for schema↔runtime fields**
   - CI fails if schema introduces runtime-unhandled fields.
10. **Create one “golden path” integration test**
   - includes retry + parallel + launch + resume.

---

## 2) High-impact actions this week (3–7 days)

### A. Architect actions
11. **Create a decision table for escalation policy**
   - SAS-first trigger rules: complexity, uncertainty, risk, disagreement.
12. **Set budget policy defaults**
   - max steps, max launches, token/cost ceilings per workflow.
13. **Define error taxonomy for orchestration**
   - retryable vs non-retryable by code/status/error type.
14. **Define observability minimum schema**
   - required fields: execution_id, state, transition, latency, token/cost, error class.
15. **Pick one backend profile for production pilot**
   - avoid “choose anything” for first rollout.

### B. Engineer actions
16. **Normalize `AgentResult` across all adapters**
   - guarantee stable fields (`error`, `rate_limit`, `provider_data`, `finish_reason`, `usage`, `cost`).
17. **Implement one concrete queue invoker**
   - from abstract `QueueInvoker` to real queue-backed path.
18. **Harden launch outbox with fault tests**
   - crash before/after launch edge cases.
19. **Add stale-worker race tests**
   - worker death while job claimed; verify release/recovery.
20. **Add deterministic “any mode” semantics tests**
   - first-finisher behavior + pending task cleanup.

---

## 3) 2–4 week acceleration bets

### A. Architect actions
21. **Publish 3 reference machine templates**
   - selective escalation
   - multi-verifier consensus
   - distributed worker pool
22. **Create architecture runbook**
   - incident response for stuck runs, replay policy, poisoned work handling.
23. **Define versioning policy for spec/runtime changes**
   - no schema additions without runtime + tests.
24. **Define rollout tiers**
   - Local dev → staging distributed → production distributed.
25. **Set acceptance benchmark suite**
   - correctness, latency, cost, recovery success, duplicate-launch prevention.

### B. Engineer actions
26. **Implement max launch depth guardrail**
27. **Implement checkpoint pruning policy**
28. **Add prompt/context size warning hooks**
29. **Add validator mode: strict in CI, warning in local dev**
30. **Add workflow replay harness**
   - replay checkpoints and compare deterministic outputs where applicable.

---

## 4) Concrete workflow features to build now (user-facing)

31. **`SelectiveRouterMachine`**
   - inputs: task metadata + uncertainty
   - outputs: `route = sas | mas`
32. **`VerifierConsensusMachine`**
   - fan-out verifiers, aggregate scores, confidence threshold.
33. **`BudgetGovernorAction`**
   - enforces run-level ceilings (steps, tokens, cost, time).
34. **`SafetyGateAction`**
   - blocks unsafe/unknown tool calls and high-risk transitions.
35. **`FallbackEscalationAction`**
   - promotes from fast model to stronger model on failure classes.

---

## 5) Operational shortcuts (quick wins)

36. **Create 2 blessed environment presets**
   - `dev-safe` and `prod-safe` env var bundles.
37. **Add “diagnostics snapshot” command**
   - dumps machine config, backend config, hooks class, versions.
38. **Add “dry-run validate” command**
   - schema + runtime support checks, no execution.
39. **Add result payload linter**
   - ensures machine outputs are stable, bounded, serializable.
40. **Add one-click local chaos test**
   - kill/restart worker during run and assert recovery.

---

## 6) Team process accelerators

41. **Daily 15-min architecture triage**
   - review only blockers tied to reliability SLOs.
42. **Single source of truth board**
   - each item tagged: `spec`, `runtime`, `test`, `docs`.
43. **“No new schema field without tests” rule**
44. **“Golden path first” review checklist**
   - decline optional complexity unless it improves reliability.
45. **Weekly failure review**
   - top 3 observed failure modes, assign hardening actions.

---

## 7) Fast prioritization (if you only do 8 things)

1. Schema/runtime parity CI gate  
2. Per-machine input support (`MachineInput[]`)  
3. Clean stdout/stderr default behavior  
4. Concrete queue invoker implementation  
5. Outbox crash/replay test suite  
6. Normalized `AgentResult` contract across adapters  
7. Budget governor + max launch depth guard  
8. One production-ready checker/worker/reaper template

---

## 8) Definition of acceleration success (next 30 days)

- Golden path workflows run with predictable behavior under failure/restart.
- No schema/runtime drift regressions enter main.
- Distributed worker topology is operationally repeatable.
- Multi-model escalation policy is reusable, not hand-crafted per workflow.
- On-call/debugging time drops because telemetry and runbooks are standardized.