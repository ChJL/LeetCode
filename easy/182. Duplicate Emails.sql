# 182. Duplicate Emails

# Write your MySQL query statement below
SELECT distinct(p1.Email)
FROM Person p1, Person p2
WHERE p1.Email = P2.Email AND
p1.Id <> P2.Id