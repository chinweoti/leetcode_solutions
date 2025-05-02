-- Write your PostgreSQL query statement below
select project_id, employee_id
from (select project_id, e.employee_id, rank() over (partition by project_id order by experience_years desc) as rnk from employee e join project p 
using(employee_id))
where rnk =1

