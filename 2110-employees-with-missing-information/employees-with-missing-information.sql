-- Write your PostgreSQL query statement below
select coalesce(e.employee_id,s.employee_id) as employee_id
from employees e
full join salaries s
on e.employee_id = s.employee_id
where s.salary is null or e.name is null
