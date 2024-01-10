class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)[::-1]
        s = sorted(s)[::-1]
        res = 0
        while g and s:
            if g[0] <= s[0]:
                res+=1
                g.pop(0)
                s.pop(0)
            else:
                g.pop(0)
        return res
