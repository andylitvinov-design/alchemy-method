# START HERE — Alchemy Method

This is the agent entry point for Andrey Li's Alchemy Method knowledge system.

## Mandatory reading order

Before free-text search, read:

1. `KNOWLEDGE-HUB.md` — human-readable navigation
2. `method-source-registry.json` — machine-readable source and repository registry
3. `governance/REPOSITORY-SYNC-CONTRACT.md` — where each type of material belongs
4. `method/master-method.md` — canonical method logic
5. `method-map.md` — detailed routing

Search is a fallback. Do not use a search result as canonical merely because it is easy to find.

## Repository boundary

- `alchemy-method` — canonical knowledge and product specifications
- `alchemy` — client application, report builder, tests, portal prototype
- `alchemy_site` — public landing implementation
- `books` — manuscripts, illustrations, and exports
- `dao-usin-bach-report-kit` — report rendering
- `ai-projects-brain` — commercial packaging and prioritization

Read `governance/REPOSITORY-SYNC-CONTRACT.md` before creating or moving files across repositories.

## Route by task

### Understand the full method
- `method/master-method.md`
- `method/dao-resource-scale.md`
- `method/wu-xing.md`
- `consultations/session-structure.md`

### Psycho-homeopathy / Alchemy of the Soul
- `products/psycho-homeopathy-monthly.md`
- `products/alchemy-of-the-soul-offer.md`
- `consultations/personality-structure-diagnosis.md`
- `consultations/express-homeopathy-diagnosis.md`
- `homeopathy/homeopathic-remedy-profile-template.md`

### Daoist Alchemy
- `products/daoist-alchemy-monthly.md`
- `books/alchemy-of-the-soul/daoist-alchemy-health-levels.md`
- `books/alchemy-of-the-soul/core-principles.md`
- `method/dao-resource-scale.md`
- `method/wu-xing.md`

### Business support
- `products/business-support-monthly.md`
- `consultations/session-structure.md`
- `products/landing-services-integrated-reference.md`

### Client report or diagnosis
Read in order:
- `consultations/reports-index.md`
- `consultations/report-logic.md`
- `consultations/examples/confidence-bach-report-example.md`
- relevant method and product files

### Landing
- `products/client-landing-master-spec.md`
- all three monthly product specifications
- `products/landing-services-integrated-reference.md`

Implementation belongs in `alchemy_site`.

### Client portal, tests, and Homeopath-style application
- `portal/CLIENT-PORTAL-ROADMAP.md`
- `portal/PORTAL-KNOWLEDGE-CONTRACT.md` when present
- `consultations/session-structure.md`
- `consultations/report-logic.md`

Implementation belongs in `alchemy` unless the owner explicitly chooses a new portal repository.

### Books and long-form educational materials
Use indexed files inside `books/alchemy-of-the-soul/` as source summaries. Publishing assets belong in the separate `books` repository.

## Core method chain

client request → current state → hidden mechanism / stress subpersonality → Dao level → Wu Xing resource → correction → remedy/support resonance → practical action → tracking → next step

## Output rules

Every professional case output should include:

- request
- current state
- hidden mechanism or bottleneck
- resource level when relevant
- Wu Xing state when relevant
- selected correction/support
- practical action
- what to track
- review date or next step

For client-facing text:

- use simple language
- present the problem and process before methods
- avoid overload and medical guarantees
- distinguish screening from diagnosis
- treat AI output as a draft until practitioner review

## New-material rule

For every new repository, PDF, Telegram post, test, book chapter, landing, or external source:

1. register it in `method-source-registry.json`
2. link it in `KNOWLEDGE-HUB.md`
3. classify it as canonical, supporting, historical, or experimental
4. record contradictions in `governance/SOURCE-CONFLICTS.md`
5. update downstream implementations only after the canonical source is approved

Do not invent the method or silently reconcile contradictions.
