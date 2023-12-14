class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows1,rows0 = [],[]
        cols1, cols0 = [],[]
        n, m = len(grid), len(grid[0])
        for row in grid:
            nrow = 0
            for col in row:
                nrow+=col
            rows1.append(nrow)
            rows0.append(n-nrow)
        
        i , j = 0,0
        while j<m:
            i = 0
            ncol = 0
            while i < n:
                ncol+=grid[i][j]
                i+=1
            cols1.append(ncol)
            cols0.append(m-ncol)
            j+=1
        res = []
        for k,row in enumerate(grid):
            resrow = []
            for l,col in enumerate(row):
                resrow.append(rows1[k]+cols1[l]-rows0[k]-cols0[l])
            res.append(resrow)
        return res
