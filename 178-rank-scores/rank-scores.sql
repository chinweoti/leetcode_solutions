-- Write your PostgreSQL query statement below
select score, dense_rank() over (order by score Desc) as rank
from scores