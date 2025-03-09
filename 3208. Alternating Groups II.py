class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors += colors[:k-1] #append end to account for additional k-1 elements at end of the circle
        left= 0
        right = 1
        res = 0
        while right < len(colors):
            if (colors[right]==colors[right-1]):
                left = right
            if right-left+1>=k:
                res+=1
            right+=1
        return res
