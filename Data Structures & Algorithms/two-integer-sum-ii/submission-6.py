class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
 
        

        res = []
        while left < right and right < len(numbers) and left >= 0:
            currSum = numbers[left] + numbers[right]
            if currSum == target:
                res.append(left + 1)
                res.append(right + 1)
                return res
            elif currSum > target:
                right = right - 1
            else:
                left = left + 1
        
        return res