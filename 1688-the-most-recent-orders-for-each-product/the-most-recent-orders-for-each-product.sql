-- Write your PostgreSQL query statement below
select distinct product_name, product_id, order_id, order_date
from orders o
left join products
using(product_id)
where (product_id, order_date) in (select product_id, max(order_date) from orders group by product_id)
order by product_name asc, product_id asc, order_id asc