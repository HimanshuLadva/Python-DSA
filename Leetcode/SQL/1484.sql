-- https://leetcode.com/problems/group-sold-products-by-the-date?envType=problem-list-v2&envId=database
-- #MIMP

select sell_date,count(*) as num_sold, 
STRING_AGG(product, ',') WITHIN GROUP (ORDER BY product) AS products 
from ( SELECT DISTINCT sell_date, product FROM Activities) AS distinct_products
group by sell_date