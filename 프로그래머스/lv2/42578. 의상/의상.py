# def solution(clothes):
#     hash = {}
#     for cloth in clothes:
#         if cloth[1] in hash:
#             hash[cloth[1]].append(cloth[0])
#         else:
#             hash[cloth[1]] = [cloth[0]]


#     cnt  = 1
#     if len(hash) == 1:
#         return len(clothes)
    
#     for i in hash:
#         cnt *= len(hash[i])

#     return len(clothes) + cnt
# ---------------------------------------------


def solution(clothes):
    hash = {}
    count = 1
    
    # hash = {"의상종류":["의상"]} -> value를 list형으로 들어가도록 구성
    for cloth in clothes:
        if cloth[1] in hash:
            hash[cloth[1]].append(cloth[0])
        else:
            hash[cloth[1]] = [cloth[0]]
    
    # 옷을 입는 경우의 수 만들기
    # 풀이방법: 입지 않는 경우도 추가하여 곱한뒤 -1 해준다
    
    for cate_cloth in hash:
        
        count *= (len(hash[cate_cloth])+1)
        
    return count -1