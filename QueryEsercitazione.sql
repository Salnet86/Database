--query amidate 
SELECT 
    (SELECT SUM(prezzo) FROM spedizione) AS SommaSpedizione,
    (SELECT SUM(prezzo) FROM ordini) AS SommaOrdini
FROM dual
HAVING (SELECT SUM(prezzo) FROM spedizione) > (SELECT SUM(prezzo) FROM ordini);

SELECT cliente_id, COUNT(*) AS numero_ordini
FROM ordini
GROUP BY cliente_id
HAVING COUNT(*) > 5;


SELECT 
    (SELECT SUM(prezzo) FROM spedizione) AS SommaSpedizione,
    (SELECT SUM(prezzo) FROM ordini) AS SommaOrdini
WHERE (SELECT SUSELECT 
    (SELECT SUM(prezzo) FROM spedizione) AS SommaSpedizione,
    (SELECT SUM(prezzo) FROM ordini) AS SommaOrdini
FROM dual
HAVING (SELECT SUM(prezzo) FROM spedizione) > (SELECT SUM(prezzo) FROM ordini);M(prezzo) FROM spedizione) > (SELECT SUM(prezzo) FROM ordini);

-- Questa query confronta la somma dei prezzi nelle tabelle 'spedizione' e 'ordini'
SELECT 
    -- Somma i prezzi nella tabella 'spedizione'
    (SELECT SUM(prezzo) FROM spedizione) AS SommaSpedizione,
    
    -- Somma i prezzi nella tabella 'ordini'
    (SELECT SUM(prezzo) FROM ordini) AS SommaOrdini
FROM dual  -- Usa 'dual' per restituire un singolo risultato aggregato
HAVING (SELECT SUM(prezzo) FROM spedizione) > (SELECT SUM(prezzo) FROM ordini);  -- Confronta le somme
