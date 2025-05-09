-- Write your PostgreSQL query statement below

WITH CTE_ROW AS(
SELECT seat_id,Seat_id - ROW_NUMBER() OVER (ORDER BY seat_id) rn
FROM Cinema
WHERE free = 1),
CTE_total AS(
SELECT	MIN(seat_id)  first_seat_id   ,MAX(seat_id) last_seat_id   , count(rn) consecutive_seats_len 
FROM CTE_ROW
GROUP BY rn)
SELECT *
FROM CTE_total
WHERE consecutive_seats_len IN (SELECT MAX(consecutive_seats_len) rn FROM CTE_total)

