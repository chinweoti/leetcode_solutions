-- Write your PostgreSQL query statement below
select 
    period_state, min(date_) as start_date, max(date_) as end_date
from
(select *, (row_number() over (order by date_) - row_number() over (partition by period_state order by date_)) as diff
    from 
    (select success_date as date_, 'succeeded' as period_state
        from Succeeded
        where success_date >= '2019-01-01' and success_date <= '2019-12-31'
        union
        select fail_date as date_, 'failed' as period_state
        from Failed
        where fail_date >= '2019-01-01' and fail_date <= '2019-12-31'
    ) t1
    order by date_
) t2
group by period_state, diff
order by 2