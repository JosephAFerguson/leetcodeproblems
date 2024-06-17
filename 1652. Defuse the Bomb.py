class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0]*n
        if k==0:
            return [0]* n
        if k >0:
            ind = k+1
            s = sum(code[1:k+1])
            for i in range(n):
                res[i] = s
                s-= code[(i+1) %n]
                s+= code[ind % n]
                ind+=1
        else:
            ind = n+k
            s = sum(code[ind:])
            for i in range(n):
                res[i] = s
                s-= code[(ind) % n]
                ind+=1
                s+= code[i]
        return res
