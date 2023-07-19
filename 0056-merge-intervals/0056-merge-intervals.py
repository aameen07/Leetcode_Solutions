class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        
        res=[]

        nums=sorted(nums,key=lambda x: x[0])
        
        for i in nums:
            if res and res[-1][1]>=i[0]:
                res[-1][1] = max(res[-1][1],i[1]) 
            else:
                res.append(i)
        return res