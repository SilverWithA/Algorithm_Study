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