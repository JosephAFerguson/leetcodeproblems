class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l , r = 0, len(s)-1
        s = [i for i in s]
        while l < r:
            if s[l] > s[r]:
                s[l] = s[r]
            else:
                s[r] = s[l]
            r-=1
            l+=1
        return "".join(s)
