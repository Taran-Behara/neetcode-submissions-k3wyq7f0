class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(0, len(position)):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))
        

        cars.sort(key = lambda x: x[0])
        
        i = len(cars) - 1
        stack = []
        while i >= 0:
            stack.append(cars[i])
            if len(stack) >= 2:
                first = stack[-1]
                second = stack[-2]
                if first[1] <= second[1]:
                    stack.pop()
            i -= 1
        
        return len(stack)

        

