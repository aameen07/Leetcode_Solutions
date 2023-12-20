class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        firstMinCost=secondMinCost=float("inf")
        
        for p in prices:
            if p < firstMinCost:
                secondMinCost,firstMinCost=firstMinCost,p
            else:
                secondMinCost = min(secondMinCost,p)
        
        leftOver = money - (firstMinCost+secondMinCost)
        
        return leftOver if leftOver>=0 else money
