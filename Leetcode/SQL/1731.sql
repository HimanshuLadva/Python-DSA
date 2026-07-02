-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/?envType=problem-list-v2&envId=database

;with ctee as (
select Employees.reports_to,count(*) as reports_count,AVG(cast(age as numeric(18,2))) AS avg_age, ROUND(avg(cast(age as numeric(18,2))),0) as average_age from Employees 
where ISNULL(Employees.reports_to, 0) <> 0
group by Employees.reports_to
)
select Employees.employee_id,Employees.name,ctee.reports_count, cast(ctee.average_age as int) as average_age  from ctee 
left outer join Employees on Employees.employee_id = ctee.reports_to
order by employee_id