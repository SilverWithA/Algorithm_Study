# def solution(board, moves):
#     busket = [0]
#     result = 0
#     n = len(moves)
    
#     for i in range(n):
#         # board에서 꺼낸 요소가 0이 아닐때
#         if board[moves[i]-1][-1] != 0:
            
#             # busket의 마지막 요소와 꺼낸 요소가 같다면
#             if busket[-1] == board[moves[i]-1][-1]:
#                 result += 2
#                 busket.pop()
                
        
             
#             # busket의 마지막 요소와 꺼낸 요소가 다르다면
#             else:
#                 # busket에 꺼낸 요소 추가
#                 busket.append(board[moves[i]-1][-1])
                
#         # board의 마지막 요소 삭제
#         board[moves[i]-1].pop()
#     return result


def solution(board, moves):
    stacklist = []
    answer = 0
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                stacklist.append(board[i][move-1])
                board[i][move-1] = 0
                
                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break
    return answer
        