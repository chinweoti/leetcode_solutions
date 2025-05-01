-- Write your PostgreSQL query statement below
with grade as (
    select student_id, course_id, grade, dense_rank() over (partition by student_id order by grade desc, course_id asc) as rank
    from enrollments
    group by student_id, course_id, grade
)

select student_id, course_id, grade
from grade 
where rank = 1