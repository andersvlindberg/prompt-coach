#!/usr/bin/env python3
"""Strukturpoäng för prompts, enligt prompt-coachens sju granskningspunkter.

Läser varje exempel i examples/, poängsätter prompten under "## Före" och
"## Efter" och skriver en tabell till evals/results.md.

Det här mäter STRUKTUR (finns byggstenarna?), inte svarskvalitet. Det är en
snabb, reproducerbar kontroll som kan köras utan API-nyckel. Svarskvalitet
mäts manuellt med evals/rubric.md.

  python3 evals/score.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CHECKS = {
    "Tydligt mål": lambda p: bool(re.search(r"(?im)^\s*uppgift\s*:|^du (hjälper|svarar|granskar)\b|\b(ska användas|beslut)\b", p)),
    "Kontext": lambda p: len(re.findall(r"(?i)\b(eftersom|för att|behöver|vill|använder)\b", p)) >= 1 and len(p.split()) > 25,
    "Format": lambda p: bool(re.search(r"(?i)svara så här|så här svarar du|högst (\d+|en|två|tre|fyra|fem)\b|format|kodblock|rubrik", p)),
    "Avgränsat underlag": lambda p: bool(re.search(r"<([a-zåäö_]+)>[\s\S]*?</\1>", p)),
    "Exempel eller data": lambda p: bool(re.search(r"<(data|exempel|källa|fråga|annons|policy|om_mig|felmeddelande)>", p)),
    "Hantera osäkerhet": lambda p: bool(re.search(r"(?i)\bom\b[^.\n]{0,80}\b(saknar|inte|kan ha|osäker)\b|säg att du inte vet|säg vad som saknas", p)),
    "Lagom och lugn": lambda p: len(p.split()) < 400 and not re.search(r"\b[A-ZÅÄÖ]{5,}\b|!!", strip_tags(p)),
}


def strip_tags(p: str) -> str:
    """Ta bort underlag inom taggar, så att t.ex. SQL i versaler inte räknas som skrik."""
    return re.sub(r"<([a-zåäö_]+)>[\s\S]*?</\1>", "", p)


def prompts(md: str):
    out = {}
    for label in ("Före", "Efter"):
        m = re.search(rf"## {label}\s*```[a-z]*\n([\s\S]*?)```", md)
        if m:
            out[label] = m.group(1)
    return out


def score(p: str):
    return {name: check(p) for name, check in CHECKS.items()}


def main():
    rows, before_total, after_total = [], 0, 0
    for f in sorted((ROOT / "examples").glob("*.md")):
        ps = prompts(f.read_text(encoding="utf-8"))
        if set(ps) != {"Före", "Efter"}:
            sys.exit(f"{f.name}: hittar inte både Före och Efter")
        b, a = score(ps["Före"]), score(ps["Efter"])
        bs, as_ = sum(b.values()), sum(a.values())
        before_total += bs; after_total += as_
        missing = [k for k, v in a.items() if not v]
        rows.append(f"| {f.stem} | {bs}/7 | {as_}/7 | {', '.join(missing) or '-'} |")
    n = len(rows)
    table = "\n".join([
        "# Resultat: strukturpoäng",
        "",
        "Genererad av `python3 evals/score.py`. Mäter om byggstenarna finns, inte hur bra svaret blir.",
        "",
        "| Exempel | Före | Efter | Saknas efter |",
        "|---|---|---|---|",
        *rows,
        f"| **Snitt** | **{before_total / n:.1f}/7** | **{after_total / n:.1f}/7** | |",
        "",
    ])
    (ROOT / "evals" / "results.md").write_text(table, encoding="utf-8")
    print(table)
    if after_total <= before_total:
        sys.exit("Efter-versionerna ska få högre poäng än Före-versionerna.")


if __name__ == "__main__":
    main()
