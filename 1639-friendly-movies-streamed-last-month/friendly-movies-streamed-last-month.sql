-- Write your PostgreSQL query statement below
select distinct title
from content 
join tvprogram
using(content_id)
where to_char(program_date, 'YYYY-MM') = '2020-06'
and Kids_content = 'Y'
and content_type = 'Movies'