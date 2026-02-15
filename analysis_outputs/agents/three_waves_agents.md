I'll go deeper on the three waves framework. Let me pull more papers on agent evolution, composite workflows, and autonomous coordination.
Let me search for more on autonomous coordination and team dynamics.
Let me read the key collaboration and team papers.
Excellent finds! Now I have solid paper backing for all three waves. Let me synthesize this into a deep framework.
Deep dive complete! Here's the expanded Three Waves framework with full research backing:


The Three Waves: Research-Backed Breakdown

Wave 1: Narrow Agents (2025 ✅ CONFIRMED)

Evidence: AI Agent Index (Casper et al., 2502.01635)

• 67 deployed systems, 73% industry-developed
• Domain split: Software (37%) + Computer Use (37%) + Robotics (6%)
• Reality check: 80% lack safety policies—deployed fast and loose
Key Pattern: Single agent → Tool use → Human review

• Cursor, Exa, Sora, Notion AI—all narrow, role-bound, verification-light

Wave 2: Composite Agents (2026 ⚠️ FEASIBLE BUT NOT DEPLOYED)
Evidence: "When One LLM Drools..." (Han et al., 2502.04506)

• Multi-agent debate beats solo models: 94.5% vs 92.0% on GSM8K
• Diversity > scale: Small diverse models > single large model
• 15-20% hallucination reduction via collaborative fact-checking
Infrastructure requirements (from corpus):

Orchestration: HTNs (Procedural Knowledge paper—81.4% success vs 0% without)
Verification: Aspect verifiers (Multi-Agent Verification paper)
Security: Encrypted prompts (execution control layer)
Routing: Dynamic model selection (LLM Bandit—42% cost reduction)
Gap: Works in research, not yet in production. Adoption barriers = orchestration complexity + talent gap.


Wave 3: Autonomous Teams (2027+ 🔬 RESEARCH-ONLY)

Evidence: COALESCE (2506.01900)
• Skill-based task outsourcing among autonomous agents
• Nash equilibrium for market stability
• Threat taxonomy: Skill spoofing, prompt leeching, result fabrication
Evidence: Tool-RoCo (2511.21510)

• Agent-as-tool paradigm: Peers modeled as functional APIs
• Self-organization without hard-coded protocols
Gap: Simulation only. No production systems. Security/trust unsolved.


Critical Revisions from Corpus

| Claim                             | Correction                                               |
| --------------------------------- | -------------------------------------------------------- |
| "Multi-agent is production-ready" | ❌ Technically feasible, NOT deployed at scale            |
| "Agents joined workforce"         | ✅ True for digital (74%), FALSE for physical (6%)        |
| "3 waves timeline"                | Wave 1 confirmed, Wave 2 uncertain, Wave 3 research-only |

Strategic Takeaway

Build for Wave 2 now (composite workflows with verification). Wave 3 is a research bet—self-organizing teams require trust infrastructure that doesn't exist yet.

Full 23K-word analysis saved to /root/clawd/papers/analysis/three-waves-framework-deep-dive.md

---

The Three Waves of Agent Adoption
Wave 1: Narrow Agents (2025 ✅ complete)
Role-bound: research, coding, content, analysis
Tool-integrated: lives inside your existing workflow
Verification-light: fast deployment, acceptable error rate
Status: Already happened. Check your plugins.

Wave 2: Composite Agents (2026)
Multi-role: combines narrow agents into workflows
Verification-heavy: checks, validation, human-in-the-loop
Blast containment: failures isolated, not cascading
Status: Early deployments emerging.

Wave 3: Autonomous Teams (2027+)
Self-organizing: agents coordinate without human routing
Goal-driven: given objectives, find their own path
Trust-layer: reputation, verification, governance built-in
Status: Research phase.

---

Article 2 (Multi-Agent Production-Ready): ⚠️ OVERSTATED — Needs Major Revision
Critical Counter-Evidence:

• "Are We Reinventing the Wheel?" (2506.01463): Current LLM multi-agent systems ignore decades of MAS research; lack autonomy, reactivity, proactivity, social capability
• AI Agent Index (2502.01635): 67 systems deployed BUT only 19.4% have public safety policies; 80%+ lack safety transparency
Verdict: "Production-ready" is wrong framing. Agents are deployed in narrow domains (software, computer use — 74.6%) but not ready for high-stakes applications. Safety gap is massive.

Required Rewrite: Change "production-ready" → "technically feasible for low-stakes domains" + acknowledge safety gap + cite MAS heritage
