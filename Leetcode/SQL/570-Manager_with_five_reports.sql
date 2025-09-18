-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports?envType=problem-list-v2&envId=database

select name from Employee where id in (
select managerId from Employee
group by managerId
having count(id) >= 5
)