class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backTrack(currl, digs):
            if len(currl) == n:
                res.append(currl)
                return
            for i,d in enumerate(digs):
                backTrack(currl+ [d], digs[:i] + digs[i+1:])
        backTrack([],nums)
        return res
