# Write your MySQL query statement below
select project_id 
from(
    select project_id, rank() over (order by count(distinct employee_id) desc) as exp
    from project
    group by project_id
)a
where exp = 1