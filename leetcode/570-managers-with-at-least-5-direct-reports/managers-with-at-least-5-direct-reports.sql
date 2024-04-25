# Write your MySQL query statement below

with direct_reports as (
    select managerId
    from Employee
    group by managerId
    having count(id) >= 5
)
select e.name 
from direct_reports dr
inner join employee e on e.id = dr.managerId;