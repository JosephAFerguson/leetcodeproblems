class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        res = 0
        switch = False
        for i in c.values():
            if i %2==0:
                res += i
            else:
                switch = True
                res +=i-1
        if switch:
            res+=1
        return res 
