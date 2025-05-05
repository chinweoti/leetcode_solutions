-- Write your PostgreSQL query statement below

with cte as(
        select action_date, round(100 * count(distinct r.post_id) /count(distinct a.post_id)::numeric, 2) as cnt
        from actions a 
        left join removals r
        using(post_id)
        where extra = 'spam' and action = 'report'
        group by action_date
        -- having (count(extra) filter (where extra = 'spam')) > 0
)
select round(avg(cnt)::numeric, 2) as average_daily_percent
from cte
