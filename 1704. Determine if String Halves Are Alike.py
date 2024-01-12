class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2
        i = 0
        j = len(s)
        res1,res2 = 0,0
        while i < j:
            if i < half:
                if s[i] in 'aeiouAEIOU':
                    res1+=1
            else:
                if s[i] in 'aeiouAEIOU':
                    res2+=1
            i+=1
        return res1==res2
