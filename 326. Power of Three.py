class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        def rec(num):
            res = 3 * num
            if res == n:
                return True
            elif res > n:
                return False
            else:
                return rec(res)
        return rec(1)
