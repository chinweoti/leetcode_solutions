-- Write your PostgreSQL query statement below

    select pay_month, department_id, case when avg(emp_amt) =  avg(avg_amt) then 'same'
                                        when avg(emp_amt) < avg(avg_amt) then 'lower'
                                        else 'higher' end as comparison
    from (select pay_date, to_char(pay_date, 'YYYY-MM') as pay_month, round(avg(amount),2) as avg_amt from salary group by pay_date)
    join (select pay_date,department_id, round(avg(amount),2) as emp_amt from salary left join employee using(employee_id) group by department_id, pay_date)
    using (pay_date)
    group by department_id, pay_month



