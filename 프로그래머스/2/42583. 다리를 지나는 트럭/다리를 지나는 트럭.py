# def solution(bridge_length, weight, truck_weights):
#     time = 0
    
#     # passedTrucks: 지난 트럭 / onBrigeTrucks: 건너는 트럭 / waitTrucks
    
#     while(True):
        
#         # 1. 대기 중인 트럭 확인
#         if(truck_weights):
#             # 1-1. 대기중인 트럭 있음 -> 다리 위 하중 체크
#             waitTruck = truck_weights.popleft
#             checkBrigeWeight = waitTruck + sum(onBrigeTrucks)
#             # 하중이 넘으면
#             if(checkBrigeWeight >= weight):
#                 # truck_weights 가장 앞에 다시 waitTruck를 넣는다
#             # 하중이 넘지 않으면
#             else:
#                 # 대기 -> 다리 위로 이동
#                 onBrigeTrucks.append(waitTruck)
#                 moveCount.append(0)

#             #트럭 이동 - moveCount의 모든 요소에 +1를 한다
#             for i in range(len(moveCount)):
#                 moveCount[i] += 1
        
#         # 대기중인 트럭이 없을때
#         else:
#             if(onBrigeTrucks):
#                 #트럭 이동 - moveCount의 모든 요소에 +1를 한다
#                 for i in range(len(moveCount)):
#                     moveCount[i] += 1
#             else:
#                 return time
            
#         time += 1


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0 for _ in range(bridge_length)]
    
    bridge_weight = 0
    while(bridge):
        time += 1
        
        bridge_weight -= bridge.pop(0)
        
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                bridge_weight += t
                bridge.append(t)
            else:
                bridge.append(0)
    return time