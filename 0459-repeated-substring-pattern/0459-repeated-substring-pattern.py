class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        s1= s[1:]+s[:-1]
        
        return s in s1
        
        