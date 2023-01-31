class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        d, count = {}, 0
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
        
        for num in nums:
            if num+k in d:
                count += d[num+k]
        
        return count
        
        # or
        
        
#         count = 0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if abs(nums[i]-nums[j]) == k:
#                     count+=1
        
#         return count
    
    
    
    
    
       