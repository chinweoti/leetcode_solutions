-- Write your PostgreSQL query statement below

select case when count(requester_id::text || accepter_id::text)= 0 then 0
            when count(sender_id::text || send_to_id::text) = 0 then 0 else
    round(count(distinct requester_id::text || accepter_id::text)::numeric /count(distinct sender_id::text || send_to_id::text), 2) end as accept_rate
from FriendRequest
left join RequestAccepted
on RequestAccepted.accepter_id = FriendRequest.send_to_id




