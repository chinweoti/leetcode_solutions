-- Write your PostgreSQL query statement below
with visit as (
    select user_id, (lead(visit_date, 1, '2021-01-01') over (partition by user_id order by visit_date) - visit_date) as date_diff
    from uservisits
)
select user_id, max(date_diff) as biggest_window
from visit
 group by user_id
 order by user_id