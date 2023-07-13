import math
def solution(n):
    result = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            if i == n //i:
                result +=1
            else:
                result += 2
    return result