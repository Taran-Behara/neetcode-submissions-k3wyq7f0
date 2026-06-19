class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}
        for num in hand:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        minH = hand
        heapq.heapify(minH)
        while minH:
            if minH[0] not in count:
                heapq.heappop(minH)
                continue
            group = []
            num = minH[0]
            while len(group) < groupSize:
                if num not in count:
                    return False
                else:
                    group.append(num)
                    if count[num] == 1:
                        if minH[0] == num:
                            heapq.heappop(minH)
                        count.pop(num, None)
                    else:
                        count[num] -= 1
                num += 1

        return True

        
        
