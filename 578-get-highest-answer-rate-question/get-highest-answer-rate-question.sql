-- Write your PostgreSQL query statement below
with cte as (
    select question_id, count(*) filter(where action = 'answer')as ans, count(*) filter(where action = 'show')as shw
from surveylog
group by question_id
),
    cte2 as (
        select question_id, row_number() over (order by ans*100/shw desc, question_id) as rnk
        from cte
        where ans > 0
    )
select question_id as survey_log
from  cte2
where rnk = 1


-- with cte as(
--     select question_id, count(*) FILTER (WHERE action = 'answer') as answer_cnt,  count(*) FILTER (WHERE action = 'show') as show_cnt
--     from SurveyLog 
--     group by 1 
--     ),
-- cte2 as 
-- (select question_id,row_number() over (order by (answer_cnt*100/show_cnt) desc,question_id) as rn 
-- from cte
-- where answer_cnt > 0)

-- select question_id as survey_log from cte2  
-- where rn = 1;