-- Write your PostgreSQL query statement below
SELECT
	E1.employee_id--, E1.employee_name, E1.manager_id, E2.manager_id, E3.manager_id, E4.manager_id
FROM 
	Employees E1
	INNER JOIN 
	Employees E2 ON E1.manager_id = E2.employee_id
	INNER JOIN
	Employees E3 ON E2.manager_id = E3.employee_id
	INNER JOIN
	Employees E4 ON E3.manager_id = E4.employee_id
    WHERE 
	E1.employee_id <> 1 AND (E1.manager_id = 1 OR E2.manager_id = 1 OR E3.manager_id = 1 OR E4.manager_id = 1 )
