-- Write your PostgreSQL query statement below
select s1.sub_id as post_id, coalesce(count(distinct s2.sub_id), 0) as number_of_comments
from submissions s1
left join submissions s2
on s1.sub_id = s2.parent_id
where s1.parent_id is Null
group by s1.sub_id
order by s1.sub_id