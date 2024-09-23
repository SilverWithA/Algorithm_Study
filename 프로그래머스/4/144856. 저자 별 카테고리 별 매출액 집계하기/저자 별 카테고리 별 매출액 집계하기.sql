-- 코드를 입력하세요
SELECT b.author_id, a.author_name, b.category
, sum(b.price * s.sales) total_sales
from book b
join author a
on b.author_id = a.author_id
join book_sales s
on b.book_id = s.book_id
where to_char(s.sales_date,'yyyy-mm') = '2022-01' 
group by b.author_id, a.author_name, b.category
order by b.author_id, b.category desc

