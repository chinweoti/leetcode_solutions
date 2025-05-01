-- Write your PostgreSQL query statement below
select round((100.0 * sum(case when order_date = customer_pref_delivery_date then 1 else 0 end) / count(*))::numeric, 2) as immediate_percentage
from delivery