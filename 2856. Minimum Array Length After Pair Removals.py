class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        mid = n//2
        i = n-1
        j = mid-1
        rem = 0
        while j>=0:
            if nums[i] > nums[j]:
                rem+=2
                i-=1
            j-=1
        return n-rem
            
