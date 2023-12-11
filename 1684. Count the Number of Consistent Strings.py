class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for word in words:
            switch = False
            for letter in word:
                if letter not in allowed:
                    switch = True
            if not switch:
                res+=1
        return res
        
        
