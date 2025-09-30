-- https://leetcode.com/problems/students-and-examinations?envType=problem-list-v2&envId=database
-- #MIMP

select s.student_id,s.student_name,sub.subject_name,count(e.student_id) as attended_exams from Students s
cross join Subjects sub
left outer join Examinations e on e.student_id = s.student_id and e.subject_name = sub.subject_name
group by s.student_id,s.student_name,sub.subject_name
order by s.student_id,sub.subject_name