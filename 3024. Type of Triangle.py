class Solution:
    def su(self,s1,s2,s3):
        return s1 + s2 > s3
    def triangleType(self, nums: List[int]) -> str:
        s1 = nums[0]
        s2 = nums[1]
        s3 = nums[2]

        sw = self.su(s1,s2,s3) and self.su(s2,s3,s1) and self.su(s3,s1,s2)
        if not sw:
            return "none"
        if s1==s2 and s2==s3:
            return "equilateral"
        elif s1==s2 or s2==s3 or s1==s3:
            return "isosceles"
        return "scalene" 
