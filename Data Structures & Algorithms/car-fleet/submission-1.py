class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_stack = []
        for p, s in zip(position, speed):
            car_stack.append((p, s))
        
        car_stack.sort(reverse=True)

        time = []
        for (p, s) in car_stack:
            time.append((target-p)/s)

        fleet_stack = []
        for t in time:
            if not fleet_stack:
                fleet_stack.append(t)
                continue
            
            if fleet_stack[-1] >= t:
                continue
            else:
                fleet_stack.append(t)
        
        return len(fleet_stack)