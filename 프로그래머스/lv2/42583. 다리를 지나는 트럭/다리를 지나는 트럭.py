from collections import deque
def solution(bridge_length, weight, truck_weights):
    totaltrucks = sum(truck_weights)
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    t = 0
    bridge_sum = 0
    while totaltrucks > 0:
        t+=1
        out = bridge.popleft()
        totaltrucks -= out
        bridge_sum -= out
        if len(trucks) >=1:
            if bridge_sum + trucks[0] <= weight:
                in_truck = trucks.popleft()
                bridge_sum += in_truck
                bridge.append(in_truck)
            else:
                bridge.append(0)
        # print(t,trucks,bridge)
    answer = t
    return answer