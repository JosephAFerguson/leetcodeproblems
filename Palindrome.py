class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = 1
        success = True
        for i in str(x):
            if i == str(x)[len(str(x))-n]:
                pass
            else:
                return False
            n +=1
        return success