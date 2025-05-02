-- Write your PostgreSQL query statement below
select player_id, player_name, (count(Wimbledon) filter (where Wimbledon = player_id) + count(Fr_open) filter (where Fr_open = player_id) + 
+ count(US_open) filter (where US_open = player_id) + count(Au_open) filter (where Au_open = player_id)) as grand_slams_count
from players p, championships c
where player_id in (Wimbledon, Fr_open , US_open , Au_open)
group by player_id, player_name
 