-- Write your PostgreSQL query statement below

with ord_freq as (
    select o.customer_id, o.product_id, p.product_name, rank() over (partition by customer_id order by count(o.product_id) desc) as p
    from products p 
    join orders o
    using(product_id)
    group by o.customer_id, o.product_id, p.product_name
)

select customer_id, product_id, product_name
from ord_freq
where p = 1