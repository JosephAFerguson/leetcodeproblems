class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        h = {}
        for i in range(len(words[0])):
            h[words[0][i]] = 0
        for i in range(len(words[0])):
            h[words[0][i]] +=1
            
        for i in words:
            c = Counter(i)
            for j in h.keys():
                if j not in c:
                    h[j] = 0
                elif h[j] > c[j]:
                    h[j] = c[j]
        
        res = []
        for i in h.keys():
            if h[i] > 0:
                for j in range(h[i]):
                    res.append(i)
        return res
