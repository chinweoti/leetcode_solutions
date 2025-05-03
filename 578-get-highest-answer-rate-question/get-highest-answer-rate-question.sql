-- Write your PostgreSQL query statement below
select question_id as survey_log
from surveylog
group by question_id
order by (count(answer_id)::numeric)/count(action) FILTER(where action='show') desc, 1 asc
limit 1


-- another way to solve
-- select question_id as survey_log 
-- from (
--         select question_id, sum(case when answer_id is not null then 1 else 0 end)*1.0/sum(case when action = 'show' then 1 else 0 end) ans
--         from surveylog
--         group by question_id
--         order by ans desc, question_id
--         limit 1 )


-- or this method using cte
-- with cte as (
--     select question_id, count(*) filter(where action = 'answer')as ans, count(*) filter(where action = 'show')as shw
-- from surveylog
-- group by question_id
-- ),
--     cte2 as (
--         select question_id, row_number() over (order by ans*100/shw desc, question_id) as rnk
--         from cte
--         where ans > 0
--     )
-- select question_id as survey_log
-- from  cte2
-- where rnk = 1
