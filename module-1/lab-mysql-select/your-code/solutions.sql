USE publications;

-- Challenge 1
select a.au_id as AUTHOR_ID, a.au_lname as LAST_NAME,
a.au_fname as FIRST_NAME, 
t.title as TITLE, 
p.pub_name as PUBLISHER 
from authors a 
join titleauthor ta on a.au_id = ta.au_id 
join titles t on ta.title_id = t.title_id 
join publishers p on t.pub_id = p.pub_id;

-- Challenge 2
select a.au_id as AUTHOR_ID, a.au_lname as LAST_NAME,
a.au_fname as FIRST_NAME, 
p.pub_name as PUBLISHER,
COUNT(t.title_id) as TITLE_COUNT
from authors a 
join titleauthor ta on a.au_id = ta.au_id 
join titles t on ta.title_id = t.title_id 
join publishers p on t.pub_id = p.pub_id
group by (t.title_id)

-- Challenge 3
select a.au_id as AUTHOR_ID, 
a.au_lname as LAST_NAME,
a.au_fname as FIRST_NAME,
SUM(s.qty) as TOTAL
from authors a 
join titleauthor ta on a.au_id = ta.au_id 
join titles t on ta.title_id = t.title_id 
join sales s on s.title_id = t.title_id
group by (a.au_id)
order by (TOTAL) DESC
LIMIT 3

-- Challenge 4
select a.au_id as AUTHOR_ID, 
a.au_lname as LAST_NAME,
a.au_fname as FIRST_NAME,
SUM(IFNULL(s.qty, 0)) as TOTAL
from authors a 
left join titleauthor ta on a.au_id = ta.au_id 
left join titles t on ta.title_id = t.title_id
LEFT join sales s on s.title_id = t.title_id
group by (a.au_id)
order by (TOTAL) DESC






