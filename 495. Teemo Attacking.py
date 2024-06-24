class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        i, n = 1 , len(timeSeries)
        if n ==1:
            return duration
        while i < n:
            if (timeSeries[i]-timeSeries[i-1]) > duration:
                res+=duration
                i+=1
            else: 
                while i<n and (timeSeries[i]-timeSeries[i-1]) <= duration:
                    res+= timeSeries[i]-timeSeries[i-1]
                    i+=1
        
        return res+duration
