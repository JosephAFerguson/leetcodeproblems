class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m , n = len(spells), len(potions)
        potions = sorted(potions)
        res = []
        for i in spells:
            l,r = 0, n
            while l<r:
                mid = (l+r)//2
                if potions[mid]*i < success:
                    l = mid+1
                else:
                    r = mid
            if potions[mid]*i < success and mid == n-1:
                res.append(0)
            elif potions[mid]*i < success:
                res.append(n-mid-1)
            else:
                res.append(n-mid)
            
        return res
