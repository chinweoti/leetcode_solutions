-- Write your PostgreSQL query statement below

-- select distinct c1.seat_id
-- from cinema c1
-- join cinema c2
-- on abs(c1.seat_id - c2.seat_id) = 1
-- where c1.free = 1 and c2.free =1
-- order by c1.seat_id



select distinct seat_id 
from (select seat_id, free, lag(free,1) over() as lag1_free, lead(free,1) over() as lead1_free from Cinema)
where (free = 1 and lag1_free = 1)
or (free = 1 and lead1_free = 1)