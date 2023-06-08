# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
        # k=k % len(nums)
        # if k>0:
        #     nums[:]=nums[-k:]+nums[:-k]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
    
    def reverse(self, nums, start, end):
        while(start<end):
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start+=1
            end-=1
        
          
            
        """
        Do not return anything, modify nums in-place instead.
        """
        