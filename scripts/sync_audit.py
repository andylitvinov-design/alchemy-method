#!/usr/bin/env python3
"""Validate the Alchemy knowledge system from a local multi-repo checkout.

Stdlib only. The script is intentionally conservative: it reports findings and
never edits source repositories.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

TEXT_EXTENSIONS = {".md", ".txt", ".json", ".yaml", ".yml", ".html", ".tsx", ".ts", ".jsx", ".js", ".py"}
IGNORE_DIRS = {".git", "node_modules", "dist", "build", ".next", ".vercel", "coverage"}

UNSAFE_CLAIMS = [
    r"гарантирован(?:но|ный|ная|ное)", r"гарантирует", r"лечит\b", r"излеч", r"cure\b",
    r"guaranteed", r"безошибочн", r"в\s*[23]\s*раза", r"точно измеряет здоровье",
    r"один цикл.*(?:переводит|поднимает).*ступен", r"одной недели достаточно",
]
PII_PATTERNS = {
    "email": r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
    "phone": r"(?<!\d)(?:\+?\d[\d\s().-]{7,}\d)(?!\d)",
    "telegram_handle": r"(?<![\w/])@[A-Za-z0-9_]{5,}\b",
}
PUBLIC_ALLOWLIST = {"@AndyTherapist", "@psychic_alchemy", "@daomagic"}


def iter_text_files(root: Path):
    for path in root.rglob("*"):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS:
            yield path


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def load_registry(root: Path) -> dict:
    path = root / "method-source-registry.json"
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(read_text(path))


def collect_paths(value):
    if isinstance(value, dict):
        for item in value.values():
            yield from collect_paths(item)
    elif isinstance(value, list):
        for item in value:
            yield from collect_paths(item)
    elif isinstance(value, str) and not value.startswith(("http://", "https://")):
        if "/" in value or value.endswith((".md", ".json", ".yaml", ".yml")):
            yield value


def check_registry(root: Path, registry: dict) -> list[dict]:
    findings = []
    for rel in sorted(set(collect_paths(registry))):
        if rel.startswith("andylitvinov-design/") or " supplied in ChatGPT" in rel:
            continue
        if not (root / rel).exists():
            findings.append({"severity": "error", "check": "registry", "path": rel, "message": "Registered local path is missing"})
    return findings


def scan_patterns(root: Path, patterns: dict[str, str], check: str, allowlist: set[str] | None = None) -> list[dict]:
    findings = []
    compiled = {name: re.compile(pattern, re.I) for name, pattern in patterns.items()}
    for path in iter_text_files(root):
        text = read_text(path)
        for line_no, line in enumerate(text.splitlines(), 1):
            for name, regex in compiled.items():
                for match in regex.finditer(line):
                    value = match.group(0)
                    if allowlist and value in allowlist:
                        continue
                    findings.append({
                        "severity": "warning", "check": check, "type": name,
                        "path": str(path.relative_to(root)), "line": line_no,
                        "match": value[:120],
                    })
    return findings


def extract_urls(root: Path):
    regex = re.compile(r"https?://[^\s<>()\]}`\"']+")
    seen = set()
    for path in iter_text_files(root):
        for url in regex.findall(read_text(path)):
            url = url.rstrip(".,;:")
            if url not in seen:
                seen.add(url)
                yield str(path.relative_to(root)), url


def check_links(root: Path, online: bool) -> list[dict]:
    findings = []
    for source, url in extract_urls(root):
        parsed = urlparse(url)
        if not parsed.netloc:
            findings.append({"severity": "warning", "check": "links", "path": source, "url": url, "message": "Malformed URL"})
            continue
        if online:
            try:
                req = Request(url, method="HEAD", headers={"User-Agent": "AlchemyKnowledgeAudit/1.0"})
                with urlopen(req, timeout=8) as response:
                    if response.status >= 400:
                        raise RuntimeError(f"HTTP {response.status}")
            except Exception as exc:
                findings.append({"severity": "warning", "check": "links", "path": source, "url": url, "message": str(exc)})
    return findings


def check_product_sync(root: Path, repos_root: Path | None, registry: dict) -> list[dict]:
    findings = []
    required = registry.get("product_sources", {})
    for key, rel in required.items():
        if not (root / rel).exists():
            findings.append({"severity": "error", "check": "product-sync", "product": key, "message": f"Missing canonical product source: {rel}"})
    if repos_root:
        report_repo = repos_root / "report"
        if report_repo.exists():
            integration = report_repo / "docs" / "alchemy-method-integration.md"
            if not integration.exists():
                findings.append({"severity": "error", "check": "product-sync", "message": "report repo lacks docs/alchemy-method-integration.md"})
        else:
            findings.append({"severity": "info", "check": "product-sync", "message": "report repo not present in local repos root"})
    return findings


def inventory(repos_root: Path | None) -> list[dict]:
    if not repos_root:
        return []
    findings = []
    for name in ["alchemy", "books", "report", "artefacts", "dao-usin-bach-report-kit", "psitrends-work"]:
        repo = repos_root / name
        if not repo.exists():
            findings.append({"severity": "warning", "check": "inventory", "repository": name, "message": "Local checkout not found"})
            continue
        counts = {"text": 0, "images": 0, "pdf": 0, "json": 0}
        for path in repo.rglob("*"):
            if any(part in IGNORE_DIRS for part in path.parts) or not path.is_file():
                continue
            suffix = path.suffix.lower()
            if suffix in TEXT_EXTENSIONS:
                counts["text"] += 1
            if suffix in {".png", ".jpg", ".jpeg", ".webp", ".svg"}:
                counts["images"] += 1
            if suffix == ".pdf":
                counts["pdf"] += 1
            if suffix == ".json":
                counts["json"] += 1
        findings.append({"severity": "info", "check": "inventory", "repository": name, "counts": counts})
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--repos-root", type=Path, default=None, help="Directory containing sibling repo checkouts")
    parser.add_argument("--online-links", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    registry = load_registry(root)
    findings = []
    findings += check_registry(root, registry)
    findings += scan_patterns(root, {f"claim_{i+1}": p for i, p in enumerate(UNSAFE_CLAIMS)}, "public-claims")
    findings += scan_patterns(root, PII_PATTERNS, "private-data", PUBLIC_ALLOWLIST)
    findings += check_links(root, args.online_links)
    findings += check_product_sync(root, args.repos_root.resolve() if args.repos_root else None, registry)
    findings += inventory(args.repos_root.resolve() if args.repos_root else None)

    if args.json:
        print(json.dumps({"root": str(root), "findings": findings}, ensure_ascii=False, indent=2))
    else:
        for item in findings:
            print(f"[{item['severity'].upper()}] {item['check']}: {item}")
        print(f"\nTotal findings: {len(findings)}")

    return 1 if any(f["severity"] == "error" for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
