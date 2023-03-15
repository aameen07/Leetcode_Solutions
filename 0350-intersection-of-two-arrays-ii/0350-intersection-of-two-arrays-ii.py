class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        D={}
        L=[]
        
        for i in nums1:
            if i in D:
                D[i]+=1
            else:
                D[i]=1
        
        for j in nums2:
            if j in D and D[j]!=0:
                L.append(j)
                D[j]-=1
        
        return L
        