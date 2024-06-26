class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        h = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6" : "mno", "7" : "pqrs", "8":"tuv", "9":"wxyz"}
        res = []

        def bt(currs,nextd):
            if not nextd:
                res.append(currs)
                return
            for let in h[nextd[0]]:
                bt(currs+let, nextd[1:])
        
        bt("", digits)
        return res
