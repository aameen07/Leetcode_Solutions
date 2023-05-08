class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        n=len(nums)
        for i in d:
            if d[i]>=(n/2):
                return i


#                   OR

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         d = {}
#         for n in nums:
#             if n in d:
#                 d[n] += 1
#             else:
#                 d[n] = 1
        
#         return max(d, key=d.get)
        
    