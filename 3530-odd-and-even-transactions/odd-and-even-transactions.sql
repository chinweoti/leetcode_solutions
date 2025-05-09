-- Write your PostgreSQL query statement below
-- select transaction_date, coalesce(sum(amount) filter (where amount % 2 = 1),0) as odd_sum,
--                          coalesce(sum(amount) filter (where amount % 2 = 0),0) as even_sum

-- from transactions
-- group by transaction_date 
-- order by transaction_date asc

SELECT transaction_date,
       SUM(case when amount % 2 != 0 then amount else 0 end) as odd_sum,
       SUM(case when amount % 2 = 0 then amount else 0 end) as even_sum
from transactions
group by 1
order by 1