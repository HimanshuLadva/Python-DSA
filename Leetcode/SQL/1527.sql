-- https://leetcode.com/problems/patients-with-a-condition?envType=problem-list-v2&envId=database
-- #MIMP

SELECT patient_id,p.patient_name, p.conditions FROM Patients AS p
CROSS APPLY STRING_SPLIT(p.conditions, ' ') AS s
where s.value like 'DIAB1%'