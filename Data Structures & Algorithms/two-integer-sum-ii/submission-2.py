class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        res = []
        while l < r:
            if numbers[l] + numbers[r] == target:
                res.append(l + 1)
                res.append(r + 1)
                return res
            elif numbers[l] + numbers[r] > target:
                r = r - 1
            else:
                l = l + 1
        return res