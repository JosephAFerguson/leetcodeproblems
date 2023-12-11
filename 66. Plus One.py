class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 0
        while i < len(digits) and digits[-1-i]+1>=10:
            digits[-1-i] = (digits[-1-i] +1) % 10
            i+=1
        if i < len(digits):
            digits[-1-i] = (digits[-1-i] +1) % 10
        else:
            digits.insert(0,1)
        return digits
