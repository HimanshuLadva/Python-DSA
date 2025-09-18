-- https://leetcode.com/problems/employee-bonus?envType=problem-list-v2&envId=database

select name, bonus from Employee
left outer join Bonus on Bonus.empId = Employee.empId
where ISNULL(Bonus.bonus, 0) < 1000
order by bonus 