class Solution:
    def jump(self, nums: List[int]) -> int:
        q = collections.deque()
        q.appendleft((0, 0))
        minJumps = float("inf")
        seenIndices = set()
        while q:
            top = q.popleft()
            index = top[0]
            if index == len(nums) - 1:
                return top[1]
            currJumps = top[1]
            jumpLength = nums[index]
            for i in range(1, jumpLength + 1):
                if index + i < len(nums) and index + i not in seenIndices:
                    q.append((index + i, currJumps + 1))
                    seenIndices.add(index + i)
        
        return minJumps
            