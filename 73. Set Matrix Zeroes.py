class Solution:
    def recurRow(self, r,c,  change, matrix , m,n): 
        if r == -1 or c == -1 or r == m or c == n:
            return 
        if matrix[r][c] != 0:
            matrix[r][c] = "f"
        self.recurRow(r+change, c, change, matrix, m, n )
    def recurCol(self,r,c , change, matrix, m, n):
        if r == -1 or c == -1 or r == m or c == n:
            return 
        if matrix[r][c] != 0:
            matrix[r][c] = "f"
        self.recurCol(r , c + change, change, matrix, m, n )
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        flag = "f"
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    self.recurRow(i,j, 1, matrix, m,n)
                    self.recurRow(i,j,  -1, matrix, m, n)
                    self.recurCol(i,j, 1, matrix, m, n)
                    self.recurCol(i,j, -1, matrix, m, n)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == flag:
                    matrix[i][j] = 0
        
