-- Write your PostgreSQL query statement below
select id
from weather w
where temperature > (select temperature from weather where w.recordDate - recordDate = 1)