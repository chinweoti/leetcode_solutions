-- Write your PostgreSQL query statement below
with cte as
(
    select purchase_id, user_id, purchase_date, lead(purchase_date) over (partition by user_id order by purchase_date) as next_purchase
    from purchases
)
select distinct user_id
from cte
where next_purchase - purchase_date  <= 7