# Repository Sync Contract — Alchemy System

## Purpose

Prevent method drift across repositories and make every file easy to locate.

## One-way ownership

### Canonical knowledge
Repository: `andylitvinov-design/alchemy-method`

Owns:
- terminology and naming
- method logic
- Dao levels and Wu Xing models
- psycho-homeopathy logic
- session and report structures
- product specifications
- source indexes
- safety language

No other repository may redefine these concepts. Other repositories may render, package, or implement them.

### Client application and portal prototype
Repository: `andylitvinov-design/alchemy`

Owns:
- structured client case schema
- test engines and questionnaires
- report builder UI
- client timeline and progress UI
- portal prototypes

It imports method definitions conceptually from `alchemy-method`. It must not become an independent source of method truth.

### Public website and landing
Repository: `andylitvinov-design/alchemy_site`

Owns:
- public landing implementation
- conversion flow
- responsive UI
- analytics and forms

Copy must be derived from `alchemy-method/products/client-landing-master-spec.md` and the three monthly product specifications.

### Publishing
Repository: `andylitvinov-design/books`

Owns:
- long-form manuscripts
- illustrations
- book layouts and exports

When a manuscript changes method logic, the change must first be approved and written into `alchemy-method`.

### Reports
Repository: `andylitvinov-design/dao-usin-bach-report-kit`

Owns:
- report rendering
- formatting
- export and delivery helpers

Interpretation rules and report semantics come from `alchemy-method`.

### Business packaging
Repository: `andylitvinov-design/ai-projects-brain`

Owns:
- pricing experiments
- offer packaging
- sales prioritization
- commercial metrics

It may propose changes but cannot silently alter canonical method definitions.

## Deprecated and transitional repositories

- `alchemist`: consolidation shell; no longer future canonical source.
- `report`: legacy report project; inventory before reuse.
- `psitrends-work`: editorial/site work; supporting, not canonical.
- `artefacts`: private artifact library; supporting assets only.

## Change flow

1. New idea or source is recorded in `alchemy-method` as `draft` or `supporting`.
2. Owner approves terminology and logic.
3. Canonical file is updated.
4. Registry and Knowledge Hub are updated.
5. Website, portal, report kit, and books consume the approved change.

Never reverse this order for method-defining changes.

## Version header for downstream content

Every product copy, test interpretation, report template, or portal module should record:

- canonical source path
- source version or commit
- last sync date
- status: current / needs-sync / historical

## Conflict handling

Record contradictions in `governance/SOURCE-CONFLICTS.md` with:

- source A
- source B
- exact contradiction
- business or clinical impact
- proposed resolution
- owner decision
- date resolved

## Privacy boundary

Public repositories must not contain identifiable client records, photos, medical histories, or private session notes. Use anonymized examples and synthetic test data only.
