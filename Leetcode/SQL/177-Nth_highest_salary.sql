-- https://leetcode.com/problems/nth-highest-salary?envType=problem-list-v2&envId=database

CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        select salary  from (select salary, ROW_NUMBER() over (order by salary desc) as rn from Employee group by salary) t
        where rn = @N
    );
END