class Solution:
    def fib(self, n: int) -> int:
        a,b = 0,1
        if n<=1: return n
        count=2
        while(count<n+1):
            c=a+b
            a=b
            b=c
            count+=1
            
        return c