class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = []
        word = ""
        finalword =""
        for i in range(len(title)):
            if title[i] != " ":
                word += title[i]
            else:
                word = word.lower()
                words.append(word)
                word = ''
        word = word.lower()
        words.append(word)
        for i in words:
            firstletter = ""
            newword = ""
            if len(i) > 2:
                firstletter += i[0]
                firstletter = firstletter.upper()
                newword = i[1:]
                finalword += firstletter + newword + " "
            else:
                finalword += i + " "
        finalword  = finalword[:-1]
        return finalword