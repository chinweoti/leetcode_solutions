-- Write your PostgreSQL query statement below
select firstName, lastName, city, state
from person p
left join address a
on a.personId = p.personId