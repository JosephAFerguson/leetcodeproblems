class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        news = ""
        for i in s:
            if i >= "A" and i<="Z":
                news += lower(i)
            elif (i >="a" and i<="z")or(i>= "0" and i <="9"):
                news += i
        l = 0
        r = len(news)-1
        while l < r:
            if news[l] != news[r]:
                return False
            l +=1
            r -=1
        return True
