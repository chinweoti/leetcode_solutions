-- Write your PostgreSQL query statement below
select followee as follower, count(follower) as num
from follow
where followee in(select follower from follow)
group by followee
order by follower asc