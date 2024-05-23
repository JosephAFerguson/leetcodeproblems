import heapq
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        res = []
        while nums:
            ele1 = heapq.heappop(nums)
            if nums:
                ele2 = heapq.heappop(nums)
                res.append(ele2)
            res.append(ele1)
        return res
