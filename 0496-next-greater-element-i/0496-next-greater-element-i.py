class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        dic = {v:i for i,v in enumerate(nums1)}
        res = [-1]*len(nums1)
        stack = []
        
        for i in range(len(nums2)):
            cur=nums2[i]
            while stack and cur>stack[-1]:
                val=stack.pop()
                idx=dic[val]
                res[idx]=cur
            if cur in dic:
                stack.append(cur)
        
        return res
            
            
        
        
        
        # or
        
#         res=[]
#         dic={}
#         for i in (nums2):
#             while res and i > res[-1]:
#                 c=res.pop()
#                 dic[c]=i
#             res.append(i)
        
#         return [dic.get(j,-1) for j in nums1]
    
    # or
    
        
        
        