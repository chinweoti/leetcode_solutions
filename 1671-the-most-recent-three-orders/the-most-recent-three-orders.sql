-- Write your PostgreSQL query statement below
select customer_name, customer_id, order_id, order_date
from (
    select name as customer_name, o.customer_id, order_id, order_date, dense_rank() over (partition by o.customer_id order by order_date desc)as rnk
    from orders o
    join customers c
    on o.customer_id = c.customer_id
    )
where rnk <= 3
order by customer_name asc, customer_id asc, order_date desc