class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pT = []
        lastList = []
        for i in range(numRows): #i+1 = width of row needed
            newList = []
            if i == 0:
                newList = [1]
            elif i==1:
                newList = [1,1]
            else:
                newList.insert(0,1)
                for j in range(1,len(lastList)):
                    susm = lastList[j] + lastList[j-1]
                    newList.insert(j,susm)
                newList.append(1)
            pT.append(newList)
            lastList = newList
        return pT
