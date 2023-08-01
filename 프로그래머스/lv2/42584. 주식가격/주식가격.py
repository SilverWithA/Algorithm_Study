def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        # print("-------------------------------------------")
        # print(f"{i}초의 가격: ", prices[i])
        
        for j in range(i+1,len(prices)):
            # print(f"prices[{j}]: ",prices[j])
            
            # 주식 가격이 떨어지면= 떨어진 시점 - 현재 시점
            if prices[i] > prices[j]:
                answer.append(j-i)
                # print("answer: ",answer)
                break
                
                
        # 끝까지 주식 가격이 떨어지지 않으면= 마지막 시점 - 현재 시점        
        if len(answer) != i+1:
            answer.append(len(prices)-i-1)
            # print("answer: ",answer)
        
    answer.append(0)
    return answer