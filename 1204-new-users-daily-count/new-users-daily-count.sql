-- Write your PostgreSQL query statement below
with cte as (
    select user_id, min(activity_date) as activity_date from traffic
    where activity = 'login'
    group by 1
)

select activity_date as login_date, count(distinct user_id) as user_count from cte
where activity_date between ('2019-06-30'::date - interval '90 day') and ('2019-06-30'::date + interval '90 day')
group by 1
having count(distinct user_id) > 0;