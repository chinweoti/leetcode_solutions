-- Write your PostgreSQL query statement below
select ad_id, 
            coalesce(round(100.0 * count(case when action = 'Clicked'then 1 end)/
            nullif(count(case when action in('Clicked', 'Viewed')then 1 end), 0), 2), 0) as ctr
from ads
group by ad_id
order by ctr desc, ad_id asc



-- SELECT 
--     ad_id,
--     COALESCE(
--         ROUND(
--             COUNT(CASE WHEN action = 'Clicked' THEN 1 END) * 100.0 / 
--             NULLIF(COUNT(CASE WHEN action IN ('Clicked', 'Viewed') THEN 1 END), 0), 
--         2), 
--         0
--     ) AS ctr
-- FROM Ads
-- GROUP BY ad_id
-- ORDER BY ctr DESC, ad_id ASC;

-- with base as (
--     select ad_id,
--     sum(case when action='Clicked' then 1 else 0 end) as total_clicks, 
--     sum(case when action='Clicked' then 1 else 0 end)+sum(case when action='Viewed' then 1 else 0 end) as total_viewed
--     from Ads
--     group by 1
-- )

-- select ad_id, 
-- round(case when total_viewed=0 then 0 else 
-- 100.0*total_clicks/total_viewed end,2) as ctr
-- from base 
-- order by 2 desc, 1