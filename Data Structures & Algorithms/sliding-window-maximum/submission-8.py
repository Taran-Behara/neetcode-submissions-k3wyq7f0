class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = collections.deque()
        
        l = 0
        r = 0

        while l <= r and r < len(nums):
            while dq and nums[dq[len(dq) - 1]] < nums[r]:
                dq.pop()

            dq.append(r)

            if l > dq[0]:
                dq.popleft()
            
            if r - l + 1 >= k:
                res.append(nums[dq[0]])
                l += 1
            r += 1
        
        return res

            