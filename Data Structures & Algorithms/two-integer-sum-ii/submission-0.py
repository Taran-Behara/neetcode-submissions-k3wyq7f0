class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        result = []

        while left < right:
            numSum = numbers[left] + numbers[right]
            if numSum == target:
                result.append(left + 1)
                result.append(right + 1)
                return result
            elif numSum > target:
                right -= 1
            else:
                left += 1
        return result