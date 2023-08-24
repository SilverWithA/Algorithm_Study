def solution(arr1, arr2):
    
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    # print("answer: ",answer)
    
    for i in range(len(arr1)): 
        for j in range(len(arr2[0])): 
            for k in range(len(arr1[0])):
                # print(f"arr1[{i}][{k}]: ",arr1[i][k])
                # print(f"arr2[{k}][{j}]: ",arr2[k][j])
                answer[i][j] += arr1[i][k] * arr2[k][j]
            #     print(f"answer[{i}][{j}]: ",answer[i][j])
            #     print()
            # print("---------------------------")
    return answer
            
                