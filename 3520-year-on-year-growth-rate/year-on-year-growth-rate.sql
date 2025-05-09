-- Write your PostgreSQL query statement below
select date_part('year', transaction_date) as year,
       product_id,
       sum(spend) as curr_year_spend,
       lag(sum(spend), 1) over(partition by product_id order by date_part('year', transaction_date)) as prev_year_spend,
       round(((sum(spend) - lag(sum(spend), 1) over(partition by product_id order by date_part('year', transaction_date)))/
       lag(sum(spend), 1) over(partition by product_id order by date_part('year', transaction_date)))*100.00, 2) as yoy_rate
from user_transactions
group by date_part('year', transaction_date), product_id
order by product_id, date_part('year', transaction_date)


-- with cte as 
-- (   select   date_part ('year',transaction_date) as year
--              ,product_id
--             ,sum(spend) as spend
--     from user_transactions
--     group by 1,2
 
-- )

-- select year
--        ,product_id
--        ,spend as curr_year_spend
--        ,lag (spend, 1) over (partition by product_id order by  year) as prev_year_spend
--        ,round ((spend*100/lag (spend, 1) over (partition by product_id order by  year))  - 100 ,2) as yoy_rate
-- from cte
-- order by 2,1