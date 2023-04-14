DROP TABLE IF EXISTS clients;
CREATE TABLE clients(
	Person_Id int PRIMARY KEY,
	Surname varchar(255),
	Name varchar(255),
	City varchar(255),
	Salary int,
	Age int
);

INSERT INTO clients (Person_Id, Surname, Name, City, Salary, Age)
VALUES
	(1, "Bianchi", "Mario", "Rimini", 1000, 20),
	(2, "Bianchi", "Ettore", "Milano", 0, 15),
	(3, "Casadei", "Mario", "Rimini", 3000, 35),
	(4, "Rossi", "Mario", "Bologna", 1500, 50),
	(5, "Rossi", "Fabio", "Firenze", 8000, 40),
	(6, "Bianchi", "Ettore", "Rimini", 4500, 25),
	(7, "Neri", "Fabio", "Arezzo", 3500, 35);

SELECT
	AVG(Age) AS Average_Age
FROM 
	clients;
	
SELECT	
	City,
	AVG(Age) AS Average_Age
FROM
	clients
GROUP BY
	City
ORDER BY
	Average_Age DESC;
	
SELECT
	MAX(Salary)
FROM
	clients
WHERE
	City = "Rimini";
	
SELECT	
	City,
	COUNT(*) AS Number_of_Client,
	AVG(Age) AS Average_Age
FROM
	clients
GROUP BY
	City
ORDER BY
	Number_of_Client DESC;

SELECT	
	City,
	COUNT(*) AS Number_of_Client
FROM
	clients
GROUP BY
	City
ORDER BY
	Number_of_Client DESC;
	
	
