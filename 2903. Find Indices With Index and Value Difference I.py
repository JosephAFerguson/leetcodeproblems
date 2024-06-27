class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        i,j = 0,0
        n = len(nums)
        pair = [-1,-1]
        while i < n-indexDifference:
            j = i+indexDifference
            while j < n:
                if abs(nums[i] - nums[j]) >= valueDifference:
                    pair = [i,j]
                j+=1
            i+=1
        return pair
