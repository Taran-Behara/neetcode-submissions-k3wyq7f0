class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        oldFast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        newSlow = 0
        while True:
            slow = nums[slow]
            newSlow = nums[newSlow]

            if slow == newSlow:
                return slow
            
        
        return -1