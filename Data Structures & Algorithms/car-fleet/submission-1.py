class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        carToSpeed = {}
        for i in range(0, len(position)):
            carToSpeed[position[i]] = speed[i]

        pos = position.copy()
        pos.sort()
        i = len(pos) - 1
        while i >= 0:
            currCar = pos[i]
            currSpeed = carToSpeed[pos[i]]

            if not stack:
                stack.append(currCar)
            else:
                top = stack[len(stack) - 1]
                topDestTime = (target - top) / carToSpeed[top]

                currDestTime = (target - currCar) / currSpeed

                if currDestTime > topDestTime:
                    stack.append(currCar)
            i -= 1
        
        return len(stack)

        