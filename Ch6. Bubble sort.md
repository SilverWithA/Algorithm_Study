## ch6. 정렬
### 6-1. 정렬이란
### 6-2. 버블 정렬
배열에서 이웃 요소의 대소 관계 비교하여 교환하는 정렬 방법

요소가 n개인 배열에서 n-1번을 각 요소를 비교하고 교환하면 정렬 끝. 이 과정을 pass라고 함


```python
# 실습 6-1 버블 정렬 구현하기- 패스를 맨 끝열부터 수행

def bubble_sort(a):
    """배열 a를 버블정렬을 이용해 오름차순 정렬"""
    n = len(a)
    for i in range(n-1): # 패스 횟수
        for j in range(n-1,i,-1): # 두 요소 비교
            if a[j-1] > a[j]:
                a[j-1],a[j] =a[j],a[j-1]   # 두 요소 자리 교환
                
                
bubble_sort([1,2,3,4])
```

* #### 알고리즘 개선1 -> 패스 횟수 줄이기

만약 요소가 8개인 배열에서 n-3 패스부터 교환이 이루어지지 않는다면 그 이후 패스에서도 교환이 이뤄지지 않는다 = 이미 정렬이 다 된 상태를 의미


```python
 # 실습 6-2 버블 정렬 알고리즘 개선1
    
def bubble_sort1(a):
    n = len(a)
    for i in range(n-1):
        
        exchg = 0  # 각 패스에서 교환이 일어난 횟수
        
        for j in range(n-1,i,-1):
            if a[j-1] > a[j]:
                a[j-1],a[j] = a[j],a[j-1]
        if exchg == 0:   # 교환이 일어나지 않았다면 break
            break
```

* #### 알고리즘 개선2 -> 패스 인덱스 줄이기

각 패스에서 마지막으로 교환이 일어난 인덱스를 저장하여 다음 패스에서 해당 인덱스까지만 비교를 진행하도록 알고리즘 개선(스캔 범위 제한)


```python
def bubble_sort(a):
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n - 1, k, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last
```
"# data-structure-algorithm" 
