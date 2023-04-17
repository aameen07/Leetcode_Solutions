class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res=[]
        dic={}
        
        for i in (nums2):
            
            while res and i > res[-1]:
                c=res.pop()
                dic[c]=i
                
            res.append(i)
        
        return [dic.get(j,-1) for j in nums1]
        
        