# Manuell utvärdering av svarskvalitet

`score.py` kontrollerar bara att byggstenarna finns. Om svaren faktiskt blir bättre testar du så här:

1. Välj ett exempel i `examples/`.
2. Kör **Före**-prompten och **Efter**-prompten i varsin ny chatt, med samma modell.
3. Betygsätt båda svaren 1–5 på punkterna nedan, utan att titta på vilken prompt som gav vilket svar. Be gärna någon annan blanda dem åt dig.

| Punkt | 1 | 5 |
|---|---|---|
| **Träffar målet** | Svarar på fel fråga | Löser exakt det som efterfrågades |
| **Korrekt** | Fel eller påhittade fakta | Allt stämmer mot underlaget |
| **Användbart format** | Måste skrivas om | Kan användas direkt |
| **Lagom längd** | Mycket utfyllnad | Inget onödigt |
| **Ärlig om osäkerhet** | Gissar tyst | Säger vad som saknas |

Fyll i tabellen och lägg den under `evals/manuellt/` med datum och modellnamn:

| Exempel | Modell | Före (snitt) | Efter (snitt) | Kommentar |
|---|---|---|---|---|
| | | | | |
