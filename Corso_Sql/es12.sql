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
	
SELECT
	COUNT(*) AS Number_For_City,
	City
FROM
	salesman
WHERE
	City IS NOT NULL
GROUP BY
	City
ORDER BY
	Number_For_City DESC;