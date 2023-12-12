class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n  = len(grid)
        rval = 0
        seen = {}
        for i,row in enumerate(grid):
            val = ''.join(str(i) + '.' for i in row)
            if seen.get(val,-1) == -1:
                seen[val] = 0
            else:
                seen[val] +=1
        j = 0
        while j < n:
            i = 0
            res = ''
            while i < n:
                res+=str(grid[i][j])+'.'
                i+=1
            val = seen.get(res,-1)
            rval += val +1
            j+=1
        return rval
