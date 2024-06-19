class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def f(bD, days, m,k):
            bqs, fls = 0, 0
            for b in bD:
                if b > days:
                    fls = 0
                else:
                    bqs+= (fls + 1)//k
                    fls= (fls+1)%k
            return bqs >=m
        if len(bloomDay) < m*k:
            return -1
        l, r = 1, max(bloomDay)
        while l < r:
            mid = l + (r-l) // 2
            if f(bloomDay, mid, m,k):
                r = mid
            else:
                l = mid +1
        return l
