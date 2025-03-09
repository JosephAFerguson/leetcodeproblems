class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        colors = colors+colors[:2]
        prevprev = colors[0]
        prev = colors[1]
        res = 0
        for i in range(2, len(colors)):
            if  colors[i] == prevprev and colors[i]!= prev:
                res+=1
            prevprev = prev
            prev = colors[i]
        return res
