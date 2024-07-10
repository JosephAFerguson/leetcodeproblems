class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for i in logs:
            if i =='../':
                depth= max(depth-1,0)
            elif i =='./':
                continue
            else:
                depth+=1
        return depth
