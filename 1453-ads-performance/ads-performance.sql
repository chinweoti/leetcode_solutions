-- Write your PostgreSQL query statement below
with base as (
    select ad_id,
    sum(case when action='Clicked' then 1 else 0 end) as total_clicks, 
    sum(case when action='Clicked' then 1 else 0 end)+sum(case when action='Viewed' then 1 else 0 end) as total_viewed
    from Ads
    group by 1
)

select ad_id, 
round(case when total_viewed=0 then 0 else 
100.0*total_clicks/total_viewed end,2) as ctr
from base 
order by 2 desc, 1