# 01 · SQL-felsökning

## Före
```text
varför funkar inte min sql
```

## Efter
```text
Du hjälper en student som lär sig SQL i BigQuery och vill förstå felet, inte bara få en rättad fråga.

<fråga>
select customer_id, count(order_id)
from shop.orders
where order_date >= '2026-01-01'
</fråga>

<felmeddelande>
SELECT list expression references column customer_id which is neither grouped nor aggregated
</felmeddelande>

Uppgift: förklara varför felet uppstår och vad som behöver ändras.

Svara så här: först orsaken i två meningar, sedan den rättade frågan i ett kodblock, sist en mening om hur jag känner igen samma fel nästa gång.
Om felet kan ha flera orsaker: nämn den troligaste först och fråga om resten.
```

## Vad som ändrades
- **Underlag:** frågan och felmeddelandet finns med, avgränsade med taggar. Utan dem måste AI:n gissa.
- **Mål:** "förstå felet" i stället för bara "fixa", så att svaret lär ut.
- **Format:** tre tydliga delar, så svaret blir kort och går att använda.
