class Solution:
    def customSortString(self, order: str, s: str) -> str:
        nots = ""
        for i in s:
            if i not in order:
                nots+=i
        h = Counter(s)
        res = ""
        for i in order:
            while h.get(i,0) >0:
                res += i
                h[i]-=1
        return res + nots
