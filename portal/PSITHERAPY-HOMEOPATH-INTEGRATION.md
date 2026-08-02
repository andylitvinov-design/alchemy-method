# PsiTherapy + Homeopath + Report Design Integration

This document unifies three previously separate parts of the system:

1. **Homeopath** — the ChatGPT project/workflow where the practitioner enters client Wu Xing / Dao / remedy values and receives a drafted client report.
2. **Report design system** — the visual/report product materials for beautiful client-facing reports.
3. **PsiTherapy** — the live client portal and funnel at `https://psitherapy.vercel.app/`.

## 1. Canonical roles

### `andylitvinov-design/alchemy-method`
Source of truth for method logic:
- Dao levels
- Wu Xing interpretation
- psycho-homeopathy
- Bach / remedy logic
- report logic
- client-facing safety language
- product specifications

### ChatGPT project `Homeopath`
Operational practitioner interface, not a repository.

Its job is:
- accept practitioner-entered client values and observations;
- structure the case;
- apply the canonical interpretation rules from `alchemy-method`;
- draft a report;
- preserve uncertainty and mark what requires practitioner confirmation.

Homeopath must not invent a diagnosis, silently change entered values, or treat its output as a medical assessment.

### `andylitvinov-design/report`
Canonical implementation repository for:
- PsiTherapy client portal;
- report UI;
- client cabinet;
- questionnaire flows;
- report templates;
- visual report design;
- PDF export;
- Supabase auth and client-facing runtime.

Primary live target: `https://psitherapy.vercel.app/`.

### `andylitvinov-design/ai-projects-brain`
Project registry and operational/business layer.

Important PsiTherapy files:
- `projects/psitherapy/PROJECT.md`
- `projects/psitherapy/SYSTEM_MAP.md`
- `projects/psitherapy/DATA_SCHEMA.md`
- `projects/psitherapy/CODEX_BRIEF.md`
- `projects/psitherapy/RISKS.md`

Important report-agent files:
- `andrey-system/agent/report-agent-instructions.md`
- `andrey-system/agent/report-agent-playbook.md`
- `andrey-system/agent/report-style-auditor-instructions.md`
- `andrey-system/core/report-diagnosis-matrix.md`
- `andrey-system/examples/sample-homeopathy-decoder.md`

### Supporting repositories
- `alchemy` — historical concept/MVP and structured case-model experiments.
- `alchemy_site` — older standalone public-site shell.
- `dao-usin-bach-report-kit` — supporting report renderer/template kit.
- `books` — long-form publications and source materials.

## 2. End-to-end operating flow

```text
Client / practitioner input
→ Homeopath structured case draft
→ practitioner confirmation
→ canonical interpretation from alchemy-method
→ report data schema
→ report rendering in report/PsiTherapy
→ client cabinet + PDF
→ weekly/monthly progress tracking
→ updated practitioner review
```

## 3. Homeopath input contract

Minimum input should include:
- client ID or anonymized name;
- request;
- date;
- Dao/resource level if measured;
- Wu Xing values and units;
- strongest and weakest elements;
- observed state / stress subpersonality;
- remedy, Bach, naturopathy, oils, or practices considered;
- practitioner confidence notes;
- what changed since the previous review.

Homeopath output must include:
- normalized entered values;
- current state summary;
- hidden mechanism / bottleneck;
- Dao level and next realistic step;
- Wu Xing interpretation;
- support resonance and rationale;
- practical actions;
- what to track;
- uncertainty / verification notes;
- next review date.

## 4. Report data boundary

Homeopath produces structured content. It does not own final visual design.

The report application owns:
- layout;
- typography;
- charts and visual hierarchy;
- client cabinet navigation;
- PDF rendering;
- accessibility;
- mobile presentation;
- version and export metadata.

The report must record:
- `method_version`;
- `report_schema_version`;
- canonical source commit SHA;
- practitioner approval status;
- report creation and review dates.

## 5. PsiTherapy business role

PsiTherapy is not only a report viewer. It is the product delivery layer for the full client journey:

1. Public explanation / landing.
2. Intake and format selection.
3. Tests and questionnaires.
4. Practitioner diagnosis and confirmation.
5. Monthly plan.
6. Client report and cabinet.
7. Weekly check-ins.
8. Second-session review.
9. Renewal or next-step recommendation.

This supports the business model:
- low-friction entry / brief analysis;
- monthly Daoist Alchemy;
- monthly Psycho-homeopathy / Alchemy of the Soul;
- monthly Business Support;
- optional intensive or single session;
- future subscription/cabinet access only when it adds real ongoing value.

## 6. Source priority for report generation

1. Latest explicit practitioner decision.
2. Structured values entered in Homeopath for the current client.
3. `alchemy-method/method-source-registry.json`.
4. Canonical method and report files in `alchemy-method`.
5. Report-agent standards in `ai-projects-brain`.
6. Visual/product implementation in `report`.
7. Historical prototypes and old PDFs.

## 7. Safety and privacy

- Do not store identifiable client data in public repositories.
- Homeopath outputs must use anonymized IDs when exported to GitHub examples.
- PsiTherapy client data must be private and access-controlled.
- No autonomous medical diagnosis or guaranteed treatment claims.
- Practitioner approval is required before a report becomes client-visible.

## 8. Next implementation priorities

1. Verify the live Vercel deploy source for `psitherapy.vercel.app`.
2. Document the exact PsiTherapy data schema and Supabase tables.
3. Convert the Homeopath input/output contract into a versioned JSON schema.
4. Map the JSON schema to the current `report` components and PDF export.
5. Connect the short landing to PsiTherapy intake.
6. Add weekly check-in and progress-history modules.
7. Add method/report version visibility for the practitioner.
