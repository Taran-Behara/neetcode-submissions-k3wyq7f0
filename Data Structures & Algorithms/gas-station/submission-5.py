class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        while start < len(gas):
            #print(start)
            currGas = 0
            ind = start
            while True:
                if currGas + gas[ind] - cost[ind] < 0:
                    break
                currGas += gas[ind] - cost[ind]
                
                if ((ind + 1) % len(gas)) == start:
                    return start
                
                ind = (ind + 1) % len(gas)
            if ind < start:
                return -1
            start = ind + 1
        return -1

