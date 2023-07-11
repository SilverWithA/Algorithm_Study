def solution(arr, k):
    
    # 짝수일때
    if k % 2 == 0:
        for i in range(len(arr)):
            arr[i] = arr[i] + k
    else:
        for i in range(len(arr)):
            arr[i] = arr[i] * k
        
    return arr