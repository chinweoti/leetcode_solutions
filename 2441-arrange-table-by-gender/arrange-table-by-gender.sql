-- Write your PostgreSQL query statement below
select user_id, gender
from 
(select user_id, gender,  CASE WHEN gender = 'female' THEN 1 WHEN gender = 'other' THEN 2 ELSE 3 END as cas, row_number() over (partition by gender order by gender, user_id) as rw
from genders
order by rw, cas)
