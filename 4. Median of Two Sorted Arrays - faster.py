class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) >len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        low,high = 0, m
        while low <= high:
            partX = (low+high)//2
            partY = (m + n +1) // 2 - partX

            maxX = float('-inf') if partX == 0 else nums1[partX-1]
            maxY = float('-inf') if partY == 0 else nums2[partY-1]
            minX =  float('inf') if partX == m else nums1[partX]
            minY = float('inf') if partY == n else nums2[partY]

            if maxX <= minY and maxY <= minX:
                if (m+n)%2==0:
                    return (max(maxX,maxY) + min(minX, minY))/2
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                high = partX - 1
            else:
                low = partX + 1
