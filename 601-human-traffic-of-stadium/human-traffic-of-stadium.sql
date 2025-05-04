-- Write your PostgreSQL query statement below
with cte as (
    select *, (id - row_number() over ()) as rown 
    from stadium
    where people >= 100
)
select id, visit_date, people
from cte
where  rown in (select rown from cte group by rown having count(*) >=3)
order by visit_date 


--OR
-- where id = lead
-- and id + 1 = lead1 
-- and id + 2 = lead2
-- and id + 3 = lead3
-- order by visit_date 


-- better option
-- with cte as (
-- select *, 
-- id - row_number() over() as diff
-- from stadium
-- where people >=100
-- )

-- select id, visit_date, people
-- from cte
-- where diff in (select diff from cte group by diff having count(*) >=3)
-- order by visit_date