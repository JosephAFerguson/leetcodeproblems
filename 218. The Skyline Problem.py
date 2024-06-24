class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        l = len(buildings)
        if l==0:
            return []
        res = []
        buildings.sort(key = lambda x: x[2])
        pos, height = [0], [0]
        for l,r, h in buildings:
            i = bisect_left(pos,l)
            j = bisect_right(pos,r)
            height[i:j] = [h, height[j-1]]
            pos[i:j] = [l,r]
        prev = 0
        for v,h in zip(pos,height):
            if h!=prev:
                res.append([v,h])
                prev = h
        return res
