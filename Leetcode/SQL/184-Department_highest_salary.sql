-- https://leetcode.com/problems/department-highest-salary?envType=problem-list-v2&envId=database


-- 679ms not optimized
select Department.name as Department, a.name as Employee, a.salary as Salary from Employee a
left outer join Department on Department.id = a.departmentId
where a.salary in (select max(salary) from Employee where departmentId = a.departmentId)
order by a.departmentId

-- second method
select d.name as Department, e.name as Employee ,e.salary as Salary from (
SELECT e.*,RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk FROM Employee e
) e
left outer join Department d on d.id =e.departmentId
where e.rnk= 1
order by d.id