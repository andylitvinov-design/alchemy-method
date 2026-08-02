# Public Repository Privacy Audit

Purpose: prevent identifiable client information from entering public repositories, public reports, landing pages, examples, books, or portal fixtures.

## Risk Levels

### Critical

Never store publicly:

- client names linked to health, psychological, relationship, financial, or spiritual information;
- client photos or image URLs;
- Telegram, WhatsApp, email, phone, address, birth date, or payment identifiers;
- raw intake forms;
- full session notes;
- medication lists linked to a person;
- exact combinations of age, city, profession, event, and story that make a client identifiable;
- private audio/video or transcripts;
- access tokens, service keys, credentials, or private database URLs.

### High

Require anonymization and explicit review:

- client case examples;
- before/after descriptions;
- timelines of sensitive symptoms;
- screenshots of messages;
- rare professions or unusual personal circumstances;
- public testimonials;
- practitioner reports based on real cases.

### Moderate

Usually safe after review:

- synthetic case fixtures;
- empty templates;
- composite cases built from several sources;
- method-level descriptions;
- aggregated metrics with sufficiently large groups.

## Repository Classification

### Public method repositories

Examples: `alchemy-method`, `books`, `alchemy`, `alchemy_site`, `dao-usin-bach-report-kit`, `report`, `artefacts` when public.

Allowed:

- method definitions;
- empty schemas;
- synthetic examples clearly marked `synthetic`;
- anonymized/composite examples after review;
- public source links;
- legal/safety language.

Not allowed:

- identifiable client data;
- raw portal exports;
- production database dumps;
- uploaded client images;
- personal diagnostic results.

### Private operational repositories

May contain implementation configuration, but still should not be used as the primary clinical/client record store. Production client data belongs in access-controlled application storage with retention and deletion rules.

## Required Metadata For Every Example

Every example file must state:

```yaml
example_type: synthetic | composite | anonymized-real
privacy_reviewed: true | false
consent_reference: none | internal-reference
public_safe: true | false
last_reviewed: YYYY-MM-DD
```

Rules:

- `anonymized-real` requires consent or a documented lawful basis and a re-identification review;
- public examples must have `public_safe: true`;
- remove metadata fields that themselves reveal identity;
- never commit the consent document to a public repository.

## Portal Data Boundary

The portal must separate:

1. canonical knowledge — public/versioned method content;
2. test definitions — versioned, license-checked;
3. client records — private and access-controlled;
4. generated reports — private by default;
5. public case studies — separately approved exports.

Minimum portal controls:

- authentication;
- role-based access;
- audit log for practitioner edits and report publication;
- deletion/export process;
- retention policy;
- encrypted transport and managed encrypted storage;
- no client data in browser demo fixtures or repository seeds;
- separate development and production databases;
- synthetic-only development seed data.

## Audit Procedure

For each public repository:

1. search for phone numbers, emails, Telegram handles, WhatsApp links, image attachments, names, and health terms;
2. inspect examples, screenshots, JSON fixtures, CSV files, PDFs, issues, and commit history;
3. classify each finding;
4. remove or rewrite current files;
5. assess whether Git history rewrite is required;
6. rotate any exposed secrets;
7. record the result in the migration matrix.

## Current Audit Status

| Repository | Status | Current conclusion | Next action |
|---|---:|---|---|
| `alchemy-method` | partial | Governance says no private data; examples still require file-by-file metadata review. | Label all examples and inspect history. |
| `alchemy` | not complete | Portal/demo fixtures may contain case-like data. | Inspect JSON, screenshots, forms, and static examples. |
| `alchemy_site` | not complete | Public site bundle requires forms and analytics review. | Ensure submissions do not enter GitHub or public logs. |
| `books` | not complete | Large public repository may contain case narratives, PDFs, and images. | Inventory manuscripts and media. |
| `report` | not complete | Public report examples are a high-risk area. | Review every example and export. |
| `dao-usin-bach-report-kit` | not complete | Templates likely safe; fixtures require review. | Mark synthetic data and inspect exports. |
| `artefacts` | not complete | Private currently, but may contain client-linked materials. | Review before any publication. |

## Publication Gate

No client-facing example, testimonial, report, screenshot, or case may be published unless:

- identity risk is reviewed;
- claims language is reviewed;
- consent status is documented when required;
- repository/publication destination is approved;
- source and example type are labeled.
