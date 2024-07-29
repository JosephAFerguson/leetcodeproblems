class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for i,val in enumerate(rating):
            ll,lg,rl,rg = 0,0,0,0
            for l in rating[:i]:
                if l < val:
                    ll+=1
                if l > val:
                    lg+=1
            for r in rating[i+1:]:
                if r< val:
                    rl+=1
                if r > val:
                    rg+=1
            res+= ll*rg + rl*lg
        return res
