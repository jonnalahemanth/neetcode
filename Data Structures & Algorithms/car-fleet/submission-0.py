class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [(p, (target-p)/s) for p,s in zip(position, speed)]

        cars.sort(reverse=True)
        # stack = []
        # for p, time in cars:
        #     if not stack or time>stack[-1]:
        #         stack.append(time)
        
        # return len(stack)
        fleets = 0
        max_time = 0

        for p, time in cars:
            if time > max_time:
                fleets += 1
                max_time = time
        return fleets