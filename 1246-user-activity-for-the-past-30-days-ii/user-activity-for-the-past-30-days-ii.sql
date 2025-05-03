-- Write your PostgreSQL query statement below

select case when count(distinct user_id) = 0 then 0 else round(count(distinct session_id)/count(distinct user_id)::numeric, 2) end as average_sessions_per_user
from activity
WHERE activity_date BETWEEN '2019-07-28'::date - INTERVAL '30 day' AND '2019-07-27'::date
-- group by user_id, activity_type, activity_date