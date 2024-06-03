class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m+n
        i, j = m-1,n-1
        ind = l-1 
        while i>=0 and j >=0:
            if nums1[i] > nums2[j]:
                nums1[ind] = nums1[i]
                i-=1
                ind-=1
            elif nums1[i] < nums2[j]:
                nums1[ind] = nums2[j]
                j-=1
                ind-=1
            else:
                nums1[ind] = nums1[i]
                nums1[ind-1] = nums2[j]
                ind-=2
                i-=1
                j-=1
        while i > -1:
            nums1[ind] = nums1[i]
            ind-=1
            i-=1
        while j > -1:
            nums1[ind] = nums2[j]
            ind-=1
            j-=1

        


        
