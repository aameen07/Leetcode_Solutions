class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l=0
        r=len(nums)-1
        s_arr = self.quick_sort(nums,l,r)
        return s_arr
    
    def quick_sort(self,arr,l,r):
        if l<r:
            partition=self.partition(arr,l,r)
            self.quick_sort(arr,l,partition-1)
            self.quick_sort(arr,partition+1,r)
        return arr
        
    def partition(self,arr,l,r):
        i=l
        j=r-1
        pivot=arr[r]
        
        while i<=j:
            while i<=j and arr[i]<=pivot:
                i+=1
            while i<=j and arr[j]>=pivot:
                j-=1
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
                
        arr[i],arr[r]=arr[r],arr[i]
        return i
        
        
#         dutch partitioning problem hai ye isko usi tareeke se solve karenge
        
#         r, w, b = 0, 1, 2
#         r, w, b = 0, 0, len(nums)-1
        
#         while w<=b:
#             if nums[w]==0:
#                 nums[w], nums[r] = nums[r], nums[w]
#                 w+=1
#                 r+=1
            
#             elif nums[w]==1:
#                 w+=1
            
#             else: 
#                 nums[w], nums[b] = nums[b], nums[w]
#                 b-=1



                
        
            