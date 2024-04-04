class Solution:
    def getN(self, mat, i, j, m, n):
        res = 0
        if i > 0:
            res += mat[i-1][j]
            if j > 0:
                res += mat[i-1][j-1]
            if j < n - 1:
                res += mat[i-1][j+1]
        if i < m - 1:
            res += mat[i+1][j]
            if j > 0:
                res += mat[i+1][j-1]
            if j < n - 1:
                res += mat[i+1][j+1]
        if j > 0:
            res += mat[i][j-1]
        if j < n - 1:
            res += mat[i][j+1]
        return res

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board), len(board[0])
        if m == 1 and n==1:
            if board[0][0] == 0:
                return
            else:
                board[0][0] = 0
                return
        copycat = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                copycat[i][j] = self.getN(board,i,j,m,n)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    if copycat[i][j] > 3 or copycat[i][j] < 2 :
                        board[i][j] = 0
                else:
                    if copycat[i][j] == 3:
                        board[i][j] = 1

        
