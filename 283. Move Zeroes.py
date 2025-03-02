class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        indexes = []
        index = 0
        for i in nums:
            if i == 0:
                count0 +=1
                indexes.append(index)
            index += 1
        for i in range(len(indexes)):
            nums.pop(indexes[i]-i)
        for i in range(count0):
            nums.append(0)
        print(nums)
