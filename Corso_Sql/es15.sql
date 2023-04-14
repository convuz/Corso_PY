DROP TABLE IF EXISTS orders;
CREATE TABLE orders(
	Ord_No int PRIMARY KEY,
	Purch_Amt float,
	Ord_Date DATE,
	Customer_Id int,
	Salesman_Id int
);

INSERT INTO orders (Ord_No, Purch_Amt, Ord_Date, Customer_Id, Salesman_Id)
VALUES
	(70001, 150.5, "2012-10-05", 3005, 5002),
	(70009, 270.65, "2012-09-10", 3001, 5005),
	(70002, 65.26, "2012-10-05", 3002, 5001),
	(70004, 110.5, "2012-08-17", 3009, 5003),
	(70007, 948.5, "2012-09-10", 3005, 5002),
	(70005,	2400.6, "2012-07-27", 3007, 5001),
	(70008,	5760, "2012-09-10", 3002, 5006),
	(70010,	1983.43, "2012-10-10", 3004, 5006),
	(70003,	2480.4, "2012-10-10", 3009, 5003),
	(70012,	250.45, "2012-06-27", 3008, 5002),
	(70011,	75.29, "2012-08-17", 3003, 5007),
	(70013,	3045.6, "2012-04-25", 3002, 5001);
	
DROP TABLE IF EXISTS customer;
CREATE TABLE customer(
	Customer_Id int PRIMARY KEY,
	Cust_Name varchar(255),
	City varchar(255),
	Grade int,
	Salesman_Id int
);

INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id)
VALUES
	(3002, "Nick Rimando", "New York", 100, 5001),
	(3005, "Graham Zusi", "California", 200, 5002),
	(3004, "Fabian Johnson", "Paris", 300, 5006),
	(3007, "Brad Davis", "New York", 200, 5001),
	(3009, "Geoff Cameron", "Berlin", 100, 5003),
	(3008, "Julian Green", "London", 300, 5002),
	(3003, "Jozy Altidore", "Moscow", 200, 5007),
	(3001, "Brad Guzan", "London", 0, 5005);
	

SELECT
	o.Ord_No,
	o.Purch_Amt,
	c.Cust_Name,
	c.City 
FROM
	orders o
	INNER JOIN
		customer c 
		ON
		o.Customer_Id = c.Customer_Id
WHERE 
	o.Purch_Amt BETWEEN 500 AND 2000
ORDER BY 
	o.Purch_Amt;