# What To Do Now — Personal Acceleration

You have 4,255 research analysis files across v1 and v2 (~43MB), 1,497 of which are digest-relevant. You have 15 standalone docs. You have a 12-category brainstorm with source mappings. You have a grading pipeline, a codebase_ripper that works, and a flatagents SDK you understand deeply. You have not yet produced a single digest.

Here's what's actually slowing you down and what to do about it.

---

## Problem 1: The corpus is unsorted noise

4,255 files. Only 1,497 have strong/medium signal for your digest topics. ~1,000 have zero relevance (adversarial robustness of classifiers, Gaussian mixture models, FPGA quantization). v2 re-analyzed 1,151 of v1's papers (presumably better — 129 avg lines vs 102). 359 papers exist only in v2. 1,163 exist only in v1.

You're sitting on a haystack and haven't built the filter.

**Do this now:**
1. Generate a manifest: one CSV with columns `file`, `version`, `arxiv_id`, `slug`, `has_v2_counterpart`, `signal_tier` (strong/medium/weak/none), `digest_categories` (which of your 12 it maps to).
2. Use rg + a cheap model (or even just rg pattern matching) to classify. You don't need to read 4,255 files. You need to tag them.
3. For the 1,151 papers with both v1 and v2 versions, use v2 (longer, newer). Drop v1 duplicates from your working set.
4. Result: a working set of ~1,800 files (1,510 v2 + ~300 v1-only relevant ones), with category tags.

**Time: 2-3 hours with scripting, or one codebase_ripper pass focused on classification.**

---

## Problem 2: Your standalone docs are conversation transcripts, not specs

`agents_for_speculative_diffs.md` (883 lines) is a Discord conversation with frenbot. `agents_are_mas_rebranded.md` is an article draft. `MCP_BOX_PLAN.md` is a 44-line sketch. `three_waves_agents.md` is a research synthesis. `OrKa_vs_flatagents.md` is a comparison table.

These are your most valuable docs — they contain your actual thinking, decisions, and architecture — but they're raw. An LLM reading them wastes tokens on conversational filler ("If you want, I can..." / "Got it — here's...").

**Do this now:**
1. Distill each standalone doc into a structured extract. For each one, pull:
   - **Claims** (what it asserts)
   - **Decisions** (what you chose and why)
   - **Open questions** (what's unresolved)
   - **Source pointers** (which research papers back it up)
2. Target: each distilled doc is 200-400 lines of signal, zero conversational filler.
3. Priority order (by downstream value):
   1. `agents_for_speculative_diffs.md` — your agent architecture blueprint
   2. `MCP_BOX_PLAN.md` — your distillation pipeline
   3. `lm_council_methodology/implementation_guide_1000_tokens.md` — already clean, leave it
   4. `lm_council_methodology/executive_summary.md` — already clean, leave it
   5. `OrKa_vs_flatagents.md` — the comparison table section is clean; strip the rest
   6. `three_waves_agents.md` — already fairly clean
   7. `agents_are_mas_rebranded.md` — article draft, distill claims only

**Time: 1-2 hours. Use an LLM to do the distillation pass — you're extracting from your own writing.**

---

## Problem 3: The digest brainstorm has 12 categories but no source→digest pipeline

`digest_brainstorm_categories_topics.md` lists categories and "Primary source files" but those source files are your standalone docs, not the 1,497 relevant research files. The research corpus is unmapped to categories.

**Do this now:**
1. Take the manifest from Problem 1 (once you have it).
2. For each of your 12 categories, pull the files tagged to that category.
3. For the first tranche (6 categories), pick the top 5-10 highest-signal files per category.
4. That gives you 30-60 source files to actually read and digest. Not 4,255. Not 1,497. Thirty to sixty.
5. Write the digest production script: for each source file × target token tier (250/500/750/1000/1250/1500), extract the digest. This is a batch job — codebase_ripper or a simple flatagents machine with a summarizer agent.

**Time: 3-4 hours for the mapping + first batch run.**

---

## Problem 4: v1 has a 7.7% generation failure rate (v2 fixed it)

203 of 2,625 v1 files are YAML-frontmatter-only with no report body. v2 has zero failures across 1,510 files. The `grades.md` sample (3/14 = 21.4%) was from one specific batch and not representative of the full corpus.

This means: v2 is clean. v1 has 203 broken files, but since v2 re-analyzed 1,151 of v1's papers, most of those failures may already be covered. The remaining v1-only papers (1,163 slugs) may still contain some of those 203 broken files.

**Do this now:**
1. For the 203 broken v1 files, check how many have a v2 counterpart (probably most — problem already solved).
2. For any v1-only broken files that are digest-relevant, flag for re-generation.
3. For any new batch jobs, use whatever pipeline produced v2 (0% failure rate).

**Time: 15 minutes scripting.**

---

## Problem 5: You're context-switching between too many workstreams

Right now you're touching: SDK assessment, SDK gap-closure planning, codebase_ripper fixes, digest brainstorming, research corpus analysis, article writing, grading pipeline, word clouds. Each one advances 10% per session.

**Do this now — pick one lane for the next 4 hours:**

**Lane A: Corpus triage (highest leverage)**
Produces the manifest, the working set, the category mapping. Everything downstream needs this.
1. Script the manifest CSV (30 min)
2. Classify files by signal tier (1-2 hours)
3. Map to categories (1 hour)
4. Deduplicate v1/v2 (30 min)

**Lane B: First 6 digests (highest visible output)**
Skip the full corpus triage. Use only the source files already named in `digest_brainstorm_categories_topics.md` plus the standalone docs. You already know which files matter for the first tranche.
1. Distill standalone docs (1 hour)
2. Read the 15-20 named source files across first 6 categories (1-2 hours)
3. Write 6 digests at the 1000-token tier first (1-2 hours)
4. Expand to other tiers later

**Lane C: Automate digest production (highest long-term velocity)**
Build the batch pipeline so digests produce themselves.
1. Write a flatmachine config: input = source file + category + token tier → output = digest
2. Use your existing profiles (cheap model for 250-500, stronger for 1000+)
3. Run against the named source files from the brainstorm
4. Grade outputs with your existing rubric

**Recommendation: Lane B today, Lane A tomorrow, Lane C when you have 20+ manual digests to validate the format against.**

---

## Problem 6: The lm_council_methodology suite is your best asset and you're underusing it

`executive_summary.md` and `implementation_guide_1000_tokens.md` are already production-quality digests. The decision rules checklist, the do/don't matrix, the method-claim table — these ARE the digests for categories 1, 4, 11, and 12. You already wrote them.

**Do this now:**
1. Map lm_council docs directly to digest categories:
   - `executive_summary.md` → Category 1 (Orchestration) 1000-token digest, done
   - `implementation_guide_1000_tokens.md` → Category 1 (Orchestration) 1500-token digest, done
   - `decision_rules_checklist.md` → Category 12 (Anti-Patterns) source
   - `methodology_do_dont_matrix.md` → Category 12 (Anti-Patterns) source
   - `method_claim_table.md` → Category 11 (Evaluation) source
   - `standalone_technical_report.md` → Category 4 (Verification/Consensus) source
2. You may already have 3-4 categories partially done just by reformatting what exists.

**Time: 1 hour to map and reformat.**

---

## Concrete next 3 sessions plan

### Session 1 (today, 3-4 hours): First digests from existing material
1. Map lm_council docs to categories (30 min)
2. Distill `agents_for_speculative_diffs.md` and `MCP_BOX_PLAN.md` (1 hour)
3. Write 6 digests at 1000-token tier from existing material (2 hours)
4. Output: `analysis_outputs/digests/` with 6 files

### Session 2 (tomorrow, 3-4 hours): Corpus triage
1. Script the manifest CSV with signal classification (2 hours)
2. Deduplicate v1/v2, pick winners (30 min)
3. Map top files per category (1 hour)
4. Output: `analysis_outputs/corpus_manifest.csv`

### Session 3 (day after, 3-4 hours): Batch digest production
1. Write the digest production agent/machine config (1 hour)
2. Run against top 5 files per first-tranche category (2 hours)
3. Grade outputs (30 min)
4. Output: 30 digests across 6 categories × 5 sources

---

## What NOT to do right now

- Don't build more SDK features. You assessed it, you know the gaps, that work will still be there.
- Don't grade more papers. The grading pipeline works. It has a known failure rate. Fix the validator, move on.
- Don't make more word clouds. Nice artifact, zero downstream value for digests.
- Don't write more brainstorm docs about what to brainstorm. You have 12 categories. Start producing.
- Don't try to read 4,255 files. Read 30-60 of the right ones.
