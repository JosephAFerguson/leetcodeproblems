class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        n-=1
        side = k // n
        rem = k % n

        return rem if side %2==0 else n-rem
