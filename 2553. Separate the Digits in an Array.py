class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(i) for i in ("".join(str(i) for i in nums))]
