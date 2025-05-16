-- Write your PostgreSQL query statement below
select b. book_id, b.name
from books b
left join orders o
on b.book_id = o.book_id
and dispatch_date > '2019-06-23'::date - interval '365 days'
where available_from < '2019-06-23'::date - interval '30 days' 
group by b.book_id, name
having sum(coalesce(quantity, 0)) < 10