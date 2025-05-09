-- Write your PostgreSQL query statement below
select candidate_id
from candidates
where skill in ('Python','Tableau', 'PostgreSQL')
group by candidate_id
having count(distinct skill) = 3
order by candidate_id asc