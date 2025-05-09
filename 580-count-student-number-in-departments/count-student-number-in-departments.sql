-- Write your PostgreSQL query statement below
select dept_name, count(s.dept_id) as student_number
from student s
right join department d
using(dept_id)
group by dept_name
order by count(s.dept_id) desc, dept_name asc