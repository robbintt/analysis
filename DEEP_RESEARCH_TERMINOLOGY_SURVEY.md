# Deep Research Terminology Survey

*A running survey of key terms the literature uses for "deep research" type workflows, their meanings, use cases, and references.*

*Generated: 2026-03-05. Source corpus: ~120,000 structured ML paper analyses (2023–2025) plus cross-references.*

---

## Table of Contents

1. [Master Term List](#master-term-list)
2. [Term Definitions, Use Cases, and References](#term-definitions-use-cases-and-references)
   - [Top-Level / Umbrella Terms](#top-level--umbrella-terms)
   - [Planning and Decomposition](#planning-and-decomposition)
   - [Retrieval and Information Acquisition](#retrieval-and-information-acquisition)
   - [Synthesis and Report Generation](#synthesis-and-report-generation)
   - [Agent Architecture and Orchestration](#agent-architecture-and-orchestration)
   - [Memory and State Management](#memory-and-state-management)
   - [Evaluation and Benchmarking](#evaluation-and-benchmarking)
   - [Domain-Specific and Specialized Variants](#domain-specific-and-specialized-variants)
   - [Commercial Implementations](#commercial-implementations)
3. [Review Notes: Omissions and Enhancements](#review-notes-omissions-and-enhancements)

---

## Master Term List

The following terms are used in the literature to describe, name, or characterize "deep research" type workflows. Grouped by conceptual area; alphabetical within each group.

### Top-Level / Umbrella Terms
1. Agentic Search
2. AI Scientist / Full-stack AI Scientist
3. Automated Literature Review
4. Autonomous Research Agent
5. Deep AI Research System (DARS)
6. Deep Research (DR)
7. Deep Research Agent (DRA)
8. Deep Research System
9. Integrated Research
10. Open-ended Information Seeking
11. Research Agent
12. Research Workflow Automation
13. Survey Automation / Automated Survey Generation

### Planning and Decomposition
14. Hierarchical Task Decomposition
15. Iterative Query Planning
16. Multi-stage Reasoning Decomposition
17. Query Decomposition (parallel, sequential, tree-based)
18. Query Routing
19. Subquery Tree
20. Task Decomposition
21. Task Planning

### Retrieval and Information Acquisition
22. Adaptive Retrieval / Adaptive Retrieval Triggering
23. Agentic RAG / Agentic Retrieval-Augmented Generation
24. Cross-source Retrieval
25. Evidence Gathering
26. Incremental Information Retrieval
27. Information Acquisition
28. Iterative Retrieval
29. Knowledge Gap Self-Diagnosis
30. Multi-hop Reasoning / Multi-hop QA
31. Multi-paradigm Retrieval
32. Proactive Retrieval
33. Retrieval-Augmented Reasoning
34. Viewpoint-aware Retrieval
35. Web Exploration / Web Navigation

### Synthesis and Report Generation
36. Citation Grounding / Citation Verification
37. Conflict-Aware Synthesis
38. Evidence Synthesis
39. Generative Research Synthesis
40. Knowledge Synthesis
41. Long-form Report Generation
42. Nugget Coverage
43. Paper Card Distillation
44. Reasoning Coherence Preservation
45. Report Generation
46. Research Synthesis
47. Structured Synthesis

### Agent Architecture and Orchestration
48. Agentic Control Flow
49. Dual-System Deep Research
50. Multi-Agent Workflow / Multi-Agent Research System
51. Plan-Code-Observe-Reflect Loop
52. Recursive Agentic Workflow
53. Simulate Before Act
54. Tool Orchestration / Tool Utilization
55. Vertical Multi-Agent System

### Memory and State Management
56. Compressed Experience Buffer
57. Dynamic Knowledge Base
58. Experience Buffer / Interaction Buffer
59. Memory Lifecycle Management
60. Memory Management
61. Persistent World State

### Evaluation and Benchmarking
62. DeepResearch-Bench
63. DR-Arena
64. DR-Bench
65. FACT Framework
66. Faithfulness vs. Groundedness
67. IntegratedScore
68. LLM-as-Judge
69. Process-aware Evaluation
70. RACE Framework
71. ResearcherBench
72. ResearchRubrics
73. Rubric-Based Evaluation
74. ScholarGym
75. Semantic Drift (evaluation metric)

### Domain-Specific and Specialized Variants
76. Iterative Survey Generation (IterSurvey)
77. Multimodal Deep Research
78. PICOS Framework (medical evidence synthesis)
79. Recurrent Outline Generation
80. Semi-Autonomous Mode
81. Two-Stage Writing Framework

### Commercial Implementations
82. Gemini Deep Research (Google)
83. OpenAI Deep Research (ChatGPT)
84. Perplexity (AI research tool)

---

## Term Definitions, Use Cases, and References

### Top-Level / Umbrella Terms

#### 1. Deep Research (DR)
**Definition:** AI systems that integrate LLMs with external tools to enable autonomous, multi-source, verifiable knowledge acquisition and synthesis. The term originated as a product name (OpenAI, Google) and was subsequently adopted by the academic community as a field descriptor.

**Use cases:** End-to-end research workflows from complex query to cited report, including web search, document analysis, evidence aggregation, and structured output generation.

**References:**
- arXiv 2512.02038 — *Deep Research: A Systematic Survey*. Defines DR systems as integrating LLMs with external tools for autonomous knowledge acquisition. Proposes a three-stage evolution: Agentic Search → Integrated Research → Full-stack AI Scientist.
- arXiv 2506.12594 — *A Comprehensive Survey of Deep Research: Systems, Methodologies, and Applications*. Describes DR systems as AI-powered applications automating complex research workflows through LLMs, advanced retrieval, and autonomous reasoning.
- arXiv 2508.12752 — *Deep Research: A Survey of Autonomous Research Agents*. Frames DR agents as autonomous systems performing complex research tasks by integrating planning, web exploration, and report generation.

#### 2. Deep Research Agent (DRA)
**Definition:** An autonomous agent that conducts multi-step research tasks: decomposes queries, searches the web or document corpora, synthesizes findings into structured reports with citations.

**Use cases:** Generating citation-rich research reports, performing literature reviews, answering complex multi-faceted questions.

**References:**
- arXiv 2506.11763 — *DeepResearch-Bench*. Defines DRAs as systems that autonomously generate citation-rich research reports from web information.
- arXiv 2510.02190 — *DR-Bench*. Defines DRAs as systems performing long-form report generation from complex queries.
- arXiv 2511.07685 — *ResearchRubrics*. Describes DRAs as LLM-based systems that conduct extended research tasks with evaluable outputs.

#### 3. Deep AI Research System (DARS)
**Definition:** Agentic systems capable of multi-iteration retrieval and dynamic planning, explicitly distinguished from single-turn RAG by their iterative and adaptive nature.

**Use cases:** Frontier scientific inquiry, multi-hop question answering requiring iterative literature search.

**References:**
- arXiv 2507.16280 — *ResearcherBench: Evaluating Deep AI Research Systems on the Frontiers of Scientific Inquiry*. Introduces DARS as a formal category.

#### 4. Autonomous Research Agent
**Definition:** An AI agent that independently conducts research tasks with minimal human supervision, encompassing planning, retrieval, analysis, and reporting.

**Use cases:** Scientific discovery, literature reviews, evidence-based report generation.

**References:**
- arXiv 2508.12752 — *Deep Research: A Survey of Autonomous Research Agents*. Central framing term throughout.
- arXiv 2601.12542 — *Rethinking the AI Scientist*. Explores interactive multi-agent workflows for scientific discovery as a form of autonomous research.

#### 5. AI Scientist / Full-stack AI Scientist
**Definition:** The most advanced vision of deep research: an autonomous system capable of the complete scientific workflow — hypothesis generation, literature review, experiment design, execution, analysis, and paper writing.

**Use cases:** Fully autonomous scientific discovery, end-to-end research automation.

**References:**
- arXiv 2512.02038 — *Deep Research: A Systematic Survey*. Positions "Full-stack AI Scientist" as the third stage in the evolution from Agentic Search → Integrated Research → Full-stack AI Scientist.
- arXiv 2601.12542 — *Rethinking the AI Scientist*. Proposes interactive multi-agent workflows with plan-code-observe-reflect loops.

#### 6. Agentic Search
**Definition:** The first stage of deep research evolution where tool-using agents employ perception, planning, and action capabilities to conduct searches beyond simple query-response.

**Use cases:** Complex web searches requiring multi-step navigation, evidence verification, and adaptive query refinement.

**References:**
- arXiv 2512.02038 — *Deep Research: A Systematic Survey*. Defines Agentic Search as the first phase of a three-stage evolution.
- arXiv 2501.05366 — *Search-o1: Agentic Search-Enhanced Large Reasoning Models*. Demonstrates agentic search where models autonomously decide when to retrieve via special tokens during reasoning.

#### 7. Integrated Research
**Definition:** The second stage of deep research evolution, characterized by more complex tool orchestration and tighter integration between retrieval, reasoning, and synthesis components.

**Use cases:** Research tasks requiring coordination of multiple tools and information sources with dynamic planning.

**References:**
- arXiv 2512.02038 — *Deep Research: A Systematic Survey*. Positions Integrated Research as the middle evolutionary stage between Agentic Search and Full-stack AI Scientist.

#### 8. Research Agent
**Definition:** An LLM-based agent designed to assist with or automate research tasks, including idea generation, literature search, and evidence synthesis.

**Use cases:** Iterative research idea generation, literature discovery, research assistance.

**References:**
- arXiv 2404.07738 — *ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models*.
- arXiv 2406.10291 — *ResearchArena: Benchmarking LLMs' Ability to Collect and Organize Information as Research Agents*.

#### 9. Automated Literature Review / Survey Automation
**Definition:** Systems that automate the process of surveying, organizing, and synthesizing scientific literature into structured review documents.

**Use cases:** Generating survey papers, literature reviews, systematic reviews, annotated bibliographies.

**References:**
- arXiv 2510.21900 — *IterSurvey: Deep Literature Survey Automation with Iterative Workflow*. Introduces iterative cycles of retrieval, reading, and updating for survey generation.
- arXiv 2510.07733 — *SurveyG*. Uses hierarchical citation graphs for automated survey generation.
- arXiv 2508.14317, 2508.17647 — *SurveyGen* variants. Scientific survey generation with LLMs.

#### 10. Open-ended Information Seeking
**Definition:** Research workflows aimed at generating diverse perspectives and comprehensive coverage rather than converging on a single answer.

**Use cases:** Exploratory research, generating multi-perspective reports, broad literature coverage.

**References:**
- arXiv 2602.00238 — *DIVERGE*. Framework for open-ended information seeking with viewpoint-aware retrieval and diversity-conscious generation.

#### 11. Research Workflow Automation
**Definition:** The broader concept of automating any part of the research pipeline — from literature search to experiment execution to writing.

**Use cases:** Accelerating research productivity, reducing manual literature search effort.

**References:**
- arXiv 2601.21654 — *ScholarGym: Benchmarking Deep Research Workflows on Academic Literature Retrieval*. Focuses specifically on benchmarking the workflow itself.

---

### Planning and Decomposition

#### 12. Query Decomposition / Task Decomposition
**Definition:** Breaking a complex research question into smaller, manageable sub-queries or sub-tasks that can be executed independently or in sequence.

**Use cases:** Multi-faceted research questions, divide-and-conquer strategies for complex information needs.

**Variants:**
- **Parallel decomposition** — Sub-queries executed simultaneously.
- **Sequential decomposition** — Sub-queries executed in order, each informed by prior results.
- **Tree-based decomposition** — Hierarchical branching of sub-queries.

**References:**
- arXiv 2512.02038 — *Deep Research: A Systematic Survey*. Describes query planning as transforming complex questions into structured sequences of executable sub-queries.
- arXiv 2510.02190 — *DR-Bench*. Uses task decomposition as a core evaluation dimension.
- arXiv 2506.12594 — *Comprehensive Survey*. Describes hierarchical task decomposition breaking high-level goals into subtasks.

#### 13. Iterative Query Planning
**Definition:** A planning approach where queries are refined and expanded across multiple stages based on intermediate results, rather than planned all at once upfront.

**Use cases:** Literature search where initial results inform follow-up queries, progressive deepening of research scope.

**References:**
- arXiv 2601.21654 — *ScholarGym*. Defines iterative query planning with DERIVE/EXPAND operations and subquery trees.
- arXiv 2510.21900 — *IterSurvey*. Uses recurrent outline generation with iterative retrieval-reading-updating cycles.

#### 14. Multi-stage Reasoning Decomposition
**Definition:** Breaking the reasoning process itself into multiple stages, where the quality of intermediate reasoning steps directly correlates with final output quality.

**Use cases:** Complex scientific questions requiring stepwise logical analysis.

**References:**
- arXiv 2506.12594 — *Comprehensive Survey*. Notes that quality of intermediate reasoning steps correlates with final output quality.

#### 15. Subquery Tree
**Definition:** A memory structure that tracks the hierarchy of queries and sub-queries across iterations, maintaining the logical relationships between them.

**Use cases:** Managing complex multi-hop research sessions, tracking which sub-questions have been answered.

**References:**
- arXiv 2601.21654 — *ScholarGym*. Introduces the subquery tree (Mt) as a core memory structure.

---

### Retrieval and Information Acquisition

#### 16. Adaptive Retrieval / Adaptive Retrieval Triggering
**Definition:** Invoking retrieval only when the model determines it lacks sufficient knowledge, based on confidence signals, rather than retrieving at every step.

**Use cases:** Efficient research workflows that minimize unnecessary API calls while ensuring coverage.

**References:**
- arXiv 2512.02038 — *Deep Research: A Systematic Survey*. Describes adaptive retrieval as retrieval invoked by confidence signals.
- arXiv 2501.05366 — *Search-o1*. Model autonomously decides when to retrieve via special tokens during reasoning.

#### 17. Agentic RAG / Agentic Retrieval-Augmented Generation
**Definition:** An extension of RAG where the retrieval component is an autonomous agent capable of planning, executing multi-step searches, and adaptively refining queries — going beyond single-query retrieve-and-read.

**Use cases:** Complex research questions requiring multiple retrieval rounds, tool selection, and dynamic strategy.

**References:**
- arXiv 2601.21916 — *JADE*. Strategic and operational agentic RAG.
- arXiv 2504.07643 — *COLLEX*. Multimodal agentic RAG for scientific collections.
- arXiv 2510.14278 — *PRISM*; arXiv 2510.07794 — *HIPRAG*. Multi-hop reasoning within agentic RAG.
- arXiv 2501.05366 — *Search-o1*. Agentic search-enhanced reasoning models.

#### 18. Retrieval-Augmented Reasoning
**Definition:** Integrating retrieved information into ongoing reasoning chains with factual grounding, as distinct from simple RAG which retrieves then generates in a single pass.

**Use cases:** Multi-step reasoning tasks requiring external knowledge at intermediate steps.

**References:**
- arXiv 2506.12594 — *Comprehensive Survey*. Frames retrieval-augmented reasoning as a core deep research capability.
- arXiv 2501.05366 — *Search-o1*. Uses a Reason-in-Documents module that refines retrieved information before injection into the reasoning chain.

#### 19. Multi-hop Reasoning / Multi-hop QA
**Definition:** Reasoning that requires synthesizing information from multiple sources or documents, connected through intermediate inference steps.

**Use cases:** Complex factual questions where the answer spans multiple documents.

**References:**
- arXiv 2501.05366 — *Search-o1*. Shows 23.2% improvement on multi-hop tasks with agentic search vs. minimal gain on single-hop.
- arXiv 2510.14278 — *PRISM*; arXiv 2510.07794 — *HIPRAG*. Multi-hop reasoning in retrieval pipelines.

#### 20. Cross-source Retrieval
**Definition:** Gathering and integrating evidence from multiple heterogeneous information sources (web, databases, APIs, documents).

**Use cases:** Research requiring synthesis across academic papers, web pages, and structured data.

**References:**
- arXiv 2510.02190 — *DR-Bench*. Evaluates cross-source retrieval as a dimension of deep research capability.

#### 21. Web Exploration / Web Navigation
**Definition:** The capability of research agents to navigate web pages, follow links, extract information from diverse page structures, and explore search results beyond surface-level snippets.

**Use cases:** Browser-based research agents, web crawling for evidence.

**References:**
- arXiv 2508.12752 — *Survey of Autonomous Research Agents*. Identifies web exploration as a core module of DRAs.

#### 22. Knowledge Gap Self-Diagnosis
**Definition:** A model's ability to identify, during its own reasoning process, when it lacks sufficient information and needs to retrieve more.

**Use cases:** Triggering retrieval mid-reasoning, avoiding hallucination by recognizing uncertainty.

**References:**
- arXiv 2501.05366 — *Search-o1*. Core mechanism enabling the model to autonomously decide when to search.

#### 23. Viewpoint-aware Retrieval
**Definition:** Diversity-conscious document selection that ensures multiple perspectives are represented in retrieved evidence.

**Use cases:** Open-ended research, balanced analysis, avoiding confirmation bias in retrieval.

**References:**
- arXiv 2602.00238 — *DIVERGE*. Introduces viewpoint-aware retrieval for open-ended information seeking.

#### 24. Incremental Information Retrieval
**Definition:** Progressive expansion of literature coverage through multiple retrieval rounds, each building on previous results.

**Use cases:** Survey generation, comprehensive literature reviews.

**References:**
- arXiv 2510.21900 — *IterSurvey*. Uses incremental retrieval as part of its iterative workflow.

---

### Synthesis and Report Generation

#### 25. Long-form Report Generation
**Definition:** Generating extended, structured research documents (as opposed to short answers), typically with sections, citations, and evidence synthesis.

**Use cases:** Research reports, literature reviews, policy briefs, technical surveys.

**References:**
- arXiv 2510.02190 — *DR-Bench*. Explicitly evaluates long-form report generation as distinct from short-answer QA.
- arXiv 2508.15804 — *ReportBench*. Benchmark for evaluating deep research agent report quality.

#### 26. Conflict-Aware Synthesis
**Definition:** Explicit detection and resolution of conflicting evidence from multiple sources during the synthesis process.

**Use cases:** Research topics with contradictory findings, evolving scientific consensus.

**References:**
- arXiv 2508.12752 — *Survey of Autonomous Research Agents*. Identifies conflict-aware synthesis with evidence-grounded decoding as key to factual consistency.

#### 27. Citation Grounding / Citation Verification
**Definition:** Ensuring that claims in generated reports are supported by and accurately attributed to specific source documents.

**Use cases:** Academic research reports, evidence-based analysis, verifiable outputs.

**References:**
- arXiv 2506.11763 — *DeepResearch-Bench*. FACT framework measures citation accuracy and effective citation counts.
- arXiv 2507.16280 — *ResearcherBench*. Distinguishes faithfulness (accuracy of cited claims) from groundedness (proportion of claims with citations).

#### 28. Faithfulness vs. Groundedness
**Definition:** Two distinct dimensions of citation quality. Faithfulness = accuracy of individual cited claims. Groundedness = proportion of all claims that have explicit citation support. Top systems can have high faithfulness but low groundedness (the "High Faith, Low Ground" paradox).

**Use cases:** Evaluation of research report quality, understanding citation coverage gaps.

**References:**
- arXiv 2507.16280 — *ResearcherBench*. Introduces this distinction and documents the paradox.

#### 29. Generative Research Synthesis
**Definition:** Creating long-form, cited research summaries from multiple sources through generative AI, as opposed to extractive summarization.

**Use cases:** Comprehensive literature reviews, state-of-the-art summaries.

**References:**
- General usage across multiple deep research papers.

#### 30. Knowledge Synthesis
**Definition:** Multi-agent coordination enabling specialized capability composition for integrating knowledge from diverse sources.

**Use cases:** Multi-faceted research requiring integration of different domains or source types.

**References:**
- arXiv 2506.12594 — *Comprehensive Survey*. Positions knowledge synthesis as a core capability enabled by multi-agent coordination.

#### 31. Evidence Synthesis
**Definition:** Aggregating evidence from multiple studies or sources, especially in medical and clinical contexts. Distinct from general knowledge synthesis in its emphasis on study quality, bias assessment, and structured evidence hierarchies.

**Use cases:** Systematic reviews, clinical guideline development, meta-analysis.

**References:**
- Medical deep research papers in the corpus. Uses the PICOS framework (Population, Intervention, Comparator, Outcome, Study design).

#### 32. Nugget Coverage
**Definition:** A metric measuring the completeness of unique information items (nuggets) extracted and represented from source materials.

**Use cases:** Evaluating whether a generated report captured all key findings from the literature.

**References:**
- Used in deep research evaluation frameworks as a completeness metric.

#### 33. Paper Card Distillation
**Definition:** A structured extraction technique that creates compact summaries ("cards") of each paper's key contributions, methods, and findings for use in survey generation.

**Use cases:** Automated survey generation, literature review preprocessing.

**References:**
- arXiv 2510.21900 — *IterSurvey*. Uses paper card distillation as a core pipeline step.

#### 34. Structured Synthesis
**Definition:** Organized composition of retrieved evidence into coherent, well-structured reports with sections, hierarchies, and logical flow.

**Use cases:** Research reports, surveys, technical documentation.

**References:**
- arXiv 2510.02190 — *DR-Bench*. Evaluates structured synthesis as part of the deep research pipeline.

---

### Agent Architecture and Orchestration

#### 35. Agentic Control Flow
**Definition:** The autonomous decision-making pattern in research agents that governs when to plan, retrieve, analyze, or synthesize — executing multi-step workflows rather than single-turn queries.

**Use cases:** End-to-end research automation, dynamic task execution.

**References:**
- arXiv 2506.12594 — *Comprehensive Survey*. Identifies agentic control flow as what distinguishes deep research from standard RAG.

#### 36. Multi-Agent Workflow / Multi-Agent Research System
**Definition:** Architectures where multiple specialized agents (planner, searcher, analyst, writer, reviewer) collaborate to complete research tasks.

**Use cases:** Complex research requiring specialized capabilities, quality assurance through review agents.

**References:**
- arXiv 2511.13288 — *Multi-Agent Deep Research*. Trains multi-agent systems with M-GRPO for research tasks.
- arXiv 2601.12542 — *Rethinking the AI Scientist*. Interactive multi-agent workflows for scientific discovery.

#### 37. Vertical Multi-Agent System
**Definition:** A hierarchical multi-agent architecture with a main planner delegating to specialized sub-agents, as opposed to flat peer-to-peer coordination.

**Use cases:** Structured research workflows where a coordinator manages specialist agents.

**References:**
- arXiv 2511.13288 — *Multi-Agent Deep Research*. Uses vertical architecture with hierarchical reinforcement learning.

#### 38. Dual-System Deep Research
**Definition:** A framework inspired by dual-process theory (Kahneman's System 1/System 2) where a fast system extracts and distills information while a deliberate reasoning system performs complex analysis.

**Use cases:** Balancing efficiency (fast information extraction) with depth (careful reasoning).

**References:**
- arXiv 2510.04935 — *MARS: Co-evolving Dual-System Deep Research via Multi-Agent Reinforcement Learning*. System 1 extracts task-relevant information; System 2 performs deliberate reasoning.

#### 39. Recursive Agentic Workflow
**Definition:** A parameter-driven workflow that repeats research stages (search, analyze, refine) with controllable depth and breadth parameters.

**Use cases:** Scaling research depth and breadth by adjusting recursion parameters.

**References:**
- arXiv 2507.10522 — *DeepResearchEco*. Uses depth parameter d ∈ {1,4} for recursion layers and breadth parameter b ∈ {1,4} for parallel query branching.

#### 40. Tool Orchestration / Tool Utilization
**Definition:** Dynamic coordination of heterogeneous tools (search engines, calculators, code interpreters, databases) as part of the research workflow.

**Use cases:** Research tasks requiring different tool types at different stages.

**References:**
- arXiv 2506.12594 — *Comprehensive Survey*. Identifies tool utilization as a foundational capability of deep research systems.

#### 41. Simulate Before Act
**Definition:** An explicit simulation phase where agents mentally roll out candidate action trajectories before executing them, selecting the most promising approach.

**Use cases:** Reducing wasted research steps, optimizing tool-call strategies.

**References:**
- arXiv 2508.12752 — *Survey of Autonomous Research Agents*. Describes the Simulate Before Act framework for planning.

#### 42. Plan-Code-Observe-Reflect Loop
**Definition:** A four-phase cycle for data analysis agents: plan what to investigate, write code to execute, observe the results, and reflect on what was learned before the next iteration.

**Use cases:** Scientific data analysis, computational experiments within research workflows.

**References:**
- arXiv 2601.12542 — *Rethinking the AI Scientist*.

#### 43. Reasoning Coherence Preservation
**Definition:** Techniques to maintain the integrity of a model's reasoning chain when injecting retrieved information, preventing noise from disrupting logical flow.

**Use cases:** Any retrieval-augmented reasoning system.

**References:**
- arXiv 2501.05366 — *Search-o1*. Decouples document analysis from the main reasoning flow via a separate Reason-in-Documents module.

---

### Memory and State Management

#### 44. Memory Management / Memory Lifecycle Management
**Definition:** Operations for consolidation, indexing, updating, and forgetting of information during long-horizon research sessions.

**Use cases:** Multi-session research, maintaining coherence across extended workflows.

**References:**
- arXiv 2512.02038 — *Deep Research: A Systematic Survey*. Identifies memory management as a core component of DR systems.

#### 45. Persistent World State
**Definition:** A structured representation (e.g., JSON object) maintaining accumulated context across iterative research cycles, as opposed to relying on conversation history.

**Use cases:** Long-running research agents, multi-session scientific discovery.

**References:**
- arXiv 2601.12542 — *Rethinking the AI Scientist*. Maintains a persistent world state across plan-code-observe-reflect cycles.

#### 46. Compressed Experience Buffer
**Definition:** A memory structure that maintains a compressed but coherent representation of the agent's interaction history for use in planning.

**Use cases:** Managing context windows in long-horizon research, efficient state representation.

**References:**
- arXiv 2601.21654 — *ScholarGym*. Uses compressed experience buffer (Bt) alongside subquery trees.

#### 47. Dynamic Knowledge Base
**Definition:** A knowledge store that evolves during the research process — rules and context items are added, updated, or removed based on observations.

**Use cases:** Constraining code generation based on observed data, accumulating research findings.

**References:**
- arXiv 2601.12542 — *Rethinking the AI Scientist*. Rules + context items constraining code generation based on observed data.

---

### Evaluation and Benchmarking

#### 48. DR-Arena
**Definition:** An automated evaluation framework using information trees (directed graphs from web crawls) with adaptive task complexity escalation.

**Use cases:** Benchmarking DRA depth (multi-hop logic) vs. width (information aggregation) capabilities.

**References:**
- arXiv 2601.10504 — *DR-Arena: An Automated Evaluation Framework for Deep Research Agents*.

#### 49. DR-Bench
**Definition:** A multidimensional evaluation framework measuring semantic quality, topical focus, and retrieval trustworthiness for deep research agents.

**Key metrics:** IntegratedScore = Quality × (1 − SemanticDrift) × TrustworthyBoost.

**References:**
- arXiv 2510.02190 — *DR-Bench: A Multidimensional Evaluation for Deep Research Agents, From Answers to Reports*.

#### 50. DeepResearch-Bench
**Definition:** A comprehensive benchmark evaluating DRAs on report quality using the RACE framework (reference-based adaptive criteria scoring) and FACT framework (citation accuracy).

**References:**
- arXiv 2506.11763 — *DeepResearch-Bench: A Comprehensive Benchmark for Deep Research Agents*.

#### 51. ResearcherBench
**Definition:** An evaluation framework for deep AI research systems on frontier scientific inquiry, distinguishing faithfulness from groundedness.

**References:**
- arXiv 2507.16280 — *ResearcherBench: Evaluating Deep AI Research Systems on the Frontiers of Scientific Inquiry*.

#### 52. ResearchRubrics
**Definition:** A benchmark using expert-written rubrics (not reference-based metrics) with a tri-axial complexity framework: Conceptual Breadth, Logical Nesting, and Exploration.

**References:**
- arXiv 2511.07685 — *ResearchRubrics: A Benchmark of Prompts and Rubrics for Evaluating Deep Research Agents*.

#### 53. ScholarGym
**Definition:** A benchmark for deep research workflows focused specifically on academic literature retrieval, with iterative query planning as the core capability.

**References:**
- arXiv 2601.21654 — *ScholarGym: Benchmarking Deep Research Workflows on Academic Literature Retrieval*.

#### 54. LLM-as-Judge
**Definition:** Using a language model as an automated evaluator to assess research outputs against criteria or rubrics, replacing or supplementing human evaluation.

**Use cases:** Scalable evaluation of deep research outputs, benchmark automation.

**References:**
- arXiv 2511.07685 — *ResearchRubrics*. Uses LLM-as-Judge with ternary grading (Satisfied/Partially Satisfied/Not Satisfied).
- arXiv 2507.16280 — *ResearcherBench*. Uses LLM-as-a-Judge for hierarchical claim verification.

#### 55. Semantic Drift
**Definition:** A measure of models losing focus on the core task during multi-stage generation, wandering from the original research question.

**Use cases:** Evaluating whether long-form reports stay on topic.

**References:**
- arXiv 2510.02190 — *DR-Bench*. Incorporates semantic drift as a penalty in the IntegratedScore.

#### 56. Process-aware Evaluation
**Definition:** Evaluating the full research trajectory (planning, retrieval, reasoning steps) rather than just the final output.

**Use cases:** Understanding where research agents succeed or fail, debugging workflows.

**References:**
- Used in ScholarGym, DR-Arena, and other benchmarks that audit intermediate steps.

---

### Domain-Specific and Specialized Variants

#### 57. Iterative Survey Generation (IterSurvey)
**Definition:** A deep literature survey automation approach using recurrent outline generation — iterative cycles of retrieval, reading, and updating, with review-and-refine loops.

**References:**
- arXiv 2510.21900 — *IterSurvey: Deep Literature Survey Automation with Iterative Workflow*.

#### 58. Multimodal Deep Research
**Definition:** Deep research workflows that integrate text, charts, images, and other modalities in both retrieval and report generation.

**References:**
- arXiv 2506.02454 — *Multimodal DeepResearcher: Generating Text-Chart Interleaved Reports from Scratch with Agentic Framework*.

#### 59. Recurrent Outline Generation
**Definition:** An iterative approach to structuring research output where the outline is progressively refined through multiple retrieval-reading-updating cycles.

**References:**
- arXiv 2510.21900 — *IterSurvey*.

#### 60. Semi-Autonomous Mode
**Definition:** A research mode where human checkpoints are triggered by specific conditions (contradiction detection, ambiguity) rather than requiring constant oversight.

**References:**
- arXiv 2601.12542 — *Rethinking the AI Scientist*.

#### 61. PICOS Framework
**Definition:** A structured framework for medical evidence synthesis: Population, Intervention, Comparator, Outcome, Study design. Used to formalize clinical research questions for automated evidence review.

**References:**
- Medical deep research papers in the corpus.

#### 62. Two-Stage Writing Framework
**Definition:** Separating the analysis/research phase from the synthesis/writing phase in report generation.

**References:**
- Referenced in multiple deep research system designs.

---

### Commercial Implementations

#### 63. OpenAI Deep Research
**Definition:** OpenAI's product feature enabling ChatGPT to conduct autonomous multi-step web research and produce comprehensive reports. One of the first commercial products to use the "deep research" label.

**References:**
- Referenced in arXiv 2506.12594, 2507.16280, 2509.13309, 2510.16844.

#### 64. Gemini Deep Research
**Definition:** Google's implementation of deep research capabilities within the Gemini product line, enabling extended autonomous research workflows.

**References:**
- Referenced in arXiv 2506.12594, 2507.16280, 2510.16844.

#### 65. Perplexity
**Definition:** An AI-powered research tool that combines search with LLM-based synthesis, often benchmarked alongside dedicated deep research systems.

**References:**
- Referenced in arXiv 2506.12594 and evaluation papers.

---

## Review Notes: Omissions and Enhancements

After compiling the full document, the following observations and potential enhancements were identified:

### Potential Omissions

1. **Reward-based Training for Deep Research.** Several papers (MARS, Multi-Agent DR) train research agents with reinforcement learning. Terms like **GRPO (Group Relative Policy Optimization)**, **M-GRPO**, and **Dual-Reward Optimization** are emerging as training paradigms specific to deep research agents. These deserve tracking as the field matures.

2. **Hallucination Propagation / Error Compounding.** The phenomenon where errors in early research steps compound through the workflow. The PIES taxonomy (from the literature) categorizes hallucination types in research trajectories. This is a failure mode unique to multi-step research workflows that deserves its own term entry.

3. **Cognitive Biases in DRAs.** Deep research agents exhibit systematic biases (anchor effects, homogeneity bias, recency bias in retrieval). This is an emerging area that may warrant its own terminology as evaluation frameworks mature.

4. **Model Context Protocol (MCP).** A standardization effort for tool integration interfaces. While not specific to deep research, MCP is becoming the de facto interface standard for research agents' tool connections.

5. **State Drift.** Related to but distinct from semantic drift — the phenomenon where accumulated context loses early constraints through summarization or compression failures. Documented in the AI Scientist literature (arXiv 2601.12542).

6. **Depth vs. Breadth Parameters.** DeepResearchEco (arXiv 2507.10522) introduces explicit parameterization of research depth and breadth. The finding that information density scales super-linearly (21x sources = only 41.5% more words) is a key insight for workflow design.

7. **Budget-Constrained Research.** Several systems implement explicit computational or API-call budgets. The trade-off between research thoroughness and resource consumption is under-discussed in the terminology literature.

8. **Hierarchical Citation Graph.** Used by SurveyG (arXiv 2510.07733) to organize papers by Foundation/Development/Frontier layers. A structural concept for automated survey generation.

### Enhancement Opportunities

1. **Taxonomy consolidation.** Many terms overlap (e.g., "query decomposition" vs. "task decomposition" vs. "hierarchical task decomposition"). A formal taxonomy mapping relationships between these terms would aid standardization.

2. **Evolution tracking.** Tracking how terminology evolves over time. "Deep research" as a field label only emerged in late 2024 / early 2025 via commercial products and was rapidly adopted by academia. Earlier work used "autonomous research agent," "AI scientist," or domain-specific terms.

3. **Cross-referencing with the general AI/ML terms.** The existing TERMS_ANALYSIS.md covers 50 core AI/ML terms. Several overlap with deep research terminology (RAG, Agentic AI, Multi-Agent Systems, Chain-of-Thought). A cross-reference map would show how deep research draws on and extends these foundational concepts.

4. **Failure mode vocabulary.** The literature is developing specific terms for deep research failures: hallucination propagation, state drift, semantic drift, tool-call hacking, reward hacking in trained DRAs. A dedicated failure-mode section could be added as this vocabulary stabilizes.

5. **Evaluation metric relationships.** The many evaluation frameworks (DR-Arena, DR-Bench, DeepResearch-Bench, ResearcherBench, ResearchRubrics, ScholarGym) each introduce their own metrics. A comparison table mapping which aspects each benchmark evaluates would aid researchers selecting evaluation approaches.

6. **Industry vs. academic terminology.** Commercial products (OpenAI, Google, Perplexity) tend to use simpler terms ("deep research"), while academic papers use more precise but varied terminology. Documenting this gap would be valuable.

---

*End of survey. This is a living document; additions should be appended to the relevant sections.*
