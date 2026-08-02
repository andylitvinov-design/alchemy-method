# Knowledge-system validation scripts

Run from the `alchemy-method` repository.

```bash
python3 scripts/sync_audit.py
```

For a local directory containing sibling repositories:

```bash
python3 scripts/sync_audit.py --repos-root /path/to/projects
```

Optional online link checks:

```bash
python3 scripts/sync_audit.py --repos-root /path/to/projects --online-links
```

Machine-readable output:

```bash
python3 scripts/sync_audit.py --json > sync-audit.json
```

The audit covers the five requested layers:

1. registry path validation;
2. unsafe public claim detection;
3. possible private-data detection;
4. URL extraction and optional live link checks;
5. product and report-repository synchronization.

Convenience wrappers:

- `validate-registry`
- `check-public-claims`
- `check-private-data-patterns`
- `check-broken-links`
- `check-product-sync`

The checks are conservative. A warning is a review request, not proof of a violation. The scripts never modify source material.
