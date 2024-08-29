class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row = defaultdict(list)
        col = defaultdict(list)
        points = {(i,j) for i,j in stones}

        def remove(i,j):
            points.discard((i,j))
            for l in row[i]:
                if (i,l) in points:
                    remove(i,l)

            for k in col[j]:
                if (k,j) in points:
                    remove(k,j)

        for i,j in stones:
            row[i].append(j)
            col[j].append(i)
        res = 0
        for i,j in stones:
            if(i,j) in points:
                remove(i,j)
                res+=1

        return len(stones)-res
