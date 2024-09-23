-- 코드를 입력하세요

SELECT c.car_id, c.car_type
, (c.daily_fee * (100 - d.discount_rate) / 100) * 30 fee
FROM (select car_id, car_type, daily_fee
      from CAR_RENTAL_COMPANY_CAR
      where car_id not in (select car_id
                           from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                           where to_char(start_date,'yyyymmdd') > '20221031' or to_char(end_date, 'yyyymmdd') > '20221031')) c
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN d
ON c.car_type = d.car_type

WHERE c.car_type in ('세단', 'SUV')
and d.duration_type = '30일 이상'
and (c.daily_fee * (100 - d.discount_rate) / 100) * 30 between 500000 and 2000000
order by 3 desc, 2, 1 desc
