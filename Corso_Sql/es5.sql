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
	Name,
	Surname,
	--Io personalmente avrei aggiunto anche Salary per rendere la query più capibile
FROM
	clients
WHERE
	Salary > 3000
ORDER BY
	Salary DESC;
	