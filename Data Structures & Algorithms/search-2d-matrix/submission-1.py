class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = (len(matrix) * len(matrix[0])) - 1

        while l <= r:
            check = (l + r) // 2
            rowInd = check // len(matrix[0])
            colInd = check % len(matrix[0])

            curr = matrix[rowInd][colInd]
            if curr == target:
                return True
            elif curr > target:
                r = check - 1
            else:
                l = check + 1
        return False