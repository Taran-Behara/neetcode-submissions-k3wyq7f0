class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            A, B = nums1, nums2
            total = len(A) + len(B)
            half = total // 2

            if len(B) < len(A):
                A, B = B, A
            

            l = 0
            r = len(A) - 1

            while True:
                mid = (l + r) // 2
                ALeft = A[mid] if mid >= 0 else float("-infinity")
                ARight = A[mid + 1] if mid + 1 < len(A) else float("infinity")
                BLeft = B[half - (mid + 1) - 1] if half - (mid + 1) - 1 >= 0 else float("-infinity")
                BRight = B[half - (mid + 1)] if half - (mid + 1) < len(B) else float("infinity")

                if ALeft <= BRight and BLeft <= ARight:
                    if total % 2 == 0:
                        return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
                    
                    return min(ARight, BRight)
                elif ALeft > BRight:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return -1
