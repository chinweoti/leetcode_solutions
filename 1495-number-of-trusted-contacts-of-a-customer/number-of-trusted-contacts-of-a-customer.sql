-- Write your PostgreSQL query statement below

select invoice_id, customer_name, price, count(c.user_id) contacts_cnt, count(contact_name) filter (where c.contact_name in (select customer_name from customers))  as trusted_contacts_cnt
from customers cu
left join contacts c
on customer_id = c.user_id
join invoices i
on customer_id = i.user_id
group by invoice_id, customer_name, price
order by invoice_id



