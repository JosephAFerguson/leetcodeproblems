class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h1 = {}
        for i,val in enumerate(nums):
            h1[val] = [target - val,i]
        for i,val in enumerate(nums):
            if h1.get(target-val):  
                f = h1[target-val][1]
                if f != i:
                    return [i,f]

