class Solution:
    def canPlaceFlowers(self, a: List[int], n: int) -> bool:
        
#         count=0
#         prev=0
        
#         for cur in a:
#             if cur==1:
#                 if prev==1:
#                     count-=1
#                 prev=1
#             else:
#                 if prev==1:
#                     prev=0
#                 else:
#                     count+=1
#                     prev=1
            
#         return count >= n


        for i in range(len(a)):
            if (a[i]==0 and (i==0 or a[i-1]==0) and (i==len(a)-1 or a[i+1]==0)):
                
                a[i]=1
                n-=1
        
        return n<=0