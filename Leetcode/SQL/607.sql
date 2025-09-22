-- https://leetcode.com/problems/sales-person?envType=problem-list-v2&envId=database

select name from SalesPerson where sales_id not in (
select sales_id from Orders
inner join Company on Orders.com_id = Company.com_id
where Company.name = 'red'
group by sales_id
)