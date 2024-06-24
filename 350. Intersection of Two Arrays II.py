class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        i , j = 0 ,0 
        n ,l  = len(nums1), len(nums2)
        while i < n and j<l:
            if nums1[i]==nums2[j]:
                res.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return res
