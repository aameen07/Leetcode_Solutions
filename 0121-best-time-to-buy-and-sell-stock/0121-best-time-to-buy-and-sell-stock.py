class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit=0
        l=prices[0]
        
        for r in range(1,len(prices)):
            
            if prices[r]<l:
                l=prices[r]
                continue
            else:
                maxProfit=max(maxProfit,prices[r]-l)
            
        return maxProfit
    