class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) <= 3:
            return 0
        op1 = nums[-1] - nums[3]
        op2 = nums[-2] - nums[2]
        op3 = nums[-3] - nums[1]
        op4 = nums[-4] - nums[0]
        return min(op1,op2,op3,op4)
