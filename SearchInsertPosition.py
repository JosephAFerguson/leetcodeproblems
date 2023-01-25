class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                if nums[i] > target and nums[i-1] <= target:
                    index = i
        if index == 0 and nums[0] < target:
            return (len(nums))
        return index