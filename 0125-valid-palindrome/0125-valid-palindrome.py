class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=s.lower()
        new_s = ""
        for i in s:
            if i.isalnum():
                new_s+=i
        
        return new_s==new_s[::-1]
        
        
        
#         s=s.lower()
#         # print(s)
#         # if s.isempty():
#         #     return True

#         l=0
#         r=len(s)-1
        
#         while(l<=r):
            
#             if not (s[l].isalnum()):
#                 l+=1
#             if not (s[r].isalnum()):
#                 r-=1
#             elif s[l]!=s[r]:
#                 return False
#             elif s[l]==s[r]:
#                 l+=1
#                 r-=1
#             print(l,r)
    
#         return True


    
    
    