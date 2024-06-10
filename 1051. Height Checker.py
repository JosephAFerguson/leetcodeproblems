class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sh = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != sh[i]:
                res+=1
        return res
