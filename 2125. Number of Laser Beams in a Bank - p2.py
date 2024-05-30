class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        sentries = []
        curr = 0
        for i in range(len(bank)):
            for j in range(len(bank[0])):
                if bank[i][j] == "1":
                    curr += 1
            if curr != 0:
                sentries.append(curr)
                curr = 0
        for i in range(1,len(sentries)):
            res += sentries[i] * sentries[i-1]
        return res
