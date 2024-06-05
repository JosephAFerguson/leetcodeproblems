class Solution:
    def minimumChairs(self, s: str) -> int:
        st = 0
        maxl = 0
        for i in s:
            if i == "E":
                st +=1
            else:
                st -=1
            maxl = max(maxl, st)
        return maxl
