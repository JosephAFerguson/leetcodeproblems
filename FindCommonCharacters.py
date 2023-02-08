class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        letters = []
        wordsnew = []
        for word in words:
            newlist = []
            for letter in word:
                newlist.append(letter)
            wordsnew.append(newlist)
        for letter in range(len(words[0])):
            corr = 0
            for word in range(1, len(words)):
                if words[0][letter] in words[word] and words[0][letter] in wordsnew[word]:
                    corr += 1
                    wordsnew[word].remove(words[0][letter])
            if corr == len(words) -1:
                letters.append(words[0][letter])
        return letters