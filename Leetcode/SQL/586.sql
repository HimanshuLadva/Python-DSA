-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders?envType=problem-list-v2&envId=database
-- #MIMP

-- 970ms
select top 1 customer_number from Orders
group by customer_number
order by count(distinct order_number) desc

