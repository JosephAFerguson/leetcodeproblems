class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        words = []
        word = ""
        thirds = []
        for i in text:
            if i != " ":
                word += i
            else:
                words.append(word)
                word = ""
        words.append(word)
        for i in range(0,len(words)-2):
            if words[i] == first and words[i+1] == second:
                thirds.append(words[i+2])
        return thirds