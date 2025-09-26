-- https://leetcode.com/problems/product-sales-analysis-i?envType=problem-list-v2&envId=database

select product_name,year,price from Sales 
inner join Product on Product.product_id = Sales.product_id 