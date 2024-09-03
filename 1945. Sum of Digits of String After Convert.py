class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def getPos(ch):
            return ord(ch) - 96
        li = []
        for i in s:
            r = str(getPos(i))
            for l in r:
                li.append(int(l))
        
        li = [sum(li)]
        def s(l):
            res = 0
            for i in l:
                res+=int(i)
            return res

        while k > 1:
            r = li[0]
            li = [i for i in str(r)]
            li = [s(li)]
            k-=1
        return li[0]
