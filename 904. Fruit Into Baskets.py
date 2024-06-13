class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)
        c = Counter()
        distinct = 0
        maxf = 0
        
        l,r = 0,0
        while r< len(fruits):
            if c[fruits[r]] == 0:
                distinct +=1
            c[fruits[r]]+=1
            
            while distinct > 2:
                c[fruits[l]]-=1
                if c[fruits[l]]==0:
                    distinct-=1
                l+=1
            maxf = max(maxf,r-l+1)
            r+=1
        return maxf
