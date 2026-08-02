# KNOWLEDGE HUB — Andrey Li Alchemy System

This is the canonical navigation page for the method, products, books, client work, and public materials.

Use this file before free-text search.

## 1. Canonical repository roles

### `andylitvinov-design/alchemy-method`
Source of truth for method logic, diagnostics, session structure, reports, Dao levels, Wu Xing, psycho-homeopathy, Bach essences, homeopathic profiles, and client-facing method explanations.

### `andylitvinov-design/books`
Long-form manuscripts, source books, images, exports, and book-production materials. Do not treat a book draft as canonical method logic when a corresponding file exists in `alchemy-method`.

### `andylitvinov-design/alchemy`
Large archive / application materials related to alchemy. Use as a secondary source until a specific file is indexed here.

### `andylitvinov-design/alchemy_site`
Website implementation for alchemy offers. Product copy must be derived from canonical product files in `alchemy-method`.

### `andylitvinov-design/alchemist`
Experimental application/project. Treat as non-canonical unless a file is explicitly registered.

### `andylitvinov-design/dao-usin-bach-report-kit`
Report-generation kit for Dao, Wu Xing, and Bach work. Templates may support delivery, but method definitions remain canonical in `alchemy-method`.

### `andylitvinov-design/psitrends-work`
Psitrends content/work repository. Use for site implementation and editorial work, not as the primary method source.

### `andylitvinov-design/ai-projects-brain`
Business packaging, offer design, prioritization, and cross-project logic. Use together with canonical method files when building products and landings.

## 2. Start here by task

### Understand the whole method
1. `START-HERE.md`
2. `method-source-registry.json`
3. `method/master-method.md`
4. `method-map.md`
5. `quick-use.md`

### Psycho-homeopathy / Alchemy of the Soul
1. `products/alchemy-of-the-soul-offer.md`
2. `consultations/session-structure.md`
3. `consultations/personality-structure-diagnosis.md`
4. `consultations/express-homeopathy-diagnosis.md`
5. `homeopathy/homeopathic-remedy-profile-template.md`
6. `method/master-method.md` — Dynamic Remedy Relevance
7. `books/alchemy-of-the-soul/source-index.md`

Core logic:

`request → state → stress subpersonality / hidden mechanism → Dao level → Wu Xing deficit → correction → remedy resonance → tracking → next step`

### Daoist Alchemy
1. `books/alchemy-of-the-soul/daoist-alchemy-health-levels.md`
2. `books/alchemy-of-the-soul/core-principles.md`
3. `method/dao-resource-scale.md`
4. `method/dao-level-profile-template.md`
5. `method/wu-xing.md`
6. `consultations/session-structure.md`

Core logic:

`current resource → Dao level → missing Wu Xing resource → personal support → weekly review → monthly level review`

### Bach essences / naturopathy support
1. `homeopathy/bach-essence-profile-template.md`
2. `consultations/session-structure.md`
3. `method/master-method.md`
4. `dao-usin-bach-report-kit` for report implementation

### Personality / subpersonality work
1. `consultations/personality-structure-diagnosis.md`
2. `consultations/session-structure.md`
3. `method/master-method.md`

### Client session and report
1. `consultations/session-structure.md`
2. `consultations/reports-index.md`
3. `consultations/report-logic.md`
4. `consultations/examples/confidence-bach-report-example.md`
5. `method/dao-resource-scale.md`

### Landing pages and offers
1. `products/alchemy-of-the-soul-offer.md`
2. `products/landing-services-integrated-reference.md`
3. `products/programs.md`
4. `integration-with-business-builder.md`
5. `ai-projects-brain/andrey-system` for packaging and prioritization

## 3. Current product architecture

### Daoist Alchemy
Monthly support for restoring strength, health resource, and Wu Xing balance through individually selected homeopathy, naturopathy, Bach essences, oils, and practices.

### Psycho-homeopathy / Alchemy of the Soul
Monthly work with stress subpersonalities and hidden mechanisms that block goals. Includes diagnosis, constellation or hypnotic/imagery correction, remedy support, and tracking.

### Business Support
Diagnosis of bottlenecks, risks, and opportunities, followed by support for desired business dynamics. Mandalas, artifacts, and symbolic tools are optional implementation instruments, not the whole product.

Default monthly format:
- 2 sessions
- 4 weeks of support
- initial diagnosis
- individual support plan
- weekly relevance review when needed
- end-of-cycle review and next-step decision

## 4. Public links

### Main sites
- https://psitrends.com/

### Telegram
- Psychic Alchemy: https://t.me/psychic_alchemy
- Dao Magic: https://t.me/daomagic
- Contact: https://t.me/AndyTherapist

### Dao source posts
- Stages: https://t.me/daomagic/170
- Levels: https://t.me/daomagic/131
- Short test, levels 1–4: https://t.me/daomagic/93

## 5. Source priority

When sources conflict, use this order:

1. Explicit latest owner statement
2. `method-source-registry.json`
3. Canonical method files in `method/` and `consultations/`
4. Canonical product files in `products/`
5. Indexed source/book files in `books/alchemy-of-the-soul/`
6. Public Telegram posts
7. Old PDFs, landings, archives, experimental repositories

Never silently merge contradictions. Record the conflict and ask for an owner decision when it changes the method or offer.

## 6. Naming rules

- **Alchemy of the Soul** = umbrella/client-facing name for archetypal psycho-homeopathy and work with inner states.
- **Psycho-homeopathy** = focused format for stress subpersonalities, goals, correction, and remedy support.
- **Daoist Alchemy** = resource, health, Wu Xing, and step-based development format.
- **Alchemy Method** = internal umbrella for the complete diagnostic and support system.

Do not use these names as interchangeable labels without explaining the relationship.

## 7. Required output for any client case

Every case note, report, or recommendation should identify:

- request
- current state
- hidden mechanism / stress subpersonality
- current Dao level or resource range when relevant
- Wu Xing bottleneck when relevant
- current support resonance
- practical action
- what to track
- review date / next step

## 8. Maintenance rule

When a new source, Telegram post, PDF, landing, or repository is added:

1. Add it to `method-source-registry.json`.
2. Link it from this hub under the correct task.
3. State whether it is canonical, supporting, historical, or experimental.
4. Record conflicts instead of overwriting them silently.
5. Update product copy only from canonical sources.
