-- https://leetcode.com/problems/find-users-with-valid-e-mails?envType=problem-list-v2&envId=database
-- #MIMP
-- for most of case
select user_id, name, mail
from Users
where right(mail,13) = '@leetcode.com'
and left(mail,LEN(mail) - 13) LIKE '[A-Za-z]%'
and left(mail,LEN(mail) - 13) NOT LIKE '%[^A-Za-z0-9._-]%'   

-- for all case
select user_id, name, mail
from Users
where RIGHT(mail,13) COLLATE Latin1_General_CS_AS = '@leetcode.com'
and left(mail,LEN(mail) - 13) LIKE '[A-Za-z]%'
and left(mail,LEN(mail) - 13) NOT LIKE '%[^A-Za-z0-9._-]%'   
