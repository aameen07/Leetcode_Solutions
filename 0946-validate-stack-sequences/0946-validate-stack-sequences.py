class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
#         stack=[]       
#         j=0
#         for i in pushed:
#             stack.append(i)
#             while stack and stack[-1]==popped[j]:
#                 stack.pop()
#                 j+=1
            
#         return stack==[]
        
        i=0
        j=0
        for x in pushed:
            pushed[i]=x
            while i>=0 and pushed[i]==popped[j]:
                i-=1
                j+=1
            i+=1
        return i==0
        
        