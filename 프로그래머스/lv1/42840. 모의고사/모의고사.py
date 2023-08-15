# def solution(answers):
    
#     n = len(answers)
#     st1 = [1, 2, 3, 4, 5] * (n //5)
#     st2 = [2, 1, 2, 3, 2] * (n //5)
#     st3 = [3, 3, 1, 1, 2,2,4,4,5,5] * (n // 10)

    
#     students = [st1,st2,st3]
#     scores =[]
    
#     for student in students:
#         score = 0
#         for i in range(n):
#             if answers[i] == student[i]:
#                 score +=1
#         scores.append(score)
    
#     final = []
    
#     for i in range(len(scores)):
#         if scores[i] == max(scores):
#             final.append(i+1)
#     return final
    
    
def solution(answers):
    st_answer = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    scores = [0] * len(st_answer)

    for idx, answer in enumerate(answers):
        for stnum, stanswer in enumerate(st_answer):
            if answer == stanswer[idx % len(stanswer)]:
                scores[stnum] += 1
                
    return [i + 1 for i, v in enumerate(scores) if v == max(scores)]
    
    
    
    
    
    
    