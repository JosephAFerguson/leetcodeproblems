class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        i, n = 1, len(nums)
        while i < n:
            prev = nums[i-1]
            if(nums[i] <= prev):
                res+= 1+prev-nums[i]
                nums[i] = prev+1
            i+=1
        return res
