class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        biggest = len(nums)+1
        for i in range(biggest-1):
            if nums[i] < 1 or nums[i] > biggest-1: #all numbers outside bounds are disregarded and will return last-case
                nums[i] = biggest

        for i in range(biggest-1):
            val = abs(nums[i])
            if val > biggest-1: #bigger than what we care about, disregard
                continue
            val-=1
            if nums[val] > 0:
                nums[val] = -1*nums[val]

        for i in range(biggest-1):
            if nums[i] >=0:
                return (i+1)
        return biggest

        return biggest

