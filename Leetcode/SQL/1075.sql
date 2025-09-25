-- https://leetcode.com/problems/project-employees-i?envType=problem-list-v2&envId=database

select project_id,
cast(round(avg(cast(experience_years as decimal(10,4))), 2) as decimal(10,2)) as average_years from Project
inner join Employee on Employee.employee_id = Project.employee_id
group by project_id
order by project_id