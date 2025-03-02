class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanVals = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        val = 0
        switch = 0
        for i in range(len(s)):
            if i != len(s) - 1:
                if s[i] == 'I' and s[i+1] == 'V':
                    val += 4
                    switch =2
                elif s[i] == 'I' and s[i+1] == 'X':
                    val += 9
                    switch =2
                elif s[i] == 'X' and s[i+1] == 'L':
                    val += 40
                    switch =2
                elif s[i] == 'X' and s[i+1] == 'C':
                    val += 90
                    switch =2
                elif s[i] == 'C' and s[i+1] == 'D':
                    val += 400
                    switch =2
                elif s[i] == 'C' and s[i+1] == 'M':
                    val += 900
                    switch =2
            if switch == 0:
                val += romanVals[s[i]]
            else:
                switch -= 1
        return val
            
