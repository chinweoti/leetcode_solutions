-- Write your PostgreSQL query statement below
select id, month, coalesce(sum(salary) over (partition by id order by month range between 2 preceding and current row), 0) as Salary
from employee
where (id, month) not in (select id, max(month) from employee group by id)
order by id, month desc

