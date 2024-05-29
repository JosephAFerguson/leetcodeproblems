class Solution:
    def add1(self, s, l):
        num = l-1
        res = ""
        while num > 0 and s[num] == "1":
            res += "0"
            num -=1
        if num > 0 :
            res = s[:num] + "1" + res
        else:
            res = "1" + res + "0"
        return res
    def numSteps(self, s: str) -> int:
        res = 0
        while s != "1":
            if s[-1] == '1':#odd
                s = self.add1(s, len(s))
            else:#even
                s = s[:-1]
            res +=1
        
        return res
