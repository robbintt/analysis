# Concrete Gap-Closure Plan (Python SDKs + Specs)

Scope:
- Specs: `flatagent.d.ts`, `flatmachine.d.ts`, `flatagents-runtime.d.ts`, `profiles.d.ts`
- Python packages: `sdk/python/flatagents`, `sdk/python/flatmachines`
- Excludes JS SDK work for now.

## Goal
Make the framework reliably production-capable for mixed-model / heterogeneous multi-agent workflows by closing schema/runtime drift, hardening distributed execution paths, and standardizing observability behavior.

---

## Phase 1 — Correctness + Contract Alignment (highest priority)

### 1) Close schema/runtime drift in FlatMachine state handling
**Problem**
- `tool_loop`, `sampling`, and parts of `MachineInput[]` are present in schema/types but not fully implemented in runtime.

**Work**
- Implement runtime behavior (or remove/deprecate fields) for:
  - `tool_loop`
  - `sampling`
  - `machine: MachineInput[]` per-machine input mapping
- Add explicit validation errors for unsupported fields while rollout is in progress.

**Acceptance criteria**
- Every state field in `flatmachine.d.ts` is either:
  1) fully executed in runtime, or
  2) explicitly marked deprecated/unsupported by validator with clear warnings.
- Integration tests cover each implemented field path.

---

### 2) Enforce spec/runtime parity checks in CI
**Problem**
- Drift can recur silently.

**Work**
- Add a parity test suite that asserts runtime support map vs schema field map.
- Add version-lock checks for:
  - package versions
  - `SPEC_VERSION` values
  - bundled schema assets

**Acceptance criteria**
- CI fails when schema fields are introduced/changed without runtime and tests.

---

## Phase 2 — Runtime Hygiene + Deterministic Interfaces

### 3) Make stdout/stderr contract strict by default
**Problem**
- metrics/log output can pollute machine-readable stdout.

**Work**
- Default library logging stream to stderr.
- Default metrics to disabled in CLI paths, or OTLP when enabled.
- If console metrics are enabled, send them to stderr.
- Add one doc section: “CLI-safe defaults and data channel contract”.

**Acceptance criteria**
- `--json` runners always output valid JSON on stdout with no extra lines.
- Logs/metrics only on stderr unless explicitly overridden.

---

### 4) Normalize `AgentResult` contract end-to-end
**Problem**
- adapters/backends have slight shape variability.

**Work**
- Make all adapters return normalized fields consistently:
  - `error`, `rate_limit`, `provider_data`, `finish_reason`, `usage`, `cost`
- Add strict coercion tests across adapters and execution types.

**Acceptance criteria**
- Execution strategies (`retry/parallel/mdap_voting`) can rely on uniform fields without per-adapter conditionals.

---

## Phase 3 — Distributed Maturity

### 5) Provide at least one concrete queue-backed invoker
**Problem**
- `QueueInvoker` is abstract; no production-ready queue implementation in tree.

**Work**
- Implement a concrete queue invoker (one target backend first).
- Include idempotency key handling for launch intents.
- Add worker recovery semantics test matrix.

**Acceptance criteria**
- Fire-and-forget and blocking invoke both work with queue backend.
- Relaunch/replay does not duplicate side effects.

---

### 6) Expand backend support matrix for persistence/results/registration/work
**Problem**
- default in-memory behavior is great local, insufficient distributed by default.

**Work**
- Add production-grade backend implementations for key interfaces (prioritized order):
  1) result backend,
  2) persistence backend,
  3) registration/work backends.
- Standardize URI and locking semantics across backends.

**Acceptance criteria**
- Same machine config executes consistently across local and distributed backend profiles.

---

### 7) Harden resume/outbox semantics under failure
**Problem**
- launch/recovery semantics need heavy adversarial testing.

**Work**
- Add chaos/fault tests for:
  - crash after intent checkpoint, before launch
  - crash after launch, before mark-launched
  - duplicate resume/restart
  - partial parallel completion with timeout/any mode

**Acceptance criteria**
- Exactly-once launch intent semantics are preserved under tested failure modes.

---

## Phase 4 — Policy and Workflow Features for Selective Multi-Agent Use

### 8) Add first-class routing policy helpers
**Problem**
- selective escalation policies are currently hand-rolled in hooks/states.

**Work**
- Add reusable policy helpers for:
  - SAS-first gating
  - uncertainty/disagreement escalation
  - cost/latency budget gating
  - fallback policy

**Acceptance criteria**
- Teams can configure policy behavior declaratively with minimal custom hook code.

---

### 9) Add verifier-centric consensus utility components
**Problem**
- verifier scaling and consensus are possible but not first-class.

**Work**
- Add reusable machine/action patterns for:
  - multi-verifier vote/score aggregation
  - candidate-vs-verifier budgeting
  - confidence-triggered re-evaluation

**Acceptance criteria**
- Reference machine templates exist and pass integration tests for consensus scenarios.

---

## Phase 5 — Validation, Testing, and Operability

### 10) Raise distributed and long-horizon test depth
**Problem**
- current integration tests are mostly smoke-level.

**Work**
- Add scenario tests for:
  - long-running loops (drift, checkpoint growth)
  - stale worker reaping + job release race windows
  - mixed adapter workflows (`flatagent` + `smolagents` + `pi-agent`)
  - rate-limit/error behavior under retry strategy

**Acceptance criteria**
- Test suite demonstrates stable behavior under realistic load/failure patterns.

---

### 11) Add operational guardrails
**Problem**
- operational limits are not enforced consistently.

**Work**
- Add built-in guards for:
  - max launch depth
  - checkpoint pruning policy
  - context/output size thresholds before persistence
  - optional prompt-size warnings against model window

**Acceptance criteria**
- Guardrails are configurable and documented; defaults prevent common runaway failure modes.

---

## Suggested implementation order (practical)
1. Phase 1 items (schema/runtime correctness)  
2. Phase 2 item 3 (stdout/stderr contract)  
3. Phase 3 item 5 (concrete queue invoker)  
4. Phase 3 item 7 (failure semantics hardening)  
5. Phase 4 policy helpers (selective escalation + verifier components)  
6. Phase 5 testing + guardrails

---

## Definition of done for this roadmap
- No unresolved schema/runtime drift in Python runtime.
- JSON/CLI outputs are deterministic and clean by default.
- At least one production-grade distributed execution path is fully tested.
- Selective escalation and verifier workflows are supported via reusable components (not only ad hoc hooks).
- Integration test coverage includes fault/recovery and long-running workflows.