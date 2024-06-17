class Solution:
    def squareSum(self, i , j):
        return i**2+j**2
    def judgeSquareSum(self, c: int) -> bool:
        i , j = 0, int(sqrt(c))
        if c <=1:
            return True
        while i <= j:
            val = self.squareSum(i,j)
            if val > c:
                j -=1
            elif val < c:
                i+=1
            else:
                return True
        return False
