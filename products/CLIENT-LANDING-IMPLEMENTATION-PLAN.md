# Client Landing Implementation Plan

Purpose: convert the cleaned knowledge system into a short client-facing landing page.

The page is not a complete explanation of the method. Its job is:

`understand the situation → choose a direction → begin one month of work`

## 1. Canonical inputs

Use only:

1. `products/client-landing-master-spec.md`
2. `products/daoist-alchemy-monthly.md`
3. `products/psycho-homeopathy-monthly.md`
4. `products/business-support-monthly.md`
5. `governance/CLAIMS-AND-DUPLICATES-AUDIT.md`
6. `portal/PSITHERAPY-HOMEOPATH-INTEGRATION.md`

Do not build final copy directly from Telegram posts, book chapters, old PDFs, or historical landing pages.

## 2. Primary audience problem

The visitor usually does not know which method is needed.

They may experience:
- low energy or unstable health resource;
- anxiety, internal compression, or repeating emotional reactions;
- difficulty acting toward a goal;
- stalled relationships, money, work, or business processes;
- confusion after previous attempts did not create enough movement.

The landing must not require the visitor to understand Dao, Wu Xing, archetypes, potency, or systemic-field terminology before contacting the practitioner.

## 3. First screen

### Headline

**Понять, что удерживает проблему. Изменить состояние. Начать движение.**

### Subheadline

Индивидуальное месячное сопровождение для восстановления ресурса, работы с внутренними блоками и развития важных жизненных или бизнес-процессов.

### Format line

**2 личные сессии + 4 недели сопровождения**

### Primary CTA

**Коротко описать ситуацию**

### Secondary CTA

**Пройти начальную диагностику в PsiTherapy**

Do not place a long method list on the first screen.

## 4. Recognition block

Headline:

**С чем можно обратиться**

Use 6–8 concise situations:
- мало сил, сложно восстановиться;
- тревога, внутреннее сжатие или эмоциональная замороженность;
- повторяется один и тот же сценарий;
- понимаю цель, но не могу начать действовать;
- страх проявляться, говорить о себе или занимать пространство;
- сложности в отношениях, деньгах или работе;
- бизнес-процесс остановился, а причина неясна;
- обычного разговора и общих рекомендаций оказалось недостаточно.

Avoid disease lists and clinical promises.

## 5. Three directions

### Daoist Alchemy

**Восстановление ресурса**

Для состояний истощения, нестабильной энергии и необходимости вернуть телу и психике больше опоры.

The internal method may use Dao level, Wu Xing, homeopathy, naturopathy, Bach essences, oils, and practices. Do not list all of them before the client understands the result.

CTA: **Восстановить ресурс**

### Psycho-homeopathy / Alchemy of the Soul

**Работа с внутренним блоком**

Для страхов, стрессовых субличностей и повторяющихся реакций, которые мешают действовать, строить отношения и достигать целей.

CTA: **Разобрать внутренний стоп**

### Business Support

**Сдвиг бизнес-процесса**

Для диагностики точки ступора, рисков, возможностей и следующего практического движения в проекте.

CTA: **Разобрать бизнес-ситуацию**

## 6. How the month works

### Step 1 — Initial clarity

You describe the situation in a few sentences or complete the initial PsiTherapy intake.

### Step 2 — First session

The practitioner identifies the current state, hidden mechanism, resource bottleneck, and realistic direction of change.

### Step 3 — Four weeks of support

The client receives an individual plan. Changes are tracked, and the relevance of supports is reviewed as the state changes.

### Step 4 — Second session

The movement is reviewed, the new state is stabilized, and the next step is chosen.

Use cautious wording: the cycle is built around movement toward the next stage; the actual pace is individual.

## 7. What the client receives

- a clear explanation of what is happening;
- an individual map of the problem and resource;
- a focused monthly plan;
- two personal sessions;
- support and correction during four weeks;
- a client report in PsiTherapy when appropriate;
- a final review and next-step decision.

## 8. PsiTherapy block

Headline:

**Ваши результаты не теряются между сессиями**

Text:

PsiTherapy is the client cabinet where questionnaires, confirmed reports, recommendations, and progress can be kept in one place. Interpretation is reviewed by the practitioner before it becomes a client-facing conclusion.

CTA:

**Открыть начальную диагностику**

Do not promise that an automated test diagnoses or selects treatment independently.

## 9. Trust and boundaries

Use a concise block:

- the work is individual rather than based on one universal protocol;
- supports are reviewed as the client state changes;
- the client can begin with a short description instead of choosing a method alone;
- the work does not replace medical, psychiatric, or emergency care.

Do not use numeric amplification claims, guaranteed level transitions, guaranteed cures, or superiority claims about remote work.

## 10. Final CTA

Headline:

**Начните не с выбора метода, а с понимания ситуации**

Text:

Describe what is happening in 3–5 sentences. The practitioner will suggest whether it is better to begin with resource restoration, work with an internal block, or business-process analysis.

Buttons:
- **Написать Андрею**
- **Начать в PsiTherapy**

## 11. Recommended URL architecture

- `/` — short landing;
- `/daoist-alchemy` — detailed resource-restoration page;
- `/psycho-homeopathy` — detailed inner-block page;
- `/business-support` — detailed business page;
- `/how-it-works` — process and boundaries;
- `/login` — PsiTherapy login;
- `/profile` — client cabinet.

The short landing should remain readable without opening the detailed pages.

## 12. Conversion events

Track:
- primary CTA click;
- PsiTherapy diagnostic start;
- intake completion;
- Telegram/contact click;
- product-direction selection;
- login success;
- report viewed;
- monthly-support inquiry.

Do not send sensitive questionnaire answers to marketing analytics.

## 13. Release acceptance criteria

A new visitor should understand within one minute:
- what problems can be brought;
- that there are three directions;
- that the main format is two sessions plus four weeks;
- that diagnosis precedes method selection;
- what the next action is.

Before release, run:

```bash
python3 scripts/sync_audit.py --online-links
```

For a multi-repository local checkout:

```bash
python3 scripts/sync_audit.py --repos-root /path/to/projects --online-links
```
