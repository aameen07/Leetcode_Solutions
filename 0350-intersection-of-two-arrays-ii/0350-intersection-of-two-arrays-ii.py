class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
#         D={}
#         L=[]
        
#         for i in nums1:
#             if i in D:
#                 D[i]+=1
#             else:
#                 D[i]=1
        
#         for j in nums2:
#             if j in D and D[j]!=0:
#                 L.append(j)
#                 D[j]-=1
        
#         return L

        D={}
        L=[]
        
        for num in nums1:
            D[num]=D.get(num,0)+1
        
        for num in nums2:
            if num in D and D[num]>0:
                L.append(num)
                D[num]-=1
        
        return L