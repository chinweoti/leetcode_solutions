-- Write your PostgreSQL query statement below
with row_num as (
    select log_id, log_id - row_number() over (order by log_id) as rw from logs
)
select min(log_id) as start_id, max(log_id) as end_id
from row_num
group by rw
order by start_id