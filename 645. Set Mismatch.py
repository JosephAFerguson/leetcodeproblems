class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0,0]
        length = len(nums)
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                res[0] = nums[i]
        nums = sorted(list(set(nums)))
        val = length
        for i in range(1,length+1):
            if i-1 < len(nums):
                if nums[i-1] != i:
                    res[1] = i
                    return res
            else:
                res[1] = i
                return res
