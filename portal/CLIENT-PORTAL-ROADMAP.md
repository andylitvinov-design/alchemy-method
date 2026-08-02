# Client Portal Roadmap

## Goal

Create one client journey from first interest to diagnosis, monthly support, reports, tests, and progress tracking.

## Repository boundary

- Knowledge and interpretations: `alchemy-method`
- Portal/application implementation: `alchemy`
- Public landing and acquisition pages: `alchemy_site`
- Report rendering/export: `dao-usin-bach-report-kit`
- Book and educational exports: `books`

## Client journey

1. Landing explains three formats in simple language.
2. Client selects a starting problem: resource/health, internal block, or business process.
3. Client completes a short intake and optional relevant tests.
4. Practitioner receives a structured case draft, not an automatic diagnosis.
5. First session confirms request, mechanism, level, and support plan.
6. Client portal shows the agreed plan, practices, tracking fields, and next review.
7. Weekly check-ins track state and support relevance.
8. Second session reviews movement and next cycle.
9. Client receives a concise report and history of changes.

## MVP modules

### Public
- short landing
- three product cards
- FAQ and safety boundaries
- Telegram/contact CTA

### Intake
- request in 3–5 sentences
- current difficulties
- goals
- consent and privacy notice
- red-flag routing to appropriate professional care

### Tests
- Dao resource screening
- Wu Xing balance screening
- personality developmental-rights questionnaire
- stress-subpersonality prompts
- optional psychological questionnaires whose licensing permits digital use

Tests provide screening and discussion prompts, not autonomous clinical diagnoses.

### Practitioner workspace
- structured case model
- request and current state
- hidden mechanism / subpersonality
- Dao level and Wu Xing state
- selected support and rationale
- practical actions
- tracking plan
- next review

### Client workspace
- current month plan
- practices and supports
- weekly check-in
- personal reports
- timeline of changes
- appointment/contact link

## Data model principle

`raw intake → structured case draft → practitioner verification → approved client plan → tracked outcomes`

AI-generated interpretations must remain drafts until approved by the practitioner.

## Privacy and safety

- identified client data belongs in a private database, not GitHub
- separate public knowledge from private cases
- explicit consent for storing photos and sensitive information
- role-based access
- deletion/export workflow
- no medical guarantees
- urgent medical or psychiatric symptoms require appropriate professional routing

## Phases

### Phase 1 — Landing and lead intake
Create the short landing, product selection, and 3–5 sentence intake.

### Phase 2 — Practitioner report workspace
Reuse the structured report prototype from `alchemy`; connect it to canonical schemas.

### Phase 3 — Tests and client timeline
Add approved screenings, weekly check-ins, and progress history.

### Phase 4 — Full portal
Authentication, private reports, support plan, secure messaging, payments, and scheduling integrations.

## Success measures

- user understands the relevant format within 60 seconds
- intake completion rate
- percentage of inquiries converted to a first session
- report preparation time
- weekly check-in completion
- client retention to the second session
- number of method files with verified canonical source links
