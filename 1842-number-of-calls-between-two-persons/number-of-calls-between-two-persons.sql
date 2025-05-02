-- Write your PostgreSQL query statement below
select least(from_id, to_id) as person1, greatest(from_id, to_id) as person2, count(duration) as call_count, sum(duration) as total_duration
from calls
group by person1, person2


--using case statement
-- select case when from_id > to_id then from_id else to_id end as person2,
--         case when from_id < to_id then from_id else to_id end as person1 , 
--             count(duration) as call_count, sum(duration) as total_duration
-- from calls
-- group by person1, person2