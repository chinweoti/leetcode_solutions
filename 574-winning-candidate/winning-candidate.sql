-- Write your PostgreSQL query statement below
select name 
from candidate c
where id in (select candidateId from vote group by candidateId order by count(candidateId) desc limit 1)


