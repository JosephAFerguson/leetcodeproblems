class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = [0,0]
        n = len(grid)
        find = [0]*(n*n)
        for row in grid:
            for col in row:
                if (find[col-1]):
                    res[0] = col
                else:
                    find[col-1] = 1
        for i in range(n*n):
            if find[i]==0:
                res[1] = i+1
                return res
