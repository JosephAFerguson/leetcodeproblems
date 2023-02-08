class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n==2:
            return True
        if n==0:
            return False
        k = float(n)
        while k!=0:
            k = k / 2
            if k == 2:
                return True
            if (k % 2)!=0:
                return False
        return True