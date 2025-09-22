-- https://leetcode.com/problems/classes-with-at-least-5-students?envType=problem-list-v2&envId=database

select class from Courses
group by class
having COUNT(student) >= 5