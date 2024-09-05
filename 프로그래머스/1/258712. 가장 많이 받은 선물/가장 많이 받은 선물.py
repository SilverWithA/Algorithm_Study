import collections
def solution(friends, gifts):
    # 각 사람에 대한 정보/총 받은 선물/총 준 선물/선물 지수
    info = collections.defaultdict(lambda: [[],0,0,0])
    pred = collections.defaultdict(int)
    
    for friend in friends:
        info[friend]
        pred[friend]

        
    for gift in gifts:
        giver, taker = gift.split(" ")
        
        # 각 사람과의 선물 교환 정보
        info[giver][0].append(taker)
        # 총 받은 선물
        info[taker][1] += 1
        # # 총 준 선물
        info[giver][2] += 1
    
    # 선물 지수 계산
    for k, v in info.items():
        info[k][3] = info[k][2] - info[k][1]
    # print(info)
    
        
    # 다음달 예측하기
    for i, friend in enumerate(friends):
        # print()
        # print(i, friend)
        if i == (len(friends)-1):
            continue
        for j in range(i+1, len(friends)):
            # print(j, friends[j])
            
            # 왼 -> 오가 더 많이 줬다면 왼(friend)가 다음달에 하나 받음
            if info[friend][0].count(friends[j]) > info[friends[j]][0].count(friend):
                pred[friend] += 1
                
            # 왼 <- 오가 더 많이 줬다면 오(friends[j])가 다음달에 하나 받음
            elif info[friend][0].count(friends[j]) < info[friends[j]][0].count(friend):
                pred[friends[j]] += 1
            
            # 서로 주고받지 않았거나 주고받은 개수가 같다면 선물지수 비교
            elif info[friend][0].count(friends[j]) == info[friends[j]][0].count(friend):
                if info[friend][3] > info[friends[j]][3]:
                    pred[friend] += 1
                elif info[friend][3] < info[friends[j]][3]:
                    pred[friends[j]] += 1
            # print(pred)
    return max(pred.values())
                    
            
            