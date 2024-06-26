class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        h = Counter()
        for i in words:
            h["".join(sorted(i))] +=1
        print(h)
        res = 0
        for i in h.values():
            res+= i//2
        return res
