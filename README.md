# Astrology Repository - SUTDOG454/astro44

## Overview
This is a **comprehensive astrology knowledge base** containing frameworks, interpretations, delineations, and reference materials for:
- Natal chart analysis
- Synastry and relationship astrology
- Transit predictions
- Vedic astrology
- Psychological astrology
- Planetary symbolism and meanings
- House and aspect interpretations
- Advanced astrological methodologies (Magi Astrology, midpoints, harmonics, etc.)

**Status**: Under reorganization and deduplication (as of June 2026)

---

## Directory Structure

```
astro44/
├── README.md (this file)
├── REPOSITORY_ORGANIZATION_PLAN.md
├── .gitignore
├── .gitattributes
│
├── docs/                                    # Documentation & Guides
│   ├── README_DOCS.md
│   ├── MASTER_FRAMEWORK.md                 # Master unified framework
│   ├── QUICKSTART.md                       # Getting started guide
│   ├── contributing.md                      # Contribution guidelines
│   └── DEDUPLICATION_LOG.md                # Log of cleanup operations
│
├── frameworks/                             # Core Astrological Frameworks
│   ├── README_FRAMEWORKS.md
│   ├── natal/                              # Natal chart interpretation
│   │   ├── MASTER_UNIFIED_ASTROLOGY_FRAMEWORK.json
│   │   ├── natal_chart_interpretation.json
│   │   ├── birth_chart_components.json
│   │   └── core_identity_formula.json
│   │
│   ├── synastry/                           # Relationship astrology
│   │   ├── synastry_master_framework.json
│   │   ├── synastry_house_overlays.json
│   │   ├── anti_vertex_synastry_framework.json
│   │   ├── hieros_gamos_sacred_marriage.json
│   │   └── relationship_timing_techniques.json
│   │
│   ├── transits/                           # Transit & progression systems
│   │   ├── astrological_transits_2026.json
│   │   ├── transit_tracking_predictive.json
│   │   ├── secondary_progressions.json
│   │   ├── solar_arc_directions.json
│   │   └── venus_pluto_conjunction_2026.json
│   │
│   ├── vedic/                              # Vedic/Eastern astrology
│   │   ├── vedic_astrology_framework.json
│   │   ├── dashas_system.json
│   │   └── rashi_delineations.json
│   │
│   ├── advanced/                           # Advanced techniques
│   │   ├── magi_astrology_framework.json
│   │   ├── midpoint_analysis_engine.json
│   │   ├── harmonic_analysis.json
│   │   ├── asteroids_framework.json
│   │   ├── chiron_complete_framework.json
│   │   ├── fixed_stars_framework.json
│   │   ├── arabic_parts_framework.json
│   │   ├── antiscion_framework.json
│   │   └── tno_transneptunian_objects.json
│   │
│   └── specialized/                        # Specialized applications
│       ├── financial_astrology.json
│       ├── mundane_world_events.json
│       ├── medical_health_astrology.json
│       └── relationship_needs_guide.json
│
├── delineations/                           # Planet, Sign & Aspect Meanings
│   ├── README_DELINEATIONS.md
│   ├── planets/                            # Planetary interpretations
│   │   ├── sun_delineations.json
│   │   ├── moon_delineations.json
│   │   ├── mercury_delineations.json
│   │   ├── venus_delineations.json
│   │   ├── mars_delineations.json
│   │   ├── jupiter_saturn_delineations.json
│   │   ├── uranus_neptune_pluto.json
│   │   └── chiron_delineations.json
│   │
│   ├── signs/                              # Zodiac sign meanings
│   │   ├── sign_interpretations_master.json
│   │   ├── aries_through_gemini.json
│   │   ├── cancer_through_virgo.json
│   │   ├── libra_through_sagittarius.json
│   │   └── capricorn_through_pisces.json
│   │
│   ├── houses/                             # House delineations
│   │   ├── house_delineations_master.json
│   │   ├── houses_1_4.json
│   │   ├── houses_5_8.json
│   │   └── houses_9_12.json
│   │
│   ├── aspects/                            # Aspect interpretations
│   │   ├── aspect_interpretation_library.json
│   │   ├── major_aspects.json
│   │   ├── minor_aspects.json
│   │   ├── aspect_orbs.json
│   │   └── aspect_patterns.json
│   │
│   └── keywords/                           # Keywords & symbolism
│       ├── keywords_master_list.json
│       ├── psychological_meanings.json
│       └── archetypal_symbolism.json
│
├── reference/                              # Reference Materials
│   ├── README_REFERENCE.md
│   ├── ephemeris/                          # Ephemeris data
│   │   ├── MASTER_ASTRO_EPHEMERIS_2026_2035.json
│   │   ├── ULTIMATE_VERBOSE_EPHEMERIS.json
│   │   └── planetary_positions_reference.json
│   │
│   ├── books_authors/                      # Literary references
│   │   ├── stephen_arroyo_interpretations.json
│   │   ├── donna_cunningham_topics.json
│   │   ├── demetra_george_methodology.json
│   │   └── tracy_marks_chart_interpretation.json
│   │
│   ├── tools_prompts/                      # AI prompts & templates
│   │   ├── astrology_expert_persona.json
│   │   ├── astrology_prompts_library.json
│   │   ├── stable_diffusion_prompts.json
│   │   └── interpretation_templates.json
│   │
│   └── misc/                               # Miscellaneous references
│       ├── decans_framework.json
│       ├── ruler_chart_medieval.json
│       └── chakra_correspondences.json
│
├── clients/                                # Client & personal data
│   ├── .gitignore (clients data ignored)
│   ├── clients_master_index.json           # Master index of clients
│   ├── james_jimmy_sutton/                 # Personal natal chart
│   │   ├── JIMMY_NATAL.json
│   │   ├── natal_interpretations.json
│   │   └── progression_data.json
│   │
│   └── [other_clients]/                    # Additional client charts
│       └── (organized by confidentiality)
│
├── archive/                                # Deprecated/Legacy Files
│   ├── README_ARCHIVE.md
│   ├── deprecated_versions/
│   ├── old_formats/
│   └── backups/
│
├── scripts/                                # Utility scripts
│   ├── clean_json.py                       # JSON cleaning script
│   ├── extract_json.py                     # JSON extraction script
│   ├── deduplication_utils.py              # Deduplication tools
│   └── organize_files.py                   # File organization script
│
└── data/                                   # Raw data files
    ├── extracted_content/
    ├── consolidated/
    └── processed/

```

---

## Current Issues & Cleanup Status

### Problems Identified
1. **Massive Duplication**: 600+ files with many duplicates containing " - Copy", "(1)", "(2)", etc.
2. **No Directory Structure**: All files in root directory - overwhelming and unmaintainable
3. **Inconsistent Naming**: Mix of timestamp-based, descriptive, and hash-based filenames
4. **Mixed File Types**: JSON metadata mixed with PDFs, text files, and actual content
5. **Semantic Redundancy**: Same content in multiple formats and locations

### Cleanup Plan

#### Phase 1: Analysis & Deduplication (PRIORITY)
- [ ] Create comprehensive file manifest
- [ ] Identify duplicate content by hash and semantic analysis
- [ ] Consolidate duplicates into single canonical versions
- [ ] Remove " - Copy" variants
- [ ] Remove numbered duplicates "(1)", "(2)", etc.
- [ ] Document deduplication mapping

#### Phase 2: Directory Organization
- [ ] Create logical directory structure (see above)
- [ ] Move files to appropriate categories
- [ ] Establish consistent naming conventions
- [ ] Create README files for each directory

#### Phase 3: Content Consolidation & Synthesis
- [ ] Merge related JSON files into unified frameworks
- [ ] Normalize data structure and schema
- [ ] Enrich content with missing metadata
- [ ] Cross-reference related interpretations
- [ ] Create master index documents

#### Phase 4: Documentation
- [ ] Create comprehensive guide documents
- [ ] Add metadata to all JSON files
- [ ] Document frameworks and methodologies
- [ ] Create quick-start guides

#### Phase 5: Quality Assurance
- [ ] Validate JSON structure
- [ ] Check for broken references
- [ ] Test data accessibility
- [ ] Review content for completeness

---

## File Statistics

**Current State (Before Cleanup):**
- Total files: ~600+
- JSON files: ~500+ (many duplicates)
- PDF files: ~40+
- Python scripts: 3-5
- Estimated redundancy: 40-50%
- Duplicates to remove: ~200-250 files

**Target State (After Cleanup):**
- Total files: ~150-200
- JSON files: ~120-150 (deduplicated, organized)
- PDF files: ~10-15 (archived old versions)
- Python scripts: 5+ (utilities)
- Directory categories: 15+
- Redundancy: <5%

---

## Quick Start

### For Users
1. See `docs/QUICKSTART.md` for navigation guide
2. Check `docs/MASTER_FRAMEWORK.md` for comprehensive overview
3. Browse `frameworks/` for specific methodologies
4. Use `delineations/` for interpretations

### For Contributors
1. Read `docs/contributing.md`
2. Follow directory structure guidelines
3. Use consistent JSON schema (see schema documentation)
4. Document all additions

### For Astrology Practitioners
1. Start with `frameworks/natal/` for chart interpretation
2. Use `synastry/` for relationship analysis
3. Consult `delineations/` for detailed meanings
4. Reference `reference/` for ephemeris and tools

---

## Technical Details

### JSON Schema
All JSON files should follow a standardized schema:
```json
{
  "metadata": {
    "title": "...",
    "description": "...",
    "version": "...",
    "last_updated": "YYYY-MM-DD",
    "author": "...",
    "source": "...",
    "tags": ["..."]
  },
  "content": {
    // Main content here
  }
}
```

### Deduplication Criteria
Files are considered duplicates if:
- Identical SHA256 hash
- Same size and similar modification date
- Same semantic content with minor variations
- Same title/subject matter and 90%+ content overlap

### Naming Conventions
- Use descriptive kebab-case: `natal_chart_interpretation.json`
- Use version numbers: `framework_v2.json` (not "(1)", "(2)")
- Avoid OS-generated suffixes: No " - Copy", " (1)", etc.
- Use date stamps for timestamped files: `YYYY-MM-DD_description.json`

---

## Files Requiring Special Attention

### Potential Content to Merge/Consolidate
1. **Master frameworks**: Merge duplicate "UNIFIED", "COMPREHENSIVE", "MASTER", "COMPLETE" files
2. **Framework versions**: Keep only latest version (v4, v6, v12, etc.)
3. **Deepseek JSON files**: 100+ timestamp-based files that appear duplicated
4. **Astrolog delineations**: Multiple similar delineation files to consolidate

### High-Value Files to Preserve
- Core interpretation frameworks
- Comprehensive delineation libraries
- Methodology documents
- Personal natal chart data (James/Jimmy Sutton)
- Reference materials and citations

---

## Contributing & Maintenance

### Code of Conduct
- Maintain semantic integrity
- Avoid creating new duplicates
- Document all modifications
- Keep README updated
- Test JSON validity

### Tools Available
- `clean_json.py` - Validate and format JSON
- `extract_json.py` - Extract content from PDFs/text
- `organize_files.py` - Auto-organize files
- `deduplication_utils.py` - Find and manage duplicates

---

## Next Steps

1. **Review this README** and the organization plan
2. **Run deduplication analysis** - use provided scripts
3. **Create archive branch** - before major changes
4. **Begin Phase 1** - systematic deduplication
5. **Document progress** - maintain DEDUPLICATION_LOG.md
6. **Migrate files** - to new structure
7. **Test & validate** - ensure everything works
8. **Update documentation** - after completion

---

## Contact & Questions

For questions about organization or astrology content:
- See `docs/contributing.md` for contribution guidelines
- Check existing documentation first
- Follow established patterns and conventions

---

**Repository Last Updated**: June 2026  
**Status**: ⚠️ REORGANIZATION IN PROGRESS  
**Next Major Update**: Phase 2 - Directory Organization

---

**Master Framework Version**: v12  
**Deduplication Progress**: Phase 1 Starting  
**Documentation Completeness**: 40%

