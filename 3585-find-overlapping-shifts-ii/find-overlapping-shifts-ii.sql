-- Write your PostgreSQL query statement below
with t1 as (
    select 
        e1.employee_id, 
        e1.start_time,
        (extract('EPOCH' from e1.end_time) - extract('EPOCH' from e2.start_time))/60 as "overlap_duration"
    from EmployeeShifts as e1
    left join EmployeeShifts as e2
     on (e1.employee_id = e2.employee_id) 
     and (e1.start_time < e2.start_time)
     AND (e1.start_time, e1.end_time) OVERLAPS (e2.start_time, e2.end_time)
    --  and (e1.end_time between e2.start_time and e2.end_time)
), t2 as (
    -- group by employee id + start time to get overlapping shift of each group
    -- count + 1 because k overlapping rows means k+1 overlapping shifts 
    select 
        employee_id, 
        count(overlap_duration)+1 as "overlapping_shift", 
        coalesce(sum(overlap_duration), 0) as "overlap_duration"
    from t1
    group by employee_id, start_time
)

-- get summary stats
select employee_id, max(overlapping_shift) as "max_overlapping_shifts", sum(overlap_duration) as "total_overlap_duration"
from t2
group by employee_id
order by employee_id