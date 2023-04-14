DROP TABLE IF EXISTS salesman;
CREATE TABLE salesman(
	Salesman_Id int PRIMARY KEY,
	Name varchar(255),
	City varchar(255),
	Commission float
);

INSERT INTO salesman (Salesman_Id, Name, City, Commission)
VALUES
	(5001, "James Hoog", "New York", 0.15),
	(5002, "Nail Knite", "Paris", 0.13),
	(5005, "Pit Alex", "London", 0.11),
	(5006, "Mc Lyon", "Paris", 0.14),
	(5007, "Paul Adam", "Rome", 0.13);
	
INSERT INTO salesman (Salesman_Id, Name, Commission)
VALUES
	(5003, "Lauson Hense", 0.12);
	
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
	c.Cust_Name,
	c.City AS cust_city,
	s.Name AS sales_name,
	s.Commission * 100 AS Commission_Percentual
FROM 
	customer c 
	INNER JOIN
		salesman s
		ON
		c.Salesman_Id  = s.Salesman_Id
WHERE 
	s.Commission >= 0.12
ORDER BY 
	s.Commission DESC;