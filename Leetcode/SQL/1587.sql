-- https://leetcode.com/problems/bank-account-summary-ii?envType=problem-list-v2&envId=database

select Users.name, sum(amount) as balance from Transactions t
inner join Users on Users.account = t.account
group by Users.name
having sum(amount) > 10000