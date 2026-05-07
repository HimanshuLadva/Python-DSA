-- https://leetcode.com/problems/sales-analysis-iii/?envType=problem-list-v2&envId=database
select distinct Sales.product_id, Product.product_name from Sales 
inner join Product on Product.product_id = Sales.product_id
where Sales.product_id not in (select product_id from Sales where sale_date not between '2019-01-01' and '2019-03-31')