# Write your MySQL query statement below
select trim(lower(product_name)) as product_name, date_format(sale_date, '%Y-%m') as sale_date, count(trim(lower(product_name))) as total
from sales
group by trim(lower(product_name)), date_format(sale_date, '%Y-%m')
order by trim(lower(product_name)), date_format(sale_date, '%Y-%m')


-- date_format(sale_date, '%Y-%m')
-- trim(lower(product_name)) as product_name, date_format(sale_date, '%Y-%m') as sale_date,