# prompt-coach

**En skill som hjälper dig att skriva prompts som ger rätt svar första gången. Den fungerar i Claude-appen, i Claude Code och i Hermes Agent.**

> *English summary: an Agent Skill that writes, reviews and teaches prompts using six building blocks and a seven-point review checklist. It includes before/after examples from data work and a reproducible structure eval.*

## Vad den gör

| Läge | När | Resultat |
|---|---|---|
| **Skriv** | Du har ett mål men ingen prompt | En färdig prompt att kopiera |
| **Förbättra** | Du klistrar in en prompt | Betyg på sju punkter och en omskriven version |
| **Lär** | Du vill förstå varför en prompt fungerar | Före/efter-genomgång, sedan skriver du om en egen prompt |

Prova: *"Förbättra den här prompten: …"*

## Metoden

**Sex byggstenar:** roll och situation · uppgift · kontext · underlag i taggar · format · gränser och kvalitet

**Sju granskningspunkter:** tydligt mål · kontext · format · avgränsat underlag · exempel · hantering av osäkerhet · längd

Några regler som gör störst skillnad:
- Förklara **varför** en regel finns, så generaliserar AI:n rätt.
- Lägg underlag i taggar som `<data>` och `<exempel>`, så blandas det inte ihop med instruktionerna.
- Säg vad AI:n ska göra när den är osäker, annars gissar den.
- Skriv lugnt. VERSALER och "MÅSTE!!!" fungerar sämre än tydlig text.

Hela instruktionen finns i [`skill/prompt-coach/SKILL.md`](skill/prompt-coach/SKILL.md).

## Exempel från dataarbete

| # | Exempel | Före | Efter |
|---|---|---|---|
| 01 | [SQL-felsökning](examples/01-sql-felsokning.md) | "varför funkar inte min sql" | Fråga och felmeddelande i taggar, mål att förstå felet, svar i tre delar |
| 02 | [dbt-modell](examples/02-dbt-modell.md) | "Skriv en dbt-modell för ordrar." | Stack, källkolumner och lagerregler, plus "hitta inte på statusvärden" |
| 03 | [GA4-analys](examples/03-ga4-analys.md) | "Analysera min trafik…" | Beslut i fokus, resonemang före svar, "säg vad som saknas" |
| 04 | [LIA-ansökan](examples/04-lia-ansokan.md) | "Skriv ett personligt brev…" | Fakta bara från underlaget, struktur, inga klichéer |
| 05 | [Systemprompt](examples/05-systemprompt.md) | "Var ALLTID trevlig!!!" | Lugn ton, avgränsad policy, säkerhetsgräns |

## Utvärdering

Påstå inte, mät. [`evals/score.py`](evals/score.py) poängsätter varje prompt mot de sju granskningspunkterna:

```bash
python3 evals/score.py
```

| | Före | Efter |
|---|---|---|
| Snitt, strukturpoäng | **0,8 / 7** | **7,0 / 7** |

Två ärliga förbehåll:
- Poängen mäter om **byggstenarna finns**, inte om svaret blir bättre. Det testas manuellt med [`evals/rubric.md`](evals/rubric.md): kör båda versionerna med samma modell och betygsätt svaren utan att veta vilket som är vilket.
- Exemplen och poängskriptet är skrivna av samma person, så skriptet är en snabb kontroll och inget oberoende bevis. Fler exempel och manuella resultat är nästa steg.

## Installera

Skillen följer det öppna SKILL.md-formatet, så samma fil fungerar på alla tre ställen.

**Claude-appen:** zippa mappen `skill/prompt-coach` (eller ladda ner zip-filen under Releases) och ladda upp den under Skills.

**Claude Code:**
```bash
cp -r skill/prompt-coach ~/.claude/skills/
```

**Hermes Agent:**
```bash
cp -r skill/prompt-coach ~/.hermes/skills/
```
Se även [trygg-ai-kollega](https://github.com/andersvlindberg/trygg-ai-kollega).

## Struktur

```
skill/prompt-coach/SKILL.md   själva skillen
examples/                     fem före/efter-exempel
evals/score.py                strukturpoäng (körs utan API-nyckel)
evals/rubric.md               manuell utvärdering av svarskvalitet
evals/results.md              senaste resultat
```

## Licens

MIT
