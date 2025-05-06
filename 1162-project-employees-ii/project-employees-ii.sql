# Write your MySQL query statement below
with cte as(
    select project_id, count(distinct employee_id) as exp
    from project
    group by project_id
)
select project_id 
from cte
where exp = (select max(exp) from cte)


