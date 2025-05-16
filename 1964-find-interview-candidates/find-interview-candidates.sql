-- Write your PostgreSQL query statement below
WITH unnested AS (
    SELECT 
    contest_id,
    UNNEST(ARRAY[gold_medal, silver_medal, bronze_medal]) AS user_id,
    UNNEST(ARRAY['gold', 'silver', 'bronze']) AS medal
    FROM contests
),
joined_and_grouping AS (
    SELECT 
    contest_id, medal, user_id, name, mail,
    contest_id - ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY contest_id) AS groups
    FROM unnested
    JOIN users USING(user_id)
)

SELECT DISTINCT name, mail 
FROM joined_and_grouping 
GROUP BY user_id, name, mail, groups 
HAVING COUNT(groups) >= 3

UNION 

SELECT name, mail 
FROM joined_and_grouping 
WHERE medal = 'gold'
GROUP BY user_id, name, mail 
HAVING COUNT(contest_id) >= 3