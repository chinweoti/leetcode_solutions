-- Write your PostgreSQL query statement below
select extra report_reason, count(distinct post_id) report_count
from actions 
where action_date = ('2019-07-05'::date - interval '1 day')
and action = 'report'
group by extra