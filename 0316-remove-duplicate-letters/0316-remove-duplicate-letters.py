class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d={}
        for i,val in enumerate(s):
            d[val]=i
        
        
        stack=[]
        for i,val in enumerate(s):
            # print(stack)
            if val not in stack:
                while stack and stack[-1]>val and d[stack[-1]]>i:
                    stack.pop()
                # print(stack)
                stack.append(val)
        # print(stack)
        return "".join(stack)
            
            