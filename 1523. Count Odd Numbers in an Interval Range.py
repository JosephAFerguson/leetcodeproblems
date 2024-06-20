class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ran = high-low+1
        if ran % 2 == 0 :
            return int(ran /2)
        else:
            if high % 2== 0:
                return ran//2
            else:
                return ran//2+1
