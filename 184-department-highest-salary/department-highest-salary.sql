-- Write your PostgreSQL query statement below
with salaries as (
    select d.name as department, e.name as employee,salary, dense_rank() over (partition by d.name order by salary desc) as rn
from employee e
join department d
on e.departmentId = d.id 
group by department, employee, salary
) 
select department, employee, salary 
from salaries
where rn = 1
