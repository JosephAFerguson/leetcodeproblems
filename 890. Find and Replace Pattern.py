class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        h = {}
        num = 0
        patt =""
        for i in pattern:
            if i not in h:
                h[i] = num
                num+=1
        for i in pattern:
            patt+=str(h[i]) + "."
        res = []
        for word in words:
            h = {}
            num = 0
            for i in word:
                if i not in h:
                    h[i] = num
                    num+=1
            mat = ""
            for i in word:
                mat+=str(h[i]) + "."
            if mat==patt:
                res.append(word)
        return res
