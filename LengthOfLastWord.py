class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = []
        newWord= ''
        for i in s:
            if i != ' ':
                newWord += i
            else:
                words.append(newWord)
                newWord = ''
        words.append(newWord)
        for i in range(len(words), 0, -1):
            if len(words[i-1]) != 0:
                return(len(words[i-1]))