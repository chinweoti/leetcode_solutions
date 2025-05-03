-- Write your PostgreSQL query statement below
select request_at as Day,
round(sum(case when status like 'cancelled%' then 1.0 else 0 end)::numeric/ count(distinct id), 2) as "Cancellation Rate"
from trips t
left join users u1
on t.client_id = u1.users_id 
left join users u2
on t.driver_id = u2.users_id
where u1.banned = 'No' and u2.banned = 'No'
and request_at between '2013-10-01' and '2013-10-03'
group by request_at



-- SELECT 
--     request_at AS Day,
--     ROUND(
--         SUM(CASE 
--                 WHEN t.status IN ('cancelled_by_driver', 'cancelled_by_client') 
--                 THEN 1 ELSE 0 END) * 1.0 / 
--         COUNT(DISTINCT t.id), 2) AS "Cancellation Rate"
-- FROM 
--     Trips t
-- JOIN 
--     Users u_client ON t.client_id = u_client.users_id AND u_client.banned = 'No'
-- JOIN 
--     Users u_driver ON t.driver_id = u_driver.users_id AND u_driver.banned = 'No'
-- WHERE 
--     t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
-- GROUP BY 
--     t.request_at
-- ORDER BY 
--     t.request_at;