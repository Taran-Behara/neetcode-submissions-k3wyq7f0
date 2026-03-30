class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        first = []
        second = []

        if len(nums1) < len(nums2):
            first = nums1
            second = nums2
        else:
            first = nums2
            second = nums1
        
        l = 0
        r = len(first) - 1
        while True:
            mid = (l + r)//2
            j = half - mid - 2

            fLeft = first[mid] if mid >= 0 else float("-infinity")
            fRight = first[mid + 1] if (mid + 1) < len(first) else float("infinity")
            sLeft = second[j] if j >= 0 else float("-infinity")
            sRight = second[j + 1] if (j + 1) < len(second) else float("infinity")

            if fLeft <= sRight and sLeft <= fRight:
                if total % 2 == 0:
                    return (max(fLeft, sLeft) + min(fRight, sRight))/2
                return min(fRight, sRight)
            elif fLeft > sRight:
                r = mid - 1
            else:
                l = mid + 1