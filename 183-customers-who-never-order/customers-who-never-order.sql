-- Write your PostgreSQL query statement below
select name as customers
from customers 
where id Not in (select customerId from orders)
-- order by name asc