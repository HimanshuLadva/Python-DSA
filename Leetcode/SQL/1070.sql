-- https://leetcode.com/problems/product-sales-analysis-iii/description/?envType=problem-list-v2&envId=database
;with demos as (
select *,DENSE_RANK() over (partition by product_id order by year) as Rowno from Sales
)
select product_id, year as first_year, quantity, price from demos where Rowno = 1
