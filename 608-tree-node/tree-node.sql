-- Write your PostgreSQL query statement below
select id, case when p_id is null then 'Root'
                when id not in (select p_id from tree where P_id is not NULL) then 'Leaf' else 'Inner' end as type
from tree