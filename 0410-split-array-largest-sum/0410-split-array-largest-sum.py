class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def feasible(capacity):
            days=1
            total=0
            for num in nums:
                total+=num
                if total>capacity:
                    days+=1
                    total=num
                    if days>k:
                        return False
            return True
            
            
        l=max(nums)
        r=sum(nums)
        
        while(l<r):
            
            m=(l+r)//2
            
            if feasible(m):
                r=m
            else:
                l=m+1
        
        return l
        