# Focused Vision — LoreblendrAI + MCP-Box + Agent Nets

Date: 2026-02-08

---

## The product is LoreblendrAI (iOS)

Everything else serves this.

---

## Three value streams, one app

### 1. MCP-Box as a Service
Teacher models (GPT-5.2, Opus) solve tasks and emit reusable MCPs. Those MCPs get packaged into MCP-Boxes. Cheap models (Qwen2.5-7B, Gemma) execute the boxes at inference without full reasoning.

**What this means for LoreblendrAI users:**
- Premium-quality output at budget-model prices
- The app ships pre-built MCP-Boxes for common creative workflows (character voice, scene generation, lore consistency, dialogue polish)
- Power users can create/share their own boxes
- Backend: teacher runs once, students run forever → margin improves with scale

**Revenue angle:**
- Free tier: basic model access
- Paid tier: MCP-Box library access (the distilled capabilities)
- Pro tier: custom box creation, teacher model access for personal distillation

### 2. Agentic Flows for Creative Output
SillyTavern users care about output quality: voice consistency, narrative coherence, character memory, style control. Current approach: one model, one prompt, hope for the best.

**What selective council does here:**
- Fast model drafts the response
- If confidence is low or the scene is complex (fight scene, plot twist, multi-character dialogue), escalate to stronger model or multi-agent flow
- Verifier checks lore consistency, character voice, continuity
- Compressor manages context so long conversations don't degrade
- User never sees the orchestration — they just get better output

**What this means for LoreblendrAI users:**
- Noticeably better creative output than single-model apps
- Automatic cost management: cheap for easy turns, expensive only when it matters
- Lore/character memory that actually works across long sessions
- Differentiator vs SillyTavern, Janitor, KoboldAI: those are chat UIs. This is an orchestrated creative engine.

### 3. Agent Nets on iOS
Bring the flatagents concept to mobile. Users visually build agent workflows ("agent nets") on their phone.

**What this looks like:**
- Drag-and-drop nodes: model call, condition, loop, verify, merge
- Pre-built templates: "writer + critic", "brainstorm → rank → refine", "character voice tuner"
- Users can chain models: use free/cheap model for drafts, paid model for polish
- Share agent nets like sharing playlists
- Power users build sophisticated flows; casual users use templates

**What this means for LoreblendrAI:**
- Unique feature no competitor has on iOS
- User-generated content (shared nets) creates ecosystem stickiness
- Advanced users become evangelists
- Each agent net is a lightweight flatmachine config under the hood

---

## How the layers map now

| Layer | What it is | Role in product |
|---|---|---|
| FlatAgents SDK | Declarative orchestration engine | Runtime powering agent nets + agentic flows on backend |
| Selective Council methodology | When/how to escalate | Decision logic inside pre-built flows + cost governor |
| MCP-Box distillation | Teacher→student capability transfer | The service layer that makes cheap models good enough |
| Research corpus + digests | Evidence base | Feeds design decisions, trains your own judgment, potentially feeds content/docs |

---

## What to build (priority order)

### Phase 1: MCP-Box proof of concept (weeks 1-3)
- Pick 3 creative tasks (character voice, scene generation, lore check)
- Run teacher (GPT-5.2) on 20-30 examples per task
- Extract + abstract MCPs
- Package into boxes
- Test: can Qwen2.5-7B with boxes match GPT-5.2 quality on these 3 tasks?
- Success metric: human eval — "which output is better?" at <30% of the cost

### Phase 2: Agentic creative flow MVP (weeks 3-5)
- Build one end-to-end flow in the app: draft → verify lore → polish
- Use selective routing: cheap model first, escalate on complexity
- Wire cost tracking so you can measure actual spend per conversation turn
- Test with real SillyTavern-style conversations
- Success metric: output quality ≥ single frontier model, cost ≤ 40% of always-frontier

### Phase 3: Agent Nets UI (weeks 5-8)
- Build visual node editor on iOS
- Ship 5 pre-built templates
- Let users connect nodes and run flows
- Share/import agent nets
- Success metric: 3 non-you users build and use a custom agent net

### Phase 4: MCP-Box marketplace (weeks 8-12)
- Users can publish boxes
- Rating/review system
- Creator gets credit/revenue share
- Curated "staff picks" library
- Success metric: 20+ community-contributed boxes

---

## What this clarifies about the research work

The digests exist to:
1. **Feed your own design decisions** — which agentic patterns to pre-build into the app
2. **Train MCP-Box creation** — the methodology guides what boxes to create and how to validate them
3. **Power the selective routing logic** — the decision rules become the actual router logic in the app

The digests do NOT need to be a standalone product. They're internal fuel.

Tomorrow when you rebuild topics from the refreshed v1 corpus, filter for:
- Creative/generative output quality techniques
- Cost-aware routing and model selection
- Distillation and capability transfer methods
- Long-context memory management for conversation
- Verification and consistency checking

Drop categories that don't serve the product (e.g., enterprise infrastructure patterns, distributed worker hardening — those are framework concerns, not app concerns).

---

## What to stop doing

- Stop assessing the SDK from the outside. You own it. Fix what blocks the app, skip what doesn't.
- Stop producing artifacts about artifacts (brainstorms about brainstorm categories about digest topics). Pick the 3 creative tasks for Phase 1 and start the teacher runs.
- Stop worrying about the JS/Rust SDK. The iOS app needs a backend service running Python flatmachines, and a mobile client. The SDK is fine for that.
- Stop grading papers for pipeline quality. v2 works. Move on.

---

## What to start doing

- Define the 3 MCP-Box proof-of-concept tasks by tomorrow
- Run the first teacher session (GPT-5.2 generating character voice examples) this week
- Sketch the agent net UI (even paper wireframes) so the iOS work has a target
- Write the one-paragraph pitch for LoreblendrAI that says what it does, not how it works

---

## The one-paragraph pitch (draft)

LoreblendrAI is an iOS app that makes AI-generated creative writing dramatically better and cheaper. Instead of sending every message to an expensive model and hoping for the best, LoreblendrAI orchestrates multiple models behind the scenes — using fast cheap models for routine turns and escalating to powerful models only when the story demands it. Pre-built "MCP-Boxes" give budget models the capabilities of premium ones. Power users can build their own "agent nets" — visual workflows that chain models, verifiers, and creative tools — and share them with the community.
