# def solution(phone_book):
#     n = len(phone_book)
#     hash_value = [i for i in range(1,n+1)]
#     hash_phone = [[] for i in range(n) ]
#     # print(hash_phone)
    
    
    
#     for i in range(hash_phone)
#         if hash_phone[i][0] in hash_value:
#             return false
#     return true
        
#     for phone_number in phone_book:
#         for i in phone_book:
#             if i != phone_number and i in phone_number:
#                 return False
#     return True


# ----------------------------------------
def solution(phone_book):
    answer = True
    hash = {}
    
    for i in phone_book:
        hash[i] = 2   # dictionary에 전화번호를 key값으로 넣기 위한 for문
    # print("hash: ",hash)
        
    for phone_number in phone_book:
        temp =''
        # print("phone_number: ",phone_number,"========================")
        for num in phone_number:
            temp += num
            
            # print("temp: ",temp)
            if temp in hash and temp != phone_number:  # hash에 key값으로 있는지 확인
                answer = False
                # print("answer: ",answer)
    return answer











