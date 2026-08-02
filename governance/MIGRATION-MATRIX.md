# Migration Matrix — Alchemy System

Purpose: move from scattered sources to one navigable system without losing history.

Status values:

- `canonical` — authoritative current source;
- `supporting` — implementation or evidence source;
- `historical` — preserved, not used for current claims;
- `experimental` — may inform future work, not production authority;
- `needs-review` — owner decision or detailed inventory required;
- `redirect` — source should point to a canonical file and stop redefining the method.

## Current Matrix

| Old / current source | Canonical destination | Status | Required action |
|---|---|---:|---|
| `alchemy-method/method/master-method.md` | same file | canonical | Maintain as method source of truth. |
| `alchemy-method/START-HERE.md` | `KNOWLEDGE-HUB.md` + registry + sync contract | redirect | Keep task routing; do not duplicate the whole architecture. |
| `alchemy-method/README.md` | `KNOWLEDGE-HUB.md` | redirect | README is a concise entrance; hub contains full navigation. |
| `books/alchemy-of-the-soul/*` inside `alchemy-method` | relevant files in `method/`, `products/`, `consultations/` | supporting | Preserve source summaries; promote new rules into canonical files before use. |
| `Homeotherapy1.pdf` / Life Force manual | `books/homeotherapy1-life-force/source-summary.md` plus relevant method/product files | historical/supporting | Keep PDF as source artifact; do not use old claims directly on landing. Add checksum/location when the binary is stored. |
| Telegram `daomagic/170`, `/131`, `/93` | Dao files in `method/` and `books/alchemy-of-the-soul/` | supporting | Keep URLs in registry; review periodically for changed/deleted posts. |
| Telegram `psychic_alchemy` | psycho-homeopathy product and source index | supporting | Register specific posts when they introduce new method rules. |
| `alchemy/README.md` and portal notes | `portal/*` for architecture; `alchemy` for implementation | supporting | Keep application architecture in `alchemy`; method rules must link back here. |
| `alchemy` static report MVP | `alchemy` application | experimental | Reuse UI and structured case ideas; replace hard-coded interpretations with versioned canonical data. |
| `alchemy_site` HTML modules | `products/client-landing-master-spec.md` + `alchemy_site` implementation | redirect | Public copy should carry source version and canonical product IDs. |
| `alchemist/README.md` claiming future canonical role | `alchemy-method` + repository sync contract | historical/conflict | Replace with a redirect README after owner/tool access permits. |
| `books` repository | `books` for manuscripts; `alchemy-method` for rules | supporting | Inventory manuscripts; add source metadata and canonical dependencies. |
| `dao-usin-bach-report-kit` | report logic here; renderer there | supporting | Add schema version compatibility and link to canonical report contract. |
| `report` repository | `consultations/report-logic.md` and renderer projects | needs-review | Inventory whether it contains live templates, old exports, or public examples; migrate unique material. |
| `artefacts` repository | future canonical artifact definitions in `alchemy-method/artefacts/` | needs-review | Inventory and classify symbolic descriptions, operational rules, and client-specific data. |
| `ai-projects-brain` | business packaging remains there | supporting | Reference canonical product IDs and method version. Do not restate method rules independently. |
| `psitrends-work` | site/editorial implementation | supporting | Link landing and articles to canonical product/source IDs. |
| prior ChatGPT project “homeopath” | `alchemy` portal + `alchemy-method` source | needs-review | Locate exports/conversations/specs; register unique tests, schemas, or UX flows. |
| prior Vercel/Supabase Homeopath project | `alchemy` portal deployment record | needs-review | Locate project name, repo, deployment URL, database schema, and ownership. |

## Migration Rules

1. Never delete a source solely because it is duplicated; first classify and link it.
2. Never copy a new rule into several repositories. Add it canonically once and consume it elsewhere.
3. Every public page or generated report should carry a `source_version` or canonical commit SHA.
4. Historical source language may be quoted for research but must not silently become current product language.
5. Client data is migrated only to private, access-controlled storage; never into this public method library.

## Remaining Inventory Queue

Priority 1:

- full `alchemy` application tree and structured case schema;
- `report` repository;
- `artefacts` repository;
- previous Homeopath ChatGPT/Codex project;
- Vercel and Supabase resources associated with Homeopath.

Priority 2:

- full `books` repository manuscript inventory;
- Psitrends pages mentioning the services;
- all relevant Telegram post URLs beyond the currently registered three;
- old PDFs and landing exports.

## Completion Definition

Migration is complete when every relevant source has:

- repository/location;
- owner;
- classification;
- canonical replacement or explicit unique role;
- privacy status;
- claims status;
- last-reviewed date;
- next action.
