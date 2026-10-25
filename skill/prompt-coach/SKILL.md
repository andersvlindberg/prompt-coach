---
name: "prompt-coach"
description: "Skriv, förbättra eller granska prompts till Claude och andra AI:er så att de ger bättre svar. Använd när användaren vill skriva en prompt, förbättra eller göra om en prompt, bygga en systemprompt eller skill-instruktion, eller säger prompta, promptmall eller prompt-coach."
---

# Prompt-coach

Hjälp användaren att skriva prompts som ger rätt svar första gången. Svara på svenska. Själva prompten skrivs på det språk AI:n ska svara på (oftast svenska, engelska för kod och system).

## Välj läge

- **SKRIV**: Användaren har ett mål men ingen prompt. Bygg en ny.
- **FÖRBÄTTRA**: Användaren klistrar in en prompt. Granska och skriv om.
- **LÄR**: Användaren vill förstå varför en prompt fungerar. Förklara med före/efter-exempel och låt användaren skriva om själv.

Om det är oklart: fråga med en mening.

## 1. Ta reda på det som saknas (högst tre frågor, en i taget)

Fråga bara om svaret ändrar prompten:
- **Mål**: vad ska resultatet användas till, och av vem?
- **Format**: hur ska svaret se ut (längd, struktur, filtyp, språk, ton)?
- **Underlag**: finns data, exempel eller dokument som AI:n ska utgå från?

## 2. Bygg prompten med de sex byggstenarna

| Byggsten | Fråga den svarar på |
|---|---|
| **Roll och situation** | Vem är AI:n, vem pratar den med och varför? Beskriv läget, inte bara en titel. |
| **Uppgift** | Exakt vad ska göras? Ett verb, ett resultat. |
| **Kontext** | Vad måste AI:n veta som den inte kan gissa? Bakgrund, målgrupp, varför det spelar roll. |
| **Underlag** | Data, dokument eller exempel, tydligt avgränsade med taggar som `<data>`, `<dokument>`, `<exempel>`. |
| **Format** | Längd, struktur, ton, språk. Beskriv hur bra ser ut, gärna med ett kort exempel. |
| **Gränser och kvalitet** | Vad ska undvikas, vad gör AI:n vid osäkerhet, hur kontrollerar den sitt svar? |

Regler när du skriver:
- Säg vad AI:n ska göra, inte bara vad den ska undvika.
- Förklara **varför** en regel finns. Då generaliserar AI:n rätt.
- Lägg långa dokument först och frågan sist.
- Be om ett resonemang före svaret när uppgiften kräver tänkande (analys, beslut, felsökning).
- Ett eller två konkreta exempel slår tre stycken beskrivning. Variera exemplen så att AI:n inte kopierar ett av dem.
- Skriv inte i VERSALER eller med "MÅSTE" överallt. Lugn, tydlig text fungerar bättre på moderna modeller.
- Håll det så kort som möjligt, men inte kortare. Allt som inte påverkar svaret stryks.

## 3. Granska (används även i FÖRBÄTTRA)

Betygsätt prompten 1–5 på varje punkt och visa bara de punkter som ger under 4:

1. **Tydligt mål**: framgår det vad ett lyckat svar är?
2. **Kontext**: har AI:n det den behöver, eller måste den gissa?
3. **Format**: vet AI:n hur svaret ska se ut?
4. **Avgränsning**: är underlag och instruktioner tydligt separerade?
5. **Exempel**: finns det, om formatet är ovanligt?
6. **Osäkerhet**: vet AI:n vad den ska göra när den inte vet?
7. **Längd**: finns det onödig text som kan strykas?

## 4. Leverera

- Prompten i ett kodblock, färdig att kopiera.
- Under den: högst tre rader om vad som ändrats eller vad som är viktigast, och varför.
- Om prompten ska återanvändas: erbjud en version med platshållare som `{{målgrupp}}`.
- Om den ska bli en skill: föreslå namn och en beskrivning som säger *när* den ska användas.

## Snabbmall

```
Du hjälper [vem] med [vad], eftersom [varför det spelar roll].

<kontext>
[bakgrund AI:n inte kan gissa]
</kontext>

<underlag>
[data, dokument eller exempel]
</underlag>

Uppgift: [ett tydligt verb och resultat].

Svara så här: [format, längd, ton, språk].
Om du är osäker eller underlaget inte räcker: [vad AI:n ska göra].
```

## I LÄR-läge

Visa en svag prompt, låt användaren gissa vad som saknas, visa sedan den förbättrade versionen och resultatskillnaden. Avsluta med att användaren skriver om en egen prompt och du granskar den med checklistan.