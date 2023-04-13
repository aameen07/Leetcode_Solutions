class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        stack=[]
        total=0
        
        for i in ops:
            
            if i=="+":
                stack.append(stack[-1]+stack[-2])
                total+=stack[-1]
            
            elif i=="C":
                total-=stack.pop()
            
            elif i=="D":
                stack.append(stack[-1] * 2)
                total+=stack[-1]
            
            else:
                stack.append(int(i))
                total+=stack[-1]
            
        
        return total
        
        
        