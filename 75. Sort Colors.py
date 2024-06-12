class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        l = len(nums)
        j = l-1
        #swap ends where 2's are in the wrong spot
        while i < j:
            #2's are in the right spot, move on
            while j > 0  and nums[j] ==2:
                j-=1
            if nums[i] == 2 and i<j:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                j-=1
            i+=1
        #while things are in the right spot, move on
        while j>0 and nums[j]==2:
            j-=1
        while j>0 and nums[j] ==1:
            j-=1
        #swap ends where 1's are in the wrong spot
        i = 0
        while i < j:
            #1's are in the right spot, move on
            while j > 0  and nums[j] ==1:
                j-=1
            if nums[i] == 1 and i <j:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                j-=1
            i+=1
        
