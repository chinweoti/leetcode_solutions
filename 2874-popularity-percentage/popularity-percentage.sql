-- Write your PostgreSQL query statement below
with cte as (select * from friends
union
select user2,user1 from friends)

select user1, round(count(user2)*100.0/(select count(distinct user1) from cte),2) percentage_popularity from cte 
group by 1 
order by 1 