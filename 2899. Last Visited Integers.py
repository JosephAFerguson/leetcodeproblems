class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        k = 0
        for i,val in enumerate(nums):
            if val >0:
                k = 0
                seen.insert(0,val)
            else:
                k+=1
                if k <= len(seen):
                    ans.append(seen[k-1])
                else:
                    ans.append(-1)
        return ans
