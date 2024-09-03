def solution(name):
    answer = 0
    min_move = len(name) - 1
    
    for i, char in enumerate(name):        
        # 알파벳 이동 횟수
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 연속된 A에 대한 처리
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
    
        min_move = min([min_move, # 기존 가장 작은 이동 횟수
                        2 *i + len(name)-next, # 연속된 A의 왼편을 두번 탐색하는 경우
                        i + 2*(len(name)-next)])   # 연속된 A의 오른편을 두번 탐색
    answer += min_move
    return answer