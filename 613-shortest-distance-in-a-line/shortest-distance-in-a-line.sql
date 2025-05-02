-- Write your PostgreSQL query statement below
select min(shortest) as shortest
from (select x, least(
    abs(x - lead(x) over(order by x)), -- to check the succeeding
    abs(x - lag(x) over(order by x))   -- to check the preceeding
    ) as shortest from point) a


