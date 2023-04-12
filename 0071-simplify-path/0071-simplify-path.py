class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack=[]
        path1 = path.split("/")
        
        for p in path1:
            if p == ".." and stack:
                stack.pop()
            elif p!="" and p!="." and p!="..":
                stack.append(p)
        
        return "/"+ "/".join(stack)
        
        