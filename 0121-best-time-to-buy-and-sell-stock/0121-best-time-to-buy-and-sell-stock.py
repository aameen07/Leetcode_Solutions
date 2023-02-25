class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit=0
        l=prices[0]
        
        for i in range(len(prices)):
            
            if prices[i]<l:
                l = prices[i]
            
            maxProfit = max(prices[i]-l,maxProfit)
            
        return maxProfit
                
            
        
        