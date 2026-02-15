# Acceleration Tasks — What to Build, Where, How

Every item names the file, the function/class, and what to change.

---

## 1. Per-machine inputs in parallel execution

**File:** `flatmachines/flatmachine.py` ~line 1004 (the TODO)

Right now `machine: [a, b]` sends the same `input` to every child machine. The spec supports `MachineInput[]` where each entry can have its own input block.

**Do this:**
- In `_execute_parallel_machines()`, check if `machine_spec` entries are dicts with `name` + `input` keys vs bare strings.
- If dict, use per-machine input. If string, use shared input (current behavior).
- Add test: parallel with 2 machines getting different inputs, assert each child received its own.

**Example YAML that should work after:**
```yaml
parallel_analysis:
  machine:
    - name: sentiment_machine
      input:
        text: "{{ context.text }}"
    - name: summarizer_machine
      input:
        max_length: 100
        text: "{{ context.text }}"
```

---

## 2. `tool_loop` runtime support

**File:** `flatmachines/flatmachine.py`, agent state execution path

`tool_loop: true` on a state should re-invoke the agent when it returns `finish_reason: tool_use`, feeding tool results back in until the agent produces a non-tool response or hits a limit.

**Do this:**
- After agent invocation in `_execute_agent_state()`, check `state.get('tool_loop')`.
- If true and result has `tool_calls`, call `hooks.on_tool_call()` (or a new hook) to execute tools, then re-invoke agent with tool results appended.
- Add `tool_loop_max` (default 10) to prevent runaways.
- Add test: agent that returns tool_call, hook resolves it, agent re-invoked, produces final answer.

---

## 3. `sampling` field handling

**File:** `flatmachines/execution.py`

`sampling: "multi"` on a state should trigger multiple completions (n>1) from the same agent call and return all candidates. `sampling: "single"` is current default behavior.

**Do this:**
- In `DefaultExecutionType.execute()`, check for `sampling` in state config.
- If `"multi"`, set `n` param on agent call (default n=3), return list of results.
- Wire `output_to_context` to receive list when sampling is multi.
- Add test: multi-sample returns list of 3 results.

---

## 4. Clean stdout in monitoring.py (both packages)

**Files:**
- `flatagents/flatagents/monitoring.py` line 211, 236
- `flatmachines/flatmachines/monitoring.py` line 211, 236

**Do this:**
- Change default: `FLATAGENTS_METRICS_ENABLED` → `'false'`
- Change console exporter to write to `sys.stderr` instead of stdout.
- Change all `get_logger()` handlers to stderr.
- Total: ~4 line changes per file.

```python
# line 211: change 'true' to 'false'
enabled = os.getenv('FLATAGENTS_METRICS_ENABLED', 'false').lower() not in ('false', '0', 'no')

# line 236: console exporter → stderr
# Replace ConsoleMetricExporter() with ConsoleMetricExporter(out=sys.stderr)
```

---

## 5. `QueueInvoker` — SQLite-backed concrete implementation

**File:** `flatmachines/flatmachines/actions.py` after line 249

`QueueInvoker` is abstract. Build a concrete one using SQLite (matches existing SQLite backends for registration/work).

**Do this:**
- Add `SQLiteQueueInvoker(QueueInvoker)` class.
- `_enqueue()`: insert row into `launch_queue` table (machine_name, input_json, status, created_at).
- Add `poll()` method: claim oldest unclaimed row, return machine config + input.
- Add `mark_complete()` / `mark_failed()`.
- Add test: enqueue 3 launches, poll gets them FIFO, mark complete removes them.

---

## 6. Normalize `AgentResult` fields across adapters

**Files:**
- `flatmachines/adapters/flatagent.py` — `FlatAgentAdapter.invoke()`
- `flatmachines/adapters/smolagents.py` — `SmolagentsAdapter.invoke()`
- `flatmachines/adapters/pi_agent_bridge.py` — `PiAgentBridgeAdapter.invoke()`

**Do this:**
- Define canonical result shape:
  ```python
  {"content": str, "error": Optional[str], "finish_reason": str,
   "usage": {"prompt_tokens": int, "completion_tokens": int},
   "cost": Optional[float], "rate_limit": Optional[dict],
   "provider_data": Optional[dict]}
  ```
- Each adapter's `invoke()` return must populate all keys (use `None` for unavailable).
- Add test: invoke each adapter type, assert all 7 keys present in result dict.

---

## 7. Max launch depth guard

**File:** `flatmachines/flatmachine.py`, in `_launch_machine()` and `_execute_machine_state()`

**Do this:**
- Add `_launch_depth` field to `FlatMachine.__init__()`, default 0.
- When launching/invoking a child machine, pass `parent_depth + 1`.
- Add `max_launch_depth` setting (default 10). Reject with error if exceeded.
- Add test: machine that launches itself recursively, hits depth limit, errors cleanly.

---

## 8. Checkpoint size guard

**File:** `flatmachines/flatmachines/persistence.py`

**Do this:**
- After serializing checkpoint, check byte size.
- If > configurable threshold (default 5MB), log warning.
- If > hard limit (default 50MB), raise error with context about which state/key is largest.
- Add test: artificially large context triggers warning/error.

---

## 9. Schema/runtime parity test

**File:** new file `tests/unit/test_schema_runtime_parity.py`

**Do this:**
- Parse `flatmachine.d.ts` state fields (the `MachineState` interface).
- For each field, assert one of:
  - handled in `flatmachine.py` state execution
  - listed in explicit `UNSUPPORTED_FIELDS` set with rationale
- Fails if a new field appears in schema without runtime or explicit skip entry.

---

## 10. Selective escalation machine template

**File:** new file `sdk/python/flatmachines/templates/selective_escalation.yml`

Not a library feature — a concrete reusable machine config.

```yaml
states:
  start:
    type: initial
    transitions:
      - to: fast_attempt

  fast_attempt:
    agent: fast_model
    execution:
      type: retry
      backoffs: [1, 2]
    output_to_context:
      fast_result: "{{ output.content }}"
      fast_confidence: "{{ output.confidence }}"
    on_error: escalate
    transitions:
      - condition: "context.fast_confidence >= 0.8"
        to: done
      - to: escalate

  escalate:
    agent: strong_model
    output_to_context:
      strong_result: "{{ output.content }}"
    transitions:
      - to: done

  done:
    type: final
    output:
      result: "{{ context.strong_result | default(context.fast_result) }}"
      escalated: "{{ context.strong_result is defined }}"
```

Wire with profiles so `fast_model` and `strong_model` resolve to different provider/model combos.

---

## 11. Multi-verifier consensus machine template

**File:** new file `sdk/python/flatmachines/templates/multi_verifier_consensus.yml`

```yaml
states:
  start:
    type: initial
    transitions:
      - to: generate

  generate:
    agent: generator
    output_to_context:
      candidate: "{{ output.content }}"
    transitions:
      - to: verify

  verify:
    agent: verifier
    execution:
      type: mdap_voting
      samples: 3
      threshold: 0.67
    input:
      candidate: "{{ context.candidate }}"
    output_to_context:
      verdict: "{{ output.content }}"
      agreement: "{{ output.agreement }}"
    transitions:
      - condition: "context.agreement >= 0.67"
        to: accepted
      - to: regenerate

  regenerate:
    agent: generator
    input:
      previous: "{{ context.candidate }}"
      feedback: "{{ context.verdict }}"
    output_to_context:
      candidate: "{{ output.content }}"
    transitions:
      - to: verify

  accepted:
    type: final
    output:
      result: "{{ context.candidate }}"
      agreement: "{{ context.agreement }}"
```

---

## 12. Budget governor hook

**File:** new file `flatmachines/flatmachines/budget.py`

```python
class BudgetGovernor(MachineHooks):
    def __init__(self, max_steps=50, max_tokens=500_000, max_cost_usd=5.0, max_wall_seconds=300):
        self.max_steps = max_steps
        self.max_tokens = max_tokens
        self.max_cost_usd = max_cost_usd
        self.max_wall_seconds = max_wall_seconds
        self._step_count = 0
        self._total_tokens = 0
        self._total_cost = 0.0
        self._start_time = None

    async def on_enter_state(self, state_name, context):
        if self._start_time is None:
            self._start_time = time.monotonic()
        self._step_count += 1
        elapsed = time.monotonic() - self._start_time
        if self._step_count > self.max_steps:
            raise BudgetExceededError(f"step limit {self.max_steps}")
        if elapsed > self.max_wall_seconds:
            raise BudgetExceededError(f"wall time {self.max_wall_seconds}s")

    async def on_agent_result(self, state_name, result, context):
        usage = result.get("usage", {})
        self._total_tokens += usage.get("prompt_tokens", 0) + usage.get("completion_tokens", 0)
        self._total_cost += result.get("cost", 0.0) or 0.0
        if self._total_tokens > self.max_tokens:
            raise BudgetExceededError(f"token limit {self.max_tokens}")
        if self._total_cost > self.max_cost_usd:
            raise BudgetExceededError(f"cost limit ${self.max_cost_usd}")
```

Hook it in any machine via `hooks:` config or programmatic attachment.

---

## Priority if you only have 3 days

| Day | Task | Why first |
|-----|------|-----------|
| 1 | #4 (stdout fix) + #9 (parity test) | Stop bleeding, prevent drift |
| 2 | #1 (per-machine input) + #7 (depth guard) | Unblock parallel workflows safely |
| 3 | #10 (escalation template) + #12 (budget hook) | Ship a usable selective-council pattern |
