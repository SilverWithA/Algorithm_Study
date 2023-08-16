# def solution(arr, queries):
    
#     data = [[] for row in range(len(queries))]
#     result= []
    
#     for order,query in enumerate(queries):
#         print("order: ",order,"query: ", query,"-----------------")
        
#         data[order] = arr[query[0]:query[1]]
#         data[order].sort
        
#         for i in data[order]:
#             if i > query[2]:
#                 result.append(data)
#                 break
#         print("result: ",result)

#         if not result[order]:
#             result.append(-1)
        
            
#     return result



def solution(arr, queries):
    result = []
    for query in queries:
        temp_list = []
        for i in range(query[0], query[1] + 1):
            if arr[i] > query[2]:
                temp_list.append(arr[i])
        try:   
            result.append(min(temp_list))
        except:
            result.append(-1)
    return result

        
            
