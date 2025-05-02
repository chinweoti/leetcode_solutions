-- Write your PostgreSQL query statement below
select product_id, 'store1' as store, store1 as price
from products 
where store1 is not null

union all

select product_id, 'store2' as store, store2 as price
from products 
where store2 is not null

union all
select product_id, 'store3' as store, store3 as price
from products 
where store3 is not null



-- cross join
-- select p.product_id, t.store, t.price from products p
--     cross join lateral (
--         values
--             (store1, 'store1'),
--             (store2, 'store2'),
--             (store3, 'store3')
--     ) as t(price, store)
-- where t.price is not null
-- order by t.store