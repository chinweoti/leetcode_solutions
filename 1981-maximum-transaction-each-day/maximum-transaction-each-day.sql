-- Write your PostgreSQL query statement below
select transaction_id
from (select transaction_id, rank() over (partition by day order by amount desc) as rnk from transactions group by transaction_id, day, amount)
where rnk = 1
order by transaction_id asc