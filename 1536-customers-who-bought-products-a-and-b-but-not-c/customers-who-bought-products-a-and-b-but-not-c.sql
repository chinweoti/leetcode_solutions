-- Write your PostgreSQL query statement below
select c.customer_id as customer_id, c.customer_name as customer_name
from customers c
right join orders o
on c.customer_id = o.customer_id
group by c.customer_id, c.customer_name
having sum((product_name = 'A')::int) > 0
and sum((product_name = 'B')::int) > 0
and sum((product_name = 'C')::int) = 0
order by customer_id

