class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        """
        Notes: ID's are distinct, if an ID appears in both arrays its value is the sum of those values
               If the ID does not exist in both but only one, its value is assumed to be 0 in the array it does not exist in, 
                    so the value of the array it does exist in

        """
        res =[]
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            id1 = nums1[i][0]
            id2 = nums2[j][0]
            if id1 == id2:
                res.append([id1, nums1[i][1] + nums2[j][1]])
                i+=1
                j+=1
            elif id1 < id2:
                res.append([id1, nums1[i][1]])
                i+=1
            else:
                res.append([id2, nums2[j][1]])
                j+=1
        #add the rest of the leftover ids from the longer array
        while i < len(nums1):
            res.append([nums1[i][0], nums1[i][1]])
            i+=1
        while j < len(nums2):
            res.append([nums2[j][0], nums2[j][1]])
            j+=1
        return res
