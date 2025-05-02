-- Write your PostgreSQL query statement below
select distinct title
from content c, tvprogram t
-- using(content_id)
where c.content_id = t.content_id
and to_char(program_date, 'YYYY-MM') = '2020-06'
and Kids_content = 'Y'
and content_type = 'Movies'