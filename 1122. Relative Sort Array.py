class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        h = Counter(arr1)
        h2 = Counter(arr2)
        res = []
        nots = []
        for i in arr1:
            if h2.get(i,-1)==-1:
                nots.append(i)
        for i in arr2:
            while h[i] > 0:
                res.append(i)
                h[i] -=1
        

        return res + sorted(nots)
