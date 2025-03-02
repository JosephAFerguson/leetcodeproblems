class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            exclude = nums[:i] + nums[i+1:]
            if nums[i] not in exclude:
                return nums[i]
