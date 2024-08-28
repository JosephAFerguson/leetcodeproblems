class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        if not grid2:
            return 0
        m,n = len(grid2), len(grid2[0])
        res = 0
        def dfs(i,j, li):
            grid2[i][j] = 2
            for ival,jval in (0,1),(0,-1),(1,0),(-1,0):
                row = i + ival
                col = j +jval
                if col >=0 and col <n and row >= 0 and row < m and grid2[row][col] == 1:
                    li.append([row,col])
                    li = dfs(row,col, li)
            return li
        def check(li):
            for l in li:
                i = l[0]
                j = l[1]
                if not grid1[i][j]:
                    return False
            return True

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    li = dfs(i,j, [[i,j]])
                    print(li)
                    if check(li):
                        res+=1
        return res
