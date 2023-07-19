class Solution:
    def candy(self, ratings: List[int]) -> int:
        c= [1] * len(ratings)
        
        for i in range (1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                c[i] = c[i-1]+1
            
        for j in range(len(ratings)-1,0,-1):
            if ratings[j-1]>ratings[j]:
                c[j-1] = max(c[j-1],c[j]+1)
        
        return sum(c)
            
        