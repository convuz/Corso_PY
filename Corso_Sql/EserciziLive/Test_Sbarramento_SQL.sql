/*
Show, for each order (OrderID), the number of different products ordered, 
the average price for single item (UnitPrice) rounded to the second decimal place, 
the total Quantity of items ordered in the "Order Details" table.
Take only the orders with less than 50 units.
*/

SELECT
	od.OrderID,
	COUNT(od.ProductID) AS Number_Of_Diff_Prod_Ord,
	AVG(od.UnitPrice) AS Average_Price_Of_Prod,
	SUM(od.Quantity) AS Total_Quantity_Of_Item_Ord
FROM
	"Order Details" od
WHERE
	od.Quantity < 50
GROUP BY 
	od.OrderID
ORDER BY 
	Number_Of_Diff_Prod_Ord DESC,
	Average_Price_Of_Prod DESC;


/*
Show all the information about the products which category name is 'Beverages'
(HINT: use Categories and Products tables)
*/

SELECT 
	p.*
FROM 
	Categories c
		LEFT JOIN
			Products p
			ON
			c.CategoryID = p.CategoryID
WHERE 
	c.CategoryName = 'Beverages'
ORDER BY 
	p.ProductID;

--

SELECT 
	p.*
FROM 
	Products p
		LEFT JOIN
			Categories c
			ON
			p.CategoryID = c.CategoryID
WHERE 
	c.CategoryName = 'Beverages'
ORDER BY 
	p.ProductID;

/*
Show if an employee can retire or not. if one is >= 50 can retire.
(HINT: select datetime('now') -BirthDate from Employees, use the datetime(’now’) function to calculate the age of the employee.)
*/

SELECT
	DATETIME('now') - e.BirthDate AS Age_Of_Employees,
	CASE
		WHEN DATETIME('now') - e.BirthDate >= 50 THEN "YES"
		ELSE "NO"
	END "Can Retire?"
FROM 
	Employees e
ORDER BY
	Age_Of_Employees DESC;
	
			
			
			
			
			
			
			
			