# 시도(1): 런타임에러-----------------------------------------

# import re
# def solution(skill, skill_trees):
    
#     # 1. 스킬트리 알파벳 순서대로 1,2,3 순번으로 변환하기
#     cnt = 0
#     for skill_tree in skill_trees:
#         # print("----------------------------------")
#         # print("skill_tree: ",skill_tree)
        
#         for i in range(len(skill)):
#             # print(f"skill[{i}]: ",skill[i])
#             if skill[i] in skill_tree:
#                 skill_tree = skill_tree.replace(skill[i],str(i+1))
#         # print("skill_tree: ",skill_tree)
        
#         # 2. 문자열 중 숫자형태의 문자면 추출
#         numbers = re.sub(r'[^0-9]', '', skill_tree)
#         numbers = int(numbers)
#         # print("numbers: ",numbers)
        
#         if numbers == 123 or numbers ==12 or numbers < 4:
#             cnt += 1
#             # print("cnt: ",cnt)
#     return cnt

# 시도(2): 런타임에러-----------------------------------------
def solution(skill, skill_trees):
    answer = 0
    
    
    for skill_tree in skill_trees:
        skill_list = list(skill)
        # print("------------------------------")
        # print("skill_list: ",skill_list)
        
        for s in skill_tree:
            if s in skill:
                # print("skill_tree: ",skill_tree)
                # print("s: ",s)
                if s != skill_list.pop(0):
                    break
        else:
            answer +=1
            # print("answer: ",answer)
    return answer

                    
                    
                
        
            
        

