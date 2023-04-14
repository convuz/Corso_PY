/*
dalla tabella trakc chiamare una colonna classe dorata se la traccia supera i 200k millisecondi.
Ritorna Nome, lunghezza traccia e classe dorata
*/

SELECT
	Name,
	Milliseconds AS Lunghezza_traccia,
CASE
	WHEN Milliseconds >= 200000 THEN 'Lunga'
	ELSE 'Corta'
END AS Classe_Dorata
FROM 
	Track
ORDER BY
	Lunghezza_traccia,
	Name;
