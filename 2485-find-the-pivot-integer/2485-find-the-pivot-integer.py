class Solution:
    def pivotInteger(self, n: int) -> int:
        
        rsum=sum([i for i in range(1,n+1)])
        # print(rsum)
        lsum=0
        for i in range(1,n+1):
            lsum+=i
            if lsum!=rsum:
                
                rsum-=i
            
            else:
                return i
            # print(lsum,rsum)
        return -1
            