-- Write your PostgreSQL query statement below
-- with t1 as(
-- select *, row_number() over(partition by Company order by Salary) as row,
-- count(Id) over(partition by Company) as cnt
-- from Employee 
-- )

-- select Id, Company, Salary
-- from t1
-- where row between (cnt/2.0) and (cnt/2.0) +1;


SELECT Id, Company, Salary
FROM (
    SELECT 
        *, 
        ROW_NUMBER() OVER(PARTITION BY COMPANY ORDER BY Salary ASC, Id ASC) AS RN_ASC,
        ROW_NUMBER() OVER(PARTITION BY COMPANY ORDER BY Salary DESC, Id DESC) AS RN_DESC
FROM Employee
) AS temp
WHERE abs(RN_ASC-RN_DESC) BETWEEN 0 AND 1
ORDER BY Company, Salary;