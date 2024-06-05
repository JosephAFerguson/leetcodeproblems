class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k,l = len(nums1),  len(nums2)
        n = k+l
        res = [0] * n
        i , j = 0,0
        ind = 0
        while i < k and j < l:
            if nums1[i] < nums2[j]:
                res[ind] = nums1[i]
                i+=1
            else:
                res[ind] = nums2[j]
                j+=1
            ind+=1
        while i < k:
            res[ind] = nums1[i]
            ind+=1
            i+=1
        while j < l:
            res[ind] = nums2[j]
            ind+=1
            j+=1
        if n%2==0:
            return (res[n//2] + res[n//2 - 1]) / 2
        return res[n//2]
