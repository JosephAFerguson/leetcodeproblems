class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        lastamo = 0
        curramo = 0
        frow = False
        for i,row in enumerate(bank):
            for j, col in enumerate(row):
                if not frow:
                    if col == "1":
                        lastamo +=1
                else:
                    if col == "1":
                        curramo +=1
            if not frow and lastamo>0:
                frow = True
                
            if curramo != 0:
                res += curramo * lastamo
                lastamo = curramo
                curramo = 0
        return res
