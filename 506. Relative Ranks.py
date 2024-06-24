class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        par = [i for i in range(n)]
        z = zip(par, score)
        sor = sorted(z, key = lambda x:x[1], reverse = True)
        res = [""]*n
        count = 1
        for ob in sor:
            if count == 1:
                res[ob[0]] = "Gold Medal"
            elif count == 2:
                res[ob[0]] = "Silver Medal"
            elif count == 3:
                res[ob[0]] = "Bronze Medal"
            else:
                res[ob[0]] = str(count)
            count+=1
        return res
