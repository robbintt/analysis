# Technique Extraction Procedure

Repeatable method for identifying a research topic within the corpus, building a paper group, and extracting recurring technique categories. Uses corpus grep to define groups, grep-seeded extraction for technique discovery, and an LLM refinement pass for semantic depth.

## Inputs

- Markdown analysis corpus in `ml_research_analysis_2025/` (and/or `2024/`)
- SQLite database at `analysis_outputs/research_index.sqlite` with `papers` table
- A research topic to investigate (selected via [topic_selection_and_scoping.md](topic_selection_and_scoping.md))

## Output

All artifacts live under `spot_analyses/technique_extraction/`:

- A `spot_analysis_paper_groups` entry in SQLite
- `{group}.md` — top-level analysis (merged result of extraction)
- `{group}/` — subfolder containing:
  - `papers.md` — paper list with arxiv + digest links (regenerable from SQLite)
  - `option_c_extraction.md` — grep-seeded categories with paper counts
  - `option_a_refinement.md` — LLM refinement pass
  - `overview.md` — optional lightweight stub/overview

The extraction queue lives in [`queue.md`](queue.md). For how topics are selected and scoped, see [`topic_selection_and_scoping.md`](topic_selection_and_scoping.md).

---

## Phase 0: Group Definition

### 0.1 Choose candidate search terms

Start with the obvious terms for your topic. Cast wide — you'll narrow later.

```bash
# Quick hit counts to gauge corpus coverage
for term in "term one" "term-two" "term three"; do
  echo "=== $term ==="
  rg -li "$term" ml_research_analysis_2025/ 2>/dev/null | wc -l
done
```

Check the existing word clouds for related vocabulary:

```bash
ls ~/code/research_crawler/research_paper_analysis_v2/queries/word_clouds/
grep -li 'your topic' ~/code/research_crawler/research_paper_analysis_v2/queries/word_clouds/*.txt
```

### 0.2 Disambiguate term usage

Different research communities reuse the same words for different concepts. Before committing to a group definition, **sample actual usage** to check for semantic splits.

```bash
# Sample 30 random matches and read the surrounding context
rg -i 'your.term' ml_research_analysis_2025/ --max-count=1 -m 1 2>/dev/null | shuf -n 30
```

Look for:
- **Same term, different meaning** — e.g., "inference time" as a latency metric vs. "inference-time compute" as a scaling concept
- **Different terms, same meaning** — e.g., "test-time scaling" and "inference-time scaling" used interchangeably
- **Subtopic splits** — e.g., "test-time adaptation" (distribution shift) vs. "test-time scaling" (compute allocation) share a prefix but are distinct research areas

If you find a semantic split, **create separate groups**. The small overlap between groups is fine and expected.

### 0.3 Finalize search terms and count

Settle on the union of terms that define your group. Run final counts:

```bash
# Union of term variants, deduplicated by filename
{
  rg -li 'term.variant.one' ml_research_analysis_2025/ 2>/dev/null
  rg -li 'term.variant.two' ml_research_analysis_2025/ 2>/dev/null
} | sed 's|.*/||' | sort -u > /tmp/{group}_files.txt

echo "Papers: $(wc -l < /tmp/{group}_files.txt)"
```

### 0.4 Populate SQLite

Create the `spot_analysis_paper_groups` table if it doesn't exist:

```sql
CREATE TABLE IF NOT EXISTS spot_analysis_paper_groups (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name  TEXT NOT NULL,
    arxiv_id    TEXT NOT NULL,
    title       TEXT,
    source_url  TEXT,
    filepath    TEXT,           -- repo-root-relative path to digest
    added_at    TEXT DEFAULT (datetime('now')),
    UNIQUE(group_name, arxiv_id)
);
CREATE INDEX IF NOT EXISTS idx_sapg_group ON spot_analysis_paper_groups(group_name);
CREATE INDEX IF NOT EXISTS idx_sapg_arxiv ON spot_analysis_paper_groups(arxiv_id);
```

Insert by joining grep results against the `papers` table:

```bash
while IFS= read -r fname; do
  echo "INSERT OR IGNORE INTO spot_analysis_paper_groups (group_name, arxiv_id, title, source_url, filepath)
    SELECT '${GROUP}', arxiv_id, title, source_url, 'ml_research_analysis_2025/' || filename
    FROM papers WHERE filename = '${fname}';"
done < /tmp/${GROUP}_files.txt | sqlite3 analysis_outputs/research_index.sqlite
```

Verify counts and spot-check:

```bash
sqlite3 analysis_outputs/research_index.sqlite \
  "SELECT group_name, COUNT(*) FROM spot_analysis_paper_groups WHERE group_name='${GROUP}'"
```

Note: grep may find files not in the `papers` table (stale duplicates with different timestamps). The join handles this — papers are deduplicated by arxiv_id via the UNIQUE constraint.

### 0.5 Generate paper list

Generate a markdown file with clickable links, ordered chronologically by arxiv_id. The file lives inside the group's subfolder:

```bash
mkdir -p spot_analyses/technique_extraction/${GROUP}

sqlite3 analysis_outputs/research_index.sqlite <<SQL > spot_analyses/technique_extraction/${GROUP}/papers.md
.mode list
.separator ""
SELECT '- [' || arxiv_id || '](https://arxiv.org/abs/' || arxiv_id || '): [' ||
       replace(title, '''', '''') || '](../../../' || filepath || ')'
FROM spot_analysis_paper_groups
WHERE group_name = '${GROUP}'
ORDER BY arxiv_id;
SQL
```

Arxiv IDs sort chronologically as `YYMM.NNNNN`, so `ORDER BY arxiv_id` gives you a timeline.

Validate a few links:

```bash
shuf -n 5 spot_analyses/technique_extraction/${GROUP}/papers.md | \
  sed -n 's|.*(\.\./\.\./\.\./\([^)]*\)).*|\1|p' | while read p; do
  if [ -f "$p" ]; then echo "✓ $p"; else echo "✗ $p"; fi
done
```

### 0.6 Create analysis stub

The stub goes in `spot_analyses/technique_extraction/{group}.md` — the top-level file paired with the `{group}/` subfolder containing papers.md and extraction artifacts.

```markdown
# {Topic Title}

## Corpus Coverage

- **{N} papers** in 2025 corpus (52K total)
- {M} papers in 2024 corpus (28K files)

## Scope

{One-sentence description of what this group covers.}

## Techniques

<!-- TODO: Link to technique extraction -->

## Key Findings

<!-- TODO -->

## Open Questions

<!-- TODO -->

## Paper List

See [papers.md]({group}/papers.md) ({N} papers).
```

### 0.7 Phase-0 Quality Gate (required)

Before moving to Phase 1, run a quick integrity + scope check and save results to `{group}/overview.md`.

```bash
GROUP="{group_name}"

# 1) Structural integrity
DB_COUNT=$(sqlite3 analysis_outputs/research_index.sqlite \
  "SELECT COUNT(*) FROM spot_analysis_paper_groups WHERE group_name='${GROUP}'")
FILE_COUNT=$(wc -l < spot_analyses/technique_extraction/${GROUP}/papers.md)
DUP_GROUP_IDS=$(sqlite3 analysis_outputs/research_index.sqlite \
  "SELECT COUNT(*) FROM (SELECT arxiv_id, COUNT(*) c FROM spot_analysis_paper_groups WHERE group_name='${GROUP}' GROUP BY arxiv_id HAVING c>1)")
BROKEN_LINKS=$(sed -n 's|.*(\.\./\.\./\.\./\([^)]*\)).*|\1|p' \
  spot_analyses/technique_extraction/${GROUP}/papers.md | while read -r p; do
  [ -f "$p" ] || echo "$p"
done | wc -l)

echo "DB: ${DB_COUNT}, papers.md: ${FILE_COUNT}, dup_group_ids: ${DUP_GROUP_IDS}, broken_links: ${BROKEN_LINKS}"

# 2) Join safety for Phase 1 export
# If >0, arxiv_id join can duplicate rows; use filepath-based join in Phase 1.1.
DUP_IN_PAPERS=$(sqlite3 analysis_outputs/research_index.sqlite \
  "SELECT COUNT(*) FROM (SELECT p.arxiv_id, COUNT(*) c FROM papers p JOIN spot_analysis_paper_groups g ON g.arxiv_id=p.arxiv_id WHERE g.group_name='${GROUP}' GROUP BY p.arxiv_id HAVING c>1)")
echo "duplicate_arxiv_rows_in_papers: ${DUP_IN_PAPERS}"

# 3) Scope smoke test (manual)
sqlite3 analysis_outputs/research_index.sqlite \
  "SELECT g.arxiv_id || ' | ' || SUBSTR(REPLACE(p.core_contribution, CHAR(10), ' '),1,220)
   FROM spot_analysis_paper_groups g
   JOIN papers p ON ('ml_research_analysis_2025/' || p.filename = g.filepath
                     OR 'ml_research_analysis_2024/' || p.filename = g.filepath)
   WHERE g.group_name='${GROUP}' ORDER BY random() LIMIT 20;"
```

**Gate criteria (recommended):**
- `DB_COUNT == FILE_COUNT`
- `DUP_GROUP_IDS == 0`
- `BROKEN_LINKS == 0`
- Spot sample has acceptable precision for your topic (typically ≥70% clearly in-scope)

If the gate fails, refine Phase 0 terms/filters and regenerate `papers.md` before continuing.

---

## Phase 1: Grep-Seeded Extraction

### 1.1 Export core_contributions

Dump `arxiv_id | core_contribution` to a flat file, one paper per line, newlines flattened, chronological order.

```bash
GROUP="{group_name}"
WORK="/tmp/${GROUP}"

sqlite3 analysis_outputs/research_index.sqlite <<SQL > ${WORK}_core_contributions.txt
SELECT g.arxiv_id || ' | ' || REPLACE(p.core_contribution, CHAR(10), ' ')
FROM spot_analysis_paper_groups g
JOIN papers p
  ON ('ml_research_analysis_2025/' || p.filename = g.filepath
      OR 'ml_research_analysis_2024/' || p.filename = g.filepath)
WHERE g.group_name = '${GROUP}'
ORDER BY g.arxiv_id;
SQL
```

Check size — this determines whether Phase 2 can be a single pass or needs chunking:

```bash
wc -c ${WORK}_core_contributions.txt  # ÷4 ≈ tokens
```

### 1.2 Broad term frequency scan

Cast a wide net with ~50–100 technique terms relevant to the topic. The goal is discovery, not precision.

```bash
cat ${WORK}_core_contributions.txt | tr '[:upper:]' '[:lower:]' | \
  grep -oiE 'term1|term2|term3|...' | \
  sort | uniq -c | sort -rn
```

**Seed list tips:**
- Start with terms from the relevant word cloud files in `~/code/research_crawler/research_paper_analysis_v2/queries/word_clouds/`
- Add topic-specific jargon you expect
- Include both hyphenated and space-separated variants
- Don't worry about false positives at this stage — you're looking for signal

Review the frequency output. Terms appearing ≥3 times are candidate category anchors. Terms appearing once are noise or niche subcategories.

### 1.3 Define category grep patterns

For each candidate category, write a grep pattern that captures the technique family. Extract matching arxiv_ids to a file:

```bash
grep -i 'pattern1\|pattern2\|pattern3' ${WORK}_core_contributions.txt | \
  cut -d'|' -f1 | tr -d ' ' | sort -u > ${WORK}_cat_{name}.txt
wc -l ${WORK}_cat_{name}.txt
```

**Pattern tips:**
- Use `\w*` for suffix wildcards (e.g., `entropy minim\w*` catches "minimization", "minimizing")
- Use `.` for flexible separators (e.g., `test.time` catches "test-time" and "test time")
- Use `\b` for word boundaries when needed to avoid false matches
- Review a few matches to check for false positives: `grep -i 'pattern' ${WORK}_core_contributions.txt | head -5`

### 1.4 Measure coverage

```bash
cat ${WORK}_cat_*.txt | sort -u > ${WORK}_all_matched.txt
cut -d'|' -f1 ${WORK}_core_contributions.txt | tr -d ' ' | sort -u > ${WORK}_all_papers.txt

echo "Total: $(wc -l < ${WORK}_all_papers.txt)"
echo "Matched: $(wc -l < ${WORK}_all_matched.txt)"
echo "Unmatched: $(comm -23 ${WORK}_all_papers.txt ${WORK}_all_matched.txt | wc -l)"
```

**Target: ≥70% coverage.** Below that, you're missing major categories.

### 1.5 Sample unmatched papers

```bash
comm -23 ${WORK}_all_papers.txt ${WORK}_all_matched.txt | shuf -n 25 | while read id; do
  echo "--- $id ---"
  grep "^$id " ${WORK}_core_contributions.txt | cut -d'|' -f2 | head -c 300
  echo
done
```

Look for:
- **New technique families** you didn't seed for → add patterns, repeat 1.3–1.4
- **Tangential papers** that mention the topic but don't propose techniques → expected, leave unmatched
- **Empty entries** → ignore

Iterate until coverage stabilizes (usually 2–3 rounds).

### 1.6 Write Option C extraction

Document each category:
- Name
- Paper count
- One-line description
- Note coverage and characterize unmatched papers

Save as `option_c_extraction.md` in the working directory.

---

## Phase 2: LLM Refinement Pass

The grep-seeded structure is the skeleton. The LLM pass adds flesh: semantic nuance, sub-categories, and catches what grep missed.

### 2.1 Decide scope

Check the core_contributions file size from Step 1.1.

| Size | Approach |
|---|---|
| < 50K tokens | Single LLM pass on full text |
| 50–150K tokens | Feed category-by-category with representative samples |
| > 150K tokens | Chunk into ~100-paper batches, merge |

### 2.2 Prepare the LLM prompt

For a single-pass refinement (< 50K tokens), the prompt structure is:

> I have {N} papers on {topic}. Grep-based extraction found these technique categories:
>
> {paste Option C categories with counts}
>
> Below are the core_contribution summaries. Review and:
> 1. Identify sub-categories within large groups (>15 papers)
> 2. Find techniques grep missed — especially conceptually similar terms with different vocabulary
> 3. Flag any categories that should be merged
> 4. Add representative paper IDs (arxiv_id) for each category
> 5. Note any domain-specific application clusters
>
> {paste core_contributions text}

For category-by-category refinement (50–150K tokens):

> Category: {name} ({N} papers)
> Description: {one-liner}
>
> Here are the core_contributions for papers in this category:
> {paste only the matching papers' core_contributions}
>
> Review: Are there sub-categories? Any papers that don't belong? What's the common thread?

### 2.3 Capture to file

Write the LLM's output to `option_a_refinement.md`. Do not let it overwrite the Option C extraction — they're complementary artifacts.

**Important:** Have the LLM write to a file rather than streaming through the conversation context. For large corpora this preserves context window for the merge step.

```
Write your analysis to spot_analyses/technique_extraction/{group}/option_a_refinement.md
```

---

## Phase 3: Merge

### 3.1 Compare and reconcile

Read both extractions and write `analysis.md` covering:

1. **Where they agree** — these are high-confidence categories
2. **What the LLM added** — sub-categories, semantic catches, merged groups
3. **What the LLM disagreed with** — flag for manual review
4. **Final category list** — the merged taxonomy with paper counts

### 3.2 Update the analysis stub

Add technique categories to the main spot analysis document (e.g., `test_time_adaptation.md`). Link to the extraction directory for full details.

### 3.3 TTA-grade quality standard (required for final doc)

Use `test_time_adaptation.md` as the reference quality bar. The final top-level analysis should be readable as a standalone document without chat context.

Required sections in final `{group}.md`:

1. **Header summary**
   - Date
   - Group + corpus count
   - Grep coverage
   - Links to Option C and Option A

2. **Method summary**
   - What Option C did
   - What Option A did
   - How reconciliation was performed

3. **Final taxonomy** (grouped into coherent blocks)
   - Taxonomy header must explicitly state category accounting, e.g.:
     - `Final Taxonomy: N Technique Categories`
     - or `Final Taxonomy: N Technique Categories + M Overlay Categories`
   - If overlay/context categories are used (domains, benchmarks, surveys), label them explicitly and keep them separate from core mechanism categories.
   - For each category include:
     - one-line mechanism definition
     - important sub-families (bullets)
     - representative `arxiv_id`s (`Key papers:`)
     - agreement/disagreement note where relevant

4. **Extraction reconciliation**
   - Where Option C and Option A agree
   - What Option A added
   - What Option A disagrees with / merges / drops

5. **Coverage reconciliation table**
   - total papers
   - grep matched
   - semantically classifiable
   - tangential papers
   - malformed/empty entries (if any)

6. **Application/domain summary** (if meaningful)
   - domain cluster table (`domain | ~papers | note`)

### 3.4 Evidence density checks (required)

Before considering Phase 3 complete, validate:

- **Category evidence:** each major category has representative `arxiv_id`s in the final doc.
- **Taxonomy accounting clarity:** header explicitly states counts for technique categories (and any overlay categories).
- **Non-trivial taxonomy:** categories are mechanism-level, not generic labels (`framework`, `pipeline`, `system`) unless explicitly scoped.
- **Overlap handling:** large overlaps are explained with explicit merges/splits.
- **Standalone clarity:** reader can understand decisions without seeing Option A/Option C raw files.

Recommended minimums:
- ≥70% of final categories include a `Key papers:` line.
- At least one explicit merge/drop decision documented in reconciliation.
- Coverage reconciliation counts included numerically.

---

## Phase 4: Paper List Regeneration

The `papers.md` file is a derived artifact — it can always be regenerated from the `spot_analysis_paper_groups` SQLite table. Regenerate whenever the group membership changes (new papers added, duplicates removed, etc.).

### 4.1 Regenerate papers.md

```bash
GROUP="{group_name}"

sqlite3 analysis_outputs/research_index.sqlite <<SQL > spot_analyses/technique_extraction/${GROUP}/papers.md
.mode list
.separator ""
SELECT '- [' || arxiv_id || '](https://arxiv.org/abs/' || arxiv_id || '): [' ||
       replace(title, '''', '''') || '](../../../' || filepath || ')'
FROM spot_analysis_paper_groups
WHERE group_name = '${GROUP}'
ORDER BY arxiv_id;
SQL
```

### 4.2 Validate

```bash
# Count matches DB expectation
echo "File lines: $(wc -l < spot_analyses/technique_extraction/${GROUP}/papers.md)"
echo "DB count:   $(sqlite3 analysis_outputs/research_index.sqlite \
  "SELECT COUNT(*) FROM spot_analysis_paper_groups WHERE group_name='${GROUP}'")"

# Spot-check digest links resolve
shuf -n 5 spot_analyses/technique_extraction/${GROUP}/papers.md | \
  sed -n 's|.*(\.\./\.\./\.\./\([^)]*\)).*|\1|p' | while read p; do
  if [ -f "$p" ]; then echo "✓ $p"; else echo "✗ $p"; fi
done
```

The link format `../../../{filepath}` assumes the standard layout where `papers.md` sits three directories below the repo root: `spot_analyses/technique_extraction/{group}/papers.md`. Adjust the relative prefix if the directory depth changes.

---

## Checklist

- [ ] Topic selected and scoped (see [topic_selection_and_scoping.md](topic_selection_and_scoping.md))
- [ ] Queue entry written in [`queue.md`](queue.md)
- [ ] Candidate search terms chosen, hit counts checked
- [ ] Term usage sampled and disambiguated
- [ ] Search terms finalized, group file list generated
- [ ] `spot_analysis_paper_groups` populated in SQLite
- [ ] Paper list markdown generated in `{group}/papers.md`, links validated
- [ ] Analysis stub created in `{group}.md`
- [ ] Phase-0 quality gate run (counts/links/join safety/scope sample)
- [ ] Core contributions exported to `/tmp/`
- [ ] Broad term frequency scan done
- [ ] Category grep patterns defined, iterated
- [ ] Coverage ≥70%
- [ ] Unmatched papers sampled and characterized
- [ ] Option C extraction written
- [ ] LLM refinement pass done (scope matched to corpus size)
- [ ] Merge written with final category list
- [ ] Final doc meets TTA-grade standalone structure (header, method, taxonomy with explicit category counts, reconciliation, coverage table)
- [ ] Final categories include representative key paper IDs (evidence density check)
- [ ] Main analysis stub updated
- [ ] Paper list regenerated from SQLite (Phase 4) if group membership changed

---

## Notes

- **Reproducibility:** Save the exact Phase-0 group definition (SQL/grep logic), Phase-1 category grep patterns, and final reconciliation decisions in-file (`overview.md` + final analysis). The LLM pass is not deterministic, but your evidence and merge rationale must be auditable.
- **Iteration:** Expect 2–3 rounds of pattern refinement in Phase 1. Don't try to get it perfect in one pass.
- **False positives vs. coverage:** Err toward broader patterns and higher coverage. False positives are easier to clean in the merge than missing categories.
- **Large corpora (>500 papers):** Phase 1 scales well. Phase 2 needs chunking. Consider adding a Step 2.4 where chunks are merged before the final analysis.
- **Tangential papers:** Every group will have 15–30% of papers that mention the topic in passing. This is expected and fine — note it in the coverage gaps section, don't force them into categories.
