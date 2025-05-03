-- Write your PostgreSQL query statement below
with trans_count as (
    SELECT v.user_id, v.visit_date, sum(case when t.amount is not null then 1 else 0 end) as transactions
    FROM Visits as v 
    LEFT JOIN Transactions as t 
    ON v.user_id = t.user_id 
    AND v.visit_date = t.transaction_date
    GROUP BY 1, 2
), 
count_series as (
    SELECT generate_series as num
    FROM generate_series(0, (SELECT max(transactions) from trans_count))
)

select num as transactions_count, count(transactions) as visits_count
FROM count_series as c 
LEFT JOIN trans_count as t 
ON c.num = t.transactions
GROUP BY 1
ORDER BY 1