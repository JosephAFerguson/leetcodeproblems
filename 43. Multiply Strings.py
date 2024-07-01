class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        num1l = []
        num2l = []
        for i in num1:
            num1l.append(ord(i)-48)
        for i in num2:
            num2l.append(ord(i)-48)
        n1 = len(num1)
        n2 = len(num2)
        first = 0
        second = 0
        for i in range(n1):
            first += (10**i) * num1l[-i-1]
        for i in range(n2):
            second += (10**i) * num2l[-i-1]
        resnum = first*second
        res = ""
        while resnum :
            res = chr(resnum%10+48) + res
            resnum//=10
        return res
