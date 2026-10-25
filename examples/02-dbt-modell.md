# 02 · dbt-modell

## Före
```text
Skriv en dbt-modell för ordrar.
```

## Efter
```text
Du är en analytics engineer som granskar och skriver dbt-kod enligt dbt Labs stilguide. Projektet använder Snowflake och lagren staging, intermediate och marts.

<källa>
Tabellen raw.shop.orders har kolumnerna: id, user_id, created, status, amount_ore (belopp i öre).
</källa>

Uppgift: skriv staging-modellen stg_shop__orders.sql och dess YAML med tester.

Svara så här:
- SQL med import-CTE överst och en final-CTE, bara rename, cast och enkla beräkningar (inga joins).
- Döp om till snake_case: order_id, customer_id, ordered_at, status, amount_sek (öre delat med 100).
- YAML med beskrivning, unique och not_null på order_id, accepted_values på status.
Om du saknar information om statusvärdena: skriv en kommentar i YAML-filen i stället för att hitta på.
```

## Vad som ändrades
- **Roll och situation:** stack och lagerstruktur gör att koden följer projektets konventioner.
- **Underlag:** källkolumnerna finns med, så AI:n inte hittar på namn.
- **Gränser:** "inga joins" och "hitta inte på statusvärden" stoppar de vanligaste felen.
