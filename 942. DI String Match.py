class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        res = [0] * (n+1)
        j = 0
        big = n
        small = 0
        while j < n:
            if s[j] == "D":
                res[j] = big
                big -=1
            else:
                res[j] = small
                small +=1
            j+=1
        res[j] =(small)
        return res


