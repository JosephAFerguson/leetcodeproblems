class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        z = zip(names,heights)
        res = sorted(z, key = lambda x:x[1], reverse = True)
        return [i[0] for i in res]
