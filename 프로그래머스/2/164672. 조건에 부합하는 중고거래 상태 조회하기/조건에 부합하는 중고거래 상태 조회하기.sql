-- 코드를 입력하세요
SELECT BOARD_ID, WRITER_ID, TITLE, PRICE
, DECODE(STATUS
       ,'SALE','판매중'
       ,'RESERVED','예약중'
       ,'DONE','거래완료'
       ,STATUS) AS STATUS
       
from USED_GOODS_BOARD 
where to_char(created_date, 'yyyy-mm-dd') = '2022-10-05'
order by BOARD_ID desc

