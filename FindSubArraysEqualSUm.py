class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)-1):
            for j in range(len(nums)-1):
                if i != j:
                    if nums[i]+nums[i+1] == nums[j] + nums[j+1]:
                        return True
        return False