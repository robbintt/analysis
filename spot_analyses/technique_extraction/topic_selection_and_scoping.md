# Topic Selection & Scoping

How to choose research topics for technique extraction and scope them into workable groups. This is the decision process that feeds the [extraction queue](queue.md) and precedes the [extraction procedure](technique_extraction_procedure.md).

---

## 1. Where Topics Come From

### 1.1 Extraction spin-offs

The richest source. Every completed extraction surfaces technique categories that warrant their own deep dive. A finished extraction with 20 categories will typically yield 3–5 viable spin-off topics.

**Example A:** `test_time_compute_scaling` (987 papers) produced:
- Process Reward Models (32 papers in parent, likely 80–150 standalone)
- Adaptive Compute Allocation (50 papers in parent)
- Reasoning Distillation (45 papers in parent)
- Multi-Agent Debate (22 papers in parent, ~170 standalone)

**Example B:** `test_time_adaptation` (284 papers) suggests additional spin-offs:
- Continual / Online TTA (~35 papers in parent)
- VLM / Foundation Model TTA (~45 papers in parent)
- Prompt-based TTA (~18 papers in parent)
- Training-free / Gradient-free TTA (~20 papers in parent)

**Why these are good candidates:** The parent extraction has already done partial disambiguation. You know the term hits, the semantic boundaries, and roughly how many papers exist. Phase 0 of the extraction procedure is half-done.

### 1.2 Corpus term frequency

Run broad term scans over the corpus to find high-frequency topics without extractions:

```bash
# Check word cloud files for curated vocabulary clusters
ls ~/code/research_crawler/research_paper_analysis_v2/queries/word_clouds/
cat ~/code/research_crawler/research_paper_analysis_v2/queries/word_clouds/reasoning_cognition.txt
```

Pick terms from the word clouds and check hit counts:

```bash
for term in "term one" "term two" "term three"; do
  echo "$(rg -li "$term" ml_research_analysis_2025/ 2>/dev/null | wc -l | tr -d ' ')  $term"
done | sort -rn
```

### 1.3 Research questions

Sometimes you start with a question, not a term. "What agent architectures are people using?" or "How are people handling overthinking?" The question implies a topic, but the right group name and scope need investigation.

### 1.4 External prompts

A paper you read, a conversation, a trend you noticed. These need the most scoping work because they haven't been validated against the corpus yet.

---

## 2. Volume Check

Before any deeper investigation, run quick hit counts. This takes 30 seconds and immediately tells you whether you're dealing with a thin topic, a tractable group, or a decomposition problem.

```bash
for term in "candidate term" "candidate-term" "variant phrase"; do
  echo "$(rg -li "$term" ml_research_analysis_2025/ 2>/dev/null | wc -l | tr -d ' ')  $term"
done | sort -rn
```

### Volume decision table

| Hits | Verdict | Action |
|---|---|---|
| < 30 | Too thin | Note as a sub-category within a larger group. Don't extract standalone. |
| 30–200 | Ideal | Proceed directly to Phase 0 of the extraction procedure. |
| 200–500 | Large but workable | Check for semantic splits (Section 3). May proceed as-is if scope is clean. |
| 500–1000 | Likely needs scoping | Almost certainly contains semantic splits. Run Section 3 before committing. |
| > 1000 | Decomposition required | This is an umbrella, not a topic. Run Section 3 and split. |

### Union counting

Most topics have multiple term variants. Get the deduplicated union:

```bash
{
  rg -li 'variant.one' ml_research_analysis_2025/ 2>/dev/null
  rg -li 'variant.two' ml_research_analysis_2025/ 2>/dev/null
  rg -li 'variant.three' ml_research_analysis_2025/ 2>/dev/null
} | sort -u | wc -l
```

The union count is what matters, not individual term counts. Some terms will be near-complete subsets of others.

---

## 3. Disambiguation & Decomposition

This is the most important step and the one most often skipped. A topic that looks like one thing from the outside often contains 2–5 distinct research communities using overlapping vocabulary.

### 3.1 Sample actual usage

Pull 30–40 core_contribution summaries and read them:

```bash
sqlite3 analysis_outputs/research_index.sqlite \
  "SELECT arxiv_id || ' | ' || SUBSTR(REPLACE(core_contribution, CHAR(10), ' '), 1, 250)
   FROM papers WHERE core_contribution LIKE '%your term%'" \
  | shuf -n 35
```

**What you're looking for:**

- **Same term, different meaning.** "Inference time" = latency metric vs. "inference-time compute" = scaling concept. These are separate research areas wearing the same label.
- **Different terms, same meaning.** "Test-time scaling" and "inference-time scaling" used interchangeably. These should be merged into one group.
- **Subtopic splits.** "Test-time adaptation" (distribution shift) and "test-time scaling" (compute allocation) share a prefix but are distinct. Separate groups.
- **Technique vs. application.** "Multi-agent" includes papers *about* multi-agent techniques AND papers *applying* agents to medical/legal/code domains. The applications aren't a technique group.
- **Hierarchical nesting.** "Agents" contains "debate", "workflows", "tool use", "planning" — each a distinct technique. The umbrella is too broad; extract the children.

### 3.2 Sub-cluster investigation

When you suspect splits, count the sub-clusters:

```bash
# Hit counts for suspected sub-topics
for term in "sub-topic one" "sub-topic two" "sub-topic three"; do
  echo "$(rg -li "$term" ml_research_analysis_2025/ 2>/dev/null | wc -l | tr -d ' ')  $term"
done | sort -rn
```

Then check overlap between sub-clusters:

```bash
rg -li 'sub.topic.one' ml_research_analysis_2025/ 2>/dev/null | sort -u > /tmp/cluster_a.txt
rg -li 'sub.topic.two' ml_research_analysis_2025/ 2>/dev/null | sort -u > /tmp/cluster_b.txt

echo "Cluster A: $(wc -l < /tmp/cluster_a.txt)"
echo "Cluster B: $(wc -l < /tmp/cluster_b.txt)"
echo "Overlap:   $(comm -12 /tmp/cluster_a.txt /tmp/cluster_b.txt | wc -l)"
```

**High overlap (>50%):** These are the same topic — merge.  
**Low overlap (<20%):** These are different topics — split.  
**Medium overlap (20–50%):** Judgment call. Check whether the overlap papers are "bridge" papers or noise.

### 3.3 Check against existing groups

Before creating a new group, verify it doesn't substantially overlap with completed or queued extractions:

```bash
sqlite3 analysis_outputs/research_index.sqlite \
  "SELECT group_name, COUNT(*) FROM spot_analysis_paper_groups GROUP BY group_name"
```

Some overlap is fine and expected (the procedure says so). But if >40% of your candidate papers are already in an existing group, consider whether you're re-extracting the same thing from a different angle.

### 3.4 Decomposition patterns

Common patterns and how to handle them:

**Pattern: Umbrella topic**
- Signal: >1000 papers, no one-sentence scope covers 70%
- Example: "Agents" (3000+ papers)
- Action: Don't extract the umbrella. Identify 3–5 children and extract those.

**Pattern: Technique + applications**
- Signal: Core technique cluster (~200 papers) surrounded by domain applications (~500+ papers)
- Example: "RAG" — the retrieval technique vs. RAG-for-medical, RAG-for-legal, etc.
- Action: Extract the technique. Domain applications are coverage gaps or parking lot items.

**Pattern: Adjacent but distinct**
- Signal: Two topics share a term prefix but have different methods, communities, and goals
- Example: "Test-time adaptation" vs. "test-time compute scaling"
- Action: Separate groups. Note the relationship in both stubs.

**Pattern: Technique hierarchy**
- Signal: One technique is a component of another
- Example: "Process reward models" as a component of "test-time compute scaling"
- Action: Extract both. The parent extraction gives breadth; the child gives depth. Link them.

---

## 4. The Scope Test

Before writing a queue entry, apply this test:

> **Can you write a one-sentence scope statement that would cover >70% of the papers without being vacuous?**

| Result | Verdict |
|---|---|
| Yes, easily | Good scope. Proceed. |
| Yes, but it's awkward or has caveats | Probably fine. The 30% uncovered will be your "tangential" papers in extraction. |
| Only if the sentence is vague ("papers about X") | Needs decomposition. The topic is an umbrella. |
| No — the papers are doing 3 different things | Needs decomposition. You have 2–3 topics, not one. |

**Good scope statements (from completed extractions):**
- "Techniques for allocating additional compute at inference to improve output quality" (test_time_compute_scaling)
- "Techniques for adapting model parameters or behavior at deployment to handle distribution shift without full retraining" (test_time_adaptation)

**Bad scope statements (from failed attempts):**
- "Papers about agents" — vacuous, covers 3000+ papers doing completely different things
- "Agentic orchestration" — umbrella over debate, workflows, collaboration, domain applications

---

## 5. Writing the Queue Entry

Once scoped, add to [`queue.md`](queue.md):

```markdown
### N. `group_name`

- **Scope:** {one-sentence scope statement}
- **Est. papers:** ~{N}
- **Source:** {where this topic came from — spin-off, corpus scan, question, external}
- **Dependencies:** {does it build on another extraction? list it}
- **Decomposition notes:** {if split from a broader topic, explain the split and what sibling groups exist}
```

### Required fields

- **Group name:** Snake_case, descriptive, unique. This becomes the directory name and SQLite group_name.
- **Scope:** The one-sentence statement from the scope test. This is the single most important field — it defines what's in and what's out.
- **Est. papers:** From volume check. Doesn't need to be exact — within 2x is fine.
- **Source:** Traceability. Where did this topic come from?

### Optional fields

- **Dependencies:** If this group is a sub-topic of a completed extraction, say so. The parent extraction's patterns and samples are useful context for Phase 0.
- **Decomposition notes:** If this group was split from a broader topic, document the split. Future you (or a collaborator) will want to know why "agentic orchestration" became three separate groups.

---

## 6. Prioritization

When choosing what to extract next from the queue, weight by:

### 6.1 Tractability

| Factor | Weight | Why |
|---|---|---|
| Builds on completed extraction | High | Phase 0 is partially done. Patterns, terms, and semantic boundaries are known. |
| Clean scope (passes scope test easily) | High | Less disambiguation work, fewer false positives. |
| Moderate size (50–300 papers) | Medium | Large enough for patterns, small enough for single-session execution. |
| Term variants are few and unambiguous | Medium | Simpler grep patterns, fewer false positives. |

### 6.2 Value

| Factor | Weight | Why |
|---|---|---|
| Answers a question you actually have | High | Motivation matters for manual review steps. |
| Connects multiple completed extractions | Medium | Builds network of cross-referenced analyses. |
| Covers a fast-moving research area | Medium | Analysis is more valuable while the field is active. |
| Fills a gap in the overall taxonomy | Low | Completeness is nice but not urgent. |

### 6.3 Anti-patterns

- **Don't extract umbrellas** just because they're big. "Agents" at 3000 papers will produce a diffuse extraction. Extract the children.
- **Don't chase novelty** over tractability. A 50-paper topic with clean scope yields more insight than a 500-paper topic with messy boundaries.
- **Don't block on dependencies.** If topic B "builds on" topic A, that means A's output is *useful context* for B, not that A must be complete first. You can run B standalone; it'll just take slightly longer in Phase 0.

---

## Worked Example: Agentic Orchestration

This example walks through the full selection and scoping process for a real topic that required decomposition.

### Starting point

The `test_time_compute_scaling` extraction identified "Agentic Orchestration" (~20 papers) as a Tier 2 enabling technique. Question: is there a larger group here worth extracting?

### Volume check

```
1715  agentic
1469  orchestrat
1261  agent system
 760  agent framework
 231  agent pipeline
 214  agentic framework
```

Red flag: "agentic" alone hits 1715. This is not one topic.

### Disambiguation

Sampled 35 core_contributions from the intersection of "agentic/orchestrat/agent framework/agent pipeline" with "language model/llm/foundation model". Found **1038 unique LLM-related agent papers.**

Term frequency within that set:

```
445  framework        (generic)
130  evaluat           (benchmarks, not techniques)
107  rag               (retrieval — different topic)
107  collaborat        (multi-agent teaming)
 91  workflow          (workflow design)
 70  debate            (structured argumentation)
 51  coordinat         (coordination mechanisms)
 47  scientific        (domain application)
 34  medical           (domain application)
```

### Identified splits

| Cluster | Est. papers | Distinct? |
|---|---|---|
| Multi-Agent Debate | ~170 | Yes — clear technique with defined formats |
| Agentic Workflow Design | ~250 | Yes — meta-layer about designing agent systems |
| Multi-Agent Collaboration | ~300 | Partially — bleeds into RL multi-agent and robotics |
| Agent Benchmarks/Evals | ~130 | Not a technique — will land as "unmatched" |
| Domain Applications | ~110+ | Not a technique — medical/legal/science agents |

### Scope test

- "Agentic orchestration" — **fails.** Can't write a non-vacuous one-sentence scope.
- "Multi-LLM debate/deliberation frameworks for improving output quality through structured argumentation" — **passes.** Covers ~170 papers cleanly.
- "Designing, generating, and optimizing agent workflow graphs" — **passes.** Covers ~250 papers.
- "Teams of specialized LLM agents coordinating on tasks" — **marginal.** Bleeds into RL/robotics.

### Decision

Don't extract "agentic orchestration." Extract three children:
1. `multi_agent_debate` (clean, small, extends TTC)
2. `agentic_workflow_design` (clean, medium)
3. `multi_agent_collaboration` (needs further scoping, queue last)

### Queue entries written

See [queue.md](queue.md) items 1, 2, 6.

---

## Checklist

For each candidate topic, before adding to queue:

- [ ] Source identified (spin-off / corpus scan / question / external)
- [ ] Volume check done — hits are in the 30–1000 range
- [ ] If >500 hits: disambiguation sampling done (30+ core_contributions read)
- [ ] Semantic splits identified and documented
- [ ] Scope test passed (one-sentence statement covers >70% non-vacuously)
- [ ] Checked against existing groups for overlap
- [ ] Queue entry written with all required fields
