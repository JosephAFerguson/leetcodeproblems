class Solution:
    def countTestedDevices(self, bP: List[int]) -> int:
        res = 0
        for i,val in enumerate(bP):
            if val-res > 0:
                res+=1
        return res
