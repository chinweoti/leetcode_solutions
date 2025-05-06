-- Write your PostgreSQL query statement below

with words as (
    Select
    post_id, unnest(string_to_array(lower(content),' ')) as content
    from Posts
)
SELECT post_id, COALESCE(string_agg(topic_id::text,',' ORDER BY topic_id asc),'Ambiguous!') as topic
FROM (
        select distinct post_id, topic_id from words w
        left join Keywords k on lower(word)=w.content
        )P 
GROUP BY 1
order by 1