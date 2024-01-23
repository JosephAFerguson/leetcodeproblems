class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [i for i in range(n+1)]
        def count(val):
            if val == 0:
                return 0
            num = 1
            while val//2 !=0:
                if val % 2 != 0:
                    num+=1
                val //= 2
            return num
        for i,val in enumerate(res):
            res[i] = count(val)
        return res
