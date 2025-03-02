class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digits = []
        for i in str(n):
            digits.append(int(i))
        num = 0
        not1 =0
        while num !=1:
            sums = 0
            for i in digits:
                sums += i**2
            if sums == 1:
                return True
            else:
                not1 += 1
            if not1 >=100:
                return False
            digits = []
            for i in str(sums):
                digits.append(int(i))
