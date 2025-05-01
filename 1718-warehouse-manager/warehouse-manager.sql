-- Write your PostgreSQL query statement below
select w.name as warehouse_name, sum(width*length*height* units) as volume
from products p
join warehouse w
using (product_id)
group by w.name