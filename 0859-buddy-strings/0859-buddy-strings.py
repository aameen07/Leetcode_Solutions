class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        if s == goal and len(s) != len(set(s)):
            return True
        
        d=[]
        for i in range(len(s)):
            if s[i]!=goal[i]:
                d.append([s[i],goal[i]])
        
        if len(d)==2 and d[0]==d[-1][::-1]:
            return True
        
        return False
        