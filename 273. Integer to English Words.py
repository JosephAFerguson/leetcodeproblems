class Solution:
    keyword = {1:'One', 2: 'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six',7:'Seven', 8:'Eight', 9:'Nine', 10: 'Ten',
    11: 'Eleven', 12: 'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen',
     17:'Seventeen', 18:'Eighteen', 19:'Nineteen', 20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty'
     , 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety'}
    def helper(self,num):
        #num should be ###
        res = ""
        if num // 100:
            res+= " " + self.keyword[num//100] + " Hundred"
        num -= num//100*100
        if num > 10:
            if num>=10 and num <20:
                res+=  " " + self.keyword[num] 
            else:
                res+= " " + self.keyword[num//10*10]
                num-=num//10*10
                if num:
                    res += " " + self.keyword[num]
        elif num > 0:
            res+=" " + self.keyword[num]
        return res
            
    def numberToWords(self, num: int) -> str:
        if not num:
            return 'Zero'
        res = ""
        multiples = ['Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quintillion', 'Sextillion', 'Septillion', 'Octillion', 'Nonillion']
        n = 1000
        nums = [1000**i for i in range(1,11)]
        keymult = {key: value for key, value in zip(nums,multiples)}
        keymult[1] = ""
        i = 2
        while num > n:
            n = 1000**i
            i+=1
        while num:
            addition = self.helper(num//n)
            res+=addition
            if addition:
                res +=  " " + keymult[n]
            num -= num//n*n
            n//=1000

        return res.strip()
        
