class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        l1=[]
        for i in range(len(candies)):
            total = candies[i]+extraCandies
            l1.append(total >= max(candies))
            
        return l1
    
    