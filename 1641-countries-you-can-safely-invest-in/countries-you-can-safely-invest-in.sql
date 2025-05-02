-- Write your PostgreSQL query statement below
select co.name as country--, substring(p.phone_number, 1, 3) as country_code, avg(duration), (select avg(duration) from calls)
from country co
join person p
on co.country_code = substring(p.phone_number, 1, 3)
join calls c
on c.caller_id = p.id or c.callee_id = p.id
group by co.name
having avg(duration) > (select avg(duration) from calls)