-- Write your PostgreSQL query statement below
SELECT u1.user_id, ROUND(AVG(u1.activity_duration),2) AS trial_avg_duration, ROUND(AVG(u2.activity_duration*1.0),2) AS paid_avg_duration
FROM UserActivity u1
JOIN UserActivity u2
ON u1.user_id = u2.user_id
WHERE u1.activity_type = 'free_trial' AND u2.activity_type = 'paid'
GROUP BY u1.user_id