class Solution:
    def candy(self, ratings: List[int]) -> int:
#         c= [1] * len(ratings)
        
#         for i in range (1,len(ratings)):
#             if ratings[i]>ratings[i-1]:
#                 c[i] = c[i-1]+1
            
#         for j in range(len(ratings)-1,0,-1):
#             if ratings[i-1]>ratings[i]:
#                 c[i-1] = max(c[i-1],c[i]+1)
        
#         return sum(c)

        l=[1] * len(ratings)
        r=[1] * len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                l[i] = l[i-1]+1
        
        for i in range(len(ratings)-1,0,-1):
            if ratings[i-1]>ratings[i]:
                r[i-1] = r[i]+1
                
        return sum([max(l[i],r[i]) for i in range(len(ratings))])