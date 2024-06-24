class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        i = 0
        fl = [0]*n
        flips = 0
        while i < n:
            flips+= fl[i]
            num = nums[i]^1 if flips%2 else nums[i]
            nums[i] = num

            if num == 0:
                if i +k > n:
                    return -1
                nums[i] ^= 1
                if i +k < n:
                    fl[i+k]-=1
                flips+=1
                res+=1
    
            i+=1

        return res
