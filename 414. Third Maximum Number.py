class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        n = len(nums)
        if n < 3:
            return max(nums)
        return sorted(nums)[-3]
