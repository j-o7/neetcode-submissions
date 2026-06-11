class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_stack = [(p, s) for p, s in zip(position, speed)]
        car_stack.sort(reverse=True)

        fleets = 1
        prev_time = (target - car_stack[0][0]) / car_stack[0][1]

        for i in range(1, len(car_stack)):
            cur_time = (target - car_stack[i][0]) / car_stack[i][1]
            if cur_time > prev_time:
                fleets += 1
                prev_time = cur_time

        return fleets

        # fleet_stack = []
        # for t in time:
        #     if not fleet_stack:
        #         fleet_stack.append(t)
        #         continue
            
        #     if fleet_stack[-1] >= t:
        #         continue
        #     else:
        #         fleet_stack.append(t)
        
        # return len(fleet_stack)