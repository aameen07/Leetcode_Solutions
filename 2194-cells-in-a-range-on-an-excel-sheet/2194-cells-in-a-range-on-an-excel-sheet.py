class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1,r1,c2,r2 = s[:1],s[1:2],s[3:4],s[4:]
        LIST=[]
        for i in range(ord(c1),ord(c2)+1):
            x=chr(i)
            for j in range(int(r1),int(r2)+1):
                y=x+str(j)
                LIST.append(y)
        
        return LIST