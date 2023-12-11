class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        h = Counter(arr)
        vals = list(h.values())
        keys = list(h.keys())
        mostfreq = vals.index(max(vals))
        return keys[mostfreq]
