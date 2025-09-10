-- https://leetcode.com/problems/second-highest-salary?envType=problem-list-v2&envId=database

select MAX(salary) as SecondHighestSalary from Employee 
where salary < (select MAX(salary) from Employee)