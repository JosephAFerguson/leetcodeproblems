class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
    
        for val in num:
            while stack and k>0 and stack[-1]>val:
                stack.pop()
                k-=1
            stack.append(val)

        if k>0:
            stack = stack[:-k]
        
        res = "".join(stack).lstrip("0")
        return res if res else "0"
