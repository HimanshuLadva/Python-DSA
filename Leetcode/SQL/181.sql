-- https://leetcode.com/problems/employees-earning-more-than-their-managers?envType=problem-list-v2&envId=database

select Employee.name as Employee from Employee
inner join Employee as e on e.id = Employee.managerId
where Employee.salary > e.salary