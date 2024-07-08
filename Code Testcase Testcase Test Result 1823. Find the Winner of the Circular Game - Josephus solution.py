class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i = 1
        ans = 0
        while i <= n:
            ans = (ans+k)%i
            i+=1
        return ans+1
