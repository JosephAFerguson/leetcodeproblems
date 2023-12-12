class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        stack = [0,0]
        for num in nums:
            if num > stack[-1]:
                stack[-2] = stack[-1]
                stack[-1] = num
            elif num > stack[-2]:
                stack[-2] = num
        return (stack[-1]-1)*(stack[-2]-1)
