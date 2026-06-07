class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        index = len(nums) - k

        def quickSelect(l, r):
            import random
            pivotIndex = random.randint(l, r)
            nums[r], nums[pivotIndex] = nums[pivotIndex], nums[r]
            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[r], nums[p] = nums[p], nums[r]

            if p < index:
                return quickSelect(p + 1, r)
            elif p > index:
                return quickSelect(l, p - 1)
            else:
                return nums[p]
        
        return quickSelect(0, len(nums) - 1)