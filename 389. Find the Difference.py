class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        total1 = sum([ord(i) for i in s])
        total2 = sum([ord(i) for i in t])
        res = total2-total1
        return chr(res)
