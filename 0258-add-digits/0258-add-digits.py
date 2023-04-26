class Solution:
    def addDigits(self, num: int) -> int:
        
        while num>9:
            asum=0
            while num:
                asum+=(num%10)
                num=num//10
            
            num=asum
        
        return num
        
        