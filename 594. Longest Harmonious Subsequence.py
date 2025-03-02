class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
            Notes: just sort and determine longest it goes with a max min being 1
        """
        nums.sort()
        n = len(nums)
        if n==1 or len(set(nums))==1:
            return 0
        res = 0
        i = 1
        j = 0
        while i < n:
            if nums[i]-nums[j] ==1:
                res = max(res, i-j+1)
                i+=1
            elif nums[i]-nums[j] < 1:
                i+=1
            else:
                j +=1
        return res
