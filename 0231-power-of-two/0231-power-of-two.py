class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n==1:
            return True
        elif n%2!=0 or n==0:
            return False
        
        return self.isPowerOfTwo(n/2)
    
        # print(1.0%2==1)
# or


        # return (n>0) and (n & n-1)==0
        
        
        # or
        # if n>0:
        #     a=bin(n).count('1')
        #     if a == 1:
        #         return True
        # return False
        
        