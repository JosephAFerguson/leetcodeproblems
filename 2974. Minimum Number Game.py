class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        b = 0
        a = 0
        n = len(nums)
        res = []
        while n > 0:
            a = min(nums)
            nums.remove(a) 
            if len(nums)>0:
                b = min(nums)
                nums.remove(b)
                res.append(b)
            res.append(a)
            n = len(nums)
        return res
