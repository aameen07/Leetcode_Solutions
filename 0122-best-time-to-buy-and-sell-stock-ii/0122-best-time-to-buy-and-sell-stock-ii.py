class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        l=prices[0]
        
        for r in range(1,len(prices)):
            if l>prices[r]:
                l=prices[r]
            else:
                res+=prices[r]-l
                l=prices[r]
                
        return res
            