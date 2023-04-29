class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
#         [1,2,-1,3,7,-4]
#         3


        psum=0
        d={0:1}
        count=0
        
        for i, val in enumerate(nums):
            psum+=val
            if psum-k in d:
                count+=d[psum-k]
    
            d[psum]=d.get(psum,0)+1
            
        
        return count
        
        
            
            