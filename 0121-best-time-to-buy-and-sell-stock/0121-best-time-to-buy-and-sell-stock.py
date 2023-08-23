class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit=0
        l=prices[0]
        # if len(prices)==2 and prices[l+1]>prices[l]:
        #     return prices[l+1]-prices[l]
        
        for r in range(1,len(prices)):
            if prices[r]<=l:
                l=prices[r]
                continue
            else:
                maxProfit=max(maxProfit,prices[r]-l)
                print(maxProfit)
        
        return maxProfit
        