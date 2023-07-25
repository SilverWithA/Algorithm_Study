# def solution(my_string, indices):
#     answer = ''
#     idx = [i for i in range(0,len(my_string))]
#     # print(idx)
#     remains = set(idx) - set(indices)
#     remains = list(remains)
#     # print(remains)
#     for i in remains:
#         answer += my_string[i]
#     return answer


# -------------------------------------------
def solution(my_string, indices):
    answer = ''
    # indices.sort()
    # print(indices)
    
    for i in range(len(my_string)):
        if i in indices:
            continue
        else:
            answer += my_string[i]
    return answer
 