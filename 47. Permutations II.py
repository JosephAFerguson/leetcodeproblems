class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        c = Counter(nums)
        def backTrack(currl):
            if len(currl) == n:
                res.append(currl)
                return
            for k in c:
                if c[k]:
                    c[k]-=1
                    backTrack(currl+[k])
                    c[k]+=1
        backTrack([])
        return res
