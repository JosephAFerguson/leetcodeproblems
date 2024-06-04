class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        curr = 0
        lines = 1
        for i in s:
            w  = widths[ord(i) - 97]
            if w+curr > 100:
                lines +=1
                curr = w
            else:
                curr += w
        return [lines,curr]
