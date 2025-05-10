-- Write your PostgreSQL query statement below
with cte as (
    select p1.user_id, p1.post_date, count(distinct p2.post_id)::numeric as max_7day_posts
    from posts p1 left join posts p2 on p2.post_date between p1.post_date and p1.post_date+6 and p1.user_id = p2.user_id
    where p1.post_date <= '2024-02-28' and p2.post_date <= '2024-02-28'
    group by p1.user_id, p1.post_date
    )

SELECT *
FROM(select p1.user_id, max(max_7day_posts) as max_7day_posts, count(distinct p1.post_id)::numeric/4 as avg_weekly_posts
from posts p1 left join cte c on p1.user_id = c.user_id
where p1.post_date <= '2024-02-28' 
group by p1.user_id)
where max_7day_posts >= 2*avg_weekly_posts
order by user_id