# < Do it! 자료구조와 함께 배우는 알고리즘 입문 파이썬 >
## Ch 5. 재귀 알고리즘

### (1) 재귀: 자기 자신을 사용하여 정의
##### ex) 팩토리얼  n! = n * (n-1)!

* #### 직접 재귀: 자기 자신과 같으 매서드를 호출
* #### 간접 재귀: 대른 매서드를 통해 자기 자신과 같은 매서드 호출



```python
# 실습 5-1. 양의 정수 팩토리얼 구하기
def factorial(n):
    if n > 0:
        return n * factorial(n - 1) # 재귀적 정의
    else:
        return 1
    

factorial(3)

```




    6




```python
# 실습 5-2 유클리드 호제법으로 최대 공약수 구하기

def gcd(x,y):
    if y == 0:  # 나머지가 0일때 
        return x   # gcd 발견
    else:
        return gcd(y, x%y) # y와 x%y의 나머지
    
print(f"8과 22의 최대 공약수는 {gcd(8,22) }이다.")

```

    8과 22의 최대 공약수는 2이다.
    

### (2) 재귀 알고리즘 분석
* #### 하향식 분석: recur(4)부터 시작하여 아래로 내려가는 분석
* #### 상향식 분석: 가장 아래인 recur(-1)부터 위로 올라가는 분석



```python
# 실습 5-3 순수 재귀 함수 구현
def recur(n):
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)


recur(4)
```

    1
    2
    3
    1
    4
    1
    2
    

### 재귀 알고리즘의 비재귀적 표현


```python
# 실습 5-4 꼬리 재귀 제거

def recur(n):
    
    while n > 0:
        recur(n-1)
        print(n)
        n = n - 2 # 꼬리 재귀 제거
        
recur(4)
```

    1
    2
    3
    1
    4
    1
    2
    

### (3) 하노이의 탑

#### 원반을 최소 횟수로 옮기기 위한 알고리즘
##### 원반 5개가 쌓인 하노이 탑을 이동하려면 원반 4개 이동 하노이 + 원반 3개 하노이 + 원반 2개 하노이 + 원반 1개 하노이의 과정을 거쳐야한다 - 재귀적


```python
def move(no: int, x: int, y: int) -> None:
    """원반을 no개를 x 기둥에서 y 기둥으로 옮김"""
    if no > 1:
        move(no - 1, x, 6 - x - y)

    print(f'원반 [{no}]을(를) {x}기둥에서 {y}기둥으로 옮깁니다.')

    if no > 1:
        move(no - 1, 6 - x - y, y)

move(4, 1, 3)
```

### (4) 8퀸 문제
