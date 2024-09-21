-- 코드를 입력하세요

select extract(Month from start_date) as MONTH,
car_id, count(*) as records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where car_id in (select car_id 
                 from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
                 where extract(Month from start_date) in (8,9,10)
                 group by car_id 
                 having count(*)> 4)
and 8 <= extract(Month from start_date) 
and extract(Month from start_date) < 11
group by extract(Month from start_date), car_id
having count(history_id) > 0
order by extract(Month from start_date), car_id desc
