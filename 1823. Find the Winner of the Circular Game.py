class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        fries = [i+1 for i in range(n)]
        i = 0
        while len(fries)>1:
            i = (i+k-1)%len(fries)
            fries.pop(i)
        return fries[0]
