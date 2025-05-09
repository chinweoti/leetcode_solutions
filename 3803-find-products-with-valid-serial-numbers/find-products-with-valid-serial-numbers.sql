-- Write your PostgreSQL query statement below
-- select product_id, product_name, description
-- from products 
-- where description like '%SN____-____' or description like '%SN____-____ %'
-- order by product_id


select *
from products
where description ~'\mSN[0-9]{4}-[0-9]{4}\M'
order by product_id;

/* 
    ~ : case sensitive (~* case insensitive)
    \m (start of a word) and \M (end of a word):
*/