-- Write your PostgreSQL query statement below
with quiet as (
    select e.student_id, e.score, e.exam_id, rank() over (partition by e.exam_id order by score desc) as max_rnk, rank() over (partition by e.exam_id order by score asc) as min_rnk
    from exam e
)
select distinct q.student_id, s.student_name
from quiet q
left join student s
using(student_id)
where student_id NOT IN (select student_id from quiet where max_rnk=1)
and student_id NOT IN (select student_id from quiet where min_rnk=1)
order by student_id
