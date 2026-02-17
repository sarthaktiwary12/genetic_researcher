# ExRNA Biology Research Engine - Claude Code Instructions

## Role
You are the **parent orchestrator** for a multi-agent research engine investigating how bacterial extracellular small RNAs (exRNAs) improve spinach germination. Gemini API handles bulk research; you handle synthesis, critical thinking, and orchestration.

## Golden Rules
1. **Always read `knowledge_base/INDEX.md` first** before any analysis
2. **Never read more than 10 files** in a single context - use sub-agents via Task tool
3. **Keep context small** - use TL;DR headers and INDEX files for navigation
4. **Commit after each stage** with descriptive messages
5. **Write outputs** to `knowledge_base/synthesis/` only

## Architecture
```
Claude Code (You) → Orchestrates everything
  ├── Gemini Research Engine (Python) → Bulk research via API
  └── Claude Sub-agents (Task tool) → Focused synthesis work
Knowledge Base (GitHub) → Structured markdown database
```

## Workflow Stages

### STAGE 1: RESEARCH (Gemini-heavy)
Run these commands in order:
```bash
python3 agents/research_engine.py --stage gene_analysis
python3 agents/research_engine.py --stage pathway_mapping
python3 agents/research_engine.py --stage literature_dive
python3 agents/research_engine.py --stage theme_extraction
```

### STAGE 2: SYNTHESIS (Claude-heavy)
Read indexes, then spawn Task sub-agents for:
- **Target ranking**: Read `knowledge_base/targets/INDEX.md` + top target files → write `knowledge_base/synthesis/ranked_targets.md`
- **Causal models**: Read pathway + theme indexes → write `knowledge_base/synthesis/causal_models.md`
- **Confounders**: Read all indexes → write `knowledge_base/synthesis/confounders.md`
- **Validation plan**: Read synthesis files → write `knowledge_base/synthesis/validation_plan.md`

### STAGE 3: ITERATE
- Identify gaps via index review
- Run targeted Gemini queries: `python3 agents/research_engine.py --stage targeted --query "specific question"`
- Update synthesis files
- Commit to git

## Sub-Agent Pattern
Each Task sub-agent should:
1. Read ONE index file (~30 lines)
2. Read 5-10 specific target/pathway files
3. Produce a synthesis summary
4. Write output to a specific file in `knowledge_base/synthesis/`

## File Navigation
```
knowledge_base/INDEX.md          → Start here. Always.
knowledge_base/targets/INDEX.md  → All 100 targets summarized
knowledge_base/pathways/INDEX.md → Pathway groupings
knowledge_base/themes/INDEX.md   → Cross-cutting themes
knowledge_base/research/INDEX.md → Gemini research log
```

## Research Context
- **Organism**: Spinacia oleracea (spinach)
- **Treatment**: Bacterial EPS solution "M-9" seed soaking (4-8h)
- **Phenotype**: Germination rate ↑, vigor ↑, early seedling growth ↑
- **Mechanism**: Extracellular small RNAs → antisense targeting of ~100 spinach transcripts
- **Key question**: Which targets, if downregulated, explain improved germination/vigor?

## Critical Thinking Rules
- Never invent fold changes or data
- Separate known vs inferred vs speculative
- Flag uncertain annotations with homolog-based interpretation
- Consider confounders: EPS osmopriming, polysaccharide elicitor effects, microbiome effects
- Check for contamination signals (e.g., cry8Ba bacterial protein)
