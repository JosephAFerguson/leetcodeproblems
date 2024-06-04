class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n,m = len(mat), len(mat[0])
        if (m*n)!=r*c:
            return mat
        newm = []
        fr, fc = 0,0
        row, col = 0,0
        while fr < r:
            fc = 0
            newr = []
            while fc< c:
                if col >= m:
                    row+=1
                    col = 0
                val = mat[row][col]
                newr.append(val)
                col+=1
                fc+=1
            newm.append(newr)
            fr+=1
        return newm
