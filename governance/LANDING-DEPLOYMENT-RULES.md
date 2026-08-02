# Landing and deployment rules

## Purpose

Prevent two recurring failures:

1. publishing a landing page whose text is overloaded, repetitive, and difficult to scan;
2. deploying encoded or wrapped text instead of a valid HTML document.

## Content rule: no water

A short client landing page must answer only five questions:

1. What problem does this address?
2. What happens on the first session?
3. What does the client receive?
4. What is the monthly format?
5. What is the next action?

Default maximum structure:

- Hero;
- result of the first session;
- three-step process;
- one short transition or differentiation block;
- final CTA;
- one-line disclaimer.

Do not repeat the same idea in the hero, cards, process, FAQ, and CTA. Each fact should normally appear once.

Before release, remove:

- explanations of Daoism that are not required for a decision;
- repeated definitions of resource, balance, Usin, support, and dynamics;
- long method histories;
- more than one paragraph per card;
- FAQ questions already answered in the main flow;
- lists of every possible tool unless the list directly helps the client choose.

Target: a new visitor should understand the offer in under 30 seconds.

## Recommended message hierarchy

1. Result: find the cause and restore strength.
2. Method: symptom/psychological cause + Usin assessment.
3. Deliverable: an individual support plan.
4. Format: two sessions per month, with a re-check after two weeks.
5. CTA: describe the situation in Telegram.

## Deployment safety rule

Never deploy content that has been base64-encoded, JSON-stringified, escaped, or wrapped as plain text unless the deployment API explicitly requires that format and decodes it server-side.

The published `index.html` must begin with a real HTML doctype, for example:

```html
<!doctype html>
<html lang="ru">
```

It must not begin with:

- a base64 string;
- a JSON object;
- quotation marks containing the whole document;
- a local file path;
- markdown fences.

## Mandatory pre-production check

Before changing the production alias:

1. deploy a preview;
2. fetch the preview URL;
3. verify HTTP 200;
4. verify `content-type: text/html`;
5. verify the response body starts with `<!doctype html` or `<html`;
6. verify the body contains the expected title and primary CTA;
7. open or inspect at mobile width;
8. only then deploy to production;
9. fetch the production URL and repeat checks 3–6.

If any check fails, do not claim the landing page is fixed or published.

## Postmortem: 2026-08-02

An encoded representation of the page was deployed as the response body. Safari displayed a white page with a long character string instead of rendering the site.

Root cause:

- deployment output was trusted without inspecting the actual response body;
- production was updated before a preview content check;
- `READY` deployment status was incorrectly treated as proof that the HTML rendered correctly.

Permanent correction:

- `READY` means the deployment finished, not that the page content is valid;
- every landing deployment requires body-level verification before production;
- use preview-first deployment and explicit HTML signature checks.
