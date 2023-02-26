class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        
        def feasible(capacity):
            days=1
            total=0
            for weight in weights:
                total+=weight
                if total>capacity:
                    days+=1
                    total=weight
                    if days>D:
                        return False
            return True
            
            
        l=max(weights)
        r=sum(weights)
        
        while(l<r):
            
            m=(l+r)//2
            
            if feasible(m):
                r=m
            else:
                l=m+1
        
        return l
    
        
        