-- https://leetcode.com/problems/customers-who-never-order?envType=problem-list-v2&envId=database

select name as Customers from Customers
left outer join Orders on Orders.customerId = Customers.id
where ISNULL(customerId, 0) = 0