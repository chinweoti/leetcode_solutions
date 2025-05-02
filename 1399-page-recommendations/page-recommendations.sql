-- Write your PostgreSQL query statement below
select distinct page_id as recommended_page
from likes
join friendship
on user_id in (user1_id, user2_id)
where 1 in (user1_id, user2_id)

except 
select page_id as recommended_page
from likes
where user_id = 1

