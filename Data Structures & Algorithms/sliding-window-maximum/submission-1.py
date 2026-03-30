class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        res = []
        de = collections.deque()

        while l <= r and r < len(nums):
            while de and nums[de[-1]] < nums[r]:
                de.pop()
            de.append(r)

            winSize = r - l + 1
            if winSize == k:
                res.append(nums[de[0]])
                l = l + 1
                if l > de[0]:
                    de.popleft()
            r = r + 1
        return res
