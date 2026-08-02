# Portal Knowledge Contract

## Purpose

Ensure the client portal uses the same method logic as reports, sessions, landings, and books.

## Canonical source

All interpretation rules come from `andylitvinov-design/alchemy-method`.

The portal may store:
- user answers
- test scores
- practitioner-approved case models
- reports
- plans
- progress data

The portal must not invent independent meanings for Dao levels, Wu Xing states, remedies, subpersonalities, or product formats.

## Required metadata for every interpretation module

- module id
- module name
- canonical source path
- source commit or version
- interpretation status: draft / practitioner-approved
- last sync date
- safety note

## AI boundary

AI may:
- summarize intake
- propose a structured case draft
- identify missing fields
- generate a report draft from approved structured data

AI may not:
- make autonomous medical or psychiatric diagnoses
- prescribe medication without practitioner review
- guarantee outcomes
- publish a final client interpretation without approval

## Test boundary

Tests are screening and reflection tools. Each result page must distinguish:
- raw score
- provisional interpretation
- practitioner conclusion

Use only tests whose licensing permits the planned digital use.

## Synchronization

When a canonical interpretation changes:
1. update the source in `alchemy-method`
2. update `method-source-registry.json`
3. create a portal sync task
4. record the source commit in the portal module
5. verify old client reports remain traceable to the version used
