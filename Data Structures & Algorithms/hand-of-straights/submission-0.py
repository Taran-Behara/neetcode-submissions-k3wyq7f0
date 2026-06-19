class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}
        for num in hand:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        while count:
            group = []
            num = min(count)
            while len(group) < groupSize:
                if num not in count:
                    return False
                else:
                    group.append(num)
                    if count[num] == 1:
                        count.pop(num, None)
                    else:
                        count[num] -= 1
                num += 1

        return True

        
        
