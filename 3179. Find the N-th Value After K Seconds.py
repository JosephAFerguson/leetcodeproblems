class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        m = 10**9 +7
        l = [1]*n
        while k >0:
            newl = [1]
            num = 1
            for i in range(1,n):
                val = num+l[i]
                newl.append(val)
                num += l[i]
            l = newl
            k-=1
        return l[-1]%m
