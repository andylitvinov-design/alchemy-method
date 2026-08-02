# KNOWLEDGE HUB — Andrey Li Alchemy System

Canonical navigation for the method, products, Homeopath workflow, reports, books, PsiTherapy client portal, and public materials.

Use this file before free-text search.

## 1. System layers

### Method truth — `andylitvinov-design/alchemy-method`
Source of truth for method logic, diagnostics, session structure, report interpretation, Dao levels, Wu Xing, psycho-homeopathy, Bach essences, remedy profiles, safety language, and product specifications.

### Practitioner report workflow — ChatGPT project `Homeopath`
Operational workspace where the practitioner enters client Wu Xing / Dao / remedy values and receives a structured draft report.

Homeopath is not a repository and is not the source of method truth. It must apply the current canonical logic from `alchemy-method`, preserve entered values, mark uncertainty, and require practitioner confirmation.

### Client portal and visual report product — `andylitvinov-design/report`
Canonical implementation repo for PsiTherapy:
- live portal: https://psitherapy.vercel.app/
- report UI and beautiful visual report templates;
- client cabinet;
- questionnaires;
- PDF export;
- authentication and client-facing runtime.

### Business/project memory — `andylitvinov-design/ai-projects-brain`
Business packaging, offer design, project registry, priorities, report-agent standards, and PsiTherapy operational documentation.

Key PsiTherapy paths:
- `projects/psitherapy/PROJECT.md`
- `projects/psitherapy/SYSTEM_MAP.md`
- `projects/psitherapy/DATA_SCHEMA.md`
- `projects/psitherapy/CODEX_BRIEF.md`
- `projects/psitherapy/RISKS.md`

### Publishing — `andylitvinov-design/books`
Long-form manuscripts, source books, images, PDF exports, and book-production materials. Book drafts are not canonical when a corresponding method file exists in `alchemy-method`.

### Historical/supporting layers
- `andylitvinov-design/alchemy` — concept/MVP and structured case-model experiments.
- `andylitvinov-design/alchemy_site` — older standalone public-site shell.
- `andylitvinov-design/alchemist` — legacy consolidation shell.
- `andylitvinov-design/dao-usin-bach-report-kit` — supporting report renderer/template kit.
- `andylitvinov-design/psitrends-work` — Psitrends editorial/site work.
- `andylitvinov-design/artefacts` — private supporting artifact library.

## 2. Start here by task

### Understand the whole method
1. `START-HERE.md`
2. `method-source-registry.json`
3. `method/master-method.md`
4. `method-map.md`
5. `quick-use.md`

### Psycho-homeopathy / Alchemy of the Soul
1. `products/psycho-homeopathy-monthly.md`
2. `products/alchemy-of-the-soul-offer.md`
3. `consultations/session-structure.md`
4. `consultations/personality-structure-diagnosis.md`
5. `consultations/express-homeopathy-diagnosis.md`
6. `homeopathy/homeopathic-remedy-profile-template.md`
7. `method/master-method.md` — Dynamic Remedy Relevance

Core logic:

`request → state → stress subpersonality / hidden mechanism → Dao level → Wu Xing deficit → correction → remedy resonance → tracking → next step`

### Daoist Alchemy
1. `products/daoist-alchemy-monthly.md`
2. `method/dao-resource-scale.md`
3. `method/wu-xing.md`
4. `books/alchemy-of-the-soul/daoist-alchemy-health-levels.md`
5. `books/alchemy-of-the-soul/core-principles.md`
6. `consultations/session-structure.md`

Core logic:

`current resource → Dao level → missing Wu Xing resource → personal support → weekly review → monthly level review`

### Homeopath client report
1. `portal/PSITHERAPY-HOMEOPATH-INTEGRATION.md`
2. `consultations/session-structure.md`
3. `consultations/report-logic.md`
4. `consultations/reports-index.md`
5. `method/dao-resource-scale.md`
6. `method/wu-xing.md`
7. `ai-projects-brain/andrey-system/agent/report-agent-instructions.md`
8. `ai-projects-brain/andrey-system/core/report-diagnosis-matrix.md`

### Beautiful report design / PDF
Implementation source:
- `andylitvinov-design/report`

Key materials:
- `docs/design-references/reports/report-page-2-brief.md`
- `docs/design-references/reports/sample-report-data.json`
- `docs/design-references/reports/report-page-2-reference-small.base64.txt`
- `docs/design-references/reports/codex-prompt.md`
- `docs/client-cabinet/DESIGN_SOURCE_OF_TRUTH.md`
- `docs/client-cabinet/MOCKUP_IMPLEMENTATION_MAP.md`
- `docs/client-cabinet/VISUAL_QA_CHECKLIST.md`

### PsiTherapy portal
1. `portal/PSITHERAPY-HOMEOPATH-INTEGRATION.md`
2. `portal/CLIENT-PORTAL-ROADMAP.md`
3. `portal/PORTAL-KNOWLEDGE-CONTRACT.md`
4. `ai-projects-brain/projects/psitherapy/PROJECT.md`
5. `ai-projects-brain/projects/psitherapy/SYSTEM_MAP.md`
6. `report/README.md`
7. `report/AGENTS.md`

Live target: https://psitherapy.vercel.app/
Canonical implementation repo: `andylitvinov-design/report`.

### Landing pages and offers
1. `products/client-landing-master-spec.md`
2. the relevant monthly product specification
3. `products/landing-services-integrated-reference.md`
4. `integration-with-business-builder.md`
5. `ai-projects-brain/andrey-system` for pricing and packaging

## 3. Current product architecture

### Daoist Alchemy
Monthly support for restoring strength, health resource, and Wu Xing balance through individually selected homeopathy, naturopathy, Bach essences, oils, and practices.

### Psycho-homeopathy / Alchemy of the Soul
Monthly work with stress subpersonalities and hidden mechanisms that block goals. Includes diagnosis, constellation or hypnotic/imagery correction, remedy support, and tracking.

### Business Support
Diagnosis of bottlenecks, risks, and opportunities, followed by support for desired business dynamics. Mandalas, artifacts, and symbolic tools are optional implementation instruments.

Default monthly format:
- 2 sessions;
- 4 weeks of support;
- initial diagnosis;
- individual support plan;
- weekly relevance review when needed;
- end-of-cycle review and next-step decision.

## 4. End-to-end client system

```text
Short landing
→ PsiTherapy intake / tests
→ practitioner values entered in Homeopath
→ structured draft report
→ practitioner approval
→ visual report and PDF in PsiTherapy
→ monthly support and weekly check-ins
→ second-session review
→ next cycle / renewal
```

## 5. Public links

### Main sites
- Psitrends: https://psitrends.com/
- PsiTherapy portal: https://psitherapy.vercel.app/

### Telegram
- Psychic Alchemy: https://t.me/psychic_alchemy
- Dao Magic: https://t.me/daomagic
- Contact: https://t.me/AndyTherapist

### Dao source posts
- Stages: https://t.me/daomagic/170
- Levels: https://t.me/daomagic/131
- Short test, levels 1–4: https://t.me/daomagic/93

## 6. Source priority

1. Explicit latest owner statement.
2. Current client values entered by the practitioner in Homeopath.
3. `method-source-registry.json`.
4. Canonical method and consultation files in `alchemy-method`.
5. Canonical product specifications.
6. Report-agent standards in `ai-projects-brain`.
7. Visual/runtime implementation in `report`.
8. Indexed book/source summaries and public Telegram posts.
9. Old PDFs, landings, archives, and experiments.

Never silently merge contradictions. Record them in `governance/SOURCE-CONFLICTS.md`.

## 7. Naming rules

- **Alchemy of the Soul** — umbrella/client-facing name for archetypal psycho-homeopathy and work with inner states.
- **Psycho-homeopathy** — focused format for stress subpersonalities, goals, correction, and remedy support.
- **Daoist Alchemy** — resource, health, Wu Xing, and step-based development format.
- **Alchemy Method** — internal umbrella for the complete diagnostic and support system.
- **Homeopath** — ChatGPT practitioner workflow for entering values and drafting reports.
- **PsiTherapy** — client portal, report product, cabinet, tests, PDF, and support journey.

## 8. Required output for any client case

- request;
- entered source values;
- current state;
- hidden mechanism / stress subpersonality;
- current Dao level or resource range when relevant;
- Wu Xing bottleneck when relevant;
- current support resonance;
- practical action;
- what to track;
- uncertainty / practitioner verification notes;
- review date / next step;
- method and report schema versions when published through PsiTherapy.

## 9. Maintenance rule

When a new source, ChatGPT project, Telegram post, PDF, landing, repository, test, or report design is added:

1. Add it to `method-source-registry.json`.
2. Link it from this hub under the correct task.
3. State whether it is canonical, operational, supporting, historical, or experimental.
4. Record conflicts instead of overwriting them silently.
5. Update product copy only from canonical sources.
6. Update the PsiTherapy/Homeopath integration contract when the input or report schema changes.
