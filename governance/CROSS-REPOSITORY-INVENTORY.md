# Cross-Repository Inventory — Alchemy / PsiTherapy

Status: active inventory. This document separates verified findings from items that still require a local or provider-level scan.

## 1. Verified repository roles and unique materials

### `andylitvinov-design/alchemy-method`
Canonical knowledge source.

Unique materials:
- master method;
- Dao Resource Ladder;
- Wu Xing interpretation framework;
- session and report logic;
- psycho-homeopathy, Daoist Alchemy, and business-support product specs;
- source registry, governance, privacy, claims, and release rules;
- Homeopath/PsiTherapy integration contract.

### `andylitvinov-design/report`
Canonical implementation repository for `https://psitherapy.vercel.app/`.

Verified unique materials:
- React/Vite report and client-cabinet implementation;
- Supabase/Google-auth setup notes;
- `/login` and `/profile` routes;
- PDF/export requirements;
- report-page design brief;
- sample report data JSON;
- visual report reference and restoration script;
- client-cabinet SVG source of truth;
- mockup implementation map;
- visual QA checklist;
- Vercel deployment workflow and build-info version verification.

This repository is not a legacy report archive. It is the active PsiTherapy product layer.

### `andylitvinov-design/alchemy`
Verified role: concept/MVP and historical application prototype.

Unique materials already described in its README:
- project concept;
- report structure;
- data and knowledge architecture;
- agent reference;
- structured JSON case input;
- static report-rendering prototype;
- Bach and internal-dynamics display logic.

Migration rule: preserve unique architecture ideas, but move active product implementation to `report` and canonical interpretations to `alchemy-method`.

### `andylitvinov-design/books`
Publishing and long-form source layer.

Expected unique materials:
- manuscripts;
- long-form chapters;
- illustrations;
- PDF/book exports.

Required review: identify any method statement newer than the canonical `alchemy-method` source and register it as a proposed method change rather than silently treating the book as truth.

### `andylitvinov-design/dao-usin-bach-report-kit`
Supporting rendering/delivery kit.

Expected unique materials:
- report templates;
- report rendering utilities;
- Dao/Wu Xing/Bach visual components.

Migration rule: preserve rendering helpers; interpretation logic must reference `alchemy-method`.

### `andylitvinov-design/artefacts`
Private supporting library.

Expected unique materials:
- mandalas;
- artifacts;
- symbolic instruments;
- images and descriptions.

Required review: separate public-safe product illustrations from practitioner-only or client-specific materials.

### `andylitvinov-design/psitrends-work`
Psitrends editorial and site-work layer.

Expected unique materials:
- public articles;
- website copy;
- editorial source material.

Migration rule: public pages may link to products, but may not become a second source of method definitions.

## 2. Known duplicates

| Topic | Canonical location | Supporting/duplicate locations | Action |
|---|---|---|---|
| Dao levels | `alchemy-method/method/dao-resource-scale.md` | books, Telegram, old PDFs, alchemy | Keep supporting sources; update only canonical file first. |
| Wu Xing report meaning | `alchemy-method/method/wu-xing.md` and report logic | report sample JSON, report kit, Homeopath chats | Align schemas and preserve client examples as non-canonical. |
| Report structure | `alchemy-method/consultations/report-logic.md` | alchemy, report, report kit, ai-projects-brain | Canonical meaning in method repo; visual structure in report. |
| Product descriptions | `alchemy-method/products/` | Psitrends, Telegram, old landing pages | Regenerate public copy from canonical specs. |
| Client portal concept | `report` active implementation | alchemy prototype, alchemy_site shell | Migrate useful ideas; stop creating new portal logic elsewhere. |
| Homeopath report workflow | `portal/PSITHERAPY-HOMEOPATH-INTEGRATION.md` | ChatGPT project history | Use the integration contract as durable memory. |

## 3. Data and privacy review scope

The following locations require a full local scan because GitHub code search cannot prove absence of private data:

- report fixtures and sample JSON;
- alchemy example case data;
- books case histories and exported PDFs;
- artefacts images and metadata;
- report-kit sample reports;
- psitrends drafts and archived posts.

Review for:
- names;
- email addresses;
- telephone numbers;
- personal Telegram handles;
- photographs;
- medical histories;
- raw questionnaires;
- recognizable case combinations;
- secrets and environment values.

Use:

```bash
python3 scripts/sync_audit.py --repos-root /path/to/projects --json
```

A pattern match is a review candidate, not proof of exposure.

## 4. Images, PDFs, tests, and questionnaires

Verified in `report`:
- report visual reference;
- client-cabinet SVG mockup;
- sample report JSON;
- questionnaire-flow requirements.

Verified in `alchemy`:
- structured case JSON input prototype.

Still requiring a local tree scan:
- exact PDF inventory in `books`;
- exact image inventory in `artefacts`;
- all implemented questionnaires/tests in `report`;
- any test definitions in `psitrends-work` or report kit.

## 5. Homeopath status

Homeopath is a ChatGPT project, not a repository.

Durable definition:
- specialist enters measured/observed Dao, Wu Xing, state, remedy, Bach, and progress values;
- the model structures and interprets the input using `alchemy-method`;
- the practitioner confirms the draft;
- `report`/PsiTherapy renders and stores the client-facing result.

ChatGPT conversation history is a supporting source only. New rules discovered there must be written into `alchemy-method` before being relied on by the portal.

## 6. Completion criteria for inventory

The inventory is complete only when each target repository has:
- a file manifest;
- counts of text, image, PDF, and structured-data files;
- privacy scan status;
- claims scan status;
- unique-material list;
- duplicate mapping;
- migration decision for every active artifact.

Current status: architecture and key unique materials are verified; exhaustive local file manifests remain pending execution of the audit against local checkouts.
