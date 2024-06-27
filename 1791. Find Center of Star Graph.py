class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        h = [0]*(len(edges)+1)
        for edge in edges:
            h[edge[0]-1]+=1
            h[edge[1]-1]+=1
        maxv = 0
        maxind = 0
        for i,val in enumerate(h):
            if val > maxv:
                maxv = val
                maxind = i
        return maxind+1
