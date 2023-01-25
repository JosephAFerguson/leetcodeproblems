class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        stringNum = ''
        newDigits = []
        for i in digits:
            stringNum += str(i)
        number = int(stringNum)
        number += 1
        for i in str(number):
            newDigits.append(int(i))
        return newDigits