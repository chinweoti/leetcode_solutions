# Write your MySQL query statement below
WITH friends AS (
    SELECT * FROM Friendship 
    UNION ALL 
    SELECT user2_id user1_id, user1_id user2_id FROM Friendship
    ) # Take into account the order of user1 and user2

SELECT user1_id, user2_id, COUNT(*) common_friend 
FROM Friendship f 
JOIN (SELECT DISTINCT user1_id user FROM friends) b # List of all users
ON (f.user1_id, b.user) IN (SELECT * FROM friends) AND (f.user2_id, b.user) IN (SELECT * FROM friends)
GROUP BY user1_id, user2_id
HAVING common_friend >= 3