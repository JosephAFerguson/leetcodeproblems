class Solution:
    def reverseParentheses(self, s: str) -> str:
        indices = deque()
        res = []
        for ch in s:
            if ch == '(':
                indices.append(len(res))
            elif ch == ')':
                start = indices.pop()
                res[start:] = res[start:][::-1]
            else:
                res.append(ch)
        return "".join(res)
