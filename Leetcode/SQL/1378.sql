-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier?envType=problem-list-v2&envId=database

select unique_id, name from Employees
left outer join EmployeeUNI on EmployeeUNI.id = Employees.id