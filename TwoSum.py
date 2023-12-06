class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i,val in enumerate(nums):
            h[val] = i
        for i,val in enumerate(nums):
            if h.get(target- val,-99)!=-99 and h.get(target- val,-99)!=i :
                return [i,h[target- val]]
