-- 코드를 입력하세요
select b.CATEGORY, sum(sales) as total_sales
from book_sales s
join book b
on s.book_id = b.book_id
where s.SALES_DATE between TO_DATE('2022-01-01', 'YYYY-MM-DD') and TO_DATE('2022-01-31', 'YYYY-MM-DD')
group by b.CATEGORY
order by category;
