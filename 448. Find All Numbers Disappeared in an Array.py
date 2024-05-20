class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        h = {}
        n = len(nums)
        for i in range(1,n+1):
            h.update({i:0})
        for i in nums:
            if h.get(i,-1)!=-1:
                h[i] +=1 
        res = []
        for i in range(1,n+1):
            if h[i] == 0:
                res.append(i)
        return res
