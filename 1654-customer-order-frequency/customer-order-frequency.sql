-- Write your PostgreSQL query statement below
with june as (
    select c.customer_id, c.name
    from Customers c
    join orders o
    using(customer_id)
    join product p
    using (product_id)
    where to_char(o.order_date, 'YYYY-MM') = ('2020-06') 
    group by c.customer_id, c.name
    having sum(p.price*o.quantity)>=100
),
    july as (
        select c.customer_id, c.name
        from Customers c
        join orders o
        using(customer_id)
        join product p
        using (product_id)
        where to_char(o.order_date, 'YYYY-MM') = ('2020-07') 
        group by c.customer_id, c.name
        having sum(p.price*o.quantity)>=100
    )
select customer_id, name from June
intersect
select customer_id, name from July