-- Write your PostgreSQL query statement below
select id
from weather w
where recordDate > (select min(recordDate) from weather)
    and temperature > (select temperature from weather where w.recordDate - recordDate = 1)