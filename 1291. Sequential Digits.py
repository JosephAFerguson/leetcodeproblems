class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        seq = "123456789"
        for i in range(1,len(seq)):
            for j in range(len(seq)):
                val = int(seq[j:j+i])
                if val >= low and val <= high and val not in res:
                    res.append(val)
        if int(seq) >= low and int(seq) <= high:
            res.append(int(seq))
        return res
