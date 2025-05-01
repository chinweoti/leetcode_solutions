-- Write your PostgreSQL query statement below
select team_id, team_name, 
sum(case when team_id = m.host_team and m.host_goals > m.guest_goals then 3 
    when team_id = m.host_team and m.host_goals = m.guest_goals then 1 
    when team_id = m.guest_team and m.host_goals < m.guest_goals then 3 
    when team_id = m.guest_team and m.host_goals = m.guest_goals then 1 
    else 0 end) as num_points
from teams t, matches m
group by team_id, team_name
order by num_points desc, team_id asc
