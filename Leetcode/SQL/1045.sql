-- https://leetcode.com/problems/customers-who-bought-all-products?envType=problem-list-v2&envId=database

select customer_id
from customer
group by customer_id
having count(distinct product_key) = (select count(product_key) from product)