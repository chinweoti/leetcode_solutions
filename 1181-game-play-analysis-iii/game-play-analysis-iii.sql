# Write your MySQL query statement below
select player_id, event_date, sum(games_played) over (partition by player_id order by event_date) as games_played_so_far
from activity

-- when summing all previous rows
-- (rows between unbounded preceding and current row) 