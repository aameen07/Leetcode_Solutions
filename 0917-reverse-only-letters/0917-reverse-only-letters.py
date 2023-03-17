class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        nums=list(s)
        
        l=0
        r=len(s)-1
        while(l<r):
            if not nums[l].isalpha():
                l+=1
            elif not nums[r].isalpha():
                r-=1
            else:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
                
        s="".join(nums)
        
        return s