# Claims and Duplicate-Content Audit

Purpose: keep the method deep while preventing contradictory definitions, duplicated source-of-truth files, and unsafe client promises.

## Canonical Claim Categories

### A. Method claims

Allowed when presented as the author's framework:

- the method uses a step-based Dao Resource model;
- diagnosis explores current state, hidden mechanism, resource level, and Wu Xing balance;
- support is selected individually and reviewed as the state changes;
- monthly work includes two sessions and four weeks of support.

Use language such as:

- `в рамках авторской модели`;
- `мы исследуем`;
- `диагностика помогает определить`;
- `может поддерживать`;
- `резонанс перепроверяется персонально`.

### B. Outcome claims

Require cautious language:

- increased energy;
- greater clarity or confidence;
- movement in relationships or business;
- transition toward a next resource level.

Use:

- `цель цикла`;
- `возможный результат`;
- `клиент может заметить`;
- `изменения отслеживаются`.

Do not use as guarantees:

- `один цикл переводит на одну ступень`;
- `одной недели достаточно`;
- `работает так же или лучше`;
- `усиливает эффективность в 2–3 раза`.

### C. Medical/health claims

Do not present symbolic, homeopathic, naturopathic, Bach, field, or alchemical work as a substitute for medical assessment or treatment.

Avoid:

- `лечит болезнь`;
- `вакцина`;
- `точно диагностирует здоровье`;
- `препарат мгновенно устраняет боль` as a general promise;
- dosage instructions presented without an appropriate professional context;
- claims that remote photo-based exposure is medically equivalent or superior.

Preferred replacement:

> Это авторская система ресурсной, символической и психотерапевтической поддержки. Она не заменяет медицинскую или психиатрическую диагностику и лечение.

### D. Business claims

Do not guarantee sales, investment, income, or external events.

Use:

- diagnosis of bottlenecks and opportunities;
- clarification of priorities;
- support for decision-making and implementation;
- observation of business indicators.

## Known Outdated Claims To Quarantine

| Old wording/theme | Risk | Canonical replacement |
|---|---|---|
| `1 цикл дает переход на одну ступень` | guarantee | `Цикл строится вокруг движения к следующей ступени; фактическая динамика оценивается индивидуально.` |
| `обычно одной недели достаточно` | overpromise | `Первая проверка динамики обычно проводится через неделю.` |
| `дистанционное воздействие работает так же/лучше` | unsupported equivalence | Describe it as an agreed symbolic/resource format without equivalence claims. |
| `алхимия усиливает в 2–3 раза` | numerical unsupported claim | `Дополнительные инструменты могут использоваться для направления и закрепления работы; эффект отслеживается индивидуально.` |
| `элитная гомеопатическая вакцина` | medical framing | `индивидуально подобранная гомеопатическая/символическая поддержка` |
| `точно калиброванные микродозы запускают мощные изменения` | efficacy guarantee | `подбирается индивидуальная поддержка, а реакция отслеживается` |
| case-based immediate pain disappearance | anecdote generalized as result | Keep only as clearly labeled historical anecdote with no predictive promise. |
| guaranteed investor/client interest | external financial promise | Track decisions/actions and business indicators; do not promise third-party behavior. |

## Duplicate Source Rules

A duplicate is acceptable only when its role is explicit:

- canonical definition;
- short client explanation;
- book expansion;
- application data/schema;
- renderer template;
- historical source.

A duplicate is harmful when two files independently define:

- number or names of Dao levels;
- program duration and inclusions;
- diagnostic sequence;
- meaning of Alchemy of the Soul vs psycho-homeopathy;
- medical or outcome claims;
- repository authority.

## Known Duplicate/Conflict Areas

1. Dao stages appear in Telegram, book summaries, product texts, and method files.
   - Authority: `method/dao-resource-scale.md` and explicit owner updates.
2. Alchemy of the Soul appears as umbrella, offer, book title, and psycho-homeopathy label.
   - Authority: naming rules in Knowledge Hub and product specs.
3. Monthly format appears in old landings, PDF, product specifications, and business packaging.
   - Authority: the three canonical monthly product files.
4. Client report logic appears in `alchemy-method`, `report`, `dao-usin-bach-report-kit`, and `alchemy`.
   - Authority: report logic here; implementation/rendering elsewhere.
5. Repository authority conflicts between `alchemist` and `alchemy-method`.
   - Authority: repository sync contract and current owner decision.

## Content Status Labels

Every imported source or major document should include one of:

```yaml
content_status: canonical | supporting | historical | experimental | deprecated
canonical_source: path-or-url
last_reviewed: YYYY-MM-DD
```

For client/public copy also add:

```yaml
claims_reviewed: true | false
privacy_reviewed: true | false
```

## Audit Workflow

1. Identify the document's role.
2. Compare it with the registry and canonical file.
3. Extract unique useful material.
4. Move new logic into the canonical source.
5. Replace old independent definitions with a link/redirect.
6. Mark outdated promises as historical/deprecated.
7. Update the migration matrix.
8. Rebuild public copy from canonical product specifications.

## Landing Rule

The short landing must not explain the entire internal model. It should communicate:

1. the client's situation;
2. what the work helps clarify;
3. the three available directions;
4. the monthly format;
5. the next simple action.

Deep Dao, Wu Xing, subpersonality, remedy, and archetypal explanations belong on secondary pages or in the consultation, not all on the first screen.
