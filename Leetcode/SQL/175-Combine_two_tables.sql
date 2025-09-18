-- https://leetcode.com/problems/combine-two-tables?envType=problem-list-v2&envId=database

select firstName,lastName,city,state from Person
left outer join Address on Address.personId = Person.personId