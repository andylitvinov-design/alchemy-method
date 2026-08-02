# Release Checklist — Alchemy System

Use before publishing or deploying a landing page, portal feature, test, client report template, public case, or book export.

## 1. Source Integrity

- [ ] The content has a named canonical source.
- [ ] The source is registered in `method-source-registry.json`.
- [ ] The repository role follows `REPOSITORY-SYNC-CONTRACT.md`.
- [ ] No historical or experimental file is presented as current authority.
- [ ] Conflicts are recorded in `SOURCE-CONFLICTS.md`.
- [ ] The release records a canonical commit SHA or content version.

## 2. Product Integrity

For client offers:

- [ ] One of the three canonical product specifications is selected.
- [ ] Format, inclusions, duration, and CTA match the specification.
- [ ] Internal tools are not confused with the client outcome.
- [ ] The landing uses simple client language.
- [ ] Secondary pages carry deeper method explanations.

## 3. Claims Review

- [ ] No guaranteed medical, psychological, spiritual, or financial result.
- [ ] No unsupported numerical efficacy claim.
- [ ] No equivalence claim between remote symbolic support and medical treatment.
- [ ] One-cycle/one-level language is framed as a goal or working model, not a guarantee.
- [ ] Appropriate scope and safety statement is visible.
- [ ] Business copy does not promise third-party actions, income, or investment.

## 4. Privacy Review

- [ ] No identifiable client information is present.
- [ ] Examples include example type and privacy metadata.
- [ ] Screenshots and fixtures use synthetic data.
- [ ] Forms do not send private information to public logs or repositories.
- [ ] Secrets and production configuration are not committed.
- [ ] Public testimonials/cases have documented approval where required.

## 5. Portal/Test Review

- [ ] Test purpose is defined: screening, reflection, tracking, or practitioner aid.
- [ ] Test licensing permits digital use.
- [ ] Result language does not present an autonomous diagnosis.
- [ ] Test version and scoring version are stored.
- [ ] Practitioner review is required before a personalized interpretation is finalized.
- [ ] Client records are separated from canonical knowledge.
- [ ] Development uses synthetic seed data only.
- [ ] Roles, retention, deletion, and export flows are defined.

## 6. Technical Synchronization

- [ ] Site/portal references canonical product IDs.
- [ ] Report renderer supports the current report schema version.
- [ ] Broken internal and public links are checked.
- [ ] Telegram source links are still available.
- [ ] Mobile layout is reviewed.
- [ ] Analytics events cover CTA, form start, form completion, and contact action.
- [ ] Rollback path and previous release reference exist.

## 7. Client Landing Acceptance

The landing is ready only when a new visitor can answer within one minute:

- [ ] What problem can I bring?
- [ ] What are the three directions?
- [ ] What happens during the month?
- [ ] What do I receive?
- [ ] What is the next action?

Required landing structure:

1. concise promise without guarantees;
2. three directions;
3. `2 sessions + 4 weeks` format;
4. simple process;
5. practitioner/context block;
6. FAQ and boundaries;
7. one primary CTA.

## 8. Book/Methodical Export

- [ ] Book expansion is traceable to canonical method sources.
- [ ] New rules discovered during writing have first been added to the method repository.
- [ ] Historical language is labeled as historical.
- [ ] Cases and images pass privacy review.
- [ ] Medical and outcome claims pass claims review.
- [ ] Export date, source version, and edition are recorded.

## 9. Final Sign-Off Record

Record:

```yaml
release_name:
release_type: landing | portal | test | report | book | other
canonical_commit:
product_id:
report_schema_version:
claims_reviewed_by:
privacy_reviewed_by:
technical_reviewed_by:
release_date:
known_limitations:
rollback_reference:
```
