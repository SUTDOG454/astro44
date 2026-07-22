# AstroOS v3.0 Unified Architecture

AstroOS is organized as a layered platform. The computational core is deterministic and versioned; downstream predictive, relational, financial, and research systems consume canonical AstroSchema v3 data.

## Layers

1. **Computational Core v2.1** — Swiss Ephemeris, historical IANA timezone/DST normalization, object registry, geometry, canonical schema.
2. **PredictiveOS v2.2** — transits, progressions, solar arcs, returns, and timing systems.
3. **SynastryOS v2.2** — synastry, composite, Davison, relationship timing, and multi-person interaction graphs.
4. **FinancialAstroOS v2.3** — market, company, economic-event, macro-regime, and financial feature generation.
5. **AFM/AFA v3.0** — GNN, temporal models, embeddings, research experiments, hypothesis generation, validation, and promotion.

## Invariant

The v2.1 computational core is the source of canonical astronomical truth. PredictiveOS, SynastryOS, FinancialAstroOS, and AFM/AFA must not duplicate or silently override core calculations.

## Data flow

`Input -> Time Resolution -> Swiss Ephemeris -> AstroSchema v3 -> Core Engines -> Domain Feature Layers -> Unified Feature Store -> ML/Research -> Validation -> Hypothesis Registry`

## Research controls

Hypotheses are registered before evaluation, evaluated with reproducible provenance, tested out-of-sample, and promoted only after robustness and statistical validation. Discovered correlations are not automatically converted into production rules.
