# def solution(n):    
    
#     trit = ''
    
#     while n > 0:
#         n, mod = divmod(n, 3)
#         print(n,mod)
#         trit += str(mod)
#     return int(trit,3)

def solution(n):
    mod = []
    while True:
        if n == 0:
            return 0
        
        mod.append(n%3)
        n = n//3
        print(n)
        
        if n//3 == 0:
            mod.append(n%3)
            break
    # print(''.join(map(str,나머지[::-1]))) # int 리스트를 3진법으로 바꾸는 법
    # 여기선 굳이 뒤집을 필요가 없어서
    result = ""
    for i in mod:
        result += str(i)
    print(result)
    result = result.rstrip("0") # 아래 문법이 있으니 이건 필요 없게됨.
    print(result)
    
    return int(result,3) # int(String,n) => n진법인 String을 10진법으로 변환

    



