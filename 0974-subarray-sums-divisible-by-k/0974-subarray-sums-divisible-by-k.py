class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        
        psum=0
        d={0:1}
        count=0
        e=0
        for i, val in enumerate(nums):
            psum+=val 
            rem=psum%k
            
            if rem in d:
                count+=d[rem]
            d[rem]=d.get(rem,0)+1
    
        return count
        
        
            
            