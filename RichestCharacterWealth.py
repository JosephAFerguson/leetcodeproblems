class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richestcharacter = 0
        for i in accounts:
            riches = 0
            for j in i:
                riches += j
            if riches > richestcharacter:
                richestcharacter = riches
        return(richestcharacter)