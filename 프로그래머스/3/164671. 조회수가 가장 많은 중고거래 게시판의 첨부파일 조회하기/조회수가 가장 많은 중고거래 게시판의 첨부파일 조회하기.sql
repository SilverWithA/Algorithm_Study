-- 코드를 입력하세요


SELECT '/home/grep/src/' || BOARD_ID || '/' || file_id || file_name || file_ext as FILE_PATH
FROM USED_GOODS_FILE
WHERE BOARD_ID = (SELECT BOARD_ID
                FROM USED_GOODS_BOARD
                WHERE VIEWS = 
                  (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD))
ORDER BY FILE_ID DESC