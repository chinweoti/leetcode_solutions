-- Write your PostgreSQL query statement below
select department, employee,salary--, dense_rank() over (partition by d.name order by salary desc) as rn
from    (select d.name as department, e.name as employee,salary, dense_rank() over (partition by d.name order by salary desc) as rn
        from employee e
        join department d
        on e.departmentId = d.id 
        group by department, employee, salary) 
where rn = 1
