class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h1 = Counter(nums1)
        h2 = Counter(nums2)
        
        res = []
        for i in h1:
            if h2.get(i,-1) !=-1:
                res+= [i]*min(h1[i], h2[i])
        return res
