class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        h = {}
        wL = len(words[0])
        n = wL * len(words)
        ind = n
        res = []
        while ind <= len(s):
            check = s[ind-n:ind]

            h = {}
            for i in words:
                h[i] = 0
            for i in words:
                h[i] += 1

            i = 0
            sw =True
            while i < n:
                sub = check[i:i+wL]
                if h.get(sub):
                    if h[sub] !=0:
                        h[sub] -= 1
                    else:
                        sw = False
                        break
                else:
                    sw = False
                    break
                i+=wL
            if sw:
                res.append(ind-n)
            ind+=1
        return res
