-- Write your PostgreSQL query statement below
select task_id, generate_series(1, subtasks_count) as subtask_id
from tasks

EXCEPT

select task_id, subtask_id from executed