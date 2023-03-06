class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=s.lower()
        new_s = ""
        for i in s:
            if i.isalnum():
                new_s+=i
        
        return new_s==new_s[::-1]
        
        # or 
        
#         s=s.lower()
#         l=0
#         r=len(s)-1
        
#         while(l<r):
            
#             while l<r and  not s[l].isalnum():
#                 l+=1
#             while l<r and not s[r].isalnum():
#                 r-=1
#             if s[l]!=s[r]:
#                 return False
            
#             l+=1
#             r-=1
    
#         return True

            # or
    
    # return [char for char in s.lower() if char.isalnum()] == [char for char in s[::-1].lower() if char.isalnum()]
    
    
    