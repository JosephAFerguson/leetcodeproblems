class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        smallestIndex = 101
        firstLetter = ''
        for i in range(len(s)):
            for k in range(len(s)):
                if k>i and s[i] == s[k]:
                    if k < smallestIndex:
                        firstLetter = s[i]
                        smallestIndex = k
        return firstLetter
