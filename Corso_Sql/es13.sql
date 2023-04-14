DROP TABLE IF EXISTS emp_department;
CREATE TABLE emp_department(
	Dpt_Code int PRIMARY KEY,
	Dpt_Name varchar(255),
	Dpt_Allotment int
);

INSERT INTO emp_department (Dpt_Code, Dpt_Name, Dpt_Allotment)
VALUES
	(57, "IT", 65000),
	(63, "Finance", 15000),
	(47, "HR", 240000),
	(27, "RD", 55000),
	(89, "QC", 75000);

SELECT
	SUM(Dpt_Allotment) AS Sum_Of_Allotment
FROM
	emp_department;