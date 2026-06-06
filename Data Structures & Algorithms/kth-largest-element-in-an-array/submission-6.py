class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        index = len(nums) - k

        def quickSelect(l, r):
            pivot_idx = random.randint(l, r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]

            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            nums[r], nums[p] = nums[p], nums[r]
            if p > index:
                return quickSelect(l, p - 1)
            elif p < index:
                return quickSelect(p + 1, r)
            else:
                return nums[p]
        return quickSelect(0, len(nums) - 1)