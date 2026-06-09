class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for start in range(0, len(gas)):
            currGas = 0
            ind = start
            while True:
                print(ind)
                print(currGas)
                print()
                if currGas + gas[ind] - cost[ind] < 0:
                    break
                else:
                    currGas += gas[ind] - cost[ind]
                
                if ((ind + 1) % len(gas)) == start:
                    return start
                
                ind = (ind + 1) % len(gas)
        return -1

