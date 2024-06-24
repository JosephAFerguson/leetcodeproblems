class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i, n = 0 , len(nums)
        ml = 0
        currml = 0
        while i < n:
            currml = 0
            while i < n and  nums[i]:
                currml+=1
                i+=1
            ml = max(ml,currml )
            i+=1
        return ml
