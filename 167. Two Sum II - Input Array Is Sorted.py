class Solution:
    def binsearch(self, arr, tar, notind):
        h= len(arr)-1
        l = 0
        m = l+(h-l)//2
        while l <=h:
            m = l+(h-l)//2
            if arr[m]==tar:
                if(m!=notind):
                    return m
            if (arr[m] < tar):
                l = m+1
            else:
                h = m-1
        return -1
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            tar = target - numbers[i]
            isval = self.binsearch(numbers, tar, i)
            if isval >=0:
                return sorted([i+1, isval+1])
