-- CHALLENGE 1
-- STEP 1
select ta.au_id as AUTHOR_ID, 
t.title_id as TITLE, 
t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100 as Sales_Royalty
from titleauthor ta
inner join titles t on ta.title_id = t.title_id
inner join sales s on s.title_id = t.title_id

-- STEP 2
select ta.au_id as AUTHOR_ID, 
t.title_id as TITLE, 
SUM(t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100) as Sales_Royalty
from titleauthor ta
inner join titles t on ta.title_id = t.title_id
inner join sales s on s.title_id = t.title_id
group by ta.au_id, t.title_id

-- STEP 3
SELECT p.AUTHOR_ID, SUM(Sales_Royalty) AS Profits FROM
	(select ta.au_id as AUTHOR_ID, 
	t.title_id as TITLE, 
	SUM(t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100) as Sales_Royalty
	from titleauthor ta
	inner join titles t on ta.title_id = t.title_id
	inner join sales s on s.title_id = t.title_id
	group by ta.au_id, t.title_id) as p
group by p.AUTHOR_ID

-- CHALLENGE 2
-- STEP 1
CREATE TEMPORARY TABLE sales_royalty
select ta.au_id as AUTHOR_ID, 
t.title_id as TITLE, 
t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100 as Sales_Royalty
from titleauthor ta
inner join titles t on ta.title_id = t.title_id
inner join sales s on s.title_id = t.title_id

-- STEP 2
select AUTHOR_ID, 
TITLE, 
SUM(Sales_Royalty) as Sales_Royalty
from sales_royalty
group by AUTHOR_ID, TITLE

-- STEP 3
select AUTHOR_ID, 
SUM(Sales_Royalty) as Sales_Royalty
from sales_royalty
group by AUTHOR_ID

-- CHALLENGE 3
CREATE TABLE most_profiting_authors
	select AUTHOR_ID AS au_id, 
	SUM(Sales_Royalty) as profits
	from sales_royalty
	group by AUTHOR_ID