class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        if n<3:
            return False
        j = 2
        while j < n:
            if arr[j]%2!=0 and arr[j-1]%2!=0 and arr[j-2]%2!=0:
                return True
            j+=1
        return False
