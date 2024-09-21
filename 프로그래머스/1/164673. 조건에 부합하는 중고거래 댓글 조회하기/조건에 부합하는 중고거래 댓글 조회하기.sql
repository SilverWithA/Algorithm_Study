-- 코드를 입력하세요

SELECT b.title, b.board_id,
r.reply_id, r.writer_id, r.contents,
to_char(r.CREATED_DATE,'yyyy-mm-dd')
from used_goods_board b
join used_goods_reply r
on b.board_id = r.board_id
where to_char(b.created_date, 'yyyy-mm') = '2022-10'
order by r.created_date, b.title