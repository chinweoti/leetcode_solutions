-- Write your PostgreSQL query statement below


with cte as (
    select id,login_date, count(*) over (partition by id order by login_date) as cnt 
    from logins 
    group by id,login_date
)
select id, name 
from accounts
where id in (select id from cte group by id, (login_date - cnt::int) having count(login_date - cnt::int) >= 5)
order by id


-- select l1.id, l2.login_date, COUNT(*) OVER (PARTITION BY l1.id ORDER BY l2.login_date) --, count(l1.login_date)
-- from logins l1
-- join logins l2
-- on l1.login_date = l2.login_date
-- -- where l1.login_date - l2.login_date + 1 = 1 
-- group by l1.id, l2.login_date 



-- WITH cte AS (
--     SELECT *, COUNT(*) OVER (PARTITION BY id ORDER BY login_date) cnt
--     FROM Logins
--     GROUP BY 1,2
-- )
-- -- SELECT *
-- -- FROM Accounts
-- -- WHERE id IN (
--     SELECT id, login_date, cnt, (login_date - cnt::INT)a, login_date
--         FROM cte
--         -- GROUP BY id, login_date, count::int --(login_date - count::INT)
--         -- HAVING COUNT(login_date - count::INT) >= 5
-- --         )
-- -- ORDER BY 1