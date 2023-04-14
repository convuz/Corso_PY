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
	city, 
	MAX(grade) 
FROM 
	customer
GROUP BY 
	city
ORDER BY 
	MAX(grade) DESC;
