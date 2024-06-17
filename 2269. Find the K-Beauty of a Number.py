class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        def isBeaut(n):
            v = int(n)
            if v==0:
                return False
            return num % v == 0
        res = 0
        n = len(str(num))
        i , j = 0, k
        while j <= n:
            subs = str(num)[i:j]
            if(isBeaut(subs)):
                res +=1
            i+=1
            j+=1
        return res
