class Solution:
    def isValid(self, s: str) -> bool:
    
        stack=[]
        
        if len(s)==1:
            return False
        
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
        
        
        