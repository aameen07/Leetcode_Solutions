class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack=[]        #1234
        j=0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1]==popped[j]:
                stack.pop()
                j+=1
            
        return stack==[]
                
        