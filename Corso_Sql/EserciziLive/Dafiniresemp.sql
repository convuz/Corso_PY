/* Numero di invoice per customer con informazioni anagrafiche e in aggiunta
il numero totale di tracce acquistate per customer
| customer_id | numero_di_invoice | numero_di_tracce | +info anagrafiche |
ATTENZIONE NON E' COMPLETO AL MOMENTO: DA FINIRE
*/
WITH acquisti AS 
	(
	SELECT
		InvoiceId,
		sum(Quantity) AS acquisti_per_invoice
	FROM
		InvoiceLine
	GROUP BY
		InvoiceId 
	),
invoice_per_customer AS (
	SELECT
		i.CustomerId,
		i.InvoiceId,
		a.acquisti_per_invoice
	FROM
		Invoice i
		LEFT JOIN
			acquisti a
			ON
			i.InvoiceId = a.InvoiceId
)
SELECT
	inv.CustomerId,
	c.FirstName,
	c.LastName,
	inv.numero_invoice_per_customer,
	SUM(a.acquisti_per_invoice) AS numero_di_tracce_per_customer
FROM
	invoice_per_customer inv
	LEFT JOIN 
	Customer c
		ON 
		inv.CustomerId = c.CustomerId
GROUP BY 
	c.CustomerId 
;