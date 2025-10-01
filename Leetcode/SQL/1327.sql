-- https://leetcode.com/problems/list-the-products-ordered-in-a-period?envType=problem-list-v2&envId=database

select product_name,sum(unit) as unit from Orders
inner join Products on Products.product_id = Orders.product_id 
where DATENAME(month, order_date) = 'February' and DATENAME(YEAR, order_date) = 2020
group by Orders.product_id,product_name
having sum(unit) >= 100
order by Orders.product_id