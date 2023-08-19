def solution(n):
    result =[n]
    while n != 1:
    
        if n % 2 == 0:   #짝수일 때
            n //= 2
        else:
            n = n *3 +1
        result.append(n)

    return result
    