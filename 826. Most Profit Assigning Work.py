class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        l = len(profit)
        n = len(worker)

        z = zip(profit, difficulty)
        sorts = sorted(z, key = lambda x: x[1])
        difficulty = [i[1] for i in sorts]
        profit = [i[0] for i in sorts]

        worker.sort()
        res = 0
        i = 0
        j = 0
        maxp = 0
        while i < n:
            while j < l and worker[i] >= difficulty[j]:
                maxp = max(maxp, profit[j])
                j+=1
            if j-1 >= 0:
                res+= maxp
            i+=1
        return res
