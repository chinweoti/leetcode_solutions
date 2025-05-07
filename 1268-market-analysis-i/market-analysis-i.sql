-- Write your PostgreSQL query statement below

select user_id as buyer_id, u.join_date, coalesce(count(order_id) filter (where to_char(order_date, 'YYYY') = '2019'), 0) as orders_in_2019
from users u
left join orders o
on u.user_id = o.buyer_id
group by user_id, u.join_date
order by user_id

