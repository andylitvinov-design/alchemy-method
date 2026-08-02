# Alchemy Method

Canonical method library for Andrey Li's Alchemy system: Daoist Alchemy, psycho-homeopathy / Alchemy of the Soul, Wu Xing, consultations, reports, product specifications, and client-facing method language.

This repository is the source of truth for method logic. Applications, sites, books, report renderers, and business packaging consume this repository; they do not redefine the method.

---

## Start Here

Read in this order:

1. [`KNOWLEDGE-HUB.md`](KNOWLEDGE-HUB.md) — human-readable navigation across the complete system.
2. [`method-source-registry.json`](method-source-registry.json) — machine-readable registry of canonical sources and repository roles.
3. [`governance/REPOSITORY-SYNC-CONTRACT.md`](governance/REPOSITORY-SYNC-CONTRACT.md) — where each type of material belongs.
4. [`START-HERE.md`](START-HERE.md) — task routing for agents.
5. [`method/master-method.md`](method/master-method.md) — canonical logic of the method.

Do not begin with free-text search when a canonical route exists in the hub or registry.

---

## Core Method

The central working chain is:

`request → current state → hidden mechanism / stress subpersonality → Dao level → Wu Xing resource → correction → support resonance → action → tracking → next step`

Core rules:

- work from the current state, not from a fixed protocol;
- choose the resource and intervention appropriate to the current level;
- review remedy/support relevance as the state changes;
- separate internal method depth from simple client-facing language;
- do not promise guaranteed medical, psychological, financial, or spiritual outcomes.

---

## Canonical Product Specifications

- [`products/daoist-alchemy-monthly.md`](products/daoist-alchemy-monthly.md)
- [`products/psycho-homeopathy-monthly.md`](products/psycho-homeopathy-monthly.md)
- [`products/business-support-monthly.md`](products/business-support-monthly.md)
- [`products/client-landing-master-spec.md`](products/client-landing-master-spec.md)

Default monthly format:

- 2 sessions;
- 4 weeks of support;
- initial diagnosis;
- individual support plan;
- review of changes and support relevance;
- end-of-cycle decision about the next step.

---

## Main Directories

### `method/`
Canonical method logic: Dao Resource Ladder, Wu Xing, psychodynamics, level profiles, and master method.

### `consultations/`
Session structure, diagnostics, report logic, examples, and professional delivery rules.

### `homeopathy/`
Homeopathic and Bach profile structures. Remedy descriptions do not replace personal verification.

### `products/`
Canonical offers, monthly program specifications, and landing source copy.

### `books/`
Indexed source materials and staging copies used to build long-form manuscripts. Book drafts are not method authority when a canonical method file exists.

### `portal/`
Client portal roadmap and the contract between method knowledge, tests, practitioner review, and client output.

### `governance/`
Repository boundaries, agent instructions, migration status, conflicts, privacy, claims, and maintenance rules.

---

## Repository Roles

- `alchemy-method` — canonical method and product specifications.
- `alchemy` — practitioner/client portal, structured case model, tests, tracking, and report workflow.
- `alchemy_site` — public landing and acquisition interface.
- `books` — manuscripts, illustrations, PDF and publishing exports.
- `dao-usin-bach-report-kit` — report rendering and export implementation.
- `ai-projects-brain` — pricing, packaging, funnel, and business prioritization.
- `psitrends-work` — Psitrends site/editorial implementation.
- `artefacts` — supporting symbolic and artifact materials; canonical definitions must be registered here before product use.

See [`governance/REPOSITORY-SYNC-CONTRACT.md`](governance/REPOSITORY-SYNC-CONTRACT.md) for authoritative boundaries.

---

## Governance and Maintenance

- [`governance/MIGRATION-MATRIX.md`](governance/MIGRATION-MATRIX.md) — old source → canonical source → action.
- [`governance/SOURCE-CONFLICTS.md`](governance/SOURCE-CONFLICTS.md) — unresolved contradictions.
- [`governance/PUBLIC-PRIVACY-AUDIT.md`](governance/PUBLIC-PRIVACY-AUDIT.md) — public repository privacy controls.
- [`governance/CLAIMS-AND-DUPLICATES-AUDIT.md`](governance/CLAIMS-AND-DUPLICATES-AUDIT.md) — outdated promises, duplicates, and replacement language.
- [`governance/RELEASE-CHECKLIST.md`](governance/RELEASE-CHECKLIST.md) — checks before landing, portal, report, or book release.

When adding a source:

1. register it in `method-source-registry.json`;
2. link it in `KNOWLEDGE-HUB.md`;
3. classify it as canonical, supporting, historical, or experimental;
4. record conflicts rather than silently merging them;
5. update applications and public copy only from canonical sources.

---

## Safety

Do not store identifiable client data, private photos, raw health histories, credentials, tokens, or non-anonymized reports in public repositories.

Client-facing work must distinguish symbolic/resource assessment from medical or psychological diagnosis and must not claim guaranteed treatment results.
