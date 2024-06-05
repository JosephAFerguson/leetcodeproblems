class Solution:
    def isEven(self, num):
        return num %2==0
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1,len(nums)):
            if self.isEven(nums[i]) == self.isEven(nums[i-1]):
                return False
        return True
