-- https://leetcode.com/problems/find-products-with-valid-serial-numbers?envType=problem-list-v2&envId=database

select * from products
where (description COLLATE Latin1_General_CS_AS like '% SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9] %'
or description COLLATE Latin1_General_CS_AS like '% SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]'
or description COLLATE Latin1_General_CS_AS like 'SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9] %')
and description COLLATE Latin1_General_CS_AS not like '% SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9] %';