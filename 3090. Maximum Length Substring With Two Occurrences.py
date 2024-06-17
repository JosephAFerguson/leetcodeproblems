class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        h = {}
        ml = 0
        maxl = 0
        i , j = 0 , 0
        while j < len(s):
            if h.get(s[j],0) == 0:
                h[s[j]] = 1
            else:
                h[s[j]]+=1
            ml+=1
            
            while h.get(s[j],0) > 2:
                h[s[i]] -=1
                ml-=1
                i+=1
            j+=1
            maxl = max(maxl, ml)
        return maxl
