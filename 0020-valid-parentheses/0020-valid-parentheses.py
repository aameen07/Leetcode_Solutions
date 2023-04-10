class Solution:
    def isValid(self, s: str) -> bool:
    
        stack=[]
        
        
        
        for i in range (len(s)):
            if s[i]=="(":
                stack.append(")")
            elif s[i]=="{":
                stack.append("}")
            elif s[i]=="[":
                stack.append("]")
            
            elif not stack or stack.pop() != s[i]:
                return False
            
        return not stack
        
        
        