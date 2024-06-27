class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        h1 = Counter(nums1)
        h2 = Counter(nums2)

        n = len(nums1)
        n2 = n/2

        #use as many removals on duplicates as we can
        for i in h1:
            if h1[i] > 1:
                n2-= h1[i]-1
                h1[i] -= h1[i]-1
        
        n3 = n/2

        for i in h2:
            if h2[i] > 1:
                n3-= h2[i]-1
                h2[i] -= h2[i]-1
        
        if n2<0:
            n2 = 0
        if n3<0:
            n3= 0
        
        #see if we need to remove any more
        left = n2 + n3
        if left >0:
            #we need to remove more, so remove the duplicates of the combined lists
            rem = Counter(list(h1.keys())+list(h2.keys()))
            for i in rem:
                if rem[i] > 1:
                    left -= rem[i]-1
                    rem[i] -= rem[i]-1
            retn = len(list(rem.keys()))
            return retn if left <=0 else int(retn - left) #if more is needed use the rest of the removes on the unique elements
                
        else:
            #no removals needed so find the length of the combined lists's set
            return len(set(list(h1.keys()) + list(h2.keys())))
