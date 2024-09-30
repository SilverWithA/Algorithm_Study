SELECT F.CATEGORY, F.PRICE AS MAX_PRICE, F.PRODUCT_NAME
FROM food_product F
JOIN (SELECT category, max(price) AS PRICE
        FROM food_product
        WHERE category in ( '과자', '국', '김치', '식용유')
        GROUP BY category) M
ON F.CATEGORY = M. CATEGORY
AND F.PRICE = M.PRICE
ORDER BY F.PRICE DESC
