-- 코드를 입력하세요
SELECT PT_NAME, PT_NO, GEND_CD, AGE, NVL(TLNO, 'NONE')
from patient
where age <= 12
and gend_cd = 'W'
ORDER BY AGE DESC, PT_NAME