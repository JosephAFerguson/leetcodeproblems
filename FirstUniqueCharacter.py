class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            excludeS = s[:i] + s[i+1:]
            if s[i] in excludeS:
                pass
            else:
                return i
        return -1