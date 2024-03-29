class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        #   r=m-1, r=m, l=m+1, return m   ye 4 hi scenerio honge kisi condition ke andr finally 95% questions mei
        
        l=0
        r=len(nums)-1
        
        while(l<=r):
            m=(l+r)//2
            
            if target == nums[m]:
                return True
        
            while l!=m and nums[l]==nums[m]:
                l+=1
            
            if nums[l] <= nums[m]:
                
                if nums[l] <= target and target < nums[m]:
                    r=m-1
                
                else:
                    l=m+1
            
            else:
                    
                if nums[m] < target and target <= nums[r]:
                    l=m+1

                else: 
                    r=m-1
        
        return False