class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        hashset=set()
        nums.sort()        
        for i in range(len(nums)-3):            
            for j in range(i+1,len(nums)-2):
                l,r=j+1,len(nums)-1                
                while(l<r):
                    s=nums[l]+nums[r]+nums[j]+nums[i]                    
                    if s < target:
                        l+=1
                    elif s>target:
                        r-=1
                    else:
                        hashset.add((nums[l],nums[r],nums[j],nums[i]))
                        l+=1
                        r-=1                          
        return hashset
                
        