class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(t)
        l = len(s)
        i , j = 0,0
        while i<l and j< n:
            if s[i] == t[j]:
                j +=1
                i +=1
            else:
                i+=1
        return  n -j
